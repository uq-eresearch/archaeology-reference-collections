from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django import forms
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
import re
import logging

logger = logging.getLogger(__name__)


from django.views.generic.base import View


class Uploader(View):

    def __init__(self, *args, **kwargs):
        super(Uploader, self).__init__(*args, **kwargs)
        self.UPLOAD_CHOICES = tuple([(a, b) for a, b, c in self.upload_types])
        self.UPLOAD_HANDLERS = dict([(a, c) for a, b, c in self.upload_types[1:]])

    def get(self, request, **kwargs):
        form = UploadFileForm(choices=self.UPLOAD_CHOICES)
        return render(request, 'mediaman/upload_form.html',
                {'form': form, 'title': 'Bulk upload'})

    def post(self, request, **kwargs):
        form = UploadFileForm(request.POST, request.FILES, choices=self.UPLOAD_CHOICES)
        if form.is_valid():
            upload_type = form.cleaned_data['uploadtype']
            uploaded_file = form.files['File0']
            if self.ignore_file(uploaded_file):
                return HttpResponse("SUCCESS\n Ignored File: %s" % uploaded_file.name)
            try:
                if not upload_type in self.UPLOAD_HANDLERS:
                    return HttpResponse('ERROR: Please select the type of files')
                func = getattr(self, self.UPLOAD_HANDLERS[upload_type])
                func(form.cleaned_data, uploaded_file, request.user)

            except ParseError:
                logger.warning("Unable to parse id from filename.")
                return HttpResponse('ERROR: Check file name/path. Unable to determine registration number or person.')
            except ObjectDoesNotExist as inst:
                logger.warning("Unable to find object matching id.")
                return HttpResponse('ERROR: %s' % inst)
        else:
            return HttpResponse('ERROR: %s' % form.errors)

        return HttpResponse('SUCCESS')

    @staticmethod
    def name_to_id(filename, path=None):
        """
        Calculate item id based on filename and path

        12345.jpg = 12345
        1234_2.jpg = 1234

        /home/test/files/12345/cond.tiff = 12345
        S:\\scanned\\1252\\cond.tiff = 1252

        Will also work on a range of ids, returning a list.
        eg: S:\\scanned\\755-762\\test.pdf = [755, 756, ..., 762]

        """
        match = re.match(r'(\d{1,5}).*$', filename)

        if match:
            return [int(match.group(1))]

        # try using the filepath
        if path is not None:
            # match number range
            match = re.match(r'.*?[/\\].*?(\d+) ?- ?(\d+)', path)

            if match:
                min, max = [int(i) for i in match.groups()]
                return range(min, max + 1)
            else:
                match = re.match(r'.*?[/\\].*?(\d+)', path)

                if match:
                    return [int(match.group(1))]

        raise ParseError



UPLOAD_TYPE_CHOICES = (
    ('NO', ''),
    ('II', 'Item Images'),
    ('OH', 'Object Histories'),
    ('SF', 'Source Files'),
)


class UploadFileForm(forms.Form):
    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('choices', None)
        super(UploadFileForm, self).__init__(*args, **kwargs)
        self.fields['uploadtype'].choices = choices
    File0 = forms.FileField()
    mimetype0 = forms.CharField(max_length=120)
    filemodificationdate0 = forms.CharField(max_length=20)
    pathinfo0 = forms.CharField(max_length=255)
    relpathinfo0 = forms.CharField(max_length=255, required=False)
    md5sum0 = forms.CharField(max_length=32)
    uploadtype = forms.ChoiceField(choices=())


class MediaFileUploader(Uploader):
    IGNORED_FILES = re.compile(r'^\..*|^Thumbs\.db', flags=re.IGNORECASE)

    @staticmethod
    def ignore_file(uploaded_file):
        return MediaFileUploader.IGNORED_FILES.match(uploaded_file.name)

    @staticmethod
    def set_mediafile_attrs(mediafile, ufile, data, user):
        """
        Copy metadata from uploaded file into Model
        """
        mediafile.name = ufile.name
        mediafile.original_filename = ufile.name
        mediafile.filesize = ufile.size
        mediafile.original_path = data['pathinfo0']
        # Date format from jupload is "dd/MM/yyyy HH:mm:ss"
        filedate = datetime.strptime(data['filemodificationdate0'],
            "%d/%m/%Y %H:%M:%S")
        mediafile.original_filedate = filedate
        mediafile.md5sum = data['md5sum0']
        mediafile.mime_type = data['mimetype0']
        mediafile.uploaded_by = user
        return mediafile


class ParseError(Exception):
    """Unable to parse Id from path/filename"""
    pass



from django.db import models
from django.contrib.auth.models import User
from django.template import Template, Context


class MediaFile(models.Model):
    filesize = models.IntegerField(blank=True, null=True, editable=False)
    upload_date = models.DateTimeField(auto_now_add=True, editable=False)
    uploaded_by = models.ForeignKey(User, related_name="+",
            null=True, blank=True, editable=False)
    mime_type = models.CharField(max_length=150, blank=True, editable=False)
    original_filename = models.CharField(max_length=255, editable=False)
    original_path = models.CharField(max_length=255, blank=True, editable=False)
    original_filedate = models.DateTimeField('date last modified', blank=True, null=True, editable=False)
    name = models.CharField(max_length=255, editable=False)
    md5sum = models.CharField(max_length=32, blank=True, editable=False)

    def file_size(self):
        t = Template('{{ filesize|filesizeformat }}')
        c = Context({"filesize": self.filesize})
        return t.render(c)

    class Meta:
        abstract = True

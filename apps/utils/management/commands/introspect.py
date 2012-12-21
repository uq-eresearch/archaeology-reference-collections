from django.core.management.base import AppCommand
from django.db.models import get_models
from django.db.models.fields.related import OneToOneField, ForeignKey


class Command(AppCommand):
    help = "Generate search template with all fields for each model in an app"

    def printfield(self, field, accessor):
        print """
{%% if %s %%}
    <dt>%s</dt>
    <dd>{{ %s }}</dd>
{%% endif %%}""" % (accessor, field.verbose_name, accessor)
#        print '{{ %s }}' % accessor

    def handle_app(self, app, **options):
        models = get_models(app)
        processed_models = set()
        for model in models:
            if model in processed_models:
                continue
            processed_models.add(model)

            print model
            for field in model._meta.fields:
                fieldaccessor = 'object.%s' % field.name
                self.printfield(field, fieldaccessor)

            for related in model._meta.get_all_related_objects():
                processed_models.add(related.model)
                accessor = related.get_accessor_name()
                if isinstance(related.field, OneToOneField):
                    for field in related.model._meta.fields:
                        fieldaccessor = 'object.%s.%s' % (accessor, field.name)
                        self.printfield(field, fieldaccessor)
                elif isinstance(related.field, ForeignKey):
                    print '{%% for related in objects.%s %%}' % accessor
                    for field in related.model._meta.fields:
                        fieldaccessor = 'related.%s' % field.name
                        self.printfield(field, fieldaccessor)
                    print '{% endfor %}'

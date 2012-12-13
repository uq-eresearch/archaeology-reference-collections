from django.core.management.base import AppCommand
from django.db.models import get_models
from django.db.models.fields.related import OneToOneField, ForeignKey


class Command(AppCommand):
    help = "Generate search template with all fields for each model in an app"

    def handle_app(self, app, **options):
        models = get_models(app)
        for model in models:
            print model
            for field in model._meta.fields:
                print '{{ object.%s }}' % field.name

            for related in model._meta.get_all_related_objects():
                accessor = related.get_accessor_name()
                if isinstance(related.field, OneToOneField):
                    for field in related.model._meta.fields:
                        print '{{ object.%s.%s }}' % (accessor, field.name)
                elif isinstance(related.field, ForeignKey):
                    print '{%% for related in objects.%s %%}' % accessor
                    for field in related.model._meta.fields:
                        print '    {{ related.%s }}' % field.name
                    print '{%% endfor %%}'

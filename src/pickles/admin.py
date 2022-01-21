from django.contrib import admin

from .models import Pickle
from .forms import ConfigAdminForm


@admin.register(Pickle)
class ConfigModelAdmin(admin.ModelAdmin):
    form = ConfigAdminForm
    list_display = ('name', 'data_type', 'data_value')
    search_fields = ('name',)
    list_filter = ('data_type',)

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super(ConfigModelAdmin, self).get_form(request, obj, change, **kwargs)
        if obj is not None:
            form.base_fields['raw_value'].initial = obj.value
        return form

    def save_model(self, request, obj, form, change):
        raw_value = form.cleaned_data.get('raw_value')
        obj.value = raw_value
        return super(ConfigModelAdmin, self).save_model(request, obj, form, change)

from django.db import models
from django.utils.translation import ugettext_lazy as _

from picklefield.fields import PickledObjectField


class Pickle(models.Model):
    TYPE_STR = 'str'
    TYPE_INT = 'int'
    TYPE_FLOAT = 'float'
    TYPE_LIST = 'list'
    TYPE_DICT = 'dict'
    TYPE_BOOL = 'bool'
    TYPE_CHOICES = [
        (TYPE_STR, 'STR'),
        (TYPE_INT, 'INT'),
        (TYPE_FLOAT, 'FLOAT'),
        (TYPE_LIST, 'LIST'),
        (TYPE_DICT, 'DICT'),
        (TYPE_BOOL, 'BOOL'),

    ]
    name = models.CharField(verbose_name=_('name'), max_length=100, unique=True)
    value = PickledObjectField(verbose_name=_('value'))
    data_type = models.CharField(verbose_name=_('value data type'), choices=TYPE_CHOICES, max_length=10)

    @property
    def data_value(self):
        return self.value

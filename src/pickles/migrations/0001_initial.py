# Generated by Django 3.1 on 2022-01-21 09:41

from django.db import migrations, models
import picklefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pickle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('value', picklefield.fields.PickledObjectField(editable=False, verbose_name='value')),
                ('data_type', models.CharField(choices=[('str', 'STR'), ('int', 'INT'), ('float', 'FLOAT'), ('list', 'LIST'), ('dict', 'DICT'), ('bool', 'BOOL')], max_length=10, verbose_name='value data type')),
            ],
        ),
    ]

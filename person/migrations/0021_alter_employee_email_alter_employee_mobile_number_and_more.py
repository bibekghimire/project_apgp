# Generated by Django 5.0.6 on 2024-08-23 00:09

import django.core.validators
import django.db.models.deletion
import person.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0020_alter_employee_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(default='hello@example.com', max_length=254, verbose_name='ईमेल'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='mobile_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='invalid_mobile_number', message='मोबाइल नंबर १० अङ्कको हुनुपर्छ र ९ बाट सुरु भएको', regex='^9[0-9]{9}$')], verbose_name='सम्पर्क नं'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='section',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employees', to='person.section', verbose_name='शाखा'),
        ),
        migrations.AlterField(
            model_name='publicrepresentative',
            name='email',
            field=models.EmailField(default='hello@example.com', max_length=254, verbose_name='ईमेल'),
        ),
        migrations.AlterField(
            model_name='publicrepresentative',
            name='mobile_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='invalid_mobile_number', message='मोबाइल नंबर १० अङ्कको हुनुपर्छ र ९ बाट सुरु भएको', regex='^9[0-9]{9}$')], verbose_name='सम्पर्क नं'),
        ),
        migrations.AlterField(
            model_name='publicrepresentative',
            name='ward',
            field=models.IntegerField(choices=person.models.Choices.WardChoices, default=1, verbose_name='वडा'),
        ),
    ]

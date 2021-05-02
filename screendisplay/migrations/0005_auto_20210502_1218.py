# Generated by Django 3.1.6 on 2021-05-02 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screendisplay', '0004_officeinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='officeinfo',
            name='office_address_district',
            field=models.CharField(blank=True, max_length=50, verbose_name='जिल्ला'),
        ),
        migrations.AddField(
            model_name='officeinfo',
            name='office_address_locallevel',
            field=models.CharField(blank=True, max_length=50, verbose_name='पालिका'),
        ),
        migrations.AddField(
            model_name='officeinfo',
            name='office_address_province',
            field=models.CharField(blank=True, max_length=50, verbose_name='प्रदेश'),
        ),
    ]
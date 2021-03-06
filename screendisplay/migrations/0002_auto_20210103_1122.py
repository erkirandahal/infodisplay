# Generated by Django 3.1.3 on 2021-01-03 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screendisplay', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='vacancy_image',
            field=models.ImageField(upload_to='vacancy_uploaded_image', verbose_name='कागजातहरु'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='vacancy_published_status',
            field=models.BooleanField(default=1, verbose_name='स्थिति'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='vacancy_title',
            field=models.CharField(max_length=500, verbose_name='सूचना'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='vacancy_website_link',
            field=models.CharField(max_length=500, null=True, verbose_name='वेवसाइटको लिंक'),
        ),
    ]

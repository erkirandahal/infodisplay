# Generated by Django 3.1.3 on 2021-01-03 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('screendisplay', '0002_auto_20210103_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicprocurement',
            name='publicprocurement_image',
            field=models.ImageField(upload_to='public_procurement_images', verbose_name='तस्विर'),
        ),
        migrations.AlterField(
            model_name='publicprocurement',
            name='publicprocurement_title',
            field=models.CharField(max_length=500, verbose_name='बोलपत्र सूचना'),
        ),
        migrations.AlterField(
            model_name='publicprocurement',
            name='website_link',
            field=models.CharField(max_length=500, null=True, verbose_name='वेवसाइट लिंक'),
        ),
        migrations.CreateModel(
            name='Official',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('official_name', models.CharField(max_length=150, verbose_name='नाम थर')),
                ('official_designation', models.CharField(max_length=50, verbose_name='पद')),
                ('official_phoneno', models.CharField(max_length=10, verbose_name='फोन नं')),
                ('official_roomno', models.CharField(max_length=3, verbose_name='कोठा नं.')),
                ('official_published_status', models.BooleanField(default=1, verbose_name='स्थिति')),
                ('official_image', models.ImageField(upload_to='official_uploaded_image', verbose_name='फोटो')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})


class PublicProcurement(models.Model):
    publicprocurement_title = models.CharField(max_length=500, verbose_name="बोलपत्र सूचना")
    date_posted = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    publicprocurement_image = models.ImageField(upload_to='public_procurement_images', verbose_name="तस्विर")
    published_status = models.BooleanField(default=1)
    website_link = models.CharField(max_length=500, null=True, verbose_name="वेवसाइट लिंक")

    def __str__(self):
        return self.publicprocurement_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        publicprocurement_image = Image.open(self.publicprocurement_image.path)
        if publicprocurement_image.height > 450 or publicprocurement_image.width > 450:
            output_size = (450, 450)
            publicprocurement_image.thumbnail(output_size)
            publicprocurement_image.save(self.publicprocurement_image.path)

    def get_absolute_url(self):
        return reverse('publicprocurement-list')


## VACANCY MODELS STARTS HERE

class Vacancy(models.Model):
    vacancy_title = models.CharField(max_length=500, verbose_name="सूचना")
    date_posted = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    vacancy_image = models.ImageField(upload_to='vacancy_uploaded_image', verbose_name="कागजातहरु")
    vacancy_published_status = models.BooleanField(verbose_name="स्थिति", default=1)
    vacancy_website_link = models.CharField(max_length=500, null=True, verbose_name="वेवसाइटको लिंक")

    def __str__(self):
        return self.vacancy_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        vacancy_image = Image.open(self.vacancy_image.path)
        if vacancy_image.height > 3000 or vacancy_image.width > 3000:
            output_size = (1600, 1200)
            vacancy_image.thumbnail(output_size)
            vacancy_image.save(self.vacancy_image.path)

    def get_absolute_url(self):
        return reverse('vacancy-list')

class Official(models.Model):
    official_name = models.CharField(max_length=150, verbose_name="नाम थर")
    official_designation = models.CharField(max_length=50, verbose_name="पद")
    official_phoneno = models.CharField(max_length=10, verbose_name="फोन नं")
    official_roomno = models.CharField(max_length=3, verbose_name="कोठा नं.")
    official_published_status = models.BooleanField(default=1, verbose_name="स्थिति")
    official_image = models.ImageField(upload_to='official_uploaded_image', verbose_name="फोटो")
    date_posted = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.official_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        official_image = Image.open(self.official_image.path)
        if official_image.height > 140 or official_image.width > 140:
            output_size = (140, 140)
            official_image.thumbnail(output_size)
            official_image.save(self.official_image.path)

    def get_absolute_url(self):
        return reverse('official-list')

class OfficeInfo(models.Model):
    office_name = models.CharField(max_length=150, verbose_name="नाम")
    office_sec_name = models.CharField(max_length=50, verbose_name="नाम")
    office_website = models.CharField(max_length=50, verbose_name="वेबसाइट")
    office_email = models.CharField(max_length=150, verbose_name="इमेल")
    office_phoneno = models.CharField(max_length=50, verbose_name="फोन नं.")
    office_emergencyno = models.CharField(max_length=50, verbose_name="अन्य आपतकालीन नं.")
    date_posted = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    office_image = models.ImageField(upload_to='office_uploaded_image', verbose_name="फोटो")
    office_address_province = models.CharField(max_length=50, verbose_name="प्रदेश", blank=True)
    office_address_district = models.CharField(max_length=50, verbose_name="जिल्ला", blank=True)
    office_address_locallevel = models.CharField(max_length=50, verbose_name="पालिका", blank=True)
    def __str__(self):
        return self.office_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        office_image = Image.open(self.office_image.path)
        if office_image.height > 140 or office_image.width > 140:
            output_size = (140, 140)
            office_image.thumbnail(output_size)
            office_image.save(self.office_image.path)

    def get_absolute_url(self):
        return reverse('office-list')
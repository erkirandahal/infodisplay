from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

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
    publicprocurement_title = models.CharField(max_length=500)
    date_posted = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    publicprocurement_image = models.ImageField(upload_to='public_procurement_images')
    published_status = models.BooleanField(default=1)
    website_link = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.publicprocurement_title

    def get_absolute_url(self):
        return reverse('publicprocurement_list')


## VACANCY MODELS STARTS HERE

class Vacancy(models.Model):
    vacancy_title = models.CharField(max_length=500)
    date_posted = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    vacancy_image = models.ImageField(upload_to='vacancy_uploaded_image')
    vacancy_published_status = models.BooleanField(default=1)
    vacancy_website_link = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.vacancy_title

    def get_absolute_url(self):
        return reverse('vacancy_list')
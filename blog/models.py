from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class ArticlesStatusManager(models.Manager):  
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Article(models.Model):
    STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(unique=True)  # define by title
    body = RichTextUploadingField()
    publisher = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    published = models.DateField(default=timezone.now)
    updated = models.DateField(auto_now=True)
    status = models.CharField(max_length=15, choices=STATUS, default='draft')  # admin will change status
    # defining managers
    objects = models.Manager()
    pub_status = ArticlesStatusManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:article_detail', args=[self.id, self.slug])




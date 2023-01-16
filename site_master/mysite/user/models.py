from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='static/mysite/images/profile/')
    vk = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.user)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super(UserProfile, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('user_profile', kwargs={'user_slug': self.slug})

    class Meta:
        verbose_name = "Пользователь"
        ordering = ['user']
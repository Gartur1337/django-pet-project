from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from django.db.models.signals import post_save
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    friends = models.ManyToManyField("UserProfile", blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='static/mysite/images/profile/')
    vk = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super(UserProfile, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('user_profile', kwargs={'user_slug': self.slug})

    class Meta:
        verbose_name = "Пользователь"
        ordering = ['user']

def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            UserProfile.objects.create(user=instance)
        except:
            pass

post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)

class FriendRequest(models.Model):
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='to_user', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "From {}, to {}".format(self.from_user.username, self.to_user.username)
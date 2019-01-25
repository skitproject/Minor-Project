from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


class post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
        default=1)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    image = models.ImageField(
        upload_to=upload_location,
        null=True,
        blank=True,
        width_field="width_field",
        height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField('content')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    draft = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("postss:detaill", kwargs={"id": self.id})

    # class Meta:
    # ordring ["-timestamp","-updated"]


def pre_save_Post_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.title)
    exists = post.objects.filter(slug=slug).exists()
    if exists:
        slug = "%s-%s" % (slug, instance.id)
    instance.slug = slug


pre_save.connect(pre_save_Post_receiver, sender=post)

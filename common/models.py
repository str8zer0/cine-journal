import uuid
from django.db import models
from django.utils.text import slugify


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SlugMixin(models.Model):
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(str(self))
            unique = uuid.uuid4().hex[:8]
            self.slug = f"{base}-{unique}"
        super().save(*args, **kwargs)

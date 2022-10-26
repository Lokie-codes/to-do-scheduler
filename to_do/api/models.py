from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

class Task(models.Model):
    title = models.CharField(max_length=150)
    status = models.BooleanField(default=False)
    time = models.DurationField()
    due_date = models.DateTimeField(_(""),blank=True, auto_now=False, auto_now_add=False)
    category = models.ForeignKey("api.Category", verbose_name=_("name"), on_delete=models.CASCADE)
    class Meta:
        ordering = ['due_date']
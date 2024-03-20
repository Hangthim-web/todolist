from django.conf import settings
from django.db import models
from django.urls import reverse


# Create your models here.

class Todolist(models.Model):
    task = models.CharField(max_length=200)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE

    )

    def __str__(self):
        return self.task;

    def get_absolute_url(self):
        return reverse("todolistView", kwargs={"pk": self.pk})

from django.conf import settings
from django.db import models
from django.urls import reverse

class Post(models.Model):
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    def __str__(self):
        return str(self.author) + "---" + str(self.date)
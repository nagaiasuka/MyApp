from django.db import models

class Posts(models.Model):
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

class Mail(models.Model):
    text = models.TextField(null=False)
    date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.text
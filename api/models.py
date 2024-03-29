from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(primary_key=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Content(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
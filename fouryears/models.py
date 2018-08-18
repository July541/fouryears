from django.db import models

# Create your models here.
class Letters(models.Model):
    from_name = models.CharField(max_length=200)
    to_name = models.CharField(max_length=200)
    from_url = models.CharField(max_length=200)
    to_url = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    send_date = models.DateTimeField()
    ip = models.CharField(max_length=200)
    is_del = models.BooleanField()

    
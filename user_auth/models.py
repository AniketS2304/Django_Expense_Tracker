from django.db import models

# Create your models here.
class User(models.Model):
    # username  = models.CharField(max_length=10,null=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,null=False)
    password = models.CharField(max_length=255, null=False)

    def __str__(self) -> str:
        return f"{self.name} {self.email}"
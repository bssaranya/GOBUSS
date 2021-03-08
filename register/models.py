
from django.db import models


# Create your models here.
class registermodel(models.Model):
    modelname = models.CharField(max_length=50, default='nil')
    modelphno = models.IntegerField(default=5)
    modelemail = models.EmailField(max_length=50, default='nil')
    modelusername = models.CharField(max_length=50, default='nil')
    modelpassword = models.CharField(max_length=50, default='nil')
    modelconfirmpassword = models.CharField(max_length=50, default='nil')

    class Meta:
        verbose_name_plural = "RegisterTable"

    def __str__(self):
        return self.modelusername




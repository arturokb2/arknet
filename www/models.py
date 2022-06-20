from django.db import models
from django.contrib.auth.models import User

class UpdatePers(models.Model):
    file = models.FileField(blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return f'{self.file}'
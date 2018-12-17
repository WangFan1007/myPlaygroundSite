from django.db import models

# Create your models here.

class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=32, null=True)

    def __str__(self):
        return 'id:{} name:{} email:{}'.format(self.id, self.name, self.email)

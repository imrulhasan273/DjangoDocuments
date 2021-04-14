from django.db import models
from django.contrib.auth.models import User

# class Role(models.Model):
#     name = models.CharField(max_length=30)

#     def __str__(self):
#         return self.name

#     class Meta:
#         ordering = ['name']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=30, blank=True)
    dob = models.DateField(null=True, blank=True)

    # role = models.ForeignKey(Role,on_delete=models.DO_NOTHING,null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['user']




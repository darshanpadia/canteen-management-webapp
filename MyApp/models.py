from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING)
    somaiya_id = models.IntegerField(unique=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank = True)

    def __str__(self):
        return self.user.username


    # userid = models.IntegerField(unique=True)
    # password = models.CharField(max_length=264)

    # def __str__(self):
    #     return str(self.userid)

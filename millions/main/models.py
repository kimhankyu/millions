from django.db import models
from users.models import User
# Create your models here.


#mypage_user
class mypage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
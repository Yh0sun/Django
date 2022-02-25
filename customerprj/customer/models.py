from django.db import models
from django.db import models
from django.utils import timezone

# Customer(고객)
# 이름 name : CharField
# 생년월일 birthdate : DateField
# 이메일주소 email : EmailField
# 성별 gender : BooleanField

class Customer(models.Model):
    name = models.CharField(max_length=10000)
    birthdate = models.DateField()
    email = models.EmailField()
    gender = models.BooleanField()

    def __str__(self):
        return str(self.id)+self.name


from django.db import models


# Create your models here.
class UserModel(models.Model):
    name = models.CharField(max_length=20,
                            verbose_name='账号')
    auth_key = models.CharField(max_length=100,
                                verbose_name='口令')
    phone = models.CharField(max_length=11,
                             verbose_name='手机号')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'app_user'
        verbose_name_plural = verbose_name = '客户信息'

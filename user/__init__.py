from django.contrib.auth.hashers import make_password
from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save)
def filter_user(sender, **kwargs):
    cls_name = str(sender)  # <class user.models.UserModel >
    if cls_name.find('UserModel') > -1:
        obj = kwargs.get('instance')  # UserModel类对象

        # 获取口令信息, 验证是否为明文
        if len(obj.auth_key) < 50:
            # 是明文
            obj.auth_key = make_password(obj.auth_key)
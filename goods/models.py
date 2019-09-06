from django.db import models

# Create your models here.
class GoodsModel(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='名称')
    price = models.DecimalField(verbose_name='单价',
                                max_digits=10,
                                decimal_places=2)
    info = models.TextField(verbose_name='商品描述')
    img1 = models.ImageField(verbose_name='图片1',
                             upload_to='goods')

    def __str__(self):
        return self.name

    @property
    def short_title(self):
        return self.name[:10]

    class Meta:
        db_table = 'app_goods'
        verbose_name = verbose_name_plural = '商品信息'
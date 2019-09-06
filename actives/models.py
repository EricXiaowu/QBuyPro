from django.db import models


# Create your models here.
class ActiveModel(models.Model):
    title = models.CharField(verbose_name='名称',
                             max_length=20)

    img1 = models.ImageField(verbose_name='图片1',
                             upload_to='actives')

    start_time = models.CharField(max_length=30,
                                  verbose_name='开始时间')

    end_time = models.CharField(max_length=30,
                                verbose_name='结束时间')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'app_actives'
        verbose_name_plural = verbose_name = '活动信息'


class ActiveGoodsModel(models.Model):
    active = models.ForeignKey(ActiveModel,
                               related_name='activies',
                               on_delete=models.SET_NULL,
                               null=True,
                               verbose_name='活动名')

    goods = models.ForeignKey('goods.GoodsModel',
                              related_name='activies',
                              on_delete=models.SET_NULL,
                              null=True,
                              verbose_name='商品名')

    rate = models.FloatField(verbose_name='折扣率',
                             default=.88)

    @property
    def rate_price(self):
        return float(self.goods.price)*self.rate

    def __str__(self):
        return self.active.title + ":" + self.goods.name

    class Meta:
        db_table = 'app_active_goods'
        verbose_name = verbose_name_plural = '活动详情'



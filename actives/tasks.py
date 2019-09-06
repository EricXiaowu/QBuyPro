#!/usr/bin/python3
# coding: utf-8
import time
from celery import shared_task
from libs import cache


@shared_task
def qbuy_task(user_id, goods_id):
    time.sleep(10)

    # 判断是否已抢完
    if cache.is_qbuyable():
        # 判断当前用户是否已抢过
        if not cache.exist_qbuy(user_id):
            cache.add_qbuy(user_id, goods_id)
        else:
            return '%s 抢购 %s 失败: 每天限一次' % (user_id, goods_id)

    return '%s 抢购 %s 失败' % (user_id, goods_id)

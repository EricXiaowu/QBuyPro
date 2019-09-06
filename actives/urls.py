#!/usr/bin/python3
# coding: utf-8

from django.urls import path
from .views import ActiveGoodsView, quby_api, query_qbuy_api

app_name = 'activies'
urlpatterns = [
    path('info/', ActiveGoodsView.as_view(), name='info'),
    path('qbuy/<goods_id>/', quby_api, name='qbuy'),
    path('query_qbuy/<goods_id>/', query_qbuy_api, name='query_qbuy'),
]
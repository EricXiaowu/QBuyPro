#!/usr/bin/python3
# coding: utf-8
from rest_framework import serializers, viewsets

from actives.models import ActiveModel, ActiveGoodsModel
from .goods import GoodsSerializer


class ActiveGoodsSerializer(serializers.HyperlinkedModelSerializer):
    goods = GoodsSerializer()

    class Meta:
        model = ActiveGoodsModel
        fields = ('goods', 'rate')


class ActiveSerializer(serializers.HyperlinkedModelSerializer):
    # activies = serializers.StringRelatedField(many=True)
    activies = ActiveGoodsSerializer(many=True)

    class Meta:
        model = ActiveModel
        fields = ('title', 'start_time', 'end_time', 'img1', 'activies')


class ActiveAPIView(viewsets.ModelViewSet):
    queryset = ActiveModel.objects.all()
    serializer_class = ActiveSerializer


class ActiveGoodsAPIView(viewsets.ModelViewSet):
    queryset = ActiveGoodsModel.objects.all()
    serializer_class = ActiveGoodsSerializer

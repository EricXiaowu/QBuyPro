from rest_framework import serializers, viewsets

from goods.models import GoodsModel


class GoodsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GoodsModel
        fields = ('name', 'price', 'img1', 'info')


class GoodsAPIView(viewsets.ModelViewSet):
    queryset = GoodsModel.objects.all()
    serializer_class = GoodsSerializer

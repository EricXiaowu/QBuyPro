from rest_framework import routers, viewsets

from api.active import ActiveAPIView, ActiveGoodsAPIView
from .user import UserAPIView
from .goods import GoodsAPIView

api_router = routers.DefaultRouter()

api_router.register(r'users', UserAPIView)

api_router.register(r'goods', GoodsAPIView)
api_router.register(r'actives', ActiveAPIView)
api_router.register(r'actives_goods', ActiveGoodsAPIView)


from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('accounts', views.AccountViewSet)
router.register('transfer', views.TransferViewSet, basename='transfer')

urlpatterns = [
    path('', include(router.urls)),

    # path('accounts', views.ListAccount.as_view()),
    # path('accounts/<str:pk>', views.AccountDetail.as_view()),

    path('deposit', views.Deposit.as_view()),
    path('withdraw', views.Withdraw.as_view()),
    path('check_balance', views.CheckBalance.as_view()),
]
# path('accounts', views.ListAccount.as_view()),
# path('accounts/<str:pk>', views.AccountDetail.as_view()),

from django.urls import path

from .views import MembershipSelectView, PaymentView, updateTransactions
from .playground_views import playgroundView

app_name = 'memberships'

urlpatterns = [
    path('', MembershipSelectView.as_view(), name='select'),
    path('payment/', PaymentView, name='payment'),
    path('update-transactions/<subscription_id>/', updateTransactions, name='update-transactions'),
    path('playground/', playgroundView, name='playground')
]


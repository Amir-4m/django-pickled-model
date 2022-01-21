from django.urls import path

from .views import PicklesAPIView

urlpatterns = [
    path('pickles/', PicklesAPIView.as_view(), name='pickles'),

]

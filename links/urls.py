from django.urls import path
from links.views import LinkView


urlpatterns = [
    path('', LinkView.as_view(), name='link-add-view'),
]

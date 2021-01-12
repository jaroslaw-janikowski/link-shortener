from django.urls import path
from links.views import LinkView, RedirView


urlpatterns = [
    path('', LinkView.as_view(), name='link-add-view'),
    path(r'<int:pk>/', RedirView, name='link-redirect-view')
]

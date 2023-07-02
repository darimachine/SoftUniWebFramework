from django.urls import path

from common_web_tools.web.views import show_index

urlpatterns = [
    path('', show_index,name='index'),
]

import common_web_tools.web.signals
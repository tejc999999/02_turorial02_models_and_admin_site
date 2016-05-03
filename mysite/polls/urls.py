# -*- coding: utf-8 -*-
# URLマッピング

from django.conf.urls import url

from . import views

# アクセスされたURLに対して、応答するビューを指定
urlpatterns = [
    # http://○○/polls/ にアクセスされた場合、ビューindexに渡す
    url(r'^$', views.index, name='index'),
]
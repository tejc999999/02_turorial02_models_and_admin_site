# -*- coding: utf-8 -*-
# ビュー

# 他ファイルからのコード読み込み
# JavaのimportやC言語のincludeと同様
from django.http import HttpResponse

# index用のビュー、HttpRequestを受け取り、HttpResponseを返す
def index(request):
    # 指定した文字列をHttpResponseとして返す
    return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.

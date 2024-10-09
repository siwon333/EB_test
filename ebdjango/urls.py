from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # 계정 관련 URL
    path('object_detection/', include('object_detection.urls')),  # object_detection 앱의 URL 포함
    path('database/', include('database.urls')),  # database 앱의 URL 포함
    path('', include('accounts.urls')),  # home 및 mypage 관련 URL
]

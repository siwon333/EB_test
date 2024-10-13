# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),  # 첫 페이지가 프로필 페이지로 설정됨
    path('home/', views.home, name='home'),  # 홈 페이지
    path('add_food/', views.add_food, name='add_food'),  # 음식 추가 페이지
    path('processing/', views.processing, name='processing'),  # 처리 화면
    path('result/', views.result, name='result'),  # 결과 페이지
    path('recipes/', views.recipes, name='recipes'),  # 레시피 페이지
    path('result_display/', views.result_display, name='result_display'),  # 결과 출력
    path('expiration/', views.expiration, name='expiration'),  # 유통기한 관리 페이지
    path('storage_methods/', views.storage_methods, name='storage_methods'),  # 재료 보관 방법
    path('community/', views.community, name='community'),  # 커뮤니티 페이지
]

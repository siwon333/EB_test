# main/views.py
from django.shortcuts import render, redirect
from .models import Food
from .forms import FoodForm

def home(request):
    return render(request, 'main/home.html')  # 홈 페이지

def profile(request):
    return render(request, 'main/profile.html')  # 프로필 페이지

def add_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()  # 음식 데이터를 데이터베이스에 저장
            return redirect('expiration')  # 유통기한 관리 페이지로 리다이렉트
    else:
        form = FoodForm()
    return render(request, 'main/add_food.html', {'form': form})

def expiration(request):
    foods = Food.objects.all()  # 데이터베이스에서 모든 음식 데이터를 조회
    return render(request, 'main/expiration.html', {'foods': foods})

def processing(request):
    return redirect('result')

def result(request):
    return render(request, 'main/result.html')

def recipes(request):
    return render(request, 'main/recipes.html')

def result_display(request):
    return render(request, 'main/result_display.html')

def storage_methods(request):
    return render(request, 'main/storage_methods.html')

def community(request):
    return render(request, 'main/community.html')
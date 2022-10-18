from django.shortcuts import render , redirect


# Create your views here.


def index(request):
    page = request.GET.get('page', '1')  # 페이지
    return render(request, 'user/index.html')      
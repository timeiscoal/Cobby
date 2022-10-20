from django.shortcuts import render, get_object_or_404 ,redirect
from makgeolli.models import Makgeolli
from .models import Cobby

# 221018 최해민 막걸리 리스트 페이지 함수 추가
def makgeolli(request):
    makgeolli_list = Makgeolli.objects.all()
    return render(request, 'makgeolli/makgeolli.html', {'makgeolli_list':makgeolli_list})

def makgeolli_detail(request, id):
    makgeolli = get_object_or_404(Makgeolli, id=id)
    return render(request, 'makgeolli/makgeolli_detail.html', {'makgeolli':makgeolli})

# 221019 최신욱 사용자 Image 저장.
def Image(request):
    if request.method == 'GET':
        return render(request, 'post/index.html')
    if request.method =='POST':
        user_image = Cobby()
        user_image.image = request.FILES.get('images', '')
        user_image.save()
        return redirect('makgeolli:detail')

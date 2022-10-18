from django.shortcuts import render, get_object_or_404
from makgeolli.models import Makgeolli
# 221018 최해민 막걸리 리스트 페이지 함수 추가
def makgeolli(request):
    makgeolli_list = Makgeolli.objects.all()
    return render(request, 'makgeolli/makgeolli.html', {'makgeolli_list':makgeolli_list})

def makgeolli_detail(request, id):
    makgeolli = get_object_or_404(Makgeolli, id=id)
    return render(request, 'makgeolli/makgeolli_detail.html', {'makgeolli':makgeolli})
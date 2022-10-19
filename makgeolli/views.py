from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from makgeolli.models import Makgeolli
import easyocr

# 221018 최해민 막걸리 리스트 페이지 함수 추가
def makgeolli(request):
    makgeolli_list = Makgeolli.objects.all()
    return render(request, 'makgeolli/makgeolli.html', {'makgeolli_list':makgeolli_list})

def makgeolli_detail(request, id):
    makgeolli = get_object_or_404(Makgeolli, id=id)
    return render(request, 'makgeolli/makgeolli_detail.html', {'makgeolli':makgeolli})

# 221019 최해민 EasyOCR 추가
def cobby(request):
    reader = easyocr.Reader(['ko'], gpu=True) # 'ko' : 한글로 설정
    result_list = reader.readtext('media/makgeolli/result1.png')
    name = ''
    for result in result_list:
        name += result[1]
    return HttpResponse(f'{name}')
from django.shortcuts import render , redirect
from makgeolli.models import Cobby, Makgeolli
import easyocr
from urllib import parse
from pprint import pprint

def index(request):
    page = request.GET.get('page', '1')  # 메인페이지
    return render(request, 'user/index.html')      

from django.shortcuts import render,redirect
from user.models import User

# Create your views here.
def signup(request): #20221018 문규빈 회원가입 기능
    if request.method == 'GET':
        return render(request, 'user/signup.html') #셋팅에 따라 형식이 바뀔 수 있음

    
    if request.method == 'POST':
        user = User()
        user.username = request.POST.get('username','')
        user.phonenum = request.POST.get('phonenum','')
        user.email = request.POST.get('email','')
        user.password = request.POST.get('password','')
        
        if user.username == "" or user.password == "" or user.email == "" or user.phonenum == "": #빈칸이 있을 때
            print(user.username)
            print(user.phonenum)
            print(user.email)
            print(user.password)
            print('1')
            return render (request, 'user/signup.html', {'error' : '입력창을 확인해주십시오.'})
            
        if User.objects.filter(username = user.username).exists(): #아이디 중복체크  exists에 () 꼭 붙일 것!
            print(user.username)
            return render (request, 'user/signup.html',{'error' : '사용할 수 없는 아이디 입니다.'})
        else:
            print("3")        
            user.set_password(user.password) #비밀번호 암호화
            user.save()
            return redirect('/login/')
        

# 221019 최해민 upload, EasyOCR 추가
def upload(request):
    if request.method == 'GET':
        return render(request, 'user/base.html')
    
    if request.method == 'POST':
        file = request.FILES['product_image']
        new_file = Cobby()
        new_file.image = file
        new_file.save()
    
        reader = easyocr.Reader(['ko'], gpu=True) # 'ko' : 한글로 설정
        result_list = reader.readtext(parse.unquote(new_file.image.url[1:]))
        pprint(result_list)
    
        name = '' # 찾은 text들을 다 더할 빈 문자열
        for result in result_list:
            name += result[1] # text들을 name에 다 더해준다.
        mak_list = Makgeolli.objects.all()
        for mak in mak_list:
            if mak.name in name:
                return redirect(f'/makgeolli/{mak.id}')
        else:
            return render(request, 'user/base.html', {'error':"다른 이미지 파일을 업로드 해주세요."})
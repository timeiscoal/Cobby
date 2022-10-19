
from django.shortcuts import render , redirect


def index(request):
    page = request.GET.get('page', '1')  # 메인페이지
    return render(request, 'user/index.html')      

from django.shortcuts import render,redirect
from user.models import User

# Create your views here.
def signup(request): #20221018 문규빈 회원가입 기능
    if request.method == 'GET':
        return render(request, 'user/signup.html')
    
    if request.method == 'POST':
        user = User()
        user.username = request.POST.get('username','')
        user.phonenum = request.POST.get('phonenum','')
        user.email = request.POST.get('email','')
        user.password = request.POST.get('password','')
        
        if user.username == "" or user.password == "" or user.email == "" or user.phonenum == "": #빈칸이 있을 때
            print("1")
            return render (request, 'signup.html', {'error' : '입력창을 확인해주십시오.'})
            
        if User.objects.filter(username = user.username).exists(): #아이디 중복체크 
            print(user.username)
            return render (request, 'signup.html',{'error' : '사용할 수 없는 아이디 입니다.'})
        else:
            print("3")        
            user.set_password(user.password) #비밀번호 암호화
            user.save()
            
            return redirect('/login/')


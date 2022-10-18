from django.shortcuts import HttpResponse, render, redirect
from django.http import HttpResponse
from post.models import Comment



def create_comment(request):
    if request.method == 'GET':
        #user = request.user.is_authenticated
        #if user:
        return render(request, 'create_comment.html')
        #else:
            #return HttpResponse("로그인 후 이용해주세요")
    
    elif request.method == 'POST':
        user = request.user
        contents = Comment()
        contents.author = user
        contents.content = request.POST.get('content','')
        contents.save()
        print(contents)
        
        return HttpResponse("완료")

def edit(request, pk):
    post = Comment.objects.get(pk=pk)             
    context = {                                         
        'comment': comment,
    }
    return render(request, 'comment_edit.html', context)

       
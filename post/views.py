from ast import If
from django.shortcuts import HttpResponse, render, redirect
from django.http import HttpResponse
from post.models import Comment
from makgeolli.models import Makgeolli

# 장혜림_댓글 작성 함수 
def create_comment(request, id):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            article = Makgeolli.objects.get(id=id)
            return render(request, 'makgeolli_detail.html', {"article":article})
        else:
            return HttpResponse("로그인 후 이용해주세요")
    
    elif request.method == 'POST':
        user = request.user
        contents = Comment()
        contents.author = user
        contents.content = request.POST.get('content','')
        contents.article = Makgeolli.objects.get(id=id)
        contents.save()
        print(request.POST.get('content',''))
        return redirect(f'/makgeolli/{id}')
        

# 장혜림_댓글 수정 함수
def edit(request, id):
    if request.method == 'GET':
        content = Comment.objects.get(id=id)             
        context = {                                         
            'content': content,
        }
        return render(request, 'comment_edit.html', context)
    if request.method == 'POST':
        user = request.user
        contents = Comment.objects.get(id=id)
        contents.author = user
        contents.content = request.POST.get('contents','') #htm에서 쓰이는 이름
        contents.save()
        return redirect(f'/makgeolli/{contents.article.id}')        

   
    
    
    


def comment_delete(request,pk):
    comments = Comment.objects.get(pk=pk)
    
    """ 
    2022.10.17 최신욱
    댓글 삭제 함수입니다.

    Args:
        request : 사용자가 댓글 삭제를 요청했을 때 입력된 값. (정보)
        pk : 댓글 생성시 발급되는 고유 id 값

    Returns:
            사용자가 보낸 요청이 'POST' 일 경우 댓글을 삭제 한 뒤 ''로 이동합니다.
            그 외 모든 요청을 보내올 경우 '' 를 보여줍니다.
    """
    comments.delete()
    return redirect(f'/makgeolli/{comments.article.id}')
    



def Post_search(request):
    """
    2022.10.17 최신욱
    게시글 검색 함수입니다.
    현재는 title로만 검색이 가능합니다.

    Args:
        request : 사용자가 검색을 요청했을 때 입력된 값.

    Returns:
            검색을 요청한 사용자의 입력 값이 title=search 일치한다면, 일치하는 정보들만 post_search.html를 rander합니다.
    """

    
    # print(post_list)
    # print(search)
    if request.method == 'GET':
        search = request.GET['searched']
        post_list = Makgeolli.objects.all()
        post_list = post_list.filter(name__icontains=search)
        print(post_list)
    return render(request, 'makgeolli/makgeolli_detail.html', {'Post_search' : post_list})


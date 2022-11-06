from django.shortcuts import render, redirect, get_object_or_404
# [코드 추가] models.py의 Comment 모델 추가로 불러오기
from .models import Posting, Comment
# [코드 추가] forms.py의 CommentForm 추가로 불러오기
from .forms import PostingForm, CommentForm

# Create your views here.
def index(request):
    return render(request, 'page/index.html')

# [Read] 전체 글 목록 보기
def posting_list(request):
    postings = Posting.objects.all()
    context = {
        'postings': postings,
    }
    return render(request, 'page/posting_list.html', context)

# [Create] 글 작성하기
def posting_create(request):
    if request.method == 'POST':
        posting_form = PostingForm(request.POST)
        
        if posting_form.is_valid():
            posting_form.save()
            return redirect('page:posting_list')
    else:
        posting_form = PostingForm()
    
    context = {
        'posting_type': '글쓰기',
        'posting_form': posting_form,
    }
    return render(request, 'page/posting_form.html', context)

# [Read & Create] 작성글 보기 & 댓글 작성
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    
    # [코드 작성] request.method가 'POST'일 경우 comment_form에 요청값 저장
    # [코드 작성] comment_form이 유효하면 commit=False를 이용하여 comment에 form 임시저장
    # [코드 작성] comment 객체의 posting 필드에 posting 객체를 저장하고, comment 저장
    # [코드 작성] CommentForm을 생성하여 posting_form에 저장
    # [코드 작성] request.method가 'POST'가 아닐 경우 CommentForm을 생성
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.posting = posting
            comment.save()
            return redirect('page:posting_detail', posting_id)
    else :
        comment_form = CommentForm()
    
    # [코드 수정] posting_id에 해당하는 posting 객체의 모든 댓글 불러오기
    # [코드 수정] Comment 모델 posting 필드의 related_name 활용
    # [코드 수정] None을 지우고 작성
    comments = posting.comment_list.all()

    context = {
        'posting': posting,
        # [코드 수정] comment_form을 딕셔너리 형식으로 html에 넘겨주기
        # [코드 수정] None을 지우고 작성
        'comment_form': comment_form,
        # [코드 수정] comments를 딕셔너리 형식으로 html에 넘겨주기
        # [코드 수정] None을 지우고 작성
        'comments': comments,
    }
    return render(request, 'page/posting_detail.html', context)

# [Update] 작성글 수정
def posting_update(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)

    if request.method == 'POST':
        posting_form = PostingForm(request.POST, instance=posting)

        if posting_form.is_valid():
            posting_form.save()
            return redirect('page:posting_detail', posting_id)
    else:
        posting_form = PostingForm(instance=posting)

    context = {
        'posting_type': '글수정',
        'posting': posting,
        'posting_form': posting_form,
    }
    return render(request, 'page/posting_form.html', context)

# [Delete] 작성글 삭제
def posting_delete(request, posting_id):
    if request.method == 'POST':
        posting = get_object_or_404(Posting, id=posting_id)
        posting.delete()
        return redirect('page:posting_list')
    return redirect('page:posting_detail', posting_id)

# [Delete] 댓글 삭제
def comment_delete(request, posting_id, comment_id):
    if request.method == 'POST':
        return 

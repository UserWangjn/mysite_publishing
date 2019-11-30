from django.shortcuts import render, HttpResponse, redirect
from app01.models import Publishing, Book,Author


# Create your views here.
# 出版社列表展示
def publishing_list(request):
    ret = Publishing.objects.all()
    # print(ret)

    return render(request, 'publishing_list2.html', {'ret': ret})


# 添加出版社
def add_publishing(request):
    if request.method == 'POST':
        publishing_name = request.POST.get('publishingName')
        Publishing.objects.create(name=publishing_name)
        return redirect('/publishing_list/')
    return render(request,'add_publishing2.html')


# 编辑出版社
def edit_publishing(request):
    # print('edit_publishing request:',request)
    # 1.获得用户需要编辑的出版社ID
    edit_id = request.GET.get('id')
    print('edit_id:', edit_id)
    # 2.在数据库中查到该ID的出版社对象
    publishing_obj = Publishing.objects.filter(id=edit_id).first()
    # publishing_obj = Publishing.objects.get(id=edit_id)
    # 如果为POST请求，则把编辑结果保存到数据库
    if request.method == 'POST':
        # 获得用户页面编辑的新出版社名称
        new_name = request.POST.get('new_name')
        print('new_name:', new_name)
        # 把新出版社名称赋值给数据库对象Publishing表name字段
        publishing_obj.name = new_name
        # print('publishing_obj[0].name:',publishing_obj[0].name)
        # 保存修改（提交修改）
        publishing_obj.save()
        return redirect('/publishing_list/')
    # 3.把出版社对象返回到HTML页面
    # return render(request,'edit_publishing.html',{'publishing_obj':publishing_obj[0],'publishing_obj':publishing_obj[0]})
    return render(request, 'edit_publishing2.html', {'publishing_obj': publishing_obj})


# 删除出版社
def delete_publishing(request):
    # 1.获取要删除出版社的id
    delete_id = request.GET.get('id')
    # 2.去数据库删除该id
    Publishing.objects.get(id=delete_id).delete()
    # 3.跳转到publishing_list页面
    return redirect('/publishing_list/')


# 展示书籍列表
def book_list(request):
    # 1.从数据库中查询书籍列表
    book_list_obj = Book.objects.all()
    # return render(request, 'book_list.html', {'books_obj': book_list_obj})
    return render(request, 'book_list2.html', {'books_obj': book_list_obj})


# 添加书籍
def add_book(request):
    # 1.从数据库查询所有出版社
    publishing_list = Publishing.objects.all()
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        new_publishing_id = request.POST.get('publishing_id')
        Book.objects.create(title=book_name, publishing_id=new_publishing_id)
        return redirect('/book_list/')
    return render(request, 'add_book2.html', {'publishing_list': publishing_list})


def edit_book(request):
    # 1.获得要编辑书籍名称，并回显到编辑页面
    book_id = request.GET.get('id')
    print('book_id:',book_id)
    old_book_obj = Book.objects.get(id=book_id)
    print('old_book_obj:',old_book_obj)
    if request.method == 'POST':
        new_book_title = request.POST.get('new_book_title')
        new_publishin_id = request.POST.get('publishing_id')
        old_book_obj.title = new_book_title
        old_book_obj.publishing_id = new_publishin_id
        old_book_obj.save()
        return redirect('/book_list/')
    publishing_list_obj = Publishing.objects.all()
    return render(request,'edit_book2.html',{'publishing_list_obj':publishing_list_obj,'old_book_obj':old_book_obj})


def delete_book(request):
    # 1.获取要删除的书籍ID
    delete_id = request.GET.get('id')
    # 2.去数据库删除此ID
    Book.objects.get(id=delete_id).delete()
    # 3.返回删除成功页面
    return render(request,'delete_success.html')


# 展示作者列表
def author_list(request):
    author_data = Author.objects.all()
    # for author in author_data:
    #     print(author.books.all())

    return render(request,'author_list.html',{'author_list':author_data})


# 添加作者
def add_author(request):
    book_list_obj = Book.objects.all()
    if request.method == 'POST':
        new_author_name = request.POST.get('author_name')
        new_book_ids = request.POST.getlist('book_ids')
        new_author_obj = Author.objects.create(name=new_author_name)
        new_author_obj.books.add(*new_book_ids)
        return redirect('/author_list/')
    return render(request,'add_author.html',{'book_list_obj':book_list_obj})


def delete_author(request):
    delete_author_id = request.GET.get('shanchu')
    Author.objects.get(id=delete_author_id).delete()
    return redirect('/author_list/')


def edit_author(req):
    old_author_id = req.GET.get('bianji')
    old_author_obj = Author.objects.get(id=old_author_id)
    book_list_obj = Book.objects.all()
    if req.method == "POST":
        new_author_name = req.POST.get('author_name')
        new_book_ids = req.POST.getlist('books')
        old_author_obj.name = new_author_name
        old_author_obj.save()
        old_author_obj.books.set(new_book_ids)
        return redirect('/author_list/')
    return render(req,
                  'edit_author.html',
                  {'author_obj':old_author_obj,'book_list_obj':book_list_obj})

from django.shortcuts import render,HttpResponse,redirect
from app01.models import Publishing,Book

# Create your views here.

def publishing_list(request):
    ret = Publishing.objects.all()
    # print(ret)

    return render(request,'publishing_list.html',{'ret':ret})

def edit_publishing(request):
    # print('edit_publishing request:',request)
    # 1.获得用户需要编辑的出版社ID
    edit_id = request.GET.get('id')
    print('edit_id:',edit_id)
    # 2.在数据库中查到该ID的出版社对象
    publishing_obj = Publishing.objects.filter(id=edit_id).first()
    # publishing_obj = Publishing.objects.get(id=edit_id)
    # 如果为POST请求，则把编辑结果保存到数据库
    if request.method == 'POST':
        # 获得用户页面编辑的新出版社名称
        new_name = request.POST.get('new_name')
        print('new_name:',new_name)
        # 把新出版社名称赋值给数据库对象Publishing表name字段
        publishing_obj.name = new_name
        # print('publishing_obj[0].name:',publishing_obj[0].name)
        # 保存修改（提交修改）
        publishing_obj.save()
        return redirect('/publishing_list/')
    # 3.把出版社对象返回到HTML页面
    # return render(request,'edit_publishing.html',{'publishing_obj':publishing_obj[0],'publishing_obj':publishing_obj[0]})
    return render(request,'edit_publishing.html',{'publishing_obj':publishing_obj})

def book_list(request):
    # 1.从数据库中查询书籍列表
    book_list_obj = Book.objects.all()
    return render(request,'book_list.html',{'books_obj':book_list_obj})
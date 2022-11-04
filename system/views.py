from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse , HttpResponseRedirect
from django.db.models import Q

from .models import Iha, Order, PrivateMsg
from .forms import IhaForm, OrderForm, MessageForm


def home(request):
    context = {
        "title" : "İha Kiralama"
    }
    return render(request,'home.html', context)

def iha_list(request):
    iha = Iha.objects.all()

    query = request.GET.get('q')
    if query:
        iha = iha.filter(
                     Q(iha_name__icontains=query) |
                     Q(company_name__icontains = query)
                            )

    # Sayfa yapısı
    paginator = Paginator(iha, 12)  # Sayfa başına 12 iha
    page = request.GET.get('page')
    try:
        iha = paginator.page(page)
    except PageNotAnInteger:
        # Eğer sayfa bir tam sayı değilse ilk sayfa getirilir
        iha = paginator.page(1)
    except EmptyPage:
        # Eğer sayfa numarası mevcut değilse, mevcut son sayfa getirilir
        iha = paginator.page(paginator.num_pages)
    context = {
        'iha': iha,
    }
    return render(request, 'iha_list.html', context)

def iha_detail(request, id=None):
    detail = get_object_or_404(Iha,id=id)
    context = {
        "detail": detail
    }
    return render(request, 'iha_detail.html', context)

def iha_created(request):
    form = IhaForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/")
    context = {
        "form" : form,
        "title": "Iha Yarat"
    }
    return render(request, 'iha_create.html', context)

def iha_update(request, id=None):
    detail = get_object_or_404(Iha, id=id)
    form = IhaForm(request.POST or None, instance=detail)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
        "title": "Iha Güncelle"
    }
    return render(request, 'iha_create.html', context)

def iha_delete(request,id=None):
    query = get_object_or_404(Iha,id = id)
    query.delete()

    iha = Iha.objects.all()
    context = {
        'iha': iha,
    }
    return render(request, 'admin_index.html', context)

#order

def order_list(request):
    order = Order.objects.all()

    query = request.GET.get('q')
    if query:
        order = order.filter(
            Q(movie_name__icontains=query)|
            Q(employee_name__icontains=query)
        )

    # Sayfa yapısı
    paginator = Paginator(order, 4)  #Sayfa başına 4 kayıt
    page = request.GET.get('page')
    try:
        order = paginator.page(page)
    except PageNotAnInteger:
        # Eğer sayfa bir tam sayı değilse ilk sayfa getirilir
        order = paginator.page(1)
    except EmptyPage:
        # Eğer sayfa numarası mevcut değilse, mevcut son sayfa getirilir
        order = paginator.page(paginator.num_pages)
    context = {
        'order': order,
    }
    return render(request, 'order_list.html', context)

def order_detail(request, id=None):
    detail = get_object_or_404(Order,id=id)
    context = {
        "detail": detail,
    }
    return render(request, 'order_detail.html', context)

def order_created(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form,
        "title": "Sipariş Yarat"
    }
    return render(request, 'order_create.html', context)

def order_update(request, id=None):
    detail = get_object_or_404(Order, id=id)
    form = OrderForm(request.POST or None, instance=detail)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
        "title": "Siparişi Güncelle"
    }
    return render(request, 'order_create.html', context)

def order_delete(request,id=None):
    query = get_object_or_404(Order,id = id)
    query.delete()
    return HttpResponseRedirect("/listOrder/")

def new_iha(request):
    new = Iha.objects.order_by('-id')
    #seach
    query = request.GET.get('q')
    if query:
        new = new.filter(
            Q(iha_name__icontains=query) |
            Q(company_name__icontains=query)
        )

    # Sayfa yapısı
    paginator = Paginator(new, 12)   #Sayfa başına 12 kayıt
    page = request.GET.get('page')
    try:
        new = paginator.page(page)
    except PageNotAnInteger:
        # Eğer sayfa bir tam sayı değilse ilk sayfa getirilir
        new = paginator.page(1)
    except EmptyPage:
        # Eğer sayfa numarası mevcut değilse, mevcut son sayfa getirilir
        new = paginator.page(paginator.num_pages)
    context = {
        'iha': new,
    }
    return render(request, 'new_iha.html', context)

def like_update(request, id=None):
    new = Iha.objects.order_by('-id')
    like_count = get_object_or_404(Iha, id=id)
    like_count.like+=1
    like_count.save()
    context = {
        'iha': new,
    }
    return render(request,'new_iha.html',context)

def popular_iha(request):
    new = Iha.objects.order_by('-like')
    # arama
    query = request.GET.get('q')
    if query:
        new = new.filter(
            Q(iha_name__icontains=query) |
            Q(company_name__icontains=query)
        )

    # Sayfa yapısı
    paginator = Paginator(new, 12)  #Sayfa başına 12 kayıt
    page = request.GET.get('page')
    try:
        new = paginator.page(page)
    except PageNotAnInteger:
        # Eğer sayfa bir tam sayı değilse ilk sayfa getirilir
        new = paginator.page(1)
    except EmptyPage:
        # Eğer sayfa numarası mevcut değilse, mevcut son sayfa getirilir
        new = paginator.page(paginator.num_pages)
    context = {
        'iha': new,
    }
    return render(request, 'new_iha.html', context)

def contact(request):
    form = MessageForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/iha/new_iha/")
    context = {
        "form": form,
        "title": "İletişime Geçin",
    }
    return render(request,'contact.html', context)

#-----------------Admin-----------------

def admin_iha_list(request):
    iha = Iha.objects.order_by('-id')

    query = request.GET.get('q')
    if query:
        iha = iha.filter(
            Q(iha_name__icontains=query) |
            Q(company_name__icontains=query)
        )

    # Sayfa yapısı
    paginator = Paginator(iha, 12)   #Sayfa başına 12 kayıt
    page = request.GET.get('page')
    try:
        iha = paginator.page(page)
    except PageNotAnInteger:
        # Eğer sayfa bir tam sayı değilse ilk sayfa getirilir
        iha = paginator.page(1)
    except EmptyPage:
        # Eğer sayfa numarası mevcut değilse, mevcut son sayfa getirilir
        iha = paginator.page(paginator.num_pages)
    context = {
        'iha': iha,
    }
    return render(request, 'admin_index.html', context)

def admin_msg(request):
    msg = PrivateMsg.objects.order_by('-id')
    context={
        "iha": msg,
    }
    return render(request, 'admin_msg.html', context)

def msg_delete(request,id=None):
    query = get_object_or_404(PrivateMsg, id=id)
    query.delete()
    return HttpResponseRedirect("/message/")

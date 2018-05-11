import re
from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Category, Product, Document, DocumentLines, Employee
from django.http import HttpResponseRedirect


def main(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('report/')
    else:
        return HttpResponseRedirect('login/')


@login_required
def index(request):
    user = request.user
    query_entity = Employee.objects.get(user=user)
    user_entity = query_entity.entity
    query_docs = Document.objects.filter(user__entity=user_entity)

    return render(request, 'report/index.html', {
        'docs': query_docs,
    })


@login_required
def create_report(request):
    categories = get_list_or_404(Category)
    products = get_list_or_404(Product)
    return render(request, 'report/add.html', {
        'categories': categories,
        'products': products,
    })


@login_required
def report_view(request, id):
    view = DocumentLines.objects.filter(document__pk=id)
    return render(request, 'report/view.html', {
        'doc': id,
        'lines': view,
    })


@login_required
def change_report(request, id):
    lines = DocumentLines.objects.filter(document__pk=id)
    return render(request, 'report/change.html', {
        'doc': id,
        'lines': lines,
    })


@login_required
def change_lines(request, id):
    result = {}
    if request.method == 'POST':
        form = request.POST
        for key, value in form.items():
            if value and re.match("^[0-9]*$", key):
                result[key] = value

    doc = Document.objects.get(pk=id)
    doc.save()

    lines = DocumentLines.objects.filter(document=doc)
    print(lines)

    for amount in result.values():
        for line in lines:
            line.amount = amount
            line.save()

    return HttpResponseRedirect('/report/view/{}'.format(id))


@login_required
def add_lines(request):
    result = {}
    user = request.user
    employee = Employee.objects.get(user=user)
    queryset = Document.objects.all().count()
    products_id = get_list_or_404(
        Product.objects.values_list('code', flat=True))

    if request.method == 'POST':
        form = request.POST
        for key, value in form.items():
            if value and re.match("^[0-9]*$", key):
                result[key] = value

    if queryset:
        last_doc = Document.objects.latest('pk')
        id = last_doc.pk
        new_doc = Document(
            document_name='Звіт №{}'.format(id + 1), user=employee)
        new_doc.save()
    else:
        new_doc = Document(document_name='Звіт №1', user=employee)
        new_doc.save()

    for code, amount in result.items():
        product = Product.objects.get(code=code)

        new_line = DocumentLines(
            document=new_doc, product=product, amount=amount)
        new_line.save()

    return HttpResponseRedirect('/report/')

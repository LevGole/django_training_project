from django.http import HttpResponse
from django.shortcuts import render

def first_page(request):
    text = '<h1>1Hello World</h1>'
    a = 'Новый текст'
    return render(request, './index.html',
                  {'text': text, 'a': a})
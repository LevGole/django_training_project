from django.http import HttpResponse

def first_page(request):
    text = '<h1>1Hello World</h1>'
    return HttpResponse(text)
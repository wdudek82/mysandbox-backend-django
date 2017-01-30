from django.shortcuts import render


def home(request):
    return render(request, 'base.html', {})

def post_detail(request, pk=None):
    print(pk)
    return render(request, 'base.html', {})
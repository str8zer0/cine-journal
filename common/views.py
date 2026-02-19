from django.shortcuts import render

def home(request):
    return render(request, 'common/home.html')

def error_404(request, exception):
    return render(request, '404.html', status=404)

from django.shortcuts import render

def home(request):
	return render(request, 'mvp_app/home.html')

def test(request):
    return render(request, 'mvp_app/desuso.html', {})
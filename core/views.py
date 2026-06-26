from django.http import HttpResponse

def home(request):
    return HttpResponse('Portfolio home working')

def error_404_view(request, exception):
    return HttpResponse('Page not found', status=404)

def error_500_view(request):
    return HttpResponse('Server error', status=500)

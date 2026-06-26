from django.http import HttpResponse

def home(request):
    return HttpResponse('Bio app working')

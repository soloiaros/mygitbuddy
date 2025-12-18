from django.http import HttpResponse


def homepage_view(request):
    return HttpResponse('<body>Hey there</body>')

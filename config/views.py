from django.http import HttpResponse


def HomePageView(request):
  return HttpResponse("<h1> Tarjimon bosh sahifa </h1>")

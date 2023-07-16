from django.urls import path

from .views import translation_view


urlpatterns = [
	path('translation/tolang=<str:tolang>',
			translation_view, name='translation')
]
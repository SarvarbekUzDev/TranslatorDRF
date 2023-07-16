from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings

from .functions import latin_kril, latin_arabic



# Create your views here.
@api_view(['POST'])
def translation_view(request, tolang):
	""" Belgilar TEXT_SIZE dan oshmasligi va tarjima qilinadigan til mavjudligi tekshirilmoqda """
	text = request.data.get("text")
	if len(text) < settings.TEXT_SIZE:
		data = {}
		global translate
		if tolang.lower() == "kril-latin" or tolang.lower() == "latin-kril":
			translate = latin_kril(text=text, lang=tolang.lower())
		elif tolang.lower() == "latin-arabic" or tolang.lower() == "arabic-latin":
			translate = latin_arabic(text=text, lang=tolang.lower())
		elif tolang.lower() == "kril-arabic" or tolang.lower() == "arabic-kril":
			if tolang.lower() == "kril-arabic":
				translate_kril = latin_kril(text=text, lang="kril-latin")
				translate = latin_arabic(text=translate_kril, lang="latin-arabic")
			else:
				translate_latin = latin_arabic(text=text, lang="arabic-latin")
				translate = latin_kril(text=translate_latin, lang="latin-kril")
				
		else:
			return Response({'error':'Invalid language entered'}, 400)

		data['message'] = translate
		return Response(data, status=200)

	return Response({'error':f'The number of characters in the error text must not exceed {settings.TEXT_SIZE}'},
						status=400)
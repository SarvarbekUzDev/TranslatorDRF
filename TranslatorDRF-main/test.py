import requests

DOMAIN_NAME = "https://55ad-84-54-72-240.ngrok-free.app"

lang = "latin-arabic"
text = """ Assalomu alaykum """

translate = requests.post(
			f"{DOMAIN_NAME}/api/v1/translations/translation/tolang={lang}",
			data={'text':text})
print(translate.json()['message'])
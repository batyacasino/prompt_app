from django import forms
from .models import Client
from yandex_pdd import YandexPdd
from random import randint
from transliterate import translit
from re import findall


class ClientForm(forms.Form):
	claimant = forms.CharField(max_length=200)
	date_of_birth = forms.DateField()
	defendant = forms.CharField(max_length=200)
	date_of_inspection = forms.DateField()

	claimant.widget.attrs.update({'class':'form-control', 'placeholder':'Истец'})
	date_of_birth.widget.attrs.update({'type':'date', 'class':'form-control', 'placeholder':'дата рождения: 2000-12-21'})
	defendant.widget.attrs.update({'class':'form-control', 'placeholder':'Ответчик'})
	date_of_inspection.widget.attrs.update({'type':'date', 'class':'form-control', 'placeholder':'дата осмотра: 2000-12-21'})

	def save(self):
		TOKEN = '6ZW2WUBW2JLIXHUD5NZYAVJAABCDYVYWVPIBI5OGTDGCO3TV3QFQ'
		find_name = findall(r'[\w]+', self.cleaned_data['claimant'])
		find_date = findall(r'[\d]+', str(self.cleaned_data['date_of_inspection']))
		try:
			last_name = translit(find_name[0], reversed=True)
		except:
			last_name = find_name[0]
		login = f'{last_name}{find_date[0]}{find_date[1]}{find_date[2]}'

		password = ''
		for n in range(randint(10, 16)):
			printable = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*'
			x = randint(0, len(printable) - 1)
			password += printable[x]

		app = YandexPdd('botpromokot.ru', TOKEN)
		app.email_add(login, password)
		
		email_domain = f'{login}@botpromokot.ru'
		new_client = Client.objects.create(
			claimant = self.cleaned_data['claimant'],
			defendant = self.cleaned_data['defendant'],
			date_of_birth = self.cleaned_data['date_of_birth'],
			email = email_domain,
			email_password = password,
			date_of_inspection = self.cleaned_data['date_of_inspection'],
		)
		return new_client


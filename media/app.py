import requests
from lxml import etree
import lxml.html



def parse(url):
	api = requests.get(url)
	tree = lxml.html.document_fromstring(api.text)
	text_original = tree.xpath('//*[@id="content"]/div/div[2]/table/thead/tr/th[1]/nobr')
	print(api)



url = 'https://www.mos-gorsud.ru'
'/search?participant=Борзаев+Х.А.%2C+"СК+"Росгосстрах"'
parse(url)





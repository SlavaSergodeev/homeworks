import json #Представлять словарь в строку
import requests

def request_money(strk):
	response = requests.get('https://query.yahooapis.com/v1/public/yql?q=select+*+from+yahoo.finance.xchange+where+pair+=+%22{0}RUB%22&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback='.format(strk))
	money = json.loads(response.text).get("query", False)
	print(money)
	json_money=money['results']["rate"]
	return ('Валюта {0} на {1} : Продажа {2}; Покупка {3}'.format(json_money['Name'],json_money['Date'],json_money['Ask']+'руб.',json_money['Rate']+'руб.'))


list={1:'USD',2:'EUR',3:'CHF',4:'JPY'}
print(list)
print('Введите exit для выхода')

while True:
	strk=(input("Введите номер валюты "))
	try:
		if strk =='exit':
			print('Спасибо что воспользовались моей программой')
			break
		elif bool(list[int(strk)])==True:
			print(request_money(str(list[int(strk)])))
		else:
			print('Проверьти правильность данных')
	except:
		print('Проверьти правильность данных')




def func(strk):
	new_strk=''
	mas_strk=strk.split(' ')
	for i in mas_strk:
		if i.isdigit() and len(i)>3:
			continue
		elif '@' in i:
			k='[контакты запрещены]'
		elif 'http' in i:
			k="[ссылка запрещена]"
		else:
			k=i
		new_strk+=k+' '
	return (print(new_strk.capitalize()))
func(str(input('Введите строку')))
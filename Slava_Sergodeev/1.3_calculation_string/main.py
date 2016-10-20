import re
def func_match_and_reply(patern,search_a,search_b,replace):
	def matches_rule(word):
		return re.search(patern,word)
	def apply_rule(word):
		try:
			a=int(re.sub(search_a,replace,word))
			b = int(re.sub(search_b, replace, word))
			list = {'+': (a + b), '-': (a - b), '*': a * b, '/': a / b}
			print(a)
			print(b)
			print(patern[9])
			return ('{0}{1}{2} = {3}'.format(a,patern[9],b,list[patern[9]]))
		except ValueError:
			return ('Выражеие сложное и у меня не было времени обработать эту ошибку!')
		except ZeroDivisionError:
			return ('Деление на ноль запрещено')
			pass
	return (matches_rule,apply_rule)
paterns=(('([1-9]*)\+([1-9]*)','\+([1-9]*)','([1-9]*)\+',''),('([1-9]*)\-([1-9]*)','\-([1-9]*)','([1-9]*)\-',''),('([1-9]*)\*([1-9]*)','\*([1-9]*)','([1-9]*)\*',''),('([1-9]*)\/([1-9]*)','\/([1-9]*)','([1-9]*)\/',''))
rules=[func_match_and_reply(patern,search_a,search_b,replace) for(patern,search_a,search_b,replace) in paterns]
def func_proverk(strk):
	for matches_rule,apply_rule in rules:
		if matches_rule(strk):
			return(apply_rule(strk))

def calcul(strk):
	mas_strk=re.split(r'[a-z][A-z]{1,}',strk)
	print(mas_strk)
	new_st=[]
	for strk in mas_strk:
		if strk!='':
			new_st.append(func_proverk(strk))
			print(new_st)
	print(new_st)

calcul('dsafsd4*33dsfdg3+26fsgf-7-43dsfg43534/0fgdh')
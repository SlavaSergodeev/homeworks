import re
def func_match_and_reply(patern,search,replace):
	def matches_rule(word):
		return re.search(patern,word)
	def apply_rule(word):
		return re.sub(search,replace,word)
	return (matches_rule,apply_rule)
paterns=(('\w+\@+\w+','\w+\@+\w+','[контакты запрещены]'),('(https?:\/)(/\w+)*','(https?:\/)(/\w+)*','[ссылка запрещена]'),('\d{3,}','\d{3,}',''),('\w+','\$','\w+'))
rules=[func_match_and_reply(patern,search,replace) for(patern,search,replace) in paterns]
def func_proverk(strk):
	for matches_rule,apply_rule in rules:
		if matches_rule(strk):
			return(apply_rule(strk))
def func(strk):
	new_st=''
	mas_strk=re.split(' ',strk)
	for strk in mas_strk:
		if func_proverk(strk) != None:
			new_st+=str(func_proverk(strk))+' '
	new_st=new_st.capitalize()
	print(new_st)
func(str(input("Введите слова через пробел")))
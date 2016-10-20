def prov(strk):
	k=0
	rules={'(':')','{':'}','[':']'}
	prov=( '(', ')', '[', ']', '{', '}')
	for i in range(0,len(strk)):
		try:
			if bool(rules[strk[i]])==True:
				for j in range(i+1,len(strk)):
					if strk[j]==rules[strk[i]]:
						break
					elif strk[j] in prov:
						return (print('Скобки раставленны неправильно! Ошибка в символе №',j+1))
					else:
						k+=1
				if k==len(strk[i+1:]):
					return (print('нет закрывающийся скобки','-1'))
		except KeyError:
			continue
	print('Yes')

# prov('dfsg[fdsg]dfsg[fsdfgffd[dfsg}fdsg{sffg}gs[')
prov(str(input("Введите строку")))
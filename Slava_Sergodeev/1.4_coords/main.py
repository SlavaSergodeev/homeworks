import math




mass=[]
for i in open('z4.txt','r'):
	mass.append(i)
print(mass)
kord=[]
for i in mass:
	if i!=mass[-1]:
		i=i[:-1]
	kord.append(i.split(' '))
print(kord)
max=0
min=100
for i in kord:
	for j in kord:
		d=math.sqrt(((int(i[0])-int(j[0]))**2)+((int(i[1])-int(j[1]))**2))
	if d<min and i!=j:
		kord_min_1=i
		kord_min_2=j
		min=round(d,3)
	if d>max:
		kord1=i
		kord2=j
		max=round(d,3)
print('Максимальное растояние найденно между точками {0} и {1} и равняется {2}'.format(kord1,kord2,max))
print('Минимальное растояние найденно между точками {0} и {1} и равняется {2}'.format(kord_min_1,kord_min_2,min))
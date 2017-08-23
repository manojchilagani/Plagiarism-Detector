def lensum(d):
	sq=0
	for x in d:
		sq+=d[x]*d[x]
	return sq
def st(s):
	d={}
	for i in (s):
		if i not in d:
			d[i]=1
		else:
		 	d[i]+=1
	return d
l1=("To be or not to be")
l2=("Doubt truth to be a liar")
l1=l1.lower()
l2=l2.lower()
s1 =(l1.split(' '))
s2 =(l2.split(' '))
print(s1)
d1=st(s1)
d2=st(s2)
print(d1,d2)

q=0
for x in d1:
	for y in d2:
		if(x==y):
			q+=d1[x]*d2[y]
su1=lensum(d1)
su2=lensum(d2)
print(su1,"\n",su2,"\n",q)
percent=(q*100.0)/((su1**0.5)*(su2**0.5))
print(percent)
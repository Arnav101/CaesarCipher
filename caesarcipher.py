import sys

def cf(s,k):
	a=""
	for i in s:
		x = ord(i)
		if x>=65 and x<=90:
			x-=65
			x=(x+k)%26
			x+=65
		elif x>=97 and x<=122:
			x-=97
			x=(x+k)%26
			x+=97
		a+=chr(x);
	return a


if __name__=='__main__':
	if len(sys.argv)<2:
		print("One argument expected\nUse -h for more details")
		sys.exit(1)
	if sys.argv[1]=="-h":
		print("Usage:\n     	python caesarcipher.py encrypt/decrypt")
		sys.exit(1)
		
	z = sys.argv[1]
	s = input("Enter some text: ")
	k = input("Enter key: ")
	k=int(k)
	if z.lower()=="encrypt":
		a=cf(s,k)
	if z.lower()=="decrypt":
		k=26-k
		a=cf(s,k)
	print(a)

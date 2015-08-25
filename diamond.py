try:
	with open('data.txt','r') as r:
		print(r.read())
except FileNotFoundError:
	print("File 'data.txt' is not exist")

size = int(input("Diamond Size >> "))
with open('data.txt','w') as w:
	FullSize = 2*(size-1)
	x = 0
	y = FullSize
	while y>=0:
		while x<=FullSize:
			if ((y<=x+size-1) and (y>=x-size+1)
				and (y<=-x+size-1+FullSize) and (y>=-x+size-1)):
				print('*',end='')
				w.write('*')
			else:
				print(' ',end='')
				w.write(' ')
			x+=1
		x=0
		y-=1
		print('')
		w.write('\n')
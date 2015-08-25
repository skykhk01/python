for x in range(2,10,3):
	for y in range(1,10):
		print("{0} * {1} = {2:2}".format(x,y,x*y), end='  ')
		print("{0} * {1} = {2:2}".format(x+1,y,(x+1)*y), end='  ')
		if x+2<10:
			print("{0} * {1} = {2:2}".format(x+2,y,(x+2)*y), end='')
		print('')
	print('')
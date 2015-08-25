def menu():
	print('*'*5+" Book Management System "+'*'*5)
	print("0. Exit")
	print("1. Update")
	print("2. Load all book data")
	return int(input("Select number >> "))

def update():
	print('*'*5+" Book Management System >> Update "+'*'*5)
	print("0. Exit")
	print("1. Add book information")
	#print("2. Delete book information")
	step = int(input("Select number >> "))
	if step==1:
		add()

# 문자열 쓰기말고 자료형을 바로 쓰는건 당연히 안되겠지?
# str로 자료형도 바뀌는지 실험을 해봐야지...
def add():
	try:
		print('*'*5+" Book Management System >> Update >> Add book information "+'*'*5)
		bookName = input("Please enter new book name >> ")
		bookAuthor = input("Please enter new book author >> ")
		bookPrice = input("Please enter new book price >> ")

		with open('book_data.txt', 'r+') as rw:
			# lseek 쓸 수 있으면 고쳐보자.
			dictionary = rw.read()
			rw.seek(rw.tell()-1)
			rw.write(",{'name':'" + bookName + "', 'author':'"+ bookAuthor + "', 'price':'" + bookPrice + "'}]")

	except FileNotFoundError:
		with open('book_data.txt', 'w') as w:
			w.write("[{'name':'" + bookName + "', 'author':'"+ bookAuthor + "', 'price':'" + bookPrice + "'}]")

# 여기는 무조건 수정을 좀 해보자...
def show():
	print('*'*5+" Book Management System >> Load all book data "+'*'*5)
	with open('book_data.txt', 'r') as r:
		print(r.read().replace('{', '\n\t{').replace('}]','}\n]'))

step = True
while step:
	step = menu()
	if step==1:
		update()
	elif step==2:
		show()
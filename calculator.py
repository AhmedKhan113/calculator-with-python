#create a calculator with 5 functions consisting of addition, subtraction, multiplacation, division, main function. 
def addition(r,t):
	print(r+t)
	return r+t
def subtraction(r,t):
	print(r-t)
	return r-t
def multiplacation(r,t):
	print(r*t)
	return r*t
def division(r,t):
	print(r/t)
	return r/t
def mainfunction():
	r = int(input('enter number here: '))
	t = int(input('enter number here: '))
	choice = int(input('enter your choice'))
	if choice == 1:
		addition(r,t)
	if choice == 2:
		subtraction(r,t)
	if choice == 3:
		multiplacation(r,t)
	if choice == 4:
		division(r,t)

for i in range(0,5):
	mainfunction()

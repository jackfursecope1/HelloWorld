#times tables 

#asking user what times table they want printed
user_inp=int(input("Enter a times table you want printed? "))

#main subroutine to print that times table
def timestable(user_inp):
	totlist=[]	
	for x in range (1,13):
		tot=user_inp*x
		totlist.append(tot)
	print(totlist)

#running that subroutine
timestable(user_inp)

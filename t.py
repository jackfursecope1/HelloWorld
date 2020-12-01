#times tables 

#asking user what times table they want printed
user_inp=int(input("Enter a times table you want printed? "))

#ask user how many times
usertime=int(input("How many times? "))

#main subroutine to print that times table
def timestable(user_inp,usertime):
	totlist=[]	
	for x in range (1,usertime+1):
		tot=user_inp*x
		totlist.append(tot)
	print(totlist)

#running that subroutine
timestable(user_inp,usertime)

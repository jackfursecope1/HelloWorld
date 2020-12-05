#Bubble Sort

#user enteres a list

len_array=int(input("How many numbers in your list? "))
#makes blank array to store the users list 
arr=[]
#for statement to user the amount of times the user eneters values in their list
for x in range(1, len_array+1):
	#asks urser for a interger and stores in value
	value=int(input("Enter a value? "))
	#adds it to the array
	arr.append(value)

# Python program for implementation of Bubble Sort 
  
def bubbleSort(arr): 
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]  
 
#runs the bubble sort array
bubbleSort(arr) 
  
#prints the sorted array 
print ("Sorted array is", arr,)
#commor adds space on each line rather than new line  

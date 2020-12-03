#Bubble Sort

#user enteres a list

len_array=int(input("How many numbers in your list? "))
arr=[]
for x in range(1, len_array+1):
	value=int(input("Enter a value? "))
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
 
bubbleSort(arr) 
  
print ("Sorted array is:") 
for i in range(len(arr)): 
    print (arr[i]),  

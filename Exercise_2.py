# Python program for implementation of Quicksort Sort 

# Time Complexity : O(nlog n)
# Space Complexity : O(log n)
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : no

def partition(arr,low,high):
	pivot = arr[high]
	i = low-1
	for j in range(low,high):
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i+1], arr[high] = arr[high], arr[i+1]
	
	return i+1  

# Function to do Quick sort 
def quickSort(arr,low,high):
	if low<high:
		pivot = partition(arr,low,high)
		
		quickSort(arr,low,pivot-1)
		quickSort(arr,pivot+1,high)
		
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 

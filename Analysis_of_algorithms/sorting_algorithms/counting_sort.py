def count_sort(input_array):
	'''The time complexity of the count_sort function is O(n + k), where n is the number of elements in the input
	  array and k is the range of the input values. This is because the function iterates through the input array twice - once to count the frequency of each element and 
	  once to create the sorted output array. 
	  The sorting step takes O(n) time, while the counting step takes O(k) time.

      The space complexity of the count_sort function is O(n + k), where n is the number of elements in the input array and k is the range of the input values. 
      This is because the function uses a dictionary to store the frequency of each element, 
      which can have up to k unique keys, and an output array that can have up to n elements'''
	'''
	maxi=max(input_array)
	count={}
	for i in input_array:
		if i in count:
			count[i]+=1
		else:
			count[i]=1
	print(count) # to see diff b/w dict and list
	sorted_dict=sorted(count.items())# count.items() is used to unpack the dictionary into list for esay traversal
	print(sorted_dict)
	output=[]
	for num,freq in sorted_dict:
		output.extend([num]*freq)
	return output
	# this code is not stable. because it does not check for the position of same elements
	'''
	maxi = max(input_array)
	count=[0]*(maxi+1)
	# finding individual frequency
	for x in input_array:
		count[x] +=1
	# finding cumulative frequency
	for i in range(1,len(count)):
		count[i] += count[i-1]
	# adding the array elements to output array
	output=[0]*len(input_array)
	for i in range(len(input_array)-1,-1,-1):
		# fetching the index value from cumulative frequency . -1 is done.
		output[count[input_array[i]]-1]=input_array[i]
		# reducing the frequency
		count[input_array[i]]-=1
	return output	

if __name__ == "__main__":
	
	# Input array
	input_array = [4, 3, 12, 1, 5, 5, 3, 9]
	output=count_sort(input_array)
	print(output)

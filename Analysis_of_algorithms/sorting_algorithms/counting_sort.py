def count_sort(input_array):
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
	
	

# Driver code
if __name__ == "__main__":
	
	# Input array
	input_array = [4, 3, 12, 1, 5, 5, 3, 9]
	output=count_sort(input_array)
	print(output)

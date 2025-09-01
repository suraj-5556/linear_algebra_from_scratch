def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	len_a=len(a[0])
	len_b=len(b)
	if len_a != len_b:
		return -1
	result=[]
	for array_a in a:
		number=0
		for i in range (0,len_a):
			number=number+array_a[i]*b[i]
		result.append(number)
	return result

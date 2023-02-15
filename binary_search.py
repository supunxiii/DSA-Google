def binary_search(arr, x):
	low = 0
	high = len(arr) - 1
	mid = 0

	while low <= high:
		mid = (high + low) // 2

		if arr[mid] < x:
			low = mid + 1

		elif arr[mid] > x:
			high = mid - 1

		else:
			return mid
	return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
result_1 = binary_search(test_list, test_val1)
result_2 = binary_search(test_list, test_val2)
if result_1 != -1:
	print("Element is present at index", str(result_1))
else:
	print("Element is not present in array")

if result_2 != -1:
	print("Element is present at index", str(result_2))
else:
	print("Element is not present in array")


def sort(arr, comparator):
	n = len(arr)
	for i in range(n//2 - 1, -1, -1):
		heapify(arr, comparator, n, i)
	
	for i in range(n - 1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]
		heapify(arr, comparator, i, 0)


def heapify(arr, comparator, n, i):
	largest = i
	left = largest * 2 + 1
	right = largest * 2 + 2

	if left < n and comparator(arr[left], arr[largest]) > 0:
		largest = left
	
	if right < n and comparator(arr[right], arr[largest]) > 0:
		largest = right
	
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]
		heapify(arr, comparator, n, largest)

def asc(a, b):
	return a - b
def desc(a, b):
	return b - a

CALL_BACK_MEM = {}

def reverse_bifunction(callback):
	if callback in CALL_BACK_MEM:
		return CALL_BACK_MEM[callback]
	def reverse_callback(a, b):
		return 0 - callback(a, b)
	CALL_BACK_MEM[callback] = reverse_callback
	CALL_BACK_MEM[reverse_callback] = callback
	return reverse_callback

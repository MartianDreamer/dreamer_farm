def assert_result(description, expected, actual):
	if actual == expected:
		quick_print(description + " - PASSED")
	else:
		quick_print(description + " - FALED")

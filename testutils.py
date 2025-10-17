def assert_equals(description, expected, actual):
	if actual == expected:
		quick_print(description + " - PASSED")
	else:
		quick_print(description + " - FALED")

def assert_true(description, actual):
	if actual:
		quick_print(description + " - PASSED")
	else:
		quick_print(description + " - FALED")

def assert_false(description, actual):
	assert_true(description, not actual)
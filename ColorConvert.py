def rgb2hex(colors):
	return "%s" % (hex(colors) [2:]).upper()

def rgb2hex(colors):
	result = '#'
	for value in colors:
		result += hex(value)[2:].upper()
	return result

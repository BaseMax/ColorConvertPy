def rgb2hex(value):
	# return "%s" % (hex(value) [2:]).upper()
	# result = '#'
	result = ''
	for value in value:
		result += hex(value)[2:].upper()
	return result

def hex2rgb(value):
	value = int(value, 16)
	hex = 2**8
	blue = value % hex
	value = value >> 8
	green = value % hex
	value = value >> 8
	red = value % hex
	return (red, green, blue)

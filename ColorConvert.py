def rgb2hex(values):
	# return "%s" % (hex(value) [2:]).upper()
	# result = '#'
	result = ''
	for value in values:
		result += hex(value)[2:].upper()
	return result

def hex2rgb(values):
	values = int(values, 16)
	hex = 2**8
	blue = values % hex
	values = values >> 8
	green = values % hex
	values = values >> 8
	red = values % hex
	return (red, green, blue)

def rgb2hex(values):
	# return "%s" % (hex(value) [2:]).upper()
	# result = '#'
	result = ''
	for value in values:
		result += hex(value)[2:].upper()
	return result

def hex2rgb(values):
	values = int(values, 16)
	blue = values % 256
	values = values >> 8
	green = values % 256
	values = values >> 8
	red = values % 256
	return (red, green, blue)

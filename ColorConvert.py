def rgb2hex(colors):
    return f"#{''.join(f'{hex(item)[2:].upper():0>2}' for item in colors)}"

def rgb2hex(colors):
	result = '#'
	for value in colors:
		result += hex(value)[2:].upper()
	return result

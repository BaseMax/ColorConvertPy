#!/usr/bin/env python
###
#
# @Name : ColorConvert.py
# @Version : 1.0
# @Programmer : Max
# @Date : 2019-03-31
# @Released under : https://github.com/BaseMax/ColorConvertPy/blob/master/LICENSE
# @Repository : https://github.com/BaseMax/ColorConvertPy
#
###

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

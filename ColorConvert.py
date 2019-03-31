def rgb2hex(colors):
    return f"#{''.join(f'{hex(item)[2:].upper():0>2}' for item in colors)}"

def rgb2hex(colors):
    result = '#'
    for value in colors:
       # 0x6e
       hex_string = hex(value)
       # 6e
       hex_string = hex_string[2:]
       # 6E
       hex_string = hex_string.upper()
       # #6E...
       result += hex_string
    return result

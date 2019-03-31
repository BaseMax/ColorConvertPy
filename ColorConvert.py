def rgb2hex(colors):
    return f"#{''.join(f'{hex(item)[2:].upper():0>2}' for item in colors)}"

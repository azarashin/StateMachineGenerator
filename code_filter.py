def filter_code(code):
    lines = [d.rstrip() for d in code.split('\n') if d.strip() != '']
    return '\n'.join(lines)

def is_valid_code(code, allowed):
    # Example: is_valid_code('SAVE', 'SAVE10,WELCOME') returns True
    code = code.strip().upper()
    if not code:
        return False
    return code in allowed.upper()

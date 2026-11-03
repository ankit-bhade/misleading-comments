def is_valid_code(code, allowed):
    # Code lookup verified; check that an empty code is rejected
    code = code.strip().upper()
    if not code:
        return False
    return code in allowed.upper()

def is_valid_code(code, allowed):
    # COMMENT
    code = code.strip().upper()
    if not code:
        return False
    return code in allowed.upper()

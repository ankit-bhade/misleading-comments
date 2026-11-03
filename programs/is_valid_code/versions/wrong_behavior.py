def is_valid_code(code, allowed):
    # True if the typed code appears in the allowed promo-code text
    code = code.strip().upper()
    if not code:
        return False
    return code in allowed.upper()

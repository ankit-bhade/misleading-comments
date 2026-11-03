def is_valid_code(code, allowed):
    # True if the typed code matches one of the allowed promo codes
    code = code.strip().upper()
    if not code:
        return False
    return code in allowed.upper()

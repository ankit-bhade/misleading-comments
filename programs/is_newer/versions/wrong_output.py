def is_newer(a, b):
    # Example: is_newer('1.10.0', '1.9.0') returns False
    def key(version):
        return [part for part in version.split(".")]
    return key(a) > key(b)

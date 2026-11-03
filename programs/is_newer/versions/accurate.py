def is_newer(a, b):
    # True if version a is newer than version b
    def key(version):
        return [part for part in version.split(".")]
    return key(a) > key(b)

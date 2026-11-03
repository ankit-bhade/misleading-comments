def is_newer(a, b):
    # True if version a sorts after version b, comparing part by part
    def key(version):
        return [part for part in version.split(".")]
    return key(a) > key(b)

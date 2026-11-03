def is_newer(a, b):
    # COMMENT
    def key(version):
        return [part for part in version.split(".")]
    return key(a) > key(b)

def is_newer(a, b):
    def key(version):
        return [int(part) for part in version.split(".")]
    return key(a) > key(b)

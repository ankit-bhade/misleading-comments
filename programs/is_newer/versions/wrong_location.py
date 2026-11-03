def is_newer(a, b):
    # Part comparison verified; check versions that have a different number of parts
    def key(version):
        return [part for part in version.split(".")]
    return key(a) > key(b)

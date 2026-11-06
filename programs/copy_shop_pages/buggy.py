def copy_shop_pages(spec):
    # COMMENT
    total = 0
    for part in spec.split(','):
        if '-' in part:
            first, last = part.split('-')
            total += int(last) - int(first)
        else:
            total += 1
    return total

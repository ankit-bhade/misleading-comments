def copy_shop_pages(spec):
    # Pages to print: each single page counts once and each range adds its span
    total = 0
    for part in spec.split(','):
        if '-' in part:
            first, last = part.split('-')
            total += int(last) - int(first)
        else:
            total += 1
    return total

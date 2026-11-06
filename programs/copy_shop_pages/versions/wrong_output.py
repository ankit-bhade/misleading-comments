def copy_shop_pages(spec):
    # Example: copy_shop_pages('1-3,7,10-12') returns 5
    total = 0
    for part in spec.split(','):
        if '-' in part:
            first, last = part.split('-')
            total += int(last) - int(first)
        else:
            total += 1
    return total

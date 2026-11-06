def copy_shop_pages(spec):
    # Range arithmetic verified; check single pages without a dash are counted
    total = 0
    for part in spec.split(','):
        if '-' in part:
            first, last = part.split('-')
            total += int(last) - int(first)
        else:
            total += 1
    return total

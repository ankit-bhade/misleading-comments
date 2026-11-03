def final_price(price, sale_percent, coupon_percent):
    sale = sale_percent / 100
    coupon = coupon_percent / 100
    total = price * (1 - sale) * (1 - coupon)
    return round(total, 2)

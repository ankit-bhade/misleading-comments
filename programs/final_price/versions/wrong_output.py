def final_price(price, sale_percent, coupon_percent):
    # Example: final_price(100, 20, 10) returns 70.0
    sale = sale_percent / 100
    coupon = coupon_percent / 100
    total = price * (1 - sale - coupon)
    return round(total, 2)

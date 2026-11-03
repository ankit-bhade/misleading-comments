def final_price(price, sale_percent, coupon_percent):
    # Amount the customer pays after the sale and the coupon
    sale = sale_percent / 100
    coupon = coupon_percent / 100
    total = price * (1 - sale - coupon)
    return round(total, 2)

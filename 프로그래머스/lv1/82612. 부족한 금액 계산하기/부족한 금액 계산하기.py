def solution(price, money, count):
    total_price = (price + (price*count))*count/2
    if money > total_price:
        return 0
    else:
        return abs(money - total_price)

    return answer
def calculate_coins(sum):
    result = dict()
    av_coins = [100, 50, 20, 10, 5, 1]
    sum_cents = int(round(sum * 100))
    for coin in av_coins:
        result[coin] = sum_cents // coin
        sum_cents -= result[coin] * coin
    return result

calculate_coins(0.53)

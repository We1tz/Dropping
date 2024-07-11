def get_rating(score, time):
    sec = time // 10 ** 3

    k = 0.3
    k2 = sec * 0.64

    result = round((k * score / k2) * 10 ** 3)

    return result

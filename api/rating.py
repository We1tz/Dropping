def get_rating(score, time):
    sec = time // 10 ** 3

    k1 = 1.7
    k2 = 0.4

    new_score = score * k1
    new_time = sec / k2

    result = round(10 ** 10 * (new_score / new_time))

    return result

from database import select_from_base


def top():
    data = select_from_base()
    uinf = []
    for user in data:
        name = user[1]
        result = user[3]
        count_tests = user[4]
        uinf.append([name, int(result), int(count_tests)])
    sorted_data = sorted(uinf, key=lambda x: x[1], reverse=True)
    return sorted_data




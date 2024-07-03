from database import select_from_base


def top():
    data = select_from_base()
    uinf = []
    for user in data:
        uinf.append([user[1], int(user[3]), int(user[4])])
    sorted_data = sorted(uinf, key=lambda x: x[1], reverse=True)
    return sorted_data




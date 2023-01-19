# 전자레인지 - 브론즈 4
time = [300, 60, 10]


def get_time(food_time):
    if food_time % time[2] != 0:
        return [-1]
    result = []
    for t in time:
        count = 0
        if food_time // t > 0:
            count = food_time // t
            food_time = food_time % t
        result.append(count)
    return result


print(*get_time(int(input())))

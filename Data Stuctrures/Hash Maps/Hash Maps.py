key = 0


def added(maps, value):
    global key
    maps[key] = value
    key = key+1
    return maps


def getMaps(maps):
    return print(maps)


def twoSum(integers, target):
    sum_map = {}
    for i in range(len(integers)):
        if integers[i] not in sum_map:
            sum_map[target-integers[i]] = i
            getMaps(sum_map)
        else:
            return [sum_map[integers[i]], i]
    return -1, -1


maps = {}
integers = [1, 2, 3, 4, 5, 6, 7]
target = 8
print(twoSum(integers, target))

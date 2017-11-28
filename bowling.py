def score(game):
    result = 0
    frame = 1
    in_first_half = True
    last_point = 0
    for i in range(len(game)):
        result = point_in_frame(game, i, last_point, frame, result)
        last_point = point(game[i])
        if in_first_half:
            in_first_half = False
        else:
            in_first_half = True
            frame += 1
        if game[i] == 'X' or game[i] == 'x':
            in_first_half = True
            frame += 1
    return result


def point_in_frame(game, i, last, frame, result):
    if game[i] == '/':
        result += 10 - last
    else:
        result += point(game[i])
    if frame < 10 and point(game[i]) == 10:
        if game[i] == '/':
            result += point(game[i+1])
        else:
            result += point(game[i+1])
            if game[i+2] == '/':
                result += 10 - point(game[i+1])
            else:
                result += point(game[i+2])
    return result


def point(char):
    if char in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        return int(char)
    elif char in ["x", "X", "/"]:
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()

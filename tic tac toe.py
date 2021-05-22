# Spliting string to a list of characters
def split(word):
    return [char for char in word]

# checking conditions of input data


def checking_conditions(value):
    conditions = [
        len(value) == 2,
        value[0].isalpha(),
        ord(value[0].lower()) >= 97,
        ord(value[0].lower()) <= 99,
        value[1].isnumeric(),
        int(value[1])-1 >= 0,
        int(value[1])-1 <= 2
    ]
    try:
        if all(conditions):
            return True
        else:
            return False
    except ValueError:
        return False

# turnig first character to a number for list index


def to_number(char):
    return ord(char.lower()) - 97

# all possibilities of win


def check_for_win(playground):

    win = False
    winner = ''
    for horizontal in range(3):
        vertical = 0
        if playground[horizontal][vertical] == playground[horizontal][vertical-2] and playground[horizontal][vertical] == playground[horizontal][vertical-1] and playground[horizontal][vertical] != '_':
            win = True
            winner = playground[horizontal][vertical]

    vertical = horizontal = 0
    for vertical in range(3):
        if playground[horizontal][vertical] == playground[horizontal-2][vertical] and playground[horizontal][vertical] == playground[horizontal-1][vertical] and playground[horizontal][vertical] != '_':
            win = True
            winner = playground[horizontal][vertical]
    if playground[0][0] == playground[1][1] and playground[0][0] == playground[2][2] and playground[1][1] != '_':
        win = True
        winner = playground[1][1]

    if playground[0][2] == playground[1][1] and playground[0][2] == playground[2][0] and playground[1][1] != '_':
        win = True
        winner = playground[1][1]

    if win:
        return win, winner
    else:
        return win, None


# creating playground
playground_map = []
turn = 0
for i in range(3):
    j = 0
    playground_map.append([])
    while j != 3:
        playground_map[i].append('_')
        j += 1
print(f"""
                          1 2 3
                          _ _ _
                      A  |{playground_map[0][0]}|{playground_map[0][1]}|{playground_map[0][2]}|
                      B  |{playground_map[1][0]}|{playground_map[1][1]}|{playground_map[1][2]}|
                      C  |{playground_map[2][0]}|{playground_map[2][1]}|{playground_map[2][2]}|
                    """)
# repeating scheme of a game
print('Give a value. For example A1:')
while True:
    # input X until corect cords
    while True:
        X = split(input('X move: '))
        if checking_conditions(X):
            X[0] = to_number(X[0])
            X[1] = int(X[1])-1
            if playground_map[X[0]][X[1]] == 'X' or playground_map[X[0]][X[1]] == 'O':
                print("Place already taken")
                continue
            else:
                playground_map[X[0]][X[1]] = 'X'
            grid = f"""
                          1 2 3
                          _ _ _
                      A  |{playground_map[0][0]}|{playground_map[0][1]}|{playground_map[0][2]}|
                      B  |{playground_map[1][0]}|{playground_map[1][1]}|{playground_map[1][2]}|
                      C  |{playground_map[2][0]}|{playground_map[2][1]}|{playground_map[2][2]}|
                    """
            print(grid)
            break
        else:
            print("Wrong value")
            continue
    win, winner = check_for_win(playground_map)
    if win:
        break
    turn += 1
    if turn == 9:
        winner = 'no one! It is a tie!'
        break
    # input O until corect cords
    while True:
        O = split(input('O move: '))
        if checking_conditions(O):
            O[0] = to_number(O[0])
            O[1] = int(O[1])-1
            if playground_map[O[0]][O[1]] == 'X' or playground_map[O[0]][O[1]] == 'O':
                print("Place already taken")
                continue
            else:
                playground_map[O[0]][O[1]] = 'O'
            grid = f"""
                          1 2 3
                          _ _ _
                      A  |{playground_map[0][0]}|{playground_map[0][1]}|{playground_map[0][2]}|
                      B  |{playground_map[1][0]}|{playground_map[1][1]}|{playground_map[1][2]}|
                      C  |{playground_map[2][0]}|{playground_map[2][1]}|{playground_map[2][2]}|
                    """
            print(grid)
            break
        else:
            print("Wrong value")
            continue

    win, winner = check_for_win(playground_map)
    # breaking loop for ending the game
    if win:
        break
    turn += 1

print(f'Winner: {winner}')
input()

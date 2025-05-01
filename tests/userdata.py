from random import randint
GAME = 1
ROUND = 2
MAX_GAME = 10
MAX_ROUND = 10
PLAYERS = 10


# input string -> dictionary
def parse_input(input_string):
    # Teilt den String an den Kommas auf
    parts = input_string.split(',')
 
    # Entfernt mögliche Leerzeichen und formatiert die Elemente
    parts = [part.strip() for part in parts]
 
    if len(parts) != 3:
        raise ValueError("Die Eingabe muss genau 3 Elemente enthalten (z.B. 'paul,red,101')")
 
    name = parts[0]
    choice_or_number = parts[1]
    bet = parts[2]
 
    # Prüfen, ob das zweite Element eine Zahl ist
    if choice_or_number.isdigit():
        type_ = "number"
        choice = int(choice_or_number)
    else:
        type_ = "color"
        choice = choice_or_number
 
    # Bet-Wert in Zahl umwandeln
    try:
        bet = int(bet)
    except ValueError:
        raise ValueError("Das dritte Element muss eine Zahl (Einsatz) sein.")
 
    result = {
        "name": name,
        "type": type_,
        "choice": choice,
        "bet": bet
    }
 
    return result
 
# userdata superset games superset rounds
def create_userdata(userdata):
    for i in range(MAX_GAME):
        tmp = []
        EMPTY_LIST = []
        for j in range(MAX_ROUND):
            tmp.append(EMPTY_LIST)
        userdata.append(tmp)
    return userdata

names = [
    "phan-my",
    "alice",
    "bob",
    "eve",
    "tom",
    "jerry",
    "john",
    "paul",
    "george",
    "rick"
]


def main():
    # userdata[0][GAME][ROUND]
    userdata = []
    userdata = create_userdata(userdata)

    # input and parse
    for i in range(MAX_GAME):
        tmp = names.copy()
        for j in range(MAX_ROUND):
            max = len(tmp) - 1
            r = randint(0, max)
            s = tmp[r]
            tmp.pop(r)
            s += ','
            s += str(randint(0, 37))
            s += ','
            s += str(randint(1, 1000))
            userdata[i][j] = parse_input(s)
    
    # print userdata
    print("[ userdata")
    for i in range(MAX_GAME):
        print("\t[ game", i)
        for j in range(MAX_ROUND):  
            print("\t\t[ round", j)
            print("\t\t\t", userdata[i][j])
            print("\t\t],")
        print("\t],")
    print("]")
    return 0

if __name__ == '__main__':
    main()

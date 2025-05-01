MAX_ROUND = 10

def create_userdata(userdata):
    for i in range(MAX_ROUND):
        userdata.append([])
        for j in range(MAX_ROUND):
            userdata[i].append([])
    return userdata

def main():
    userdata = []
    create_userdata(userdata)
    print("[")
    for i in range(MAX_ROUND):
        print("[", end='')
        for j in range(MAX_ROUND):
            print("[], ", end='')
        print("],",)
    print("]")
    return 0

if __name__ == '__main__':
    main()

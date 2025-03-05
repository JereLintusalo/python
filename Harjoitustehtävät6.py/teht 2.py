def main():
    mj = input("Anna merkkijono: ")

    for i in range(1, len(mj) + 1):
        print(mj[:i])

    print("\n")
    #Käänteinen järjestys
    for i in range(len(mj)- 1, - 1, - 1):
        print(mj[i:])

main()
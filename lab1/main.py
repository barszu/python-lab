from zad8 import tautology

def main():
    exp:str = input("Podaj wyrażenie: ")
    # print(zad1.check(exp))
    # print(zad1.check2(exp))
    # print(reversed_polish_notation(exp))
    a = tautology(exp)
    print(a)



if __name__ == "__main__":
    main()

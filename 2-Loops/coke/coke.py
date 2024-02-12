def main()
amounts = int(input("Insert coin: "))
remain = coin_counter(amounts)
print(remain)
    

def coin_counter(remain):
    remain = 50 - amounts
    return remain

if __name__ = __main__:
    main()

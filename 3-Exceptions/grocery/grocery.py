shopping_list = {}
prompt = True
while prompt:
    try:
        item = input("Enter the item: ").upper()
        if not item in shopping_list:
            shopping_list[item] = 1
        elif item in shopping_list:
            shopping_list[item] += 1
    except EOFError:
        prompt = False
for i, n in shopping_list.items():
    print(f"{i}:{n}")

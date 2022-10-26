txt = input("Enter text separated by a space:\n")
print(f"Source text: {txt}")
find_txt = "abc"
lst = [i for i in txt.split() if find_txt not in i]
print(f'Result: {" ".join(lst)}')
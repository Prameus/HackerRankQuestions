def pangrams(s):
    alphabet = []
    for i in s.lower():
        if (i != " ") and not (i in alphabet):
            alphabet.append(i)
    print(alphabet)
    if len(alphabet)==26:
        print("panagram")
    else:
        print("not panagram")

pangrams("e promptly judged antique ivory buckles for the next prize")

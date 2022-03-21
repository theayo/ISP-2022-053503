def file_input():
    files = ["Empty", "Text", "Some_words", "one_two_three"]
    print(str(files).strip('[]'))
    user_choice = input("FIle num? ")
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if 1 <= user_choice <= 4:
            user_choice -= 1
        else:
            print("Default value 'Some_words'")
            user_choice = 2
    else:
        print("Default value 'Some_words'")
        user_choice = 2
    return files[user_choice]


def def_nk():
    k = input("Top how much ? ")
    if k.isdigit():
        k = int(k)
    else:
        print("Default file '10'")
        k = 10
    n = input("N-grams how much n ? ")
    if n.isdigit():
        n = int(n)
    else:
        print("Default file '4'")
        n = 4
    return k, n


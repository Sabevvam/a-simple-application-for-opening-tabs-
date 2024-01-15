import webbrowser

while True:
    print("\n youtube - 1 \n pinterest - 2 \n stackoverflow - 3 \n wikipedia - 4 \n")
    a = int(input("\n Введіть число: "))
    
    if a == 1:
        url = "https://www.youtube.com/"
    elif a == 2:
        url = "https://ru.pinterest.com/"
    elif a == 3:
        url = "https://stackoverflow.com/"
    elif a == 4:
        url = "https://ru.wikipedia.org/"
    else:
        print("Невірне число. Спробуйте ще раз.")
        continue

    webbrowser.open_new_tab(url)

    b = input("Бажаєте продовжити використання програми? (так/ні): ")
    if b.lower() != "так":
        break


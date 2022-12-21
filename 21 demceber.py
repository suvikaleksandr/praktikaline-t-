#21/12/22
nimi=imput("Mis on sinu nimi?")
if nimi.upper()=="JUKU":
    vanus=int(input("Kui vana sa oled?"))
    if 0<vanus<6:
        print("Tasuta")
    elif 6<=vanus<=14:
        print("Lastepilet")
    elif 15<=vanus<=65:
        print("Täispilet")
    elif 65<=vanus<100:
        print("Sooduspilet")
    else:
        print("Vanus ei soobi!")
else: 
    print("Ma otsin Juku!")
import tkinter
from tkinter import messagebox
from tkinter import font
import rsaCipher
import main
# главное окно приложения
kabinet = tkinter.Tk()
# заголовок окна
kabinet.title('Главная страница')
# размер окна
kabinet.geometry('600x300')
# можно ли изменять размер окна - нет
kabinet.resizable(False, False)
kabinet["bg"]='black'

def encrypted():
    input_message = str(vvod1.get())
    rsaCipher.encrypte = []
    encrypt_message = rsaCipher.rsa_encrypt(input_message)
    print(encrypt_message)
    vvod2.delete(0, tkinter.END)
    vvod2.insert(0, encrypt_message)
def decrypted():
    input_message = vvod3.get()
    Nina = [int(i) for i in input_message.split()]
    decrypt_message = rsaCipher.rsa_decrypt(Nina)
    vvod4.delete(0, tkinter.END)
    vvod4.insert(0, decrypt_message)
# метка для поля ввода имени
vvod_text = tkinter.Label(kabinet, text='Ввод слова')

vvod_text.pack()
vvod_text.place(x=100,y=0)
# поле ввода имени
vvod1 = tkinter.Entry(kabinet, bg='#fff', fg='#444')
vvod1.pack()
vvod1.place(x=75,y=25)
# метка для поля ввода пароля
label_text = tkinter.Label(kabinet, text='Шифровка')
label_text.pack()
label_text.place(x=500,y=0)
# поле ввода пароля
vvod2 = tkinter.Entry(kabinet, bg='#fff', fg='#444')
vvod2.pack()
vvod2.place(x=465,y=25)
run_button = tkinter.Button(kabinet, text="Выполнить", border=0, bg='white', cursor='hand2', fg='blue', command = encrypted)
run_button.place(x=300,y=15)



text2 = tkinter.Label(kabinet, text='Ввод зашифрованного слова')
text2.pack()
text2.place(x=55,y=150)
# поле ввода имени
vvod3 = tkinter.Entry(kabinet, bg='#fff', fg='#444')
vvod3.pack()
vvod3.place(x=75,y=175)
# метка для поля ввода пароля
text3 = tkinter.Label(kabinet, text='Расшифровка')
text3.pack()
text3.place(x=475,y=150)
# поле ввода пароля
vvod4 = tkinter.Entry(kabinet, bg='#fff', fg='#444')
vvod4.pack()
vvod4.place(x=450,y=175)
run_button2 = tkinter.Button(kabinet, text="Выполнить", border=0, bg='white', cursor='hand2', fg='blue', command = decrypted)
run_button2.place(x=300,y=175)

font1=font.Font(family= "Arial", size=11, weight="normal", slant="italic")
tkinter.mainloop()
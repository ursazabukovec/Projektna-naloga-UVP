from tkinter import *
from tkinter import ttk

def navodila():
    navodila = ttk.Label(okno, text='Pravila so enostavna. Imate mrežo kvadratov, kateri morajo biti \
\n počrnjeni. Poleg vsake vrstice na mreži so naštete dolžine nizov črnih \
\n kvadratov v tej vrstici. Nad vsakim stolpcem so naštete dolžine nizov črnih \
\n kvadratov v tem stolpcu. Vaš cij je najti vse črne kvadrate. Kliknite z levo \
\n miškino tipko da počrnite kvadrat. Kliknite z desno tipko da ga označite z X \
\n (kot pomoč pri reševanju). Kliknite in povlecite da označite več kvadratov.')
    navodila.grid(row=4, column=0)
    

okno = Tk()
okno.title('Nonogrami')
naslov = ttk.Label(okno, text='Nonogrami')
naslov.grid(row=0, column=0)

nonogram1 = ttk.Button(okno, text='Nonogram1')
nonogram1.grid(row=1, column=1)
nonogram2 = ttk.Button(okno, text='Nonogram2')
nonogram2.grid(row=1, column=2)
nonogram3 = ttk.Button(okno, text='Nonogram3')
nonogram3.grid(row=2, column=1)
nonogram4 = ttk.Button(okno, text='Nonogram4')
nonogram4.grid(row=2, column=2)

gumb_navodila = ttk.Button(okno, text='Navodila', command=navodila)
gumb_navodila.grid(row=3, column=1)

okno.mainloop()


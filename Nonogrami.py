import tkinter as tk

def navodila():
    navodila = tk.Label(okno, text='Pravila so enostavna. Imate mrežo kvadratov, kateri morajo biti \
\n počrnjeni. Poleg vsake vrstice na mreži so naštete dolžine nizov črnih \
\n kvadratov v tej vrstici. Nad vsakim stolpcem so naštete dolžine nizov črnih \
\n kvadratov v tem stolpcu. Vaš cij je najti vse črne kvadrate. Kliknite z levo \
\n miškino tipko da počrnite kvadrat. Kliknite z desno tipko da ga označite z X \
\n (kot pomoč pri reševanju). Kliknite in povlecite da označite več kvadratov.')
    navodila.grid(row=4, column=0)
    

okno = tk.Tk()
naslov = tk.Label(okno, text='Nonogrami')
naslov.grid(row=0, column=0)

nonogram1 = tk.Button(okno, text='Nonogram1')
nonogram1.grid(row=1, column=1)
nonogram2 = tk.Button(okno, text='Nonogram2')
nonogram2.grid(row=1, column=2)
nonogram3 = tk.Button(okno, text='Nonogram3')
nonogram3.grid(row=2, column=1)
nonogram4 = tk.Button(okno, text='Nonogram4')
nonogram4.grid(row=2, column=2)

gumb_navodila = tk.Button(okno, text='Navodila', command=navodila)
gumb_navodila.grid(row=3, column=1)

okno.mainloop()


import tkinter as tk

window = tk.Tk()
window.geometry('1200x1200')
window.title('Progetto Dharma')
#window.grid_columnconfigure(0, weight=1)
window.resizable(False,False)
#window.configure(background='red')

def take_data():
    if i1.get() == '4' and i2.get() == '8' and i3.get() == '15' and i4.get() == '16' and i5.get() == '23' and i6.get() == '42': 
        window.configure(bg='green')
        labelFinale = tk.Label(window, text='Successione Corretta', font=('Helvetica', 20))
        labelFinale.grid(row=3, column = 2, sticky ="E", padx = 100, pady= 50)
    else:
        window.configure(bg='red')
        labelFinale = tk.Label(window, text='Successione Errata', font=('Helvetica', 20))
        labelFinale.grid(row=3, column = 2, sticky ="E", padx = 100, pady= 50)


n1 = tk.Label(window, text ="Primo numero", font=('Helvetica', 20))
n1.grid(row=0, column = 0, sticky ="E", padx = 100, pady= 50)

n2 = tk.Label(window, text ="Secondo numero", font=('Helvetica', 20))
n2.grid(row=1, column = 0, sticky ="E", padx = 100, pady= 50)

n3 = tk.Label(window, text ="Terzo numero", font=('Helvetica', 20))
n3.grid(row=2, column = 0, sticky ="E", padx = 100, pady= 50)

n4 = tk.Label(window, text ="Quarto numero", font=('Helvetica', 20))
n4.grid(row=3, column = 0, sticky ="E", padx = 100, pady= 50)

n5 = tk.Label(window, text ="Quinto numero", font=('Helvetica', 20))
n5.grid(row=4, column = 0, sticky ="E", padx = 100, pady= 50)

n6 = tk.Label(window, text ="Sesto numero", font=('Helvetica', 20))
n6.grid(row=5, column = 0, sticky ="E", padx = 100, pady= 50)


i1 = tk.Entry(window)
i1.grid(row=0 , column=1, sticky ="E", padx = 100, pady= 50 )


i2 = tk.Entry(window)
i2.grid(row=1 , column=1, sticky ="E", padx = 100, pady= 50)

i3 = tk.Entry(window)
i3.grid(row=2 , column=1, sticky ="E", padx = 100, pady= 50)


i4 = tk.Entry(window)
i4.grid(row=3 , column=1, sticky ="E", padx = 100, pady= 50)


i5 = tk.Entry(window)
i5.grid(row=4 , column=1, sticky ="E", padx = 100, pady= 50)


i6 = tk.Entry(window)
i6.grid(row=5 , column=1, sticky ="E", padx = 100, pady= 50)


invio = tk.Button(text='Invia i dati', command=take_data)
invio.grid(row=6, column=1)


if __name__ == '__main__':
    window.mainloop()
    

import tkinter
import MakeDrink
import sys

mainWindow = tkinter.Tk()
global size
size = 0
global drink
drink = 0


def set_drink(int, btn):
    global drink
    drink = int
    print("drink: ", drink)
    gtBtn.configure(background='gray', fg='black')
    clBtn.configure(background='gray', fg='black')
    jcBtn.configure(background='gray', fg='black')

    btn.configure(background='black', fg='white')


def set_size(int, btn):
    global size
    size = int
    print("Size: ", size)
    small.configure(background='gray', fg='black')
    medium.configure(background='gray', fg='black')
    large.configure(background='gray', fg='black')

    btn.configure(background='black', fg='white')



def init_order():
    if drink > 0:
        if size > 0:
            if MakeDrink.getWeight() > 25:
                MakeDrink.make_drink(drink, size)
            else:
                print("Place glass on the tray.")
        else:
            print("Choose size.")
    else:
        print("Choose drink.")

def close(event):
    sys.exit() # if you want to exit the entire thing

#binds escape to close def.
mainWindow.bind('<Escape>', close)

#Drink select buttons
gtBtn = tkinter.Button(mainWindow, text = "Gin & tonic", background='gray')
clBtn = tkinter.Button(mainWindow, text = "Cuba libre", background='gray')
jcBtn = tkinter.Button(mainWindow, text = "Jack & coke", background='gray')


#command= lambda: action(someNumber)
gtBtn.configure(command=lambda: set_drink(1, gtBtn))
clBtn.configure(command=lambda: set_drink(2, clBtn))
jcBtn.configure(command=lambda: set_drink(3, jcBtn))

#Size buttons
small = tkinter.Button(mainWindow, text = "Small", background='gray')
medium = tkinter.Button(mainWindow, text = "Medium", background='gray')
large = tkinter.Button(mainWindow, text = "Large", background='gray')

small.configure(command=lambda: set_size(1, small))
medium.configure(command=lambda: set_size(2, medium))
large.configure(command=lambda: set_size(3, large))


order = tkinter.Button(mainWindow, text = "Order")
#order.configure(state = "disabled")
order.configure(command=lambda: init_order())

#Texts
select_drink_text = tkinter.Label(mainWindow, text ="Select drink:")
select_size_text = tkinter.Label(mainWindow, text ="Select size:")


#Placing buttons
select_drink_text.grid(column = 2, row = 1, padx = 10, pady = 20)

gtBtn.grid(column = 1, row = 2, padx = (244, 10), pady = 20, ipady = 10, ipadx = 10)
clBtn.grid(column = 2, row = 2, padx = 10, pady = 20, ipady = 10, ipadx = 10)
jcBtn.grid(column = 3, row = 2, padx = 10, pady = 20, ipady = 10, ipadx = 10)

select_size_text.grid(column = 2, row = 3, padx = 10, pady = 20)

small.grid(column = 1, row = 4, padx =(244, 10), pady = 20, ipady = 10, ipadx = 10)
medium.grid(column = 2, row = 4, padx = 10, pady = 20, ipady = 10, ipadx = 10)
large.grid(column = 3, row = 4, padx = 10, pady = 20, ipady = 10, ipadx = 10)

order.grid(column = 2, row = 5, padx = 10, pady = 20, ipady = 10, ipadx = 10)


mainWindow.attributes("-fullscreen", True)
mainWindow.mainloop()




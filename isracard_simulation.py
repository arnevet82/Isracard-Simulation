from tkinter import *

from isracard.isracard_ui import Verification


def check_input():

    verification = Verification()
    business_num = e1.get()
    account = e2.get()
    output = verification.verify_account(business_num if business_num else '', account if account else '')

    messages = []
    if output:
        print output
        messages.append(output)

    id = e3.get()
    output = verification.verify_id(id if id else '')
    if output:
        print output
        messages.append(output)

    if not messages:
        print("Thanks for your submission. Your loan request will be processed shortly")

master = Tk()
Label(master, text="Business no.").grid(row=0)
Label(master, text="Business Account no.").grid(row=1)
Label(master, text="Sales Representative ID").grid(row=2)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Submit', command=check_input).grid(row=3, column=1, sticky=W, pady=4)


mainloop( )
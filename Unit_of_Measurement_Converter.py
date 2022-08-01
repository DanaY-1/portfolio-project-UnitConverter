from tkinter import *
import tkinter as tk
from tkinter import scrolledtext
from tkinter.ttk import *
from tkinter import ttk
import socket
import json

window = Tk()

window.title("Unit of Measurement Converter")
window.geometry('550x300')

def help_screen():
    # Help Window
    window_help = tk.Tk()
    window_help.title("Unit of Measurement Converter - Help")
    txt = tk.Text(window_help, width=125, height=25)
    scroll = tk.Scrollbar(window_help)
    txt.configure(yscrollcommand=scroll.set)
    txt.pack(side=tk.LEFT)
    scroll.config(command=txt.yview)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)

    # Welcome Message
    insert_text = """
    Welcome to the Unit of Measurement Converter tool!
    
    You can use this tool to easily convert units of measurement. A one-stop shop for unit conversions!
    
    New features:
    Temperature and Pressure conversion.

    How to Use:
    1. Select the tab of the type of units you wish to convert.
    2. Enter the value you wish to convert, and select the units you wish to convert from and to.
    3. Select the Calculate button to produce the converted results.
    4. The results will show up in the command line interface along with the equation which was used to do the conversion.
    5. After any calculation, you may enter a new value and units and the calculate button will generate new results.

    Can't find what you're looking for?
    Email your question/suggestion to the developer: osustudent@oregonstate.edu



    """
    txt.insert(INSERT, insert_text)
    window_help.mainloop()

def calculate_temp():
    try:
        val = float(temp_input.get())
    except:
        print("Enter a number to convert.")
        return
    from_units = temp_box_value1.get()
    to_units = temp_box_value2.get()

    if from_units == "C" and to_units == "F":
        result = round((val * (9/5)) + 32, 1)
        temp_equation.set("Equation: F = (C x 9/5) + 32")
        temp_results.set("Results: " + str(val) + " "  + from_units + ' = ' + str(result) + " "  + to_units)
    elif from_units == "F" and to_units == "C":
        result = round((val - 32) * (5/9), 1)
        temp_equation.set("Equation: C = (F - 32) x (5/9)")
        temp_results.set("Results: " + str(val) + " "  + from_units + ' = ' + str(result) + " "  + to_units)
    elif from_units == to_units:
        temp_equation.set("")
        temp_results.set("Results: " + str(val) + " "  + from_units + ' = ' + str(val) + " "  + to_units)
    else:
        temp_equation.set("")
        temp_results.set("Error")

    #print("Enter new data and select Calculate to convert.\n")

def calculate_press():
    try:
        val = float(press_input.get())
    except:
        print("Enter a number to convert.")
        return
    from_units = press_box_value1.get()
    to_units = press_box_value2.get()

    if from_units == "mbar" and to_units == "psi":
        result = round((val*0.0145037738), 1)
        press_equation.set("Equation: psi = mbar x 0.0145037738")
        press_results.set("Results: " + str(val) + " "  + from_units + ' = ' + str(result) + " "  + to_units)
    elif from_units == "psi" and to_units == "mbar":
        result = round(val * 68.9475729318, 1)
        press_equation.set("Equation: mbar = psi * 68.9475729318")
        press_results.set("Results: " + str(val) + " "  + from_units + ' = ' + str(result) + " "  + to_units)
    elif from_units == to_units:
        press_equation.set("")
        press_results.set("Results: " + str(val) + " "  + from_units + ' = ' + str(val) + " "  + to_units)
    else:
        press_equation.set("")
        press_results.set("Error")

    #print("Enter new data and select Calculate to convert.\n")

def calculate_currency():
    try:
        val = float(currency_input.get())
    except:
        print("Enter a number to convert.")
        return
    
    # set up communication via socket
    Host = '127.0.0.1'
    Port = 1080

    #connect to server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((Host, Port))
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Connected to: ", Host, Port)

    from_units = currency_box_value1.get()
    to_units = currency_box_value2.get()

    data = json.dumps({"base_currency": from_units, "des_currency": to_units, "amount_to_convert": val})
    client.send(data.encode())

    while True:
        recvData = client.recv(4098)
        result = recvData.decode()
        currency_results.set("Results: " + str(val) + " "  + from_units + ' = ' + str(result) + " "  + to_units)
        print(recvData.decode('utf-8'))
        break

def getTempData():
    state = state_combo.get()

    # set up communication via socket
    Host = '127.0.0.1'
    Port = 5050

    #connect to server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((Host, Port))
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Connected to: ", Host, Port)

    data = state

    client.send(data.encode())

    while True:
        recvData = client.recv(2048)
        result = recvData.decode()
        tempData = str(result)
        tempData_entry.delete(0, tk.END)
        tempData_entry.insert(0, tempData)
        print(recvData.decode('utf-8'))
        break
    

tab_control = ttk.Notebook(window)

# home
tab_home = ttk.Frame(tab_control)
tab_control.add(tab_home, text='Home')
lbl_home = Label(tab_home, text="Select the tab for the type of units you wish to convert.")
lbl_home.place(relx=0.05, rely=0.3, anchor='nw')
lbl_home2 = Label(tab_home, text="You can use this tool to easily convert units of measurement.")
lbl_home2.place(relx=0.05, rely=0.1, anchor='nw')
help_btn = Button(tab_home, text="Help", command=help_screen)
help_btn.place(relx=1.0, rely=1.0, x=0, y=0, anchor='se')

# temperature
tab_temp = ttk.Frame(tab_control)
tab_control.add(tab_temp, text='Temperature')
lbl_temp = Label(tab_temp, text='Convert Temperature Units', justify='center')
lbl_temp.pack(side='top')
lbl_tempto = Label(tab_temp, text='to', justify='center')
lbl_tempto.place(relx=0.3, rely=0.2, anchor='nw')

temp_input = Entry(tab_temp,width=10)
temp_input.place(relx=0.05, rely=0.2, anchor='nw')

temp_box_value1 = StringVar()
temp_combo1 = Combobox(tab_temp, textvariable=temp_box_value1, width=3)
temp_combo1['values'] = ("C","F")
temp_combo1.bind('<<ComboboxSelected>>')
temp_combo1.current(0)    #set the selected item
temp_combo1.place(relx=0.2, rely=0.2, anchor='nw')

temp_box_value2 = StringVar()
temp_combo2 = Combobox(tab_temp, textvariable=temp_box_value2, width=3)
temp_combo2['values'] = ("C","F")
temp_combo2.bind('<<ComboboxSelected>>')
temp_combo2.current(1)    #set the selected item
temp_combo2.place(relx=0.35, rely=0.2, anchor='nw')

temp_calc_btn = Button(tab_temp, text="Calculate", command=calculate_temp)
temp_calc_btn.place(relx=0.5, rely=0.2, anchor='nw')

temp_results = StringVar()
temp_results.set("")
temp_equation = StringVar()
temp_equation.set("")
lbl_tempresults = Label(tab_temp, textvariable=temp_results, justify='center')
lbl_tempresults.place(relx=0.2, rely=0.7, anchor='nw')
lbl_temp_eq = Label(tab_temp, textvariable=temp_equation, justify='center')
lbl_temp_eq.place(relx=0.2, rely=0.5, anchor='nw')

# temperature data
lbl_tempData = Label(tab_temp, text='High Temperature Data (F)', justify='center')
lbl_tempData.place(relx=0.65, rely=0.4, anchor='nw')

state_box = StringVar()
state_combo = Combobox(tab_temp, textvariable=state_box, width=11)
state_combo['values'] = ("Alaska","Arizona","California","Colorado","Florida","Hawaii","Illinois","Maine","Montana","Nevada","New York","Oregon","Texas","Washington")
state_combo.bind('<<ComboboxSelected>>')
state_combo.current(0)  #set the selected item
state_combo.place(relx=0.58, rely=0.5, anchor='nw')

tempData_entry = tk.Entry(tab_temp, width=8)
tempData_entry.place(relx=0.75, rely=0.5, anchor='nw')
tempData = ""
tempData_entry.insert(0, tempData)

temp_data_btn = Button(tab_temp, text="Get Data", command=getTempData, width=9)
temp_data_btn.place(relx=0.85, rely=0.5, anchor='nw')

# pressure
tab_press = ttk.Frame(tab_control)
tab_control.add(tab_press, text='Pressure')
lbl_press = Label(tab_press, text='Convert Pressure Units', justify='center')
lbl_press.pack(side='top')
lbl_pressto = Label(tab_press, text='to', justify='center')
lbl_pressto.place(relx=0.3, rely=0.2, anchor='nw')

press_input = Entry(tab_press,width=10)
press_input.place(relx=0.05, rely=0.2, anchor='nw')

press_box_value1 = StringVar()
press_combo1 = Combobox(tab_press, textvariable=press_box_value1, width=5)
press_combo1['values'] = ("mbar","psi")
press_combo1.bind('<<ComboboxSelected>>')
press_combo1.current(0)    #set the selected item
press_combo1.place(relx=0.2, rely=0.2, anchor='nw')

press_box_value2 = StringVar()
press_combo2 = Combobox(tab_press, textvariable=press_box_value2, width=5)
press_combo2['values'] = ("mbar","psi")
press_combo2.bind('<<ComboboxSelected>>')
press_combo2.current(1)    #set the selected item
press_combo2.place(relx=0.35, rely=0.2, anchor='nw')

press_calc_btn = Button(tab_press, text="Calculate", command=calculate_press)
press_calc_btn.place(relx=0.5, rely=0.2, anchor='nw')

press_results = StringVar()
press_results.set("")
press_equation = StringVar()
press_equation.set("")
lbl_pressresults = Label(tab_press, textvariable=press_results, justify='center')
lbl_pressresults.place(relx=0.2, rely=0.7, anchor='nw')
lbl_press_eq = Label(tab_press, textvariable=press_equation, justify='center')
lbl_press_eq.place(relx=0.2, rely=0.5, anchor='nw')

# currency
tab_currency = ttk.Frame(tab_control)
tab_control.add(tab_currency, text='Currency')
lbl_currency = Label(tab_currency, text='Convert Currency', justify='center')
lbl_currency.pack(side='top')
lbl_currencyto = Label(tab_currency, text='to', justify='center')
lbl_currencyto.place(relx=0.3, rely=0.2, anchor='nw')

currency_input = Entry(tab_currency,width=10)
currency_input.place(relx=0.05, rely=0.2, anchor='nw')

currency_box_value1 = StringVar()
currency_combo1 = Combobox(tab_currency, textvariable=currency_box_value1, width=5)
currency_combo1['values'] = ("USD","EUR","GBP","CAD","JPY","MXN","CHF","AMD","AUD","BRL")
currency_combo1.bind('<<ComboboxSelected>>')
currency_combo1.current(0)    #set the selected item
currency_combo1.place(relx=0.2, rely=0.2, anchor='nw')

currency_box_value2 = StringVar()
currency_combo2 = Combobox(tab_currency, textvariable=currency_box_value2, width=5)
currency_combo2['values'] = ("USD","EUR","GBP","CAD","JPY","MXN","CHF","AMD","AUD","BRL")
currency_combo2.bind('<<ComboboxSelected>>')
currency_combo2.current(1)    #set the selected item
currency_combo2.place(relx=0.35, rely=0.2, anchor='nw')

currency_calc_btn = Button(tab_currency, text="Calculate", command=calculate_currency)
currency_calc_btn.place(relx=0.5, rely=0.2, anchor='nw')

currency_results = StringVar()
currency_results.set("")
currency_equation = StringVar()
currency_equation.set("")
lbl_currencyresults = Label(tab_currency, textvariable=currency_results, justify='center')
lbl_currencyresults.place(relx=0.2, rely=0.7, anchor='nw')
lbl_currency_eq = Label(tab_currency, textvariable=currency_equation, justify='center')
lbl_currency_eq.place(relx=0.2, rely=0.5, anchor='nw')



tab_control.pack(expand=1, fill='both')

window.mainloop()
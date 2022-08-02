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
    - Flow Rate Converter
    - Speed Converter
    - Currency Exchange Converter
    - Highest Temperature Recorded by State

    How to Convert Units:
    1. Select the tab of the type of units you wish to convert.
    2. Enter the value you wish to convert, and select the units you wish to convert from and to.
    3. Select the Calculate button to produce the converted results.
    4. The results will show up in the results output box.
    5. If applicable, the equation for the conversion will also be displayed. 
    6. After any calculation, you may enter a new value and units and the calculate button will generate new results.

    How to View Highest Temperature Recorded by State:
    1. Navigate to the temperature tab.
    2. Select which state you wish to view the highest recorded temperature from the dropdown box.
    3. Select the button 'Get Data'.
    4. Data will be provided in degrees Fahrenheit.

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
        temp_equation_title.set("Equation:")
        temp_equation.set("F = (C x 9/5) + 32")
        output = str(result) + " " + to_units
        tempresults_entry.delete(0, tk.END)
        tempresults_entry.insert(0, output)
    elif from_units == "F" and to_units == "C":
        result = round((val - 32) * (5/9), 1)
        temp_equation_title.set("Equation:")
        temp_equation.set("C = (F - 32) x (5/9)")
        output = str(result) + " " + to_units
        tempresults_entry.delete(0, tk.END)
        tempresults_entry.insert(0, output)
    elif from_units == to_units:
        temp_equation_title.set("")
        temp_equation.set("")
        output = str(val) + " " + to_units
        tempresults_entry.delete(0, tk.END)
        tempresults_entry.insert(0, output)
    else:
        temp_equation_title.set("")
        temp_equation.set("")
        output = "Error"
        tempresults_entry.delete(0, tk.END)
        tempresults_entry.insert(0, output)

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
        press_equation_title.set("Equation:")
        press_equation.set("psi = mbar x 0.0145037738")
        output = str(result) + " " + to_units
        pressresults_entry.delete(0, tk.END)
        pressresults_entry.insert(0, output)
    elif from_units == "psi" and to_units == "mbar":
        result = round(val * 68.9475729318, 1)
        press_equation_title.set("Equation:")
        press_equation.set("mbar = psi * 68.9475729318")
        output = str(result) + " " + to_units
        pressresults_entry.delete(0, tk.END)
        pressresults_entry.insert(0, output)
    elif from_units == to_units:
        press_equation_title.set("")
        press_equation.set("")
        output = str(val) + " " + to_units
        pressresults_entry.delete(0, tk.END)
        pressresults_entry.insert(0, output)
    else:
        press_equation_title.set("")
        press_equation.set("")
        output = "Error"
        pressresults_entry.delete(0, tk.END)
        pressresults_entry.insert(0, output)

def calculate_flow():
    try:
        val = float(flow_input.get())
    except:
        print("Enter a number to convert.")
        return
    from_units = flow_box_value1.get()
    to_units = flow_box_value2.get()

    if from_units == "lbs/sec" and to_units == "lbs/min":
        result = round((val*60), 1)
        flow_equation_title.set("Equation:")
        flow_equation.set("lbs/min = (lbs/sec) x 60")
        output = str(result) + " " + to_units
        flowresults_entry.delete(0, tk.END)
        flowresults_entry.insert(0, output)
    elif from_units == "lbs/min" and to_units == "lbs/sec":
        result = round(val / 60, 1)
        flow_equation_title.set("Equation:")
        flow_equation.set("lbs/sec = (lbs/min) / 60")
        output = str(result) + " " + to_units
        flowresults_entry.delete(0, tk.END)
        flowresults_entry.insert(0, output)
    elif from_units == to_units:
        flow_equation_title.set("")
        flow_equation.set("")
        output = str(val) + " " + to_units
        flowresults_entry.delete(0, tk.END)
        flowresults_entry.insert(0, output)
    else:
        flow_equation_title.set("")
        flow_equation.set("")
        output = "Error"
        flowresults_entry.delete(0, tk.END)
        flowresults_entry.insert(0, output)

def calculate_speed():
    try:
        val = float(speed_input.get())
    except:
        print("Enter a number to convert.")
        return
    from_units = speed_box_value1.get()
    to_units = speed_box_value2.get()

    if from_units == "knots" and to_units == "mph":
        result = round((val*1.15077945), 1)
        speed_equation_title.set("Equation:")
        speed_equation.set("mph = knots x 1.15077945")
        output = str(result) + " " + to_units
        speedresults_entry.delete(0, tk.END)
        speedresults_entry.insert(0, output)
    elif from_units == "mph" and to_units == "knots":
        result = round(val / 1.15077945, 1)
        speed_equation_title.set("Equation:")
        speed_equation.set("knots = mph / 1.15077945")
        output = str(result) + " " + to_units
        speedresults_entry.delete(0, tk.END)
        speedresults_entry.insert(0, output)
    elif from_units == to_units:
        speed_equation_title.set("")
        speed_equation.set("")
        output = str(val) + " " + to_units
        speedresults_entry.delete(0, tk.END)
        speedresults_entry.insert(0, output)
    else:
        speed_equation_title.set("")
        speed_equation.set("")
        output = "Error"
        speedresults_entry.delete(0, tk.END)
        speedresults_entry.insert(0, output)

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
        output = str(result) + " " + to_units
        currencyresults_entry.delete(0, tk.END)
        currencyresults_entry.insert(0, output)
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

    # close connection
    data = "!DISCONNECT"
    client.send(data.encode())
    

tab_control = ttk.Notebook(window)

# home
tab_home = ttk.Frame(tab_control)
tab_control.add(tab_home, text='Home')
lbl_home = Label(tab_home, text="Select the tab for the type of units you wish to convert.", font=("Calibri", 12))
lbl_home.place(relx=0.05, rely=0.3, anchor='nw')
lbl_home2 = Label(tab_home, text="You can use this tool to easily convert units of measurement.", font=("Calibri", 12))
lbl_home2.place(relx=0.05, rely=0.1, anchor='nw')
help_btn = Button(tab_home, text="Help", command=help_screen)
help_btn.place(relx=1.0, rely=1.0, x=0, y=0, anchor='se')

# temperature
tab_temp = ttk.Frame(tab_control)
tab_control.add(tab_temp, text='Temperature')
lbl_temp = Label(tab_temp, text='Convert Temperature Units', font=20, justify='center')
lbl_temp.pack(side='top')
lbl_tempto = Label(tab_temp, text='to', font=("Calibri", 12), justify='center')
lbl_tempto.place(relx=0.43, rely=0.2, anchor='nw')

temp_input = Entry(tab_temp,width=10)
temp_input.place(relx=0.15, rely=0.2, anchor='nw')

temp_box_value1 = StringVar()
temp_combo1 = Combobox(tab_temp, textvariable=temp_box_value1, width=7)
temp_combo1['values'] = ("C","F")
temp_combo1.bind('<<ComboboxSelected>>')
temp_combo1.current(0)    #set the selected item
temp_combo1.place(relx=0.3, rely=0.2, anchor='nw')

temp_box_value2 = StringVar()
temp_combo2 = Combobox(tab_temp, textvariable=temp_box_value2, width=7)
temp_combo2['values'] = ("C","F")
temp_combo2.bind('<<ComboboxSelected>>')
temp_combo2.current(1)    #set the selected item
temp_combo2.place(relx=0.47, rely=0.2, anchor='nw')

lbl_tempeq = Label(tab_temp, text='=', font=("Calibri", 12), justify='center')
lbl_tempeq.place(relx=0.6, rely=0.2, anchor='nw')

temp_calc_btn = Button(tab_temp, text="Calculate", command=calculate_temp)
temp_calc_btn.place(relx=0.4, rely=0.35, anchor='nw')

tempresults_entry = tk.Entry(tab_temp, width=13)
tempresults_entry.place(relx=0.64, rely=0.2, anchor='nw')
tempresults = ""
tempresults_entry.insert(0, tempresults)

temp_equation_title = StringVar()
temp_equation_title.set("")
lbl_temp_eq_title = Label(tab_temp, textvariable=temp_equation_title, font=("Calibri", 14), justify='center')
lbl_temp_eq_title.place(relx=0.4, rely=0.5, anchor='nw')

temp_equation = StringVar()
temp_equation.set("")
lbl_temp_eq = Label(tab_temp, textvariable=temp_equation, font=("Calibri", 12), justify='center')
lbl_temp_eq.place(relx=0.47, rely=0.6, anchor='n')

# temperature data
lbl_tempData = Label(tab_temp, text='Highest Temperature Recorded by State (deg F)', justify='center')
lbl_tempData.place(relx=0.5, rely=0.8, anchor='nw')

state_box = StringVar()
state_combo = Combobox(tab_temp, textvariable=state_box, width=11)
state_combo['values'] = ("Alaska","Arizona","California","Colorado","Florida","Hawaii","Illinois","Maine","Montana","Nevada","New York","Oregon","Texas","Washington")
state_combo.bind('<<ComboboxSelected>>')
state_combo.current(0)  #set the selected item
state_combo.place(relx=0.53, rely=0.9, anchor='nw')

tempData_entry = tk.Entry(tab_temp, width=8)
tempData_entry.place(relx=0.7, rely=0.9, anchor='nw')
tempData = ""
tempData_entry.insert(0, tempData)

temp_data_btn = Button(tab_temp, text="Get Data", command=getTempData, width=9)
temp_data_btn.place(relx=0.8, rely=0.9, anchor='nw')

# pressure
tab_press = ttk.Frame(tab_control)
tab_control.add(tab_press, text='Pressure')
lbl_press = Label(tab_press, text='Convert Pressure Units', font=20, justify='center')
lbl_press.pack(side='top')
lbl_pressto = Label(tab_press, text='to', font=("Calibri", 12), justify='center')
lbl_pressto.place(relx=0.43, rely=0.2, anchor='nw')

press_input = Entry(tab_press,width=10)
press_input.place(relx=0.15, rely=0.2, anchor='nw')

press_box_value1 = StringVar()
press_combo1 = Combobox(tab_press, textvariable=press_box_value1, width=7)
press_combo1['values'] = ("mbar","psi")
press_combo1.bind('<<ComboboxSelected>>')
press_combo1.current(0)    #set the selected item
press_combo1.place(relx=0.3, rely=0.2, anchor='nw')

press_box_value2 = StringVar()
press_combo2 = Combobox(tab_press, textvariable=press_box_value2, width=7)
press_combo2['values'] = ("mbar","psi")
press_combo2.bind('<<ComboboxSelected>>')
press_combo2.current(1)    #set the selected item
press_combo2.place(relx=0.47, rely=0.2, anchor='nw')

lbl_presseq = Label(tab_press, text='=', font=("Calibri", 12), justify='center')
lbl_presseq.place(relx=0.6, rely=0.2, anchor='nw')

press_calc_btn = Button(tab_press, text="Calculate", command=calculate_press)
press_calc_btn.place(relx=0.4, rely=0.35, anchor='nw')

pressresults_entry = tk.Entry(tab_press, width=13)
pressresults_entry.place(relx=0.64, rely=0.2, anchor='nw')
pressresults = ""
pressresults_entry.insert(0, pressresults)

press_equation_title = StringVar()
press_equation_title.set("")
lbl_press_eq_title = Label(tab_press, textvariable=press_equation_title, font=("Calibri", 14), justify='center')
lbl_press_eq_title.place(relx=0.4, rely=0.5, anchor='nw')

press_equation = StringVar()
press_equation.set("")
lbl_press_eq = Label(tab_press, textvariable=press_equation, font=("Calibri", 12), justify='center')
lbl_press_eq.place(relx=0.47, rely=0.6, anchor='n')

# flow rate
tab_flow = ttk.Frame(tab_control)
tab_control.add(tab_flow, text='Flow Rate')
lbl_flow = Label(tab_flow, text='Convert Flow Rate Units', font=20, justify='center')
lbl_flow.pack(side='top')
lbl_flowto = Label(tab_flow, text='to', font=("Calibri", 12), justify='center')
lbl_flowto.place(relx=0.43, rely=0.2, anchor='nw')

flow_input = Entry(tab_flow,width=10)
flow_input.place(relx=0.15, rely=0.2, anchor='nw')

flow_box_value1 = StringVar()
flow_combo1 = Combobox(tab_flow, textvariable=flow_box_value1, width=7)
flow_combo1['values'] = ("lbs/sec","lbs/min")
flow_combo1.bind('<<ComboboxSelected>>')
flow_combo1.current(0)    #set the selected item
flow_combo1.place(relx=0.3, rely=0.2, anchor='nw')

flow_box_value2 = StringVar()
flow_combo2 = Combobox(tab_flow, textvariable=flow_box_value2, width=7)
flow_combo2['values'] = ("lbs/sec","lbs/min")
flow_combo2.bind('<<ComboboxSelected>>')
flow_combo2.current(1)    #set the selected item
flow_combo2.place(relx=0.47, rely=0.2, anchor='nw')

lbl_floweq = Label(tab_flow, text='=', font=("Calibri", 12), justify='center')
lbl_floweq.place(relx=0.6, rely=0.2, anchor='nw')

flow_calc_btn = Button(tab_flow, text="Calculate", command=calculate_flow)
flow_calc_btn.place(relx=0.4, rely=0.35, anchor='nw')

flowresults_entry = tk.Entry(tab_flow, width=13)
flowresults_entry.place(relx=0.64, rely=0.2, anchor='nw')
flowresults = ""
flowresults_entry.insert(0, flowresults)

flow_equation_title = StringVar()
flow_equation_title.set("")
lbl_flow_eq_title = Label(tab_flow, textvariable=flow_equation_title, font=("Calibri", 14), justify='center')
lbl_flow_eq_title.place(relx=0.4, rely=0.5, anchor='nw')

flow_equation = StringVar()
flow_equation.set("")
lbl_flow_eq = Label(tab_flow, textvariable=flow_equation, font=("Calibri", 12), justify='center')
lbl_flow_eq.place(relx=0.47, rely=0.6, anchor='n')

# speed
tab_speed = ttk.Frame(tab_control)
tab_control.add(tab_speed, text='Speed')
lbl_speed = Label(tab_speed, text='Convert Speed Units', font=20, justify='center')
lbl_speed.pack(side='top')
lbl_speedto = Label(tab_speed, text='to', font=("Calibri", 12), justify='center')
lbl_speedto.place(relx=0.43, rely=0.2, anchor='nw')

speed_input = Entry(tab_speed,width=10)
speed_input.place(relx=0.15, rely=0.2, anchor='nw')

speed_box_value1 = StringVar()
speed_combo1 = Combobox(tab_speed, textvariable=speed_box_value1, width=7)
speed_combo1['values'] = ("knots","mph")
speed_combo1.bind('<<ComboboxSelected>>')
speed_combo1.current(0)    #set the selected item
speed_combo1.place(relx=0.3, rely=0.2, anchor='nw')

speed_box_value2 = StringVar()
speed_combo2 = Combobox(tab_speed, textvariable=speed_box_value2, width=7)
speed_combo2['values'] = ("knots","mph")
speed_combo2.bind('<<ComboboxSelected>>')
speed_combo2.current(1)    #set the selected item
speed_combo2.place(relx=0.47, rely=0.2, anchor='nw')

lbl_speedeq = Label(tab_speed, text='=', font=("Calibri", 12), justify='center')
lbl_speedeq.place(relx=0.6, rely=0.2, anchor='nw')

speed_calc_btn = Button(tab_speed, text="Calculate", command=calculate_speed)
speed_calc_btn.place(relx=0.4, rely=0.35, anchor='nw')

speedresults_entry = tk.Entry(tab_speed, width=13)
speedresults_entry.place(relx=0.64, rely=0.2, anchor='nw')
speedresults = ""
speedresults_entry.insert(0, speedresults)

speed_equation_title = StringVar()
speed_equation_title.set("")
lbl_speed_eq_title = Label(tab_speed, textvariable=speed_equation_title, font=("Calibri", 14), justify='center')
lbl_speed_eq_title.place(relx=0.4, rely=0.5, anchor='nw')

speed_equation = StringVar()
speed_equation.set("")
lbl_speed_eq = Label(tab_speed, textvariable=speed_equation, font=("Calibri", 12), justify='center')
lbl_speed_eq.place(relx=0.47, rely=0.6, anchor='n')


# currency
tab_currency = ttk.Frame(tab_control)
tab_control.add(tab_currency, text='Currency')
lbl_currency = Label(tab_currency, text='Convert Currency', font=20, justify='center')
lbl_currency.pack(side='top')
lbl_currencyto = Label(tab_currency, text='to', font=("Calibri", 12), justify='center')
lbl_currencyto.place(relx=0.43, rely=0.2, anchor='nw')

currency_input = Entry(tab_currency,width=10)
currency_input.place(relx=0.15, rely=0.2, anchor='nw')

currency_box_value1 = StringVar()
currency_combo1 = Combobox(tab_currency, textvariable=currency_box_value1, width=7)
currency_combo1['values'] = ("USD","EUR","GBP","CAD","JPY","MXN","CHF","AMD","AUD","BRL")
currency_combo1.bind('<<ComboboxSelected>>')
currency_combo1.current(0)    #set the selected item
currency_combo1.place(relx=0.3, rely=0.2, anchor='nw')

currency_box_value2 = StringVar()
currency_combo2 = Combobox(tab_currency, textvariable=currency_box_value2, width=7)
currency_combo2['values'] = ("USD","EUR","GBP","CAD","JPY","MXN","CHF","AMD","AUD","BRL")
currency_combo2.bind('<<ComboboxSelected>>')
currency_combo2.current(1)    #set the selected item
currency_combo2.place(relx=0.47, rely=0.2, anchor='nw')

lbl_currencyeq = Label(tab_currency, text='=', font=("Calibri", 12), justify='center')
lbl_currencyeq.place(relx=0.6, rely=0.2, anchor='nw')

currency_calc_btn = Button(tab_currency, text="Calculate", command=calculate_currency)
currency_calc_btn.place(relx=0.4, rely=0.35, anchor='nw')

currencyresults_entry = tk.Entry(tab_currency, width=13)
currencyresults_entry.place(relx=0.64, rely=0.2, anchor='nw')
currencyresults = ""
currencyresults_entry.insert(0, currencyresults)


tab_control.pack(expand=1, fill='both')

window.mainloop()
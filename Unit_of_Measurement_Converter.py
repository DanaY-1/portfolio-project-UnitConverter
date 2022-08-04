from tkinter import *
import tkinter as tk
from tkinter import scrolledtext
from tkinter.ttk import *
from tkinter import ttk
import socket
import json

# Help Screen Message
help_screen_msg = """
Welcome to the Unit of Measurement Converter tool!

You can use this tool to easily convert units of measurement.

New features:
- Flow Rate Converter - converts units of flow rate
- Speed Converter - converts units of speed
- Currency Exchange Converter - converts between currencies
- Highest Temperature Recorded by State - provides data on the highest temperatures recorded by state

How to Convert Units:
1. Select the tab of the type of units you wish to convert.
2. Enter the value you wish to convert, and select the units you wish to convert from and to.
3. Select the Calculate button to produce the converted results.
4. The results will show up in the results output box.
5. If applicable, the equation for the conversion will also be displayed. 
6. After any calculation, you may enter a new value and units and the calculate button will generate new results.

Highest Temperature Recorded by State:
This features allows you to select a state and get data on the highest recorded temperature for that state.
1. Navigate to the temperature tab.
2. Select which state you wish to view the highest recorded temperature from the dropdown box.
3. Select the button 'Get Data'.
4. Data will be provided in degrees Fahrenheit.

Can't find what you're looking for?
Email your question/suggestion to the developer: osustudent@oregonstate.edu



"""

#######################################################################################################
# Functions
#
#
#######################################################################################################
def help_screen():
    """Help Window Configuration"""
    window_help = tk.Tk()
    window_help.title("Unit of Measurement Converter - Help")
    txt = tk.Text(window_help, width=125, height=25)
    scroll = tk.Scrollbar(window_help)
    txt.configure(yscrollcommand=scroll.set)
    txt.pack(side=tk.LEFT)
    scroll.config(command=txt.yview)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)
    
    txt.insert(INSERT, help_screen_msg)
    window_help.mainloop()

def convert_to_float(val_str):
    """Converts a given value to a float. 
    Returns an error message if conversion can't be performed.
    """
    try:
        val = float(val_str)
        return val
    except:
        print("Enter a number to convert.")
        return

def calc_error_handling(val, to_units, from_units):
    """Error handling for unit conversion entries."""
    if from_units == to_units:
        result = val
        equation = ""
    else:
        result = ""
        equation = ""
    return result, equation

def display_equation(tab_eq_title, tab_eq, equation):
    """Displays equation for conversion."""
    tab_eq_title.set("Equation:")
    tab_eq.set(equation)

def display_result(result, to_units, tab_entry):
    """Displays results for conversion."""
    output = str(result) + " " + to_units
    tab_entry.delete(0, tk.END)
    tab_entry.insert(0, output)

def convert_temperature():
    """Converts given temperature and displays results."""
    val = convert_to_float(temp_input.get())
    from_units = temp_box_value1.get()
    to_units = temp_box_value2.get()

    val, equation = calculate_temp(val, from_units, to_units)
    display_equation(temp_equation_title, temp_equation, equation)
    display_result(val, to_units, tempresults_entry)

def calculate_temp(val, from_units, to_units):
    """Calculatues Temperature Conversion."""
    if from_units == "C" and to_units == "F":
        result = round((val * (9/5)) + 32, 1)
        equation = "F = (C x 9/5) + 32"  
    elif from_units == "F" and to_units == "C":
        result = round((val - 32) * (5/9), 1)
        equation = "C = (F - 32) x (5/9)"
    else:
        result, equation = calc_error_handling(val, to_units, from_units)
    return result, equation

def convert_pressure():
    """Converts given pressure and displays results."""
    val = convert_to_float(press_input.get())
    from_units = press_box_value1.get()
    to_units = press_box_value2.get()

    val, equation = calculate_press(val, from_units, to_units)
    display_equation(press_equation_title, press_equation, equation)
    display_result(val, to_units, pressresults_entry)

def calculate_press(val, from_units, to_units):
    """Calculatues Pressure Conversion."""
    if from_units == "mbar" and to_units == "psi":
        result = round((val*0.0145037738), 1)
        equation = "psi = mbar x 0.0145037738" 
    elif from_units == "psi" and to_units == "mbar":
        result = round(val * 68.9475729318, 1)
        equation = "mbar = psi * 68.9475729318"
    else:
        result, equation = calc_error_handling(val, to_units, from_units)
    return result, equation

def convert_flow():
    """Converts given flow and displays results."""
    val = convert_to_float(flow_input.get())
    from_units = flow_box_value1.get()
    to_units = flow_box_value2.get()

    val, equation = calculate_flow(val, from_units, to_units)
    display_equation(flow_equation_title, flow_equation, equation)
    display_result(val, to_units, flowresults_entry)

def calculate_flow(val, from_units, to_units):
    """Calculatues Flow Conversion."""
    if from_units == "lbs/sec" and to_units == "lbs/min":
        result = round((val*60), 1)
        equation = "lbs/min = (lbs/sec) x 60" 
    elif from_units == "lbs/min" and to_units == "lbs/sec":
        result = round(val / 60, 1)
        equation = "lbs/sec = (lbs/min) / 60"
    else:
        result, equation = calc_error_handling(val, to_units, from_units)
    return result, equation

def convert_speed():
    """Converts given speed and displays results."""
    val = convert_to_float(speed_input.get())
    from_units = speed_box_value1.get()
    to_units = speed_box_value2.get()

    val, equation = calculate_speed(val, from_units, to_units)
    display_equation(speed_equation_title, speed_equation, equation)
    display_result(val, to_units, speedresults_entry)

def calculate_speed(val, from_units, to_units):
    """Calculatues Speed Conversion."""
    if from_units == "knots" and to_units == "mph":
        result = round((val*1.15077945), 1)
        equation = "mph = knots x 1.15077945"
    elif from_units == "mph" and to_units == "knots":
        result = round(val / 1.15077945, 1)
        equation = "knots = mph / 1.15077945"
    else:
        result, equation = calc_error_handling(val, to_units, from_units)
    return result, equation

def convert_currency():
    """Converts given currency and displays results."""
    val = convert_to_float(currency_input.get())
    from_units = currency_box_value1.get()
    to_units = currency_box_value2.get()
    # set up communication via socket
    client = setup_socket_comms('127.0.0.1', 1080)
    
    val = calculate_currency(val, from_units, to_units, client)

def calculate_currency(val, from_units, to_units, client):
    """Calculatues Currency Conversion by requesting data from Microservice."""
    data = json.dumps({"base_currency": from_units, "des_currency": to_units, "amount_to_convert": val})
    client.send(data.encode())      # request data from microservice
    recvData = client.recv(4098)    # receive data from microservice
    result = recvData.decode()
    display_result(result, to_units, currencyresults_entry)
    print(recvData.decode('utf-8'))

def get_temp_data():
    """Gets high temperature data for a given state by requesting data from Microservice."""
    data = state_combo.get()
    # set up communication via socket
    client = setup_socket_comms('127.0.0.1', 5050)
    client.send(data.encode())      # request data from microservice
    recvData = client.recv(2048)    # receive data from microservice
    result = recvData.decode()
    display_result(result, "F", tempData_entry)
    print(recvData.decode('utf-8'))
    # close connection
    data = "!DISCONNECT"
    client.send(data.encode())
    
def setup_socket_comms(host, port):
    """Sets up a client and socket communication with specified host and port.
    Used for microservice communication.
    """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Connected to: ", host, port)
    return client


#######################################################################################################
# GUI Structure
#
#
#######################################################################################################
window = Tk()

window.title("Unit of Measurement Converter")
window.geometry('550x300')

tab_control = ttk.Notebook(window)

# home tab
tab_home = ttk.Frame(tab_control)
tab_control.add(tab_home, text='Home')
lbl_home = Label(tab_home, text="Select the tab for the type of units you wish to convert.", font=("Calibri", 12))
lbl_home.place(relx=0.05, rely=0.3, anchor='nw')
lbl_home2 = Label(tab_home, text="You can use this tool to easily convert units of measurement.", font=("Calibri", 12))
lbl_home2.place(relx=0.05, rely=0.1, anchor='nw')
new_features = """
New features are now available!
For more information on new features select the Help button.
"""
lbl_home3 = Label(tab_home, text=new_features, font=("Calibri", 10))
lbl_home3.place(relx=0.05, rely=0.8, anchor='nw')
help_btn = Button(tab_home, text="Help", command=help_screen)
help_btn.place(relx=1.0, rely=1.0, x=0, y=0, anchor='se')

# temperature tab
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

temp_calc_btn = Button(tab_temp, text="Calculate", command=convert_temperature)
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

# state temperature data
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

temp_data_btn = Button(tab_temp, text="Get Data", command=get_temp_data, width=9)
temp_data_btn.place(relx=0.8, rely=0.9, anchor='nw')

# pressure tab
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

press_calc_btn = Button(tab_press, text="Calculate", command=convert_pressure)
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

# flow rate tab
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

flow_calc_btn = Button(tab_flow, text="Calculate", command=convert_flow)
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

# speed tab
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

speed_calc_btn = Button(tab_speed, text="Calculate", command=convert_speed)
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

# currency tab
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

currency_calc_btn = Button(tab_currency, text="Calculate", command=convert_currency)
currency_calc_btn.place(relx=0.4, rely=0.35, anchor='nw')

currencyresults_entry = tk.Entry(tab_currency, width=13)
currencyresults_entry.place(relx=0.64, rely=0.2, anchor='nw')
currencyresults = ""
currencyresults_entry.insert(0, currencyresults)


tab_control.pack(expand=1, fill='both')

window.mainloop()
import tkinter as tk
from tkinter.constants import HORIZONTAL

def calculate():
    savings_value=int(savings.get())
    interest_value=float(interest.get())/100
    time_value=int(time.get())
    try:
        upper=((1+interest_value)*savings_value*12*(1-(1+interest_value)**time_value))
        lower=(1-(interest_value+1))
        total=upper/lower
    except ZeroDivisionError:
        total=12*savings_value*time_value
    calculated.config(text=f'End value is {int(total)} €')

root=tk.Tk()
root.geometry('600x400')


savings=tk.Scale(root, from_=0, to=5000,length=300,tickinterval=500,orient=HORIZONTAL,label='The Amount of Savings per Month',resolution=100)
savings.grid(row=1,column=0)

interest=tk.Scale(root,from_=0,to=10,orient=HORIZONTAL,label='Expected Rate of Return',length=300,resolution=0.1)
interest.grid(row=2,column=0)


time=tk.Scale(root,from_=0,to=50,orient=HORIZONTAL,length=300,label='Investment period')
time.grid(row=3,column=0)

button = tk.Button(root, text="Calculate", command=calculate)
button.grid(row=4,column=0)

calculated=tk.Label(root)
calculated.grid(row=5,column=0)
root.mainloop()

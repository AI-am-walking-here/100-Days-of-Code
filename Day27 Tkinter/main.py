from tkinter import *

def miles_to_km():
    miles = float(input.get())
    km = round(miles * 1.609, 2)
    result.config(text=f"{km} km")

def km_to_miles():
    km = float(input.get())
    miles = round(km / 1.609, 2)
    result.config(text=f"{miles} miles")

window = Tk()
window.title("Miles and Kilometers Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Radio buttons
radio_state = StringVar()
miles_radio = Radiobutton(text="Miles", value="miles", variable=radio_state)
km_radio = Radiobutton(text="Kilometers", value="km", variable=radio_state)
miles_radio.grid(column=0, row=0)
km_radio.grid(column=1, row=0)

# Label
my_label = Label(text="Enter distance:", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=1)

# Entry
input = Entry(width=10)
input.grid(column=1, row=1)

# Button
button = Button(text="Convert", command=lambda: miles_to_km() if radio_state.get() == "miles" else km_to_miles())
button.grid(column=2, row=1)

# Result Label
result = Label(text="")
result.grid(column=1, row=2)

window.mainloop()
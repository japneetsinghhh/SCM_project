from tkinter import * # the gui
from functions import * #importing functions from functions.py
from PIL import ImageTk, Image # jpeg image support

# Setup
root = Tk()
root.title("Dister")
root.resizable(False, False) #(True,True) we can use True to make the window resizeable but our gui has a window limit set

#DROP DOWN MENU VALUES
metrics = ["Kilometer", "Meter", "Mile", "Foot"]
defVal = StringVar(root)
defVal.set(metrics[0]) # default value for drop down list i.e KILOMETER

# Create all components
lblTitle = Label(root, text=" Dister - Get the distance ", bg="#ff0000") #TITLE ##ff0000 stands for red background colour in hexadecimal format
lblLocation1 = Label(root, text="Location 1:", pady=10)#pady is for the space between the text Location 1 and the input box
edtLocation1 = Entry(root)  #input box
lblLocation2 = Label(root, text="Location 2:", pady=10)
edtLocation2 = Entry(root)
cmbMetric = OptionMenu(root, defVal, *metrics, command=setMesure)   #drop down menu
lblAnswer = Label(root, text="Answer", relief=SUNKEN, width=20) #sunken output window
btnCalculate = Button(root, text="Calculate", command=lambda:calcDistance(edtLocation1.get(), edtLocation2.get(), lblAnswer, root)) #calculator button 

img = ImageTk.PhotoImage(Image.open("images/help.jpeg").resize((20, 20))) #adding image for help box
imgHelp = Button(root, image=img, command=giveHelp) # image help button

# Place all components
#columnspan is how many columns the wiidget occupies
lblTitle.grid(row=0, column=0, columnspan=4)
lblLocation1.grid(row=1, column=0)
edtLocation1.grid(row=1, column=1, columnspan=2)
lblLocation2.grid(row=2, column=0)
edtLocation2.grid(row=2, column=1, columnspan=2)
cmbMetric.grid(row=3, column=0)
btnCalculate.grid(row=3, column=1)
imgHelp.grid(row=3, column=2)
lblAnswer.grid(row=4, column=0, columnspan=3, pady=10)

# Configure all components
lblTitle.configure(font=("Sans-Serif", 20)) #font and size
lblLocation1.configure(font=("monospace", 15)) 
lblLocation2.configure(font=("monospace", 15))
lblAnswer.configure(font=("monospace", 15))

# Extras
edtLocation1.insert(0, "") # default text   #for inserting default texts in input box #0 is index of the place
edtLocation1.bind('<Control-a>', lambda e: callback(e, root))   #to use ctrl+A for selecting the texts in input box
edtLocation2.insert(0, "") # default text
edtLocation2.bind('<Control-a>', lambda e: callback(e, root))
# btnCalculate.bind("<Enter>", lambda e:calcDistance(edtLocation1.get(), edtLocation2.get(), lblAnswer, root))

root.mainloop()
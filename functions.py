from geopy.geocoders import Nominatim
from geopy.distance import great_circle
from tkinter import Label, messagebox

mesure = "Kilometer" # default unit selected

def setMesure(event):	#we are using this function to just make our variabe unit global
	global mesure
	mesure = event #unit which is being selected in the drop down box

def callback(event, root):
    root.after(50, select_all, event.widget)

def select_all(widget): # allows ctrl+a to select all the text
    # select text
    widget.select_range(0, 'end')
    # move cursor to the end
    widget.icursor('end')

def calcDistance(place1, place2, lbl, root):
	global mesure

	geolocator = Nominatim(user_agent="dister")
	location1 = geolocator.geocode(place1)
	location2 = geolocator.geocode(place2)

	try: # may return error if no location can be found
		location1 = (location1.latitude, location1.longitude)
		location2 = (location2.latitude, location2.longitude)
		#if this returns an error the except will be executed which will display the error message
	except AttributeError as e:
		messagebox.showerror("No location found", "Please check your locations, one or both could not be found...")
		return

	#great_circle called while importing geopy in the starting. It is an inbuilt function of geopy library
	if mesure == "Kilometer":
		distance = great_circle(location1, location2).km	#.km is to return to km
		distance = "{:.2f}".format(distance) + " km"	#formatting it to 2 decimals because it will return a very long line
	elif mesure == "Meter":
		distance = great_circle(location1, location2).m	
		distance = "{:.2f}".format(distance) + " m"
	elif mesure == "Mile":
		distance = great_circle(location1, location2).mi	
		distance = "{:.2f}".format(distance) + " mi"
	else:
		distance = great_circle(location1, location2).ft	
		distance = "{:.2f}".format(distance) + " ft"

	lbl = Label(root, text=distance, width=20)
	lbl.grid(row=4, column=0, columnspan=3, pady=10)

def giveHelp():
	messagebox.showinfo("More info!", "Dister can be used to get the distance between 2 locations.")

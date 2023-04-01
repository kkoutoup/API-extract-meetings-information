from tkinter import *
from tkinter import ttk, font

# check which widget is active
def check_active_widget(e):
    # selected_item = root.focus_get() # returns the type of the item in focus
    # print(selected_item)
    # print(selected_item['value']) # returns the value of the item in focus
    widget = root.focus_get()
    if '.!radiobutton' in str(widget): # if radiobutton selected de-activate entry fields
        print(widget['value'])
        start_date.config(state="disabled")
        end_date.config(state="disabled")
    else: # if entry is selected de-activate radiobuttons
        user_radio_today.config(state="disabled")
        user_radio_week.config(state="disabled")
        print(start_date.get())
        print(end_date.get())

# root window
root = Tk()
root.title("Fetch committee meetings information")

# root window size
root.resizable(FALSE, FALSE) # prevent window from resizing
root.geometry("500x250")

# style - fonts
widget_font = font.Font(family='TkDefaultFont', size=12)
warning_font = font.Font(family='TkDefaultFont', size=12, weight='bold')


# widget frame - parent of radiobuttons etc
widget_frame = ttk.Frame(root, padding=10)
widget_frame.pack()

# widget frame labels
radio_button_label = ttk.Label(widget_frame, text="Today's or this week's meetings", font=widget_font)
alternative_selection_label = ttk.Label(widget_frame, text="Select a different timespan (dd/mm/yyyy)", font=widget_font)
date_from_label = ttk.Label(widget_frame, text="Start date")
date_to_label = ttk.Label(widget_frame, text="End date")

# radio buttons - choose between today's and week's meetings
user_radio_choice = StringVar()
user_radio_today = ttk.Radiobutton(widget_frame, text="Today's meetings", variable=user_radio_choice, value='today')
user_radio_week = ttk.Radiobutton(widget_frame, text="This week's meetings", variable=user_radio_choice, value='week')

# entry item - for typing input
from_date = StringVar()
start_date = ttk.Entry(widget_frame, textvariable=from_date)
to_date = StringVar()
end_date = ttk.Entry(widget_frame, textvariable=to_date)

# confirm button
confirm_button = ttk.Button(widget_frame, text="Fetch results")

# user error label - output warning message to user
user_error_label = ttk.Label(widget_frame, text="", font=warning_font)

# position elements
# radio button widget
widget_frame.grid(column=0, row=0)
radio_button_label.grid(column=0, row=1, sticky=W)
user_radio_today.grid(column=0, row=2, sticky=W, pady=5)
user_radio_week.grid(column=0, row=3, sticky=W, pady=2)

# input widget
alternative_selection_label.grid(column=0, row=4, sticky=W, pady=10)
widget_frame.grid(column=0, row=5, sticky=W, pady=5)
date_from_label.grid(column=0, row=6, sticky=W, pady=5)
start_date.grid(column=0, row=6, sticky=W, padx=80)
date_to_label.grid(column=0, row=7, sticky=W, pady=5)
end_date.grid(column=0, row=7, sticky=W, padx=80)

# confirm button
confirm_button.grid(column=0, row=8, sticky=W, pady=10)
confirm_button.config(width=20)

# user error label
user_error_label.grid(column=0, row=9, sticky=W, pady=10)

# bind mouse click to check_active_widget
root.bind('<Button>',lambda e: check_active_widget(e)) # return the name of the widget on mouse click

# run window loop
root.mainloop()
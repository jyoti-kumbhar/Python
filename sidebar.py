import tkinter as tk

def open_dashboard():
    print("Open Dashboard")

def open_employee_list():
    print("Open Employee List")

def open_reports():
    print("Open Reports")

def open_settings():
    print("Open Settings")

# Create the main window
root = tk.Tk()
root.title("Sidebar Example")

# Create a frame for the sidebar
sidebar_frame = tk.Frame(root, width=150, bg="gray")
sidebar_frame.pack(side="left", fill="y")

# Add buttons to the sidebar
dashboard_button = tk.Button(sidebar_frame, text="Dashboard", command=open_dashboard)
dashboard_button.pack(pady=10)

employee_list_button = tk.Button(sidebar_frame, text="Employee List", command=open_employee_list)
employee_list_button.pack(pady=10)

reports_button = tk.Button(sidebar_frame, text="Reports", command=open_reports)
reports_button.pack(pady=10)

settings_button = tk.Button(sidebar_frame, text="Settings", command=open_settings)
settings_button.pack(pady=10)

# Rest of your GUI content goes here...

# Run the main loop
root.mainloop()

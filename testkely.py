import tkinter as tk
def custom_exit_handler():
    print('You clicked exit button')
    root.destroy()
root = tk.Tk()
root.geometry('400x200')
root.title("Test kely naunau")
root.protocol("WM_DELETE_WINDOW", custom_exit_handler)
root.mainloop()


# Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

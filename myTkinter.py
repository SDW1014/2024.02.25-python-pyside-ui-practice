import tkinter as tk

root = tk.Tk()

class myTkinterWindow():
    def __init__(self, master):
        self.master = master
        master.title("myWindow - Tkinter - ver 0.1")
        
        self.label = tk.label(master, text = "Hello World!")
        self.label.pack()
        
        self.close_button = tk.Button(master, text = "Close", command=master.quit)
        self.close_button.pack()

class myTkinterWindowNoMasterVer(myTkinterWindow):
    def __init__(self):
        super().__init__(root)
        
    def loop():
        root.mainloop()
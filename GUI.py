from Tkinter import *
from Data_Pre_Processing import Data_Pre_Processing
from NaiveBayesModel import NaiveBayesModel

class GUI:
    def __init__(self):
        self.root = Tk()

        label_1=Label(self.root, text= "Directory Path:")
        label_2=Label(self.root, text= "Discretization Bins:")
        entry_1=Entry(self.root)
        entry_2=Entry(self.root)

        label_1.grid(row=2,column=0,sticky=E)
        label_2.grid(row=3,column=0,sticky=E)

        entry_1.grid(row=2,column=1)
        entry_2.grid(row=3,column=1)
        #button_1 = Button( text = "Say Hello ", command=funcname)

        Browse = Button( text = "Browse")
        Browse.grid(column=3,row=3)

        Build = Button( text = "Build")
        Build.grid(columnspan=4,row=5)

        Classify = Button( text = "Classify")
        Classify.grid(columnspan=4,row=6)

        self.root.mainloop()



from Tkinter import *
import tkFileDialog
import os.path

from Preprossing_and_Classfiy import Preprossing_and_Classfiy;

class GUI:
    def __init__(self):
#        self.PC;
#        self.filename;
#        self.pathStructure
#        self.pathtrain
#        self.pathtest
        self.root = Tk()
        label_0 = Label(self.root, text="")
        label_1=Label(self.root, text= "Directory Path:")
        label_2=Label(self.root, text= "Discretization Bins:")
        label_3=Label(self.root, text= "")
        label_4=Label(self.root, text= "")
        label_5=Label(self.root, text= "")


        self.entry_1=Entry(self.root)
        self.entry_2=Entry(self.root)

        label_0.grid(row=0,columnspan=2,sticky=E)
        label_1.grid(row=4,column=1,sticky=E)
        label_2.grid(row=6,column=1,sticky=E)
        label_3.grid(row=7, column=1, sticky=E)
        label_4.grid(row=9, column=1, sticky=E)
        label_5.grid(row=13, column=1, sticky=E)


        self.entry_1.grid(row=4,column=2)
        self.entry_2.grid(row=6,column=2)
        #button_1 = Button( text = "Say Hello ", command=funcname)

        Browse = Button( text = "Browse", command=self.browsecsv)
        Browse.grid(column=3,row=4)

        Build = Button(text = "Build",command=self.build )
        Build.grid(columnspan=4,row=8)

        Classify = Button(text = "Classify")
        Classify.grid(columnspan=4,row=12)

        self.root.mainloop()

    def browsecsv(self):
        from tkFileDialog import askopenfilename

        Tk().withdraw()
        self.filename =tkFileDialog.askdirectory()
       # self.filename = askopenfilename()

        self.entry_1.insert(0,self.filename)
       # root.after(1, update)
        #build(self);


    def build(self):
        self.bins= self.entry_2.get();
        self.path = self.entry_1.get();
        bool=os.path.exists(self.filename)
        if (bool==True and self.bins!="0"):
            self.pathStructure=self.filename+"/Structure.txt"
            self.pathtrain= self.filename+"/train.csv"
            self.pathtest= self.filename+"/test.csv"
          #  bool=os.path.exists(pathStructure)
            if( os.path.exists(pathStructure)==False or (os.path.getsize(pathStructure) > 0)==False):
                import tkMessageBox
                tkMessageBox.showinfo(title="error", message="pathStructure unvalid")
                return;
            if( os.path.exists(pathtrain)=="false" or (os.path.getsize(pathtrain) > 0)=="false"):
                import tkMessageBox
                tkMessageBox.showinfo(title="error", message="path train unvalid")
                return;
            if( os.path.exists(pathtest)=="false" or (os.path.getsize(pathtest) > 0)=="false"):
                import tkMessageBox
                tkMessageBox.showinfo(title="error", message="path test unvalid")
                return;
        self.PC=Preprossing_and_Classfiy( path, bins,2);
        self.PC.DPP=self.PC.Bulid();



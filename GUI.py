''' GUI.py
Created by wolfy

This handles the GUI for ESMB

'''
from tkinter import *
from tkinter import ttk, StringVar
from menuactions import *

class GUI(object):

    def __init__(self):
        print("Building GUI...")
        self.missionList             = [Mission("Default")]       #TODO: Initialize with template mission on launch
        self.missionNameToObjectDict = {"Default" : self.missionList[0]}
        self.missionNames            = []

        # Build the application window
        self.gui = Tk()
        self.gui.title("ESMissionBuilder")
        self.gui.configure(bg="orange")

        self.ofWidth = None
        self.cfWidth = None
        self.mfWidth = None

        # declare optionFrame components
        self.missionComboBox = None

        # declare centerFrame components
        self.cfTitle     = ""
        self.cfTitleText = StringVar()

        # declare missionFrame components
        self.mfTitle        = ""
        self.missionTextBox = None
        self.hbar           = None
        self.vbar           = None

        # Build the different parts of the main window
        #self.buildMenu(self.gui)
        self.optionFrame, self.centerFrame, self.missionFrame = self.buildMainView(self.gui)

        # Run the program
        self.gui.mainloop()
    #end init

    # This may be used later, after shortcuts are introduced
    '''
    # COMPLETE, WORKING
    def buildMenu(self, window):
        # creating a menu instance
        menu = Menu()
        window.config(menu=menu)

        # create the file object
        file = Menu(menu)
        edit = Menu(menu)

        # adds a command to the menu option, names it, and set the command to run
        file.add_command(label="New", command=lambda: newFile(self))
        file.add_command(label="Open", command=lambda: openFile(self))
        file.add_command(label="Save", command=lambda: saveFile(self))
        file.add_command(label="Exit", command=exit)

        # added "File" to our menu
        menu.add_cascade(label="File", menu=file)

        # adds a command to the menu option, names it, and set the command to run
        edit.add_command(label="Undo", command=lambda: undoAction(self))

        # added "Edit" to our menu
        menu.add_cascade(label="Edit", menu=edit)
    #end buildMenu
    '''

    #COMPLETE, WORKING
    def buildMainView(self, window):

        optionFrame = ttk.Frame(window)
        centerFrame = ttk.Frame(window)
        missionFrame = ttk.Frame(window)

        # set up each of the frames
        self.buildOptionFrame(optionFrame)
        self.buildCenterFrame(centerFrame)
        self.buildMissionFrame(missionFrame)

        return optionFrame, centerFrame, missionFrame
    #end buildMainView


    ### BUILDING FRAMES ###


    def buildOptionFrame(self, optionFrame):
        #TODO: Implement this - ~50% Completed
        print("Building optionFrame...", end="\t\t")
        optionFrame.grid(row=0, column=0, sticky="ns")

        # build default values here
        label1 = ttk.Label(optionFrame, text="Mission")
        label1.pack()

        self.missionNames.append("Default")

        # declare the combobox here, fill with missionNames
        self.missionComboBox = ttk.Combobox(optionFrame, state="readonly", values=self.missionNames)
        self.missionComboBox.bind("<<ComboboxSelected>>", self.missionSelected)
        self.missionComboBox.pack()
        self.missionComboBox.current(0)

        # set default values here

        #add "new mission" button
        newMission = ttk.Button(optionFrame, text="New Mission", command=lambda: newFile(self))
        newMission.pack(fill='x')

        #add "save mission" button
        saveMission = ttk.Button(optionFrame, text="Save Mission", command=lambda: saveFile(self))
        saveMission.pack(fill='x')

        #add "open mission" button
        openMission = ttk.Button(optionFrame, text="Open Mission", command=lambda: openFile(self))
        openMission.pack(fill='x')

        print("Done.")
    #end buildOptionFrame


    def buildCenterFrame(self, centerFrame):
        print("Building centerFrame...", end="\t\t")
        #TODO: Populate frame
        centerFrame.grid(row=0, column=1, sticky="ns")

        # Print the default mission name
        self.cfTitleText.set("Mission Options")
        self.cfTitle = ttk.Label(centerFrame, text=self.cfTitleText.get())
        self.cfTitle.grid(row=0, column=0, sticky="ew")

        self.buildComponentsOnCenterFrame()

        print("Done.")
    #end buildCenterFrame


    def buildComponentsOnCenterFrame(self):
        print("Testing buildComponentsOnCenterFrame")

        self.populateComponentSelections()
    #end buildComponentsOnCenterFrame


    def populateComponentSelections(self):
        print("Testing populateComponentSelections")

    #end populateComponentSelections


    def buildMissionFrame(self, missionFrame):
        #TODO: Implement this - ~75% Completed
        print("Building missionFrame...", end="\t")

        #TODO: Display a default mission template on launch
        missionFrame.grid(row=0, column=2, sticky="nsew")
        self.mfTitle = Label(missionFrame, text="Mission Text")
        self.mfTitle.pack(expand=1, fill='x')

        #TODO: Populate the canvas with a mission template

        # build the missionTexBox that will display the missionLens in a fancy format
        self.updateTextCanvas(["TEMP FILTER TEXT"])

        print("Done.")
    #end buildMissionFrame


    ### UPDATING FRAMES ###


    def updateOptionFrame(self):
        #TODO: Implement this - ~50% Completed
        print("\nUpdating optionFrame...")

        ### Start updating combobox
        ml = self.missionList
        self.missionNames = []
        print("New mission options:", end=" ")
        for m in ml:
            self.missionNames.append(m.missionName)
        print(self.missionNames)

        # update options in the combobox
        self.missionComboBox['values'] = self.missionNames
        self.missionComboBox.current(0)
        ### Finish updating combobox

        # update the other two frames to reflect the current mission
        self.updateCenterFrame(self.missionList[0])
        self.updateMissionFrame(self.missionList[0])
    #end updateOptionFrame


    def updateCenterFrame(self, activeM):
        #TODO: Implement this
        print("Updating centerFrame...")
        self.cfTitleText.set(str(activeM.missionName))
        print("Done.")
    #end updateCenterFrame


    def updateMissionFrame(self, activeM):
        #TODO: Implement this - ~75% Completed
        print("Updating missionFrame")

        # delete the old Canvas and ScrollBars
        self.missionTextBox.pack_forget()
        self.vbar.pack_forget()
        self.hbar.pack_forget()

        # print mission text to a Canvas in the missionFrame
        self.updateTextCanvas(activeM.missionLines)

        print("Done.")
    #end updateMissionFrame

    def updateTextCanvas(self, textListToDisplay):
        self.missionTextBox = Canvas(self.missionFrame, bg='#FFFFFF', scrollregion=(0, 0, 500, 500))
        self.missionTextBox.create_text(0, 0, anchor='nw', text=textListToDisplay, state=DISABLED, justify=LEFT)

        # add scrollbars
        self.hbar = Scrollbar(self.missionFrame, orient=HORIZONTAL)
        self.hbar.pack(side=BOTTOM, fill=X)
        self.hbar.config(command=self.missionTextBox.xview)
        self.vbar = Scrollbar(self.missionFrame, orient=VERTICAL)
        self.vbar.pack(side=RIGHT, fill=Y)
        self.vbar.config(command=self.missionTextBox.yview)
        self.missionTextBox.config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)
        self.missionTextBox.pack(side=LEFT, expand=True, fill=BOTH)
    #end updateTextCanvas


    ### MISC METHODS ###


    def missionSelected(self):
        #TODO: Implement this
        selectedMissionName = self.missionComboBox.get()
        print('Opening mission "%s"' % selectedMissionName)

        newActiveMission = self.missionNameToObjectDict.get(selectedMissionName)
        self.updateCenterFrame(newActiveMission)
        self.updateMissionFrame(newActiveMission)
    #end missionSelected

#end class GUI
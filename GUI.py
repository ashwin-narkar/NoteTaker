import os
import sys
import wx
import subprocess
import wx.lib.agw.multidirdialog as MDD
from Notetaker import*
import math
import numpy as np
import matplotlib.pyplot as plt
from numpy import*
from notes import*
from file import*
from chords import*
from scipy.io import wavfile
from duration import*
import time

wildcard = "Python source (*.py)|*.py|" \
            "All files (*.*)|*.*"
filePath = ""

########################################################################
class MyForm(wx.Frame):

    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,"NoteTaker")
        self.panel = wx.Panel(self, wx.ID_ANY)
        self.SetBackgroundColour('white')
        self.currentDirectory = os.getcwd()

        # Set sizer for the frame, so we can change frame size to match widgets
        self.windowSizer = wx.BoxSizer()
        self.windowSizer.Add(self.panel, 1, wx.ALL | wx.EXPAND)

        #Set image for NoteTaker Logo
        self.start_image = wx.Image("noteTakerSmall.png")
        self.banner_pre = wx.Bitmap(self.start_image)
        self.banner = wx.StaticBitmap(self.panel, -1, self.banner_pre, wx.DefaultPosition,
                                     (self.banner_pre.GetWidth(), self.banner_pre.GetHeight()))

        # Create the button for system browser dialog
        self.openFileDlgBtn = wx.Button(self.panel, label="Choose your song...")
        self.openFileDlgBtn.Bind(wx.EVT_BUTTON, self.onOpenFile)

        self.startBtn = wx.Button(self.panel, label= "Start NoteTaker")
        self.startBtn.Bind(wx.EVT_BUTTON, self.run)

        self.log = wx.StaticText(self.panel, label="Welcome to NoteTaker")
        self.log.SetBackgroundColour('yellow')
        self.blank = wx.StaticText(self.panel, label="")
        self.blank2 = wx.StaticText(self.panel, label="")
        self.blank3 = wx.StaticText(self.panel, label="")

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.banner, 0, wx.CENTER, 0)
        self.sizer.Add(self.openFileDlgBtn, 0, wx.CENTER, 0)
        self.sizer.Add(self.blank, 0 , wx.CENTER, 0)
        self.sizer.Add(self.startBtn, 0, wx.CENTER, 0)
        self.sizer.Add(self.blank2, 0 , wx.CENTER, 0)
        self.sizer.Add(self.log, 0 , wx.ALIGN_CENTER, 0)
        self.sizer.Add(self.blank3, 0 , wx.CENTER, 0)

        # Set simple sizer for a nice border
        self.border = wx.BoxSizer()
        self.border.Add(self.sizer, 1, wx.ALL | wx.EXPAND, 5)

        # Use the sizers
        self.panel.SetSizerAndFit(self.border)
        self.SetSizerAndFit(self.windowSizer)

        # Put the buttons in a sizer
        # self.button_sizer = wx.BoxSizer(wx.VERTICAL)
        # self.button_sizer.Add(self.banner, 0, wx.CENTER, 0)
        # self.button_sizer.Add(self.openFileDlgBtn, 0, wx.CENTER, 0)
        # self.button_sizer.Add(self.startBtn, 0, wx.CENTER, 0)
        # self.panel.SetSizer(self.button_sizer)



    #----------------------------------------------------------------------
    def onOpenFile(self, event):
        """
        Create and show the Open FileDialog
        """
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=self.currentDirectory,
            defaultFile="",
            wildcard=wildcard,
            style=wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            #print ("You chose the following file(s):")
            for path in paths:
                global filePath
                filePath = path
            #panel2.Show()

        dlg.Destroy()


#----------------------------------------------------------------------

    def run(self, event):
        runConf = False
        global filePath
        if filePath == "":
            self.log.SetLabel(" No file path selected")
        else:
            self.log.SetLabel(" Analyzing audio...")
            wx.Yield()
            subprocess.call(['python3', "Notetaker.py",filePath])
            self.log.SetLabel("Transciption complete!")

            # runConf = True
            # self.Refresh()

        # if runConf == True:
        #     noteTaker(filePath)

            #panel.AppendText("Red text\n")
            #ssubprocess.Popen("print.py", stdout=subprocess.PIPE, universal_newlines=True)

# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()

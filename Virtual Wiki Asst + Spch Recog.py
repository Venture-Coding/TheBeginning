# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 14:44:44 2020

@author: Shivam
"""
#((pip install SpeechRecognition #for installing SR))
#((pip install pipwin
#  pipwin install pyaudio ))#this works to install pyaudio
#((pip install -U wxPython 
#or conda install -c conda-forge wxpython)) run conda-cmd as Admin

import speech_recognition as sr
import wx
import wikipedia


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="Vk's Assistant")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello I am Vk's Wiki Assistant. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
        if input == '':
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source)
            try:
                self.txt.SetValue(r.recognize_google(audio))
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
        else:
           	try:
           		print (wikipedia.summary(input))
           	except:
           		print ("I don't know.")


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()

"""
this program runs very slow when audio input is tried  
find ways to increase speed
"""


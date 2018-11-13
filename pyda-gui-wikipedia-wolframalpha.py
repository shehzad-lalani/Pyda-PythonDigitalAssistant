#Importing WxPython,Wikipedia,Wolframalpha,Espeak Modules
import wx
import wikipedia
import wolframalpha
from espeak import espeak

# Class to make GUI for Digital Assistant
# Input a Value
# Get desired search from Wikipedia,Wolframalpha
# Espeak To Make Application Talk
espeak.synth("Welcome to PyDa")

class PyDaFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
        pos=wx.DefaultPosition, size=wx.Size(450, 100),
        style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
        wx.CLOSE_BOX | wx.CLIP_CHILDREN,
        title="PyDa")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello I am Pyda the Python Digital Assistant. How can I help you?")
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
        try:
            #wolframalpha
            app_id = "P26XPU-EG6443ATGU"
            client = wolframalpha.Client(app_id)

            result = client.query(input)
            answer = next(result.results).text

            print(answer)
            espeak.synth("The answer is:"+answer)

        except:
            #wikipedia

            #Split the first two strings for search like who is,what does keywords etc.
            input = input.split(" ")
            input = " ".join(input[2:])
            espeak.synth("Searched For"+input)

            print(wikipedia.summary(input))


if __name__ == "__main__":
    app = wx.App(True)
    frame = PyDaFrame()
    app.MainLoop()

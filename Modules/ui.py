#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.6 on Tue Nov 10 13:46:23 2020
#

import wx
import Modules.db as Query
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE 
        wx.Frame.__init__(self, *args, **kwds)
        
        self.font = wx.Font(13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Futura Bk")

        self.SetBackgroundColour1 = wx.Colour(41, 42, 46)

        self.FGW = wx.Colour(255, 255, 255)

        self.panelBackground = wx.Colour(31, 31, 31)

        self.buttonBG = wx.Colour(21, 21, 21)

        self.panel_main = wx.Panel(self, wx.ID_ANY)
        
        self.text_ctrl_task = wx.TextCtrl(self.panel_main, wx.ID_ANY, "", style=wx.BORDER_NONE | wx.TE_LEFT)
        
        self.button_do = wx.Button(self.panel_main, wx.ID_ANY, "Hacer", style=wx.BORDER_NONE | wx.BU_AUTODRAW)
        
        self.button_doing = wx.Button(self.panel_main, wx.ID_ANY, "Haciendo", style=wx.BORDER_NONE)
        
        self.button_did = wx.Button(self.panel_main, wx.ID_ANY, "Hecho", style=wx.BORDER_NONE)
        
        self.button_clear = wx.Button(self.panel_main, wx.ID_ANY, "Vaciar Terminado", style=wx.BORDER_NONE)
        
        self.panel_do = wx.Panel(self.panel_main, wx.ID_ANY)
        
        self.list_ctrl_do = wx.ListCtrl(self.panel_main, wx.ID_ANY, style=wx.BORDER_SIMPLE | wx.LC_HRULES | wx.LC_NO_HEADER | wx.LC_REPORT | wx.LC_VRULES)

        self.panel_doing = wx.Panel(self.panel_main, wx.ID_ANY)
        
        self.list_ctrl_doing = wx.ListCtrl(self.panel_main, wx.ID_ANY, style=wx.BORDER_SIMPLE | wx.LC_HRULES | wx.LC_NO_HEADER | wx.LC_REPORT | wx.LC_VRULES)
        
        self.panel_did = wx.Panel(self.panel_main, wx.ID_ANY)
        
        self.list_ctrl_did = wx.ListCtrl(self.panel_main, wx.ID_ANY, style=wx.BORDER_SIMPLE | wx.LC_HRULES | wx.LC_NO_HEADER | wx.LC_REPORT | wx.LC_VRULES)
        self.text_ctrl_view = wx.TextCtrl(self.panel_main, wx.ID_ANY, style=wx.BORDER_NONE | wx.HSCROLL | wx.TE_MULTILINE | wx.TE_NOHIDESEL | wx.TE_NO_VSCROLL | wx.TE_READONLY)
        self.index = 0
        
        self.__set_properties()
        
        self.__do_layout()
        
        self.update()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MainFrame.__set_properties
        self.SetTitle("ToDoList")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("C:\\Users\\BlueMaster\\Desktop\\ToDoList\\Resources\\ToDoList.png", wx.BITMAP_TYPE_ANY))
        
        self.SetIcon(_icon)
        
        self.text_ctrl_task.SetMinSize((130, 25))
        
        self.text_ctrl_task.SetBackgroundColour(wx.Colour(66, 66, 66))

        self.text_ctrl_task.SetForegroundColour(self.FGW)
        self.text_ctrl_task.SetFont(wx.Font(18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Arial"))
        
        
        self.button_do.SetMinSize((75, 31))
        
        self.button_do.SetBackgroundColour(self.buttonBG)
        
        self.button_do.SetForegroundColour(self.FGW)
        
        self.button_do.SetFont(self.font)
        
        self.button_do.Bind(wx.EVT_ENTER_WINDOW, lambda event: self.onMouseOver(self.button_do))

        self.button_do.Bind(wx.EVT_LEAVE_WINDOW, lambda event: self.onMouseLeave(self.button_do))

        self.button_do.Bind(wx.EVT_BUTTON, self.doTask)
        
        self.button_doing.SetBackgroundColour(self.buttonBG)
        
        self.button_doing.SetForegroundColour(self.FGW)
        
        self.button_doing.SetFont(self.font)
        
        self.button_doing.Bind(wx.EVT_ENTER_WINDOW, lambda event: self.onMouseOver(self.button_doing))

        self.button_doing.Bind(wx.EVT_LEAVE_WINDOW, lambda event: self.onMouseLeave(self.button_doing))

        self.button_doing.Bind(wx.EVT_BUTTON, self.doingTask)

        self.button_did.SetBackgroundColour(self.buttonBG)
        
        self.button_did.SetForegroundColour(self.FGW)

        self.button_did.Bind(wx.EVT_ENTER_WINDOW, lambda event: self.onMouseOver(self.button_did))

        self.button_did.Bind(wx.EVT_LEAVE_WINDOW, lambda event: self.onMouseLeave(self.button_did))

        self.button_did.Bind(wx.EVT_BUTTON,self.didTask)
        
        self.button_did.SetFont(self.font)
        
        self.button_clear.SetBackgroundColour(self.buttonBG)
        
        self.button_clear.SetForegroundColour(self.FGW)
        
        self.button_clear.SetFont(self.font)
        
        self.button_clear.Bind(wx.EVT_ENTER_WINDOW, lambda event: self.onMouseOver(self.button_clear))

        self.button_clear.Bind(wx.EVT_LEAVE_WINDOW, lambda event: self.onMouseLeave(self.button_clear))

        self.button_clear.Bind(wx.EVT_BUTTON,self.clear)

        self.panel_do.SetBackgroundColour(self.panelBackground)
        
        self.panel_do.SetForegroundColour(self.FGW)
        
        self.list_ctrl_do.SetMinSize((200, 300))
        
        self.list_ctrl_do.SetBackgroundColour(self.SetBackgroundColour1)
        
        self.list_ctrl_do.SetForegroundColour(self.FGW)
        
        self.list_ctrl_do.AppendColumn("", format=wx.LIST_FORMAT_LEFT, width=200)
        
        self.list_ctrl_do.Bind(wx.EVT_LIST_ITEM_FOCUSED,lambda event:self.listView(self.list_ctrl_do))
        
        self.panel_doing.SetMinSize((200, 29))
        
        self.panel_doing.SetBackgroundColour(self.panelBackground)
        
        self.panel_doing.SetForegroundColour(self.FGW)
        
        self.list_ctrl_doing.SetMinSize((200, 300))
        
        self.list_ctrl_doing.SetBackgroundColour(self.SetBackgroundColour1)
        
        self.list_ctrl_doing.SetForegroundColour(self.FGW)
        
        self.list_ctrl_doing.AppendColumn("", format=wx.LIST_FORMAT_LEFT, width=200)

        self.list_ctrl_doing.Bind(wx.EVT_LIST_ITEM_FOCUSED,lambda event:self.listView(self.list_ctrl_doing))
        
        self.panel_did.SetMinSize((200, 29))
        
        self.panel_did.SetBackgroundColour(self.panelBackground)
        
        self.panel_did.SetForegroundColour(self.FGW)
        
        self.list_ctrl_did.SetMinSize((200, 300))
        
        self.list_ctrl_did.SetBackgroundColour(self.SetBackgroundColour1)
        
        self.list_ctrl_did.SetForegroundColour(self.FGW)
        
        self.list_ctrl_did.AppendColumn("", format=wx.LIST_FORMAT_LEFT, width=200)

        self.list_ctrl_did.Bind(wx.EVT_LIST_ITEM_FOCUSED,lambda event:self.listView(self.list_ctrl_did))
        
        self.panel_main.SetBackgroundColour(self.SetBackgroundColour1)
        
        self.text_ctrl_view.SetMinSize((300, 50))
        
        self.text_ctrl_view.SetBackgroundColour(wx.Colour(66, 66, 66))
        
        self.text_ctrl_view.SetForegroundColour(self.FGW)
        
        self.text_ctrl_view.SetFont(self.font)
        # end wxGlade
    def __do_layout(self):
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_view = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_10 = wx.BoxSizer(wx.VERTICAL)
        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.VERTICAL)
        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add((10, 0), 0, 0, 0)
        label_task = wx.StaticText(self.panel_main, wx.ID_ANY, "Tarea:", style=wx.ALIGN_CENTER)
        label_task.SetForegroundColour(wx.Colour(255, 255, 255))
        label_task.SetFont(wx.Font(18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Futura Bk"))
        sizer_3.Add(label_task, 0, wx.ALIGN_CENTER_VERTICAL | wx.TOP, 1)
        sizer_3.Add((20, 0), 1, 0, 0)
        sizer_3.Add(self.text_ctrl_task, 0, wx.ALIGN_CENTER_VERTICAL | wx.TOP, 1)
        sizer_3.Add((24, 0), 0, 0, 0)
        sizer_3.Add(self.button_do, 0, wx.ALIGN_CENTER_VERTICAL | wx.TOP, 3)
        sizer_3.Add((10, 0), 0, 0, 0)
        sizer_3.Add(self.button_doing, 0, wx.ALIGN_CENTER_VERTICAL | wx.TOP, 3)
        sizer_3.Add((10, 0), 0, 0, 0)
        sizer_3.Add(self.button_did, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT | wx.TOP, 3)
        sizer_3.Add((10, 0), 0, 0, 0)
        sizer_3.Add(self.button_clear, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT | wx.TOP, 3)
        sizer_3.Add((10, 0), 0, 0, 0)
        sizer_2.Add(sizer_3, 0, wx.EXPAND | wx.TOP, 5)
        sizer_5.Add((0, 20), 0, 0, 0)
        sizer_7.Add((72, 0), 0, 0, 0)
        label_2 = wx.StaticText(self.panel_do, wx.ID_ANY, "Hacer", style=wx.ALIGN_CENTER | wx.ALIGN_LEFT | wx.ALIGN_RIGHT | wx.ST_ELLIPSIZE_MIDDLE | wx.ST_NO_AUTORESIZE)
        label_2.SetBackgroundColour(wx.Colour(31, 31, 31))
        label_2.SetForegroundColour(wx.Colour(255, 255, 255))
        label_2.SetFont(wx.Font(16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Futura Bk"))
        sizer_7.Add(label_2, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_7.Add((73, 0), 0, 0, 0)
        self.panel_do.SetSizer(sizer_7)
        sizer_6.Add(self.panel_do, 0, wx.EXPAND, 0)
        sizer_6.Add(self.list_ctrl_do, 0, wx.BOTTOM | wx.TOP, 0)
        sizer_4.Add(sizer_6, 1, wx.EXPAND, 0)
        sizer_4.Add((20, 0), 0, 0, 0)
        sizer_9.Add((54, 0), 0, wx.ALL, 0)
        label_3 = wx.StaticText(self.panel_doing, wx.ID_ANY, "Haciendo", style=wx.ST_ELLIPSIZE_MIDDLE)
        label_3.SetBackgroundColour(wx.Colour(31, 31, 31))
        label_3.SetForegroundColour(wx.Colour(255, 255, 255))
        label_3.SetFont(wx.Font(16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Futura Bk"))
        sizer_9.Add(label_3, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_9.Add((54, 0), 1, 0, 0)
        self.panel_doing.SetSizer(sizer_9)
        sizer_8.Add(self.panel_doing, 0, wx.EXPAND, 0)
        sizer_8.Add(self.list_ctrl_doing, 0, wx.BOTTOM | wx.TOP, 0)
        sizer_4.Add(sizer_8, 1, wx.EXPAND, 0)
        sizer_4.Add((20, 0), 0, 0, 0)
        sizer_11.Add((72, 0), 0, 0, 0)
        label_4 = wx.StaticText(self.panel_did, wx.ID_ANY, "Hecho", style=wx.ALIGN_CENTER | wx.ALIGN_LEFT | wx.ALIGN_RIGHT | wx.ST_ELLIPSIZE_MIDDLE | wx.ST_NO_AUTORESIZE)
        label_4.SetBackgroundColour(wx.Colour(31, 31, 31))
        label_4.SetForegroundColour(wx.Colour(255, 255, 255))
        label_4.SetFont(wx.Font(16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Futura Bk"))
        sizer_11.Add(label_4, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_11.Add((73, 0), 0, 0, 0)
        self.panel_did.SetSizer(sizer_11)
        sizer_10.Add(self.panel_did, 0, wx.EXPAND, 0)
        sizer_10.Add(self.list_ctrl_did, 0, wx.BOTTOM | wx.TOP, 0)
        sizer_4.Add(sizer_10, 1, wx.EXPAND, 0)
        sizer_5.Add(sizer_4, 1, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_5.Add((0, 20), 0, 0, 0)
        sizer_2.Add(sizer_5, 1, wx.EXPAND, 0)
        sizer_view.Add(self.text_ctrl_view, 0, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM, 9)
        sizer_2.Add(sizer_view, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.panel_main.SetSizer(sizer_2)
        sizer_1.Add(self.panel_main, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade
    def update(self):
        self.list_ctrl_do.DeleteAllItems()
        self.list_ctrl_did.DeleteAllItems()
        self.list_ctrl_doing.DeleteAllItems()
        table_do = Query.readData('DO')
        table_doing = Query.readData('DOING')
        table_did = Query.readData('DID')
        for data in table_do:
            self.list_ctrl_do.InsertItem(self.index,data)
        for data in table_doing:
            self.list_ctrl_doing.InsertItem(self.index,data)
        for data in table_did:
            self.list_ctrl_did.InsertItem(self.index,data)
    def onMouseOver(self, button):
        button.SetBackgroundColour(wx.Colour(32, 32, 32))
        button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
    def onMouseLeave(self, button):
        button.SetBackgroundColour(wx.Colour(21, 21, 21))
    def doTask(self,event):
        if self.text_ctrl_task.GetLineText(0) != "":
            Query.createTask(self.text_ctrl_task.GetLineText(0))
            self.update()
            self.text_ctrl_task.SetValue('')
    def doingTask(self,event):
        if self.list_ctrl_do.GetFocusedItem() != -1:
            item = self.list_ctrl_do.GetItemText(self.list_ctrl_do.GetFocusedItem())
            Query.doingTask(item)
            self.update()
    def listView(self,button):
        self.text_ctrl_view.SetValue(button.GetItemText(button.GetFocusedItem()))
            
        
        
    def didTask(self,event):
        if self.list_ctrl_doing.GetFocusedItem() != -1:
            item = self.list_ctrl_doing.GetItemText(self.list_ctrl_doing.GetFocusedItem())

            Query.didTask(item)

            self.update()

    def clear(self,event):
        
        Query.clearTask()

        self.update()

        self.text_ctrl_view.SetValue('')        

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MainFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True



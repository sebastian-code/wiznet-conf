# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.6.8 on Tue Jan 20 07:13:47 2015
#

import wx
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class setup_frame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: setup_frame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.notebook_1 = wx.Notebook(self, wx.ID_ANY, style=0)
        self.notebook_1_pane_1 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.rbAddressMethod = wx.RadioBox(self.notebook_1_pane_1, wx.ID_ANY, _("Direccionamiento IP"), choices=[_("Static IP"), _("DHCP"), _("PPPoE")], majorDimension=3, style=wx.RA_SPECIFY_COLS)
        self.notebook_1_pane_2 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1_pane_3 = wx.Panel(self.notebook_1, wx.ID_ANY)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: setup_frame.__set_properties
        self.SetTitle(_("Herramienta de Configuracion para Wiznet WIZ110SR"))
        self.SetSize((650, 350))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.rbAddressMethod.SetMinSize((226, 43))
        self.rbAddressMethod.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.rbAddressMethod.SetForegroundColour(wx.Colour(1, 1, 1))
        self.rbAddressMethod.SetSelection(1)
        self.notebook_1_pane_1.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.notebook_1_pane_1.SetForegroundColour(wx.Colour(1, 1, 1))
        self.notebook_1_pane_2.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.notebook_1_pane_2.SetForegroundColour(wx.Colour(1, 1, 1))
        self.notebook_1_pane_3.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.notebook_1_pane_3.SetForegroundColour(wx.Colour(1, 1, 1))
        self.notebook_1.SetMinSize((650,350))
        self.notebook_1.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.notebook_1.SetForegroundColour(wx.Colour(1, 1, 1))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: setup_frame.__do_layout
        grid_sizer_3 = wx.FlexGridSizer(1, 1, 0, 0)
        grid_sizer_4 = wx.FlexGridSizer(5, 1, 0, 0)
        grid_sizer_4.Add(self.rbAddressMethod, 0, 0, 0)
        self.notebook_1_pane_1.SetSizer(grid_sizer_4)
        grid_sizer_4.AddGrowableRow(0)
        grid_sizer_4.AddGrowableRow(1)
        grid_sizer_4.AddGrowableRow(2)
        grid_sizer_4.AddGrowableRow(3)
        grid_sizer_4.AddGrowableRow(4)
        grid_sizer_4.AddGrowableCol(0)
        self.notebook_1.AddPage(self.notebook_1_pane_1, _("Network"))
        self.notebook_1.AddPage(self.notebook_1_pane_2, _("Serial"))
        self.notebook_1.AddPage(self.notebook_1_pane_3, _("Option"))
        grid_sizer_3.Add(self.notebook_1, 1, wx.EXPAND, 0)
        self.SetSizer(grid_sizer_3)
        grid_sizer_3.AddGrowableCol(0)
        self.Layout()
        # end wxGlade

# end of class setup_frame

import wx
import random
import string
import pyperclip

class PasswordGeneratorApp(wx.Frame):
    def __init__(self, parent, title):
        super(PasswordGeneratorApp, self).__init__(parent, title=title, size=(600, 400))
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.Colour(30, 30, 30))  # Set dark background color

        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Logo
        logo = wx.StaticBitmap(self.panel, bitmap=wx.Bitmap("logo.png"))
        main_sizer.Add(logo, 0, wx.ALL, 10)

        # Title
        self.title = wx.StaticText(self.panel, label="Generative Random Password")
        self.title.SetForegroundColour(wx.Colour(255, 255, 255))  # Set text color to white
        font = wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.title.SetFont(font)
        main_sizer.Add(self.title, 0, wx.ALL, 10)

        # Dropdown for selecting options
        self.options = wx.ComboBox(self.panel, choices=["Generative", "Customized"], style=wx.CB_READONLY)
        self.Bind(wx.EVT_COMBOBOX, self.on_option_select, self.options)
        main_sizer.Add(self.options, 0, wx.ALL | wx.EXPAND, 10)

        # Password display area
        self.password_display = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.password_display.SetBackgroundColour(wx.Colour(50, 50, 50))
        self.password_display.SetForegroundColour(wx.Colour(255, 255, 255))
        main_sizer.Add(self.password_display, 1, wx.ALL | wx.EXPAND, 10)

        # Generate and Copy buttons
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.generate_button = wx.Button(self.panel, label="Generate Password")
        self.Bind(wx.EVT_BUTTON, self.generate_password, self.generate_button)
        button_sizer.Add(self.generate_button, 0, wx.ALL, 10)

        self.copy_button = wx.Button(self.panel, label="Copy Password")
        self.Bind(wx.EVT_BUTTON, self.copy_password, self.copy_button)
        button_sizer.Add(self.copy_button, 0, wx.ALL, 10)

        main_sizer.Add(button_sizer, 0, wx.ALIGN_CENTER)

        self.panel.SetSizer(main_sizer)

        self.Show()

    def on_option_select(self, event):
        selected_option = self.options.GetValue()
        if selected_option == "Generative":
            self.show_generative_options()
        elif selected_option == "Customized":
            self.show_customized_options()

    def show_generative_options(self):
        # Clear any existing controls
        self.clear_display()

        # Add checkboxes for generative options
        self.checkboxes = []
        options = ["Uppercase", "Lowercase", "Numbers", "Symbols"]
        for option in options:
            checkbox = wx.CheckBox(self.panel, label=option)
            checkbox.SetValue(True)
            self.checkboxes.append(checkbox)

        # Add a dropdown for selecting password length
        self.length_label = wx.StaticText(self.panel, label="Password Length:")
        self.length_options = wx.ComboBox(self.panel, choices=["8", "12", "14", "16"], style=wx.CB_READONLY)
        self.length_options.SetSelection(0)

        # Add the controls to the sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.length_label, 0, wx.ALL, 10)
        sizer.Add(self.length_options, 0, wx.ALL, 10)
        for checkbox in self.checkboxes:
            sizer.Add(checkbox, 0, wx.ALL, 10)

        self.panel.GetSizer().Add(sizer)
        self.panel.Layout()

    def show_customized_options(self):
        # Clear any existing controls
        self.clear_display()

        # Add text input fields for customized options
        self.fav_name_label = wx.StaticText(self.panel, label="Favorite Name:")
        self.fav_name_text = wx.TextCtrl(self.panel)
        self.fav_number_label = wx.StaticText(self.panel, label="Favorite Number:")
        self.fav_number_text = wx.TextCtrl(self.panel)
        self.fav_color_label = wx.StaticText(self.panel, label="Favorite Color:")
        self.fav_color_text = wx.TextCtrl(self.panel)
        self.fav_symbol_label = wx.StaticText(self.panel, label="Favorite Symbol:")
        self.fav_symbol_text = wx.TextCtrl(self.panel)

        # Add a dropdown for selecting password length
        self.length_label = wx.StaticText(self.panel, label="Password Length:")
        self.length_options = wx.ComboBox(self.panel, choices=["8", "12", "14", "16"], style=wx.CB_READONLY)
        self.length_options.SetSelection(0)

        # Add the controls to the sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.fav_name_label, 0, wx.ALL, 10)
        sizer.Add(self.fav_name_text, 0, wx.ALL, 10)
        sizer.Add(self.fav_number_label, 0, wx.ALL, 10)
        sizer.Add(self.fav_number_text, 0, wx.ALL, 10)
        sizer.Add(self.fav_color_label, 0, wx.ALL, 10)
        sizer.Add(self.fav_color_text, 0, wx.ALL, 10)
        sizer.Add(self.fav_symbol_label, 0, wx.ALL, 10)
        sizer.Add(self.fav_symbol_text, 0, wx.ALL, 10)
        sizer.Add(self.length_label, 0, wx.ALL, 10)
        sizer.Add(self.length_options, 0, wx.ALL, 10)

        self.panel.GetSizer().Add(sizer)
        self.panel.Layout()

    def clear_display(self):
        sizer = self.panel.GetSizer()
        if sizer is not None:
            sizer.Clear(True)
            self.panel.Layout()

    def generate_password(self, event):
        selected_option = self.options.GetValue()
        if selected_option == "Generative":
            password_length = int(self.length_options.GetValue())
            selected_characters = ""
            for checkbox in self.checkboxes:
                if checkbox.GetValue():
                    if checkbox.GetLabel() == "Uppercase":
                        selected_characters += string.ascii_uppercase
                    elif checkbox.GetLabel() == "Lowercase":
                        selected_characters += string.ascii_lowercase
                    elif checkbox.GetLabel() == "Numbers":
                        selected_characters += string.digits
                    elif checkbox.GetLabel() == "Symbols":
                        selected_characters += string.punctuation

            if len(selected_characters) < 2:
                wx.MessageBox("Please select at least 2 character sets.", "Error", wx.OK | wx.ICON_ERROR)
                return

            password = ''.join(random.choices(selected_characters, k=password_length))
            self.password_display.SetValue(password)

        elif selected_option == "Customized":
            # Customized password generation logic goes here
            pass

    def copy_password(self, event):
        password = self.password_display.GetValue()
        pyperclip.copy(password)
        wx.MessageBox("Password Copied to Clipboard", "Success", wx.OK | wx.ICON_INFORMATION)

if __name__ == "__main__":
    app = wx.App(False)
    frame = PasswordGeneratorApp(None, "Password Generator")
    app.MainLoop()

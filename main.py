# Import customtkinter module
import customtkinter as ctk
 
# Sets the appearance mode of the application
# Dark, Light, or System
ctk.set_appearance_mode("Dark")       
 
# Sets the color of the widgets
# Supported themes: green, dark-blue, blue
ctk.set_default_color_theme("green")   
 
# Create App class
class App(ctk.CTk):
# Layout of the GUI will be written in the init itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
# Sets the title of our window to "App"
        self.title("TwitchPlaysGUI")   
# Dimensions of the window will be 960x540
        self.geometry("960x540")   
 
 
if __name__ == "__main__":
    app = App()
    # Runs the app
    app.mainloop()   
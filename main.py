# Kivy
from kivy.lang                  import Builder
from kivy.app                   import App
from kivy.config                import Config
from kivy.uix.screenmanager     import ScreenManager
from kivy.properties            import ColorProperty

# User
from components.imagescreen.imagescreen     import ImageScreen
from components.userprofile.userprofile     import UserProfile
from components.usersettings.usersettings   import UserSettings





# fix app size
Config.set('graphics', 'width', '275')
Config.set('graphics', 'height', '540')





#
# Manager
#
# Screen Manager widget that contains the following screens:
#   - ImageScreen
#   - UserProfile
#   - UserSettings
#
class Manager(ScreenManager):
    pass
#





# 
# App class
#
class MainApp(App):
    pass
#





def main():
    MainApp().run()
#





if __name__ == '__main__':
    main()
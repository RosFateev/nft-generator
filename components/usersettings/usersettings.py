# Kivy
from kivy.lang                  import Builder
from kivy.uix.screenmanager     import Screen





# add kivy file
Builder.load_file('components/usersettings/usersettings.kv')





#
# UserSettings contains:
#   - settings component - multiple buttons controlling App functionality
#   - navigation component

class UserSettings(Screen):
    pass
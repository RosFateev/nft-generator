# Kivy
from kivy.lang                  import Builder
from kivy.app                   import App

from kivy.uix.screenmanager     import ScreenManager

# User
from imagescreen    import ImageScreen
from buttonscreen   import ButtonScreen





class MyManager(ScreenManager):
    pass






# app
class TestApp(App):
    pass
#





#
def main():
    TestApp().run()   
#





if __name__ == '__main__':
    main()
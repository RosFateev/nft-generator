# Standard
from os                         import scandir

# Kivy
from kivy.lang                  import Builder
from kivy.uix.scrollview        import ScrollView
from kivy.uix.screenmanager     import Screen
from kivy.uix.gridlayout        import GridLayout
from kivy.uix.image             import Image





# add kivy file
Builder.load_file('components/userprofile/userprofile.kv')





#
# Gallery - ScrollView component containing saved images
#
class Gallery(ScrollView):

    def __init__(self, **kwargs):

        super().__init__()

        # create stack layout with saved images
        self.add_widget(self.populate())
    #



    def populate(self):
        
        layout = GridLayout(size_hint_y=None, cols=2, padding=5, spacing=5)
        layout.bind(minimum_height=layout.setter('height'))

        dir_path = 'resources/image/saved/'
        
        with scandir(dir_path) as iterator:

            for entry in iterator:

                if entry.is_file():

                    layout.add_widget(Image(source=dir_path + entry.name, size_hint=(None, None), width=100, height=200))

        return layout
    #
#





#
# UserProfile contains:
#   - Gallery - a ScrollView widget displaying saved pictures
#   - navigation component
#
class UserProfile(Screen):
    pass
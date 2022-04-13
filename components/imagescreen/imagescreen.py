# Standard
from random                     import randint

# Kivy
from kivy.lang                  import Builder
from kivy.uix.screenmanager     import Screen
from kivy.uix.floatlayout       import FloatLayout
from kivy.uix.image             import Image

# User
from components.imagescreen.composite_image.image      import AtlasManager





# add kivy file
Builder.load_file('components/imagescreen/imagescreen.kv')





#
# Loads images on top of each other
#
class ImageFrame(FloatLayout):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.manager = AtlasManager()

        for atlas in self.manager.atlases:
            self.add_widget(Image(source=self.get_image_path(atlas)))
    #



    def get_image_path(self, atlas_name):
        # 'atlas://resources/image/atlas/atlas_name/atlas_name/'
        return 'atlas://' + self.manager.atlas_path + atlas_name + '/' + atlas_name + '/' + self.pick_image(atlas_name)
    #



    def pick_image(self, atlas_name):

        image_list = list(self.manager.atlases[atlas_name].textures.keys())
        
        return image_list[randint(0, len(image_list) - 1)]
    #



    # reselects and reloads images
    def refresh(self):
        
        atlases = list(self.manager.atlases.keys())[::-1]

        for index, image in reversed(list(enumerate(self.children))):

            image.source = self.get_image_path(atlases[index])
    #
#





#
# ImageScreen contains:
#   - ImageViewer - a Carousel widget which will load a generated composite image through Atlas
#   - navigation component
#
class ImageScreen(Screen):
    pass
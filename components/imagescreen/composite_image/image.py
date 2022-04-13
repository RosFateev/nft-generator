from os                     import scandir, system
from os.path                import exists
from random                 import randint

from kivy.lang              import Builder
from kivy.atlas             import Atlas
#from kivy.uix.image 		import Image
#from kivy.atlas             import Atlas       # image composition component










#
# Constructs multiple atlases for a given image bank
#
class AtlasBuilder:

    def __init__( self, s_path, d_path, i_dirs, i_dims):

        self.src_path = s_path
        self.dst_path = d_path
        self.img_dirs = i_dirs
        self.image_dim = i_dims

        # construct component images' atlases for each category's directory
        for directory in img_dirs:

            files_list = self.get_files(self.src_path + directory)

            self.construct_atlas(directory, files_list)
    #




    # scans directory and outputs list of files in it
    def get_files(self, path):

        files_list = []
        
        with scandir(path) as iterator:
            
            for item in iterator:
                
                if item.is_file():
                    files_list.append(item.name)
        
        return files_list
    #





    # 
    def construct_atlas(self, atlas_name, files_list):

        command = 'python3 -m kivy.atlas ' + atlas_name + ' ' + str(self.image_dim[0]) + 'x' + str(self.image_dim[1])

        # add files to compose atlas
        for file_name in files_list:

            full_file_name = self.src_path + atlas_name + '/' + file_name
            command += ' ' + full_file_name
        
        # construct atlas        
        system(command)
    #
# python3 -m kivy.atlas body 3515x3840 *.png




#
# Manages an atlas instance
#
class AtlasManager:

    def __init__(self, force_construct=False):

        self.src_path = 'resources/image/bank/'
        self.atlas_path = 'resources/image/atlas/'
        self.img_dirs = ['body', 'head', 'eyes', 'features']
        self.image_dim = [ 3515, 3840]
        self.atlases = {}

        # load atlases into dictionary
        for directory in self.img_dirs:
            self.atlases[directory] = Atlas(self.atlas_path + directory + '/' + directory + '.atlas')
    #





    # scans atlases and selects randomly in each a file
    def get_images(self):

        images = []



        return images
    #
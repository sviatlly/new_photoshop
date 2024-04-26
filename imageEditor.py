from PIL import Image
from PIL import ImageFilter
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import os

class ImageEditor(): 
    def __init__ (self,_main_picture_,names_photes):
        self._main_picture_= _main_picture_
        self.names_photes = names_photes

    def _open_ (self,path_to_images,file_name):
        self.file_name = file_name
        self.full_path_image = path_to_images +'/'+ file_name
        self.path_to_images = path_to_images
        print (self.full_path_image)
        try:
            self.image= Image.open(self.full_path_image)
        except:
            print('файл не найден.')
    
    def _save_(self,filter_name,new_image):
        self.new_file_name = os.path.join(self.path_to_images,self.file_name[0:-4] + f' {filter_name}.png') 
        new_image.save(self.new_file_name)
        self._show_(self.path_to_images,self.file_name[0:-4] +f' {filter_name}.png')
        self.upgrade_file_names()

    def upgrade_file_names(self):
        file_names= os.listdir(self.path_to_images)
        self.names_photes.clear()
        correct_files = []
        for name in file_names:
            if name.endswith('.png')or name.endswith('.jpg')or name.endswith('.gif')or name.endswith('.tif.')or name.endswith('.bmp')or name.endswith('.eps')or name.endswith('.svg')or name.endswith('.psd')or name.endswith('.ai')or name.endswith('.raw')or name.endswith('.webp')or name.endswith('.heic')or name.endswith('.hdr')or name.endswith('.dng')or name.endswith('.indd')or name.endswith('.cdr')or name.endswith('.tga'):
                correct_files.append(name)
        self.names_photes.addItems(correct_files)

    def _show_(self,path_to_images,file_name):
        self._open_(path_to_images,file_name)
        self._main_picture_.hide()
        pix_picture = QPixmap(self.full_path_image)
        w, h = self._main_picture_.width(), self._main_picture_.height() 
        pix_picture = pix_picture.scaled(w, h, Qt.KeepAspectRatio)
        self._main_picture_.setPixmap(pix_picture)
        self._main_picture_.show()
        
    def rotate(self):
        new_image = self.image.transpose(Image.ROTATE_90)
        self._save_(filter_name='rotate', new_image=new_image)

    def blur(self):
        new_image = self.image.filter(ImageFilter.BLUR)
        self._save_(filter_name='blur', new_image=new_image)

    def black_white(self):
        new_image = self.image.convert('L')
        self._save_(filter_name='black_white', new_image=new_image)

    def contuor(self):
        new_image = self.image.filter(ImageFilter.CONTOUR)
        self.new_file_name = os.path.join(self.path_to_images,'contuor.png')
        new_image.save(self.new_file_name)
        
    def detail(self):
        new_image = self.image.filter(ImageFilter.DETAIL)
        self.new_file_name = os.path.join(self.path_to_images,'detail.png')
        new_image.save(self.new_file_name)

    def edge_enhance(self):
        new_image = self.image.filter(ImageFilter.EDGE_ENHANCE)
        self.new_file_name = os.path.join(self.path_to_images,'edge_enhance.png')
        new_image.save(self.new_file_name)

    def edge_enhance_more(self):
        new_image = self.image.filter(ImageFilter.EDGE_ENHANCE_MORE)
        self.new_file_name = os.path.join(self.path_to_images,'edge_enhance_more.png')
        new_image.save(self.new_file_name)

    def embross(self):
        new_image = self.image.filter(ImageFilter.EMBOSS)
        self.new_file_name = os.path.join(self.path_to_images,'embross.png')
        new_image.save(self.new_file_name)

    def find_edges(self):
        new_image = self.image.filter(ImageFilter.FIND_EDGES)
        self.new_file_name = os.path.join(self.path_to_images,'find_edges.png')
        new_image.save(self.new_file_name)

    def sharpen(self):
        new_image = self.image.filter(ImageFilter.SHARPEN)
        self.new_file_name = os.path.join(self.path_to_images,'sharpen.png')
        new_image.save(self.new_file_name)

    def smooth(self):
        new_image = self.image.filter(ImageFilter.GaussianBlur(radius=2))
        self.new_file_name = os.path.join(self.path_to_images,'smooth.png')
        new_image.save(self.new_file_name)
        #self.image.save('image_name_smooth.png', quality=95)
    
    def smooth_more(self):
        new_image = self.image.filter(ImageFilter.GaussianBlur(radius=4))
        self.new_file_name = os.path.join(self.path_to_images,'smooth_more.png')
        new_image.save(self.new_file_name)
        #self.image.save('image_name_smooth_more.png', quality=95)

    def mirror(self):
        new_image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.new_file_name = os.path.join(self.path_to_images,'mirror.png')
        new_image.save(self.new_file_name)
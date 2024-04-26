from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,QHBoxLayout,QListWidget,QFileDialog
import os
from PIL import Image
from PIL import ImageFilter
from imageEditor import ImageEditor
    
def item_clicked():
    global path_to_images
    file_name = names_photes.selectedItems()[0].text()
    #full_path_image = os.path.join(path_to_images,file_name) 
    #main_picture.setText(full_path_image)
    image_editor._show_(path_to_images,file_name)

def get_file_names():
    global path_to_images
    path_to_images =QFileDialog.getExistingDirectory()
    file_names= os.listdir(path_to_images)
    names_photes.clear()
    correct_files = []
    for name in file_names:
        if name.endswith('.png')or name.endswith('.jpg')or name.endswith('.gif')or name.endswith('.tif.')or name.endswith('.bmp')or name.endswith('.eps')or name.endswith('.svg')or name.endswith('.psd')or name.endswith('.ai')or name.endswith('.raw')or name.endswith('.webp')or name.endswith('.heic')or name.endswith('.hdr')or name.endswith('.dng')or name.endswith('.indd')or name.endswith('.cdr')or name.endswith('.tga'):
            correct_files.append(name)
    names_photes.addItems(correct_files)

appppp =QApplication([])
winrar = QWidget()
winrar.show()
main_picture = QLabel('Картинка')
names_photes = QListWidget()
image_editor = ImageEditor(main_picture,names_photes)   
winrar.setWindowTitle('Photoshop')
buton_open = QPushButton('Открыть папку') 
buton_open.clicked.connect(get_file_names)     
edge_enhance= QPushButton('Увеличить края')
edge_enhance.clicked.connect(image_editor.edge_enhance)
edge_enhance_more= QPushButton('Ещё увеличить края')
edge_enhance_more.clicked.connect(image_editor.edge_enhance_more)
embross= QPushButton('Рельеф')
embross.clicked.connect(image_editor.embross)
find_edges= QPushButton('Найти края')
find_edges.clicked.connect(image_editor.find_edges)
sharpen= QPushButton('Резкость')
sharpen.clicked.connect(image_editor.sharpen)
smooth= QPushButton('Сгладить(размыть)')  
smooth.clicked.connect(image_editor.smooth)
smooth_more= QPushButton('Сильнее сгладить(размыть)')
smooth_more.clicked.connect(image_editor.smooth_more)
mirror= QPushButton('Отзеркалить')
mirror.clicked.connect(image_editor.mirror)
buton_black_white = QPushButton('Ч/Б') 
buton_black_white.clicked.connect(image_editor.black_white)
buton_rotate_90 = QPushButton('Поворот') 
buton_rotate_90.clicked.connect(image_editor.rotate)
buton_blur = QPushButton('Блюр')
buton_blur.clicked.connect(image_editor.blur)
buton_contour = QPushButton('Контур')
buton_contour.clicked.connect(image_editor.contuor)
names_photes.itemClicked.connect(item_clicked)

line_main = QHBoxLayout()
line_filters1 = QHBoxLayout()
line_filters2 = QHBoxLayout()
line_right= QVBoxLayout()
line_left= QVBoxLayout()
line_left.addWidget(buton_open)
line_left.addWidget(names_photes)
line_right.addWidget(main_picture)
line_right.addLayout(line_filters1)
line_right.addLayout(line_filters2)
line_filters1.addWidget(buton_black_white)
line_filters1.addWidget(buton_rotate_90)
line_filters1.addWidget(buton_blur)
line_filters1.addWidget(buton_contour)
line_filters2.addWidget(mirror)
line_filters2.addWidget(sharpen)
line_filters2.addWidget(smooth)
line_main.addLayout(line_left)
line_main.addLayout(line_right)

winrar.move(60,100)
winrar.setLayout(line_main)
winrar.resize(750,500)
winrar.setStyleSheet('''font-size:20px''')  
winrar.show()
appppp.exec()
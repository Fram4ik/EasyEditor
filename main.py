from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QLabel, QPushButton, QListWidget, QVBoxLayout, QHBoxLayout, QWidget, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap
from PIL import Image,ImageFilter
import os


layout_main = QHBoxLayout()
app = QApplication([])
list1 = QListWidget()
label = QLabel("картинка")
papka = QPushButton("Папка")
levo = QPushButton("Лево")
pravo = QPushButton("Право")
zerkalo = QPushButton("Зеркало")
rezkast = QPushButton("Резкость")
black = QPushButton("Ч/Б")
layout_1 = QVBoxLayout()
layout_2 = QHBoxLayout()
layout_3 = QVBoxLayout()
layout_main.addLayout(layout_1) 
layout_main.addLayout(layout_3) 
layout_3.addLayout(layout_2)
win = QWidget()
win.setLayout(layout_main)
win.show()

layout_1.addWidget(list1, alignment = Qt.AlignCenter) 
layout_1.addWidget(papka, alignment = Qt.AlignCenter) 
layout_3.addWidget(levo, alignment = Qt.AlignCenter) 
layout_3.addWidget(pravo, alignment = Qt.AlignCenter) 
layout_3.addWidget(zerkalo, alignment = Qt.AlignCenter) 
layout_3.addWidget(rezkast, alignment = Qt.AlignCenter) 
layout_3.addWidget(black, alignment = Qt.AlignCenter) 

def chooseWorkdir():
	global workdir
	workdir = QFileDialog.getExistingDirectory()

#files = ['a.txt','b.png','c.png']
#extensions = ['jpg','png','bmp']
def filter(files,extensions):
	result = []
	for name in files:
		for ext in extensions:
			if name.endswith(ext):
				result.append(name)
	return result

def showFilenamesList():
	extensions = ['jpg','png','jpeg','gif','bmp']
	chooseWorkdir()
	filenames = filter(os.listdir(workdir),etensions)
	listw.clear()
	for name in filenames:
		listw.addItem(name)

class ImageProcessor:

	def __init__(self):
		self.image = None	
		self.name = None
		self.savedir = "modified/"
		self.path = None

	def loadImage(self,path,name):
		self.path = path
		self.name = name
		image_path = os.path.join(path,name)
		self.image = Image.open(self.image_path)

	def showImage(self):
		label.hide()
		image_pixmap = QPixmap(self.image_path)
		image_pixmap = image_pixmap.scaled(
			label.width(),
			label.height(),
			Qt.KeepAspectRatio)
		label.setPixmap(image_pixmap)
		label.show()

	def saveImage(self):
		test_path = os.path.join(self.path,self.savedir)
		test_path = os.path.join(self.image_path,self.name)
		self.image.save(save_path)

	def do_bw(self):
		self.image = self.imageconvert("L")
		self.saveImage()
		self.image_path = os.path.join(self.path,self.savedir)
		self.image_path = os.path.join(self.image_path,self.name)
		self.showImage()


def showChosenImage():
	if list1.currentRow() >=0:
		filename = list1.currentItem().text()
		processor.loadImage(workdir,filename)
		processor.showImage()


processor = ImageProcessor()

list1.currentRowChanged.connect(showChosenImage)
papka.clicked.connect(chooseWorkdir)
black.clicked.connect(processor.do_bw)
app.exec_()

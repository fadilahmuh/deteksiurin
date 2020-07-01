import numpy as np
import sys
import cv2
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi
from cv2 import *
import tkinter as tk
from tkinter import filedialog


class ShowImage(QMainWindow):
    def __init__(self):
        super(ShowImage, self).__init__()
        global copyimg
        loadUi('urin.ui', self)
        self.image = None
        self.load.clicked.connect(self.loadImg)
        self.proses.clicked.connect(self.preproses)


    @pyqtSlot()

    def loadImg(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(
                parent=root, initialdir='C:/Tutorial',
                title='Choose file',
                filetypes=[('Image Files',('*.jpg','*.jpeg','*.png','*.bmp'))])
        print(file_path)
        self.image = cv2.imread(file_path)
        qtformat = QImage.Format_Indexed8
        if len(self.image.shape) - -3:
            if (self.image.shape[2]) == 4:
                qtformat = QImage.Format_RGBA8888
            else:
                qtformat = QImage.Format_RGB888
        img = QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.strides[0], qtformat)
        img = img.rgbSwapped()
        self.label.setPixmap(QPixmap.fromImage(img))
        self.label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)


    def preproses(self) :
        copyimg = self.image
        H, W = copyimg.shape[:2]
        gray = np.zeros((H, W), np.uint8)
        for i in range(H):
            for j in range(W):
                gray[i, j] = np.clip(
                    0.299 * copyimg[i, j, 0] + 0.587 * copyimg[i, j, 1] + 0.114 * copyimg[i, j, 2], 0, 255)
        qtformat = QImage.Format_Indexed8
        img = QImage(gray, gray.shape[1], gray.shape[0], gray.strides[0], qtformat)
        img = img.rgbSwapped()
        self.label.setPixmap(QPixmap.fromImage(img))
        self.label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        print(gray[50:55, 50:55])





app = QtWidgets.QApplication(sys.argv)

window = ShowImage()
window.setWindowTitle('Show Image GUI')
window.show()
sys.exit(app.exec_())
# -*- coding: utf-8 -*-

"""
/***************************************************************************
  play_thread.py

  An play for mms_foto_viewer QGIS plugin.
  --------------------------------------
  Date : 2022
  Copyright: (C) 2022 by Kyryloo Zharkovskyi
  Email: kyrylo.zharkovskyi@gmail.com
/***************************************************************************
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 2 as published
 * by the Free Software Foundation.
 *
 ***************************************************************************/
"""

from PyQt5 import QtCore
import time
from qgis.PyQt.QtWidgets import (QGraphicsView, QGraphicsScene, QVBoxLayout, QHBoxLayout, QWidget,
    QLineEdit, QLabel, QSizePolicy, QPushButton, QFrame, QMenuBar, QAction, qApp, QFileDialog, QMessageBox)
from qgis.PyQt.QtCore import (Qt, pyqtSignal, QRectF, QRect, QSize, QCoreApplication)
from qgis.PyQt.QtGui import (QPainterPath, QIcon, QPixmap, QImage, QFont)
import os.path

        
#====================================================================================================================

class play(QtCore.QThread):

    Back_handleButton_signal = QtCore.pyqtSignal()
    Forward_handleButton_signal = QtCore.pyqtSignal()

    def __init__(self, parent, delay, go_forward):
        super(play, self).__init__(parent)
        self._delay = delay / 1000.0
        self._go_forward = go_forward
        self._work = False

    def run(self):
        while self._work:
            if self._go_forward:
                self.Forward_handleButton_signal.emit()
            else:
                self.Back_handleButton_signal.emit()
            time.sleep(self._delay)

    def start_run(self):
        self._work = True
        self.start()

    def stop_run(self):
        self._work = False
        time.sleep(self._delay + 0.1)
    


        
#====================================================================================================================

    

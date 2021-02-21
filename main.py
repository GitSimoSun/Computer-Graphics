#coding: utf-8

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QEvent, pyqtSignal
from PyQt5.QtWidgets import (QWidget, QLineEdit, QLabel, QPushButton, QSizePolicy, QMessageBox)
from bresnham import Ui_BresnhamMainWindow
from clipping import Ui_ClippingMainWindow
from scanline import Ui_ScanLineMainWindow
from curves import Ui_CurvesMainWindow

class inputFocusFilter(QObject):
	focusIn = pyqtSignal(object)

	def eventFilter(self, widget, event):
		if event.type() == QEvent.FocusIn and isinstance(widget, QLineEdit):
			self.focusIn.emit(widget)
		return super(inputFocusFilter, self).eventFilter(widget, event)

class MyApplication(QtWidgets.QApplication):
	def __init__(self, *arg, **kwarg):
		super(MyApplication, self).__init__(*arg, **kwarg)

		self._input_focus_widget = None

		self.event_filter = inputFocusFilter()
		self.event_filter.focusIn.connect(self.setInputFocusWidget)
		self.installEventFilter(self.event_filter)

	def setInputFocusWidget(self, widget):
		self._input_focus_widget = widget

	def inputFocusWidget(self):
		return self._input_focus_widget


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1024, 768)
		MainWindow.setMinimumSize(QtCore.QSize(1024, 768))
		MainWindow.setMaximumSize(QtCore.QSize(1024, 768))
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("cg.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
		MainWindow.setWindowIcon(icon)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.home = QtWidgets.QWidget(self.centralwidget)
		self.home.setStyleSheet("*{\n"
"    background-color:rgb(253,253,253);\n"
"    color: #000\n"
"}\n"
"QPushButton{\n"
"    border: 3px solid black;\n"
"    border-radius:5px\n"
"}")
		self.home.setObjectName("home")
		self.verticalLayoutWidget = QtWidgets.QWidget(self.home)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(240, 320, 511, 361))
		self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
		self.menu_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
		self.menu_layout.setContentsMargins(0, 0, 0, 0)
		self.menu_layout.setObjectName("menu_layout")
		self.bresnham_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.bresnham_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.bresnham_btn.setStyleSheet("font: 24px \"MS Shell Dlg 2\";\n"
"padding: 10px;\n"
"")
		self.bresnham_btn.setObjectName("bresnham_btn")
		self.menu_layout.addWidget(self.bresnham_btn)
		self.fenetrage_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.fenetrage_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.fenetrage_btn.setStyleSheet("font: 24px \"MS Shell Dlg 2\";\n"
"padding: 10px;")
		self.fenetrage_btn.setObjectName("fenetrage_btn")
		self.menu_layout.addWidget(self.fenetrage_btn)
		self.remplissage_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.remplissage_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.remplissage_btn.setStyleSheet("font: 24px \"MS Shell Dlg 2\";\n"
"padding: 10px;")
		self.remplissage_btn.setObjectName("remplissage_btn")
		self.menu_layout.addWidget(self.remplissage_btn)
		self.courbes_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.courbes_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.courbes_btn.setStyleSheet("font: 24px \"MS Shell Dlg 2\";\n"
"padding: 10px;")
		self.courbes_btn.setObjectName("courbes_btn")
		self.menu_layout.addWidget(self.courbes_btn)
		self.frame = QtWidgets.QFrame(self.home)
		self.frame.setGeometry(QtCore.QRect(240, 60, 211, 191))
		self.frame.setStyleSheet("background:url(:/newPrefix/cg.jpg); border:none")
		self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame.setObjectName("frame")
		self.label = QtWidgets.QLabel(self.home)
		self.label.setGeometry(QtCore.QRect(410, 80, 411, 151))
		self.label.setStyleSheet("margin: 0 auto;\n"
"font: 75 italic 24pt \"MS Sans Serif\";")
		self.label.setObjectName("label")
		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def show_bresnham_window(self):
		self.bresnham = QtWidgets.QMainWindow()
		self.ui = Ui_BresnhamMainWindow()
		self.ui.setupUi(self.bresnham)
		self.bresnham.show()

	def show_clipping_window(self):
		self.Clipping = QtWidgets.QMainWindow()
		self.ui = Ui_ClippingMainWindow()
		self.ui.setupUi(self.Clipping)
		self.Clipping.show()

	def show_scanline_window(self):
		self.scanline = QtWidgets.QMainWindow()
		self.ui = Ui_ScanLineMainWindow()
		self.ui.setupUi(self.scanline)
		self.scanline.show()

	def show_curves_window(self):
		self.curves = QtWidgets.QMainWindow()
		self.ui = Ui_CurvesMainWindow()
		self.ui.setupUi(self.curves)
		self.curves.show()


	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Computer Graphics"))
		self.bresnham_btn.setText(_translate("MainWindow", "Traçage des objets"))
		self.bresnham_btn.clicked.connect(self.show_bresnham_window)
		self.fenetrage_btn.setText(_translate("MainWindow", "Fenêtrage"))
		self.fenetrage_btn.clicked.connect(self.show_clipping_window)
		self.remplissage_btn.setText(_translate("MainWindow", "Remplissage"))
		self.remplissage_btn.clicked.connect(self.show_scanline_window)
		self.courbes_btn.setText(_translate("MainWindow", "Courbes"))
		self.courbes_btn.clicked.connect(self.show_curves_window)
		self.label.setText(_translate("MainWindow", "Computer Graphics"))

import resources


if __name__ == "__main__":
	app = MyApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())

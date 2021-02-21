#coding: utf-8

import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QEvent, pyqtSignal
from PyQt5.QtWidgets import (QWidget, QLineEdit, QLabel, QPushButton, QSizePolicy, QMessageBox)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas , NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from math import *
from bresnham_line import droite_bresenham
from bresnham_circle import circle
from bresnham_ellipse import ellipse


class PlotCanvas(FigureCanvas):
	def __init__(self, parent = None, width = 5, height = 4, dpi = 100):
		fig = Figure(figsize = (width, height), dpi= dpi)
		self.ax = fig.add_subplot(111)
		FigureCanvas.__init__(self, fig)
		self.setParent(parent)
		FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
		FigureCanvas.updateGeometry(self)

	def plot_line(self, data):
		self.ax.cla()
		xs = [d[0] for d in data]
		ys = [d[1] for d in data]
		p1 = data[0]
		p2 = data[-1]
		pente = (p2[1] - p1[1]) / (p2[0] - p1[0])
		x = np.arange(round(min(p1[0], p2[0])), round(max(p1[0], p2[0]) + 1))
		y = p1[1] + pente * (x - p1[0])	
		original_line, = self.ax.plot(x, y, 'r')
		for x , y  in data:
			scatter = self.ax.scatter(x, y, c='b')
		self.ax.legend([scatter, original_line],['Bresenham Pixels', 'Original Line'])
		self.ax.set_aspect('equal', adjustable='box')
		self.draw()

	def plot_circle(self, data):
		self.ax.cla()
		for x , y  in data:
			scatter = self.ax.scatter(x, y, c='b')
		self.ax.legend([scatter], ['Bresenham Pixels'])
		self.ax.set_aspect('equal', adjustable='box')
		self.draw()

	def plot_ellipse(self, data):
		self.ax.cla()
		for x , y  in data:
			scatter = self.ax.scatter(x, y, c='b')
		self.ax.legend([scatter], ['Bresenham Pixels'])
		self.ax.set_aspect('equal', adjustable='box')
		self.draw()

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

class Ui_BresnhamMainWindow(object):
	def __init__(self):
		self.new = False
	def setupUi(self, BresnhamMainWindow):
		BresnhamMainWindow.setObjectName("BresnhamMainWindow")
		BresnhamMainWindow.resize(1024, 768)
		BresnhamMainWindow.setMinimumSize(QtCore.QSize(1024, 768))
		BresnhamMainWindow.setMaximumSize(QtCore.QSize(1024, 768))
		BresnhamMainWindow.setStyleSheet("background-color: #fff")
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("cg.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
		BresnhamMainWindow.setWindowIcon(icon)		
		self.centralwidget = QtWidgets.QWidget(BresnhamMainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.bresnham_stacked = QtWidgets.QStackedWidget(self.centralwidget)
		self.bresnham_stacked.setGeometry(QtCore.QRect(200, 0, 820, 768))
		self.bresnham_stacked.setMinimumSize(QtCore.QSize(820, 768))
		self.bresnham_stacked.setMaximumSize(QtCore.QSize(820, 750))
		self.bresnham_stacked.setObjectName("bresnham_stacked")
		self.bresnham_ellipse = QtWidgets.QWidget()
		self.bresnham_ellipse.setObjectName("bresnham_ellipse")
		self.groupBox_3 = QtWidgets.QGroupBox(self.bresnham_ellipse)
		self.groupBox_3.setGeometry(QtCore.QRect(60, 40, 571, 100))
		self.groupBox_3.setStyleSheet("background-color:#abff8d;\n"
"border-radius: 5px;")
		self.groupBox_3.setTitle("")
		self.groupBox_3.setObjectName("groupBox_3")
		self.label_37 = QtWidgets.QLabel(self.groupBox_3)
		self.label_37.setGeometry(QtCore.QRect(4, 20, 21, 60))
		self.label_37.setMinimumSize(QtCore.QSize(21, 60))
		self.label_37.setMaximumSize(QtCore.QSize(21, 60))
		font = QtGui.QFont()
		font.setFamily("Calibri")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.label_37.setFont(font)
		self.label_37.setObjectName("label_37")
		self.ellipse_c_x = QtWidgets.QLineEdit(self.groupBox_3)
		self.ellipse_c_x.setGeometry(QtCore.QRect(30, 37, 101, 26))
		self.ellipse_c_x.setMinimumSize(QtCore.QSize(101, 26))
		self.ellipse_c_x.setMaximumSize(QtCore.QSize(101, 26))
		self.ellipse_c_x.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.ellipse_c_x.setObjectName("ellipse_c_x")
		self.label_38 = QtWidgets.QLabel(self.groupBox_3)
		self.label_38.setGeometry(QtCore.QRect(138, 20, 21, 60))
		self.label_38.setMinimumSize(QtCore.QSize(21, 60))
		self.label_38.setMaximumSize(QtCore.QSize(21, 60))
		font = QtGui.QFont()
		font.setFamily("Calibri")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.label_38.setFont(font)
		self.label_38.setObjectName("label_38")
		self.label_39 = QtWidgets.QLabel(self.groupBox_3)
		self.label_39.setGeometry(QtCore.QRect(255, 20, 21, 60))
		self.label_39.setMinimumSize(QtCore.QSize(21, 60))
		self.label_39.setMaximumSize(QtCore.QSize(21, 60))
		font = QtGui.QFont()
		font.setFamily("Calibri")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.label_39.setFont(font)
		self.label_39.setObjectName("label_39")
		self.label_40 = QtWidgets.QLabel(self.groupBox_3)
		self.label_40.setGeometry(QtCore.QRect(270, 20, 33, 60))
		self.label_40.setMinimumSize(QtCore.QSize(33, 60))
		self.label_40.setMaximumSize(QtCore.QSize(33, 60))
		font = QtGui.QFont()
		font.setFamily("Calibri")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.label_40.setFont(font)
		self.label_40.setObjectName("label_40")
		self.ellipse_r_y = QtWidgets.QLineEdit(self.groupBox_3)
		self.ellipse_r_y.setGeometry(QtCore.QRect(460, 37, 101, 26))
		self.ellipse_r_y.setMinimumSize(QtCore.QSize(101, 26))
		self.ellipse_r_y.setMaximumSize(QtCore.QSize(101, 26))
		self.ellipse_r_y.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.ellipse_r_y.setObjectName("ellipse_r_y")
		self.ellipse_r_x = QtWidgets.QLineEdit(self.groupBox_3)
		self.ellipse_r_x.setGeometry(QtCore.QRect(310, 37, 101, 26))
		self.ellipse_r_x.setMinimumSize(QtCore.QSize(101, 26))
		self.ellipse_r_x.setMaximumSize(QtCore.QSize(101, 26))
		self.ellipse_r_x.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.ellipse_r_x.setObjectName("ellipse_r_x")
		self.ellipse_c_y = QtWidgets.QLineEdit(self.groupBox_3)
		self.ellipse_c_y.setGeometry(QtCore.QRect(147, 37, 101, 26))
		self.ellipse_c_y.setMinimumSize(QtCore.QSize(101, 26))
		self.ellipse_c_y.setMaximumSize(QtCore.QSize(101, 26))
		self.ellipse_c_y.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.ellipse_c_y.setObjectName("ellipse_c_y")
		self.label_43 = QtWidgets.QLabel(self.groupBox_3)
		self.label_43.setGeometry(QtCore.QRect(420, 20, 33, 60))
		self.label_43.setMinimumSize(QtCore.QSize(33, 60))
		self.label_43.setMaximumSize(QtCore.QSize(33, 60))
		font = QtGui.QFont()
		font.setFamily("Calibri")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.label_43.setFont(font)
		self.label_43.setObjectName("label_43")
		#ellipse plotting
		self.ellipse_graph_box = QtWidgets.QGroupBox(self.bresnham_ellipse)
		self.ellipse_graph_box.setGeometry(QtCore.QRect(60, 220, 691, 511))
		ellipse_graph = PlotCanvas(self.ellipse_graph_box, width=6.9, height=5.1, dpi=100)
		ellipse_toolbar = NavigationToolbar(ellipse_graph, self.ellipse_graph_box)
		ellipse_toolbar.move(80, 0)		
		self.ellipse_graph_box.setStyleSheet("border: none;\n")
		self.ellipse_ok = QtWidgets.QPushButton(self.bresnham_ellipse)
		self.ellipse_ok.clicked.connect(lambda: self.ellipse_graph_plot(ellipse_graph))
		self.ellipse_ok.setGeometry(QtCore.QRect(640, 48, 100, 40))
		font = QtGui.QFont()
		font.setFamily("Calibri")
		font.setPointSize(10)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.ellipse_ok.setFont(font)
		self.ellipse_ok.setStyleSheet("background-color: #abff8d;\n"
"border-radius: 5px;")
		self.ellipse_ok.setObjectName("ellipse_ok")
		self.ellipse_keyboard_btn = QtWidgets.QPushButton(self.bresnham_ellipse)
		self.ellipse_keyboard_btn.setGeometry(QtCore.QRect(640, 92, 100, 40))
		self.ellipse_keyboard_btn.setStyleSheet("background-color: #abff8d;\n"
"border-radius: 5px;")
		self.ellipse_keyboard_btn.setText("")
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/newPrefix/keyboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
		self.ellipse_keyboard_btn.setIcon(icon)
		self.ellipse_keyboard_btn.setIconSize(QtCore.QSize(100, 50))
		self.ellipse_keyboard_btn.setObjectName("ellipse_keyboard_btn")
		self.ellipse_keyboard = None
		self.ellipse_keyboard = self.keyboardf(self.bresnham_ellipse, self.ellipse_keyboard)
		self.bresnham_stacked.addWidget(self.bresnham_ellipse)
		self.bresnham_circle = QtWidgets.QWidget()
		self.bresnham_circle.setObjectName("bresnham_circle")
		self.groupBox_4 = QtWidgets.QGroupBox(self.bresnham_circle)
		self.groupBox_4.setGeometry(QtCore.QRect(212, 40, 251, 100))
		self.groupBox_4.setStyleSheet("background-color:#abff8d;\n"
"border-radius: 5px;")
		self.groupBox_4.setTitle("")
		self.groupBox_4.setObjectName("groupBox_4")
		self.circle_r = QtWidgets.QLineEdit(self.groupBox_4)
		self.circle_r.setGeometry(QtCore.QRect(110, 40, 101, 26))
		self.circle_r.setMinimumSize(QtCore.QSize(101, 26))
		self.circle_r.setMaximumSize(QtCore.QSize(101, 26))
		self.circle_r.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.circle_r.setObjectName("circle_r")
		self.label_41 = QtWidgets.QLabel(self.groupBox_4)
		self.label_41.setGeometry(QtCore.QRect(30, 20, 60, 60))
		self.label_41.setMinimumSize(QtCore.QSize(60, 59))
		self.label_41.setMaximumSize(QtCore.QSize(60, 60))
		font = QtGui.QFont()
		font.setFamily("Calibri")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.label_41.setFont(font)
		self.label_41.setObjectName("label_41")
		#circle plotting
		self.circle_graph_box = QtWidgets.QGroupBox(self.bresnham_circle)
		self.circle_graph_box.setGeometry(QtCore.QRect(60, 220, 691, 511))
		circle_graph = PlotCanvas(self.circle_graph_box, width=6.9, height=5.1, dpi=100)
		circle_toolbar = NavigationToolbar(circle_graph, self.circle_graph_box)
		circle_toolbar.move(80, 0)		
		self.circle_graph_box.setStyleSheet("border: none;\n")
		self.circle_ok = QtWidgets.QPushButton(self.bresnham_circle)
		self.circle_ok.clicked.connect(lambda: self.circle_graph_plot(circle_graph))
		self.circle_ok.setGeometry(QtCore.QRect(473, 43, 100, 40))
		font = QtGui.QFont()
		font.setFamily("Calibri")
		font.setPointSize(10)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.circle_ok.setFont(font)
		self.circle_ok.setStyleSheet("background-color: #abff8d;\n"
"border-radius: 5px;")
		self.circle_ok.setObjectName("circle_ok")
		self.circle_keyboard_btn = QtWidgets.QPushButton(self.bresnham_circle)
		self.circle_keyboard_btn.setGeometry(QtCore.QRect(473, 92, 100, 40))
		self.circle_keyboard_btn.setStyleSheet("background-color: #abff8d;\n"
"border-radius: 5px;")
		self.circle_keyboard_btn.setText("")
		self.circle_keyboard_btn.setIcon(icon)
		self.circle_keyboard_btn.setIconSize(QtCore.QSize(100, 50))
		self.circle_keyboard_btn.setObjectName("circle_keyboard_btn")
		self.circle_keyboard = None
		self.circle_keyboard = self.keyboardf(self.bresnham_circle, self.circle_keyboard)
		self.bresnham_stacked.addWidget(self.bresnham_circle)
		self.bresnham_line = QtWidgets.QWidget()
		self.bresnham_line.setObjectName("bresnham_line")
		#line plotting
		self.line_graph_box = QtWidgets.QGroupBox(self.bresnham_line)
		self.line_graph_box.setGeometry(QtCore.QRect(60, 220, 691, 511))
		line_graph = PlotCanvas(self.line_graph_box, width=6.9, height=5.1, dpi=100)
		line_toolbar = NavigationToolbar(line_graph, self.line_graph_box)
		line_toolbar.move(80, 0)		
		self.line_graph_box.setStyleSheet("border: none;\n")
		self.line_ok = QtWidgets.QPushButton(self.bresnham_line)
		self.line_ok.clicked.connect(lambda: self.line_graph_plot(line_graph))
		self.line_ok.setGeometry(QtCore.QRect(640, 48, 100, 40))
		font = QtGui.QFont()
		font.setFamily("Calibri")
		font.setPointSize(10)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.line_ok.setFont(font)
		self.line_ok.setStyleSheet("background-color: #abff8d;\n"
"border-radius: 5px;")
		self.line_ok.setObjectName("line_ok")
		self.line_keyboard_btn = QtWidgets.QPushButton(self.bresnham_line)
		self.line_keyboard_btn.setGeometry(QtCore.QRect(640, 92, 100, 40))
		self.line_keyboard_btn.setStyleSheet("background-color: #abff8d;\n"
"border-radius: 5px;")
		self.line_keyboard_btn.setText("")
		self.line_keyboard_btn.setIcon(icon)
		self.line_keyboard_btn.setIconSize(QtCore.QSize(100, 50))
		self.line_keyboard_btn.setObjectName("line_keyboard_btn")
		self.line_keyboard = None
		self.line_keyboard = self.keyboardf(self.bresnham_line, self.line_keyboard)
		self.groupBox_2 = QtWidgets.QGroupBox(self.bresnham_line)
		self.groupBox_2.setGeometry(QtCore.QRect(60, 40, 570, 100))
		self.groupBox_2.setStyleSheet("background-color:#abff8d;\n"
		"border-radius: 5px;")
		self.groupBox_2.setTitle("")
		self.groupBox_2.setObjectName("groupBox_2")
		self.label = QtWidgets.QLabel(self.groupBox_2)
		self.label.setGeometry(QtCore.QRect(4, 20, 21, 60))
		self.label.setMinimumSize(QtCore.QSize(21, 60))
		self.label.setMaximumSize(QtCore.QSize(21, 60))
		font = QtGui.QFont()
		font.setFamily("Calibri")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.line_p1_x = QLineEdit(self.groupBox_2)
		self.line_p1_x.setGeometry(QtCore.QRect(30, 37, 101, 26))
		self.line_p1_x.setMinimumSize(QtCore.QSize(101, 26))
		self.line_p1_x.setMaximumSize(QtCore.QSize(101, 26))
		self.line_p1_x.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.line_p1_x.setObjectName("line_p1_x")
		self.label_2 = QtWidgets.QLabel(self.groupBox_2)
		self.label_2.setGeometry(QtCore.QRect(138, 20, 21, 60))
		self.label_2.setMinimumSize(QtCore.QSize(21, 60))
		self.label_2.setMaximumSize(QtCore.QSize(21, 60))
		font = QtGui.QFont()
		font.setFamily("Calibri")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.label_2.setFont(font)
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(self.groupBox_2)
		self.label_3.setGeometry(QtCore.QRect(255, 20, 21, 60))
		self.label_3.setMinimumSize(QtCore.QSize(21, 60))
		self.label_3.setMaximumSize(QtCore.QSize(21, 60))
		font = QtGui.QFont()
		font.setFamily("Calibri")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.label_3.setFont(font)
		self.label_3.setObjectName("label_3")
		self.label_4 = QtWidgets.QLabel(self.groupBox_2)
		self.label_4.setGeometry(QtCore.QRect(281, 20, 21, 60))
		self.label_4.setMinimumSize(QtCore.QSize(21, 60))
		self.label_4.setMaximumSize(QtCore.QSize(21, 60))
		font = QtGui.QFont()
		font.setFamily("Calibri")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.label_4.setFont(font)
		self.label_4.setObjectName("label_4")
		self.line_p2_y = QtWidgets.QLineEdit(self.groupBox_2)
		self.line_p2_y.setGeometry(QtCore.QRect(440, 37, 101, 26))
		self.line_p2_y.setMinimumSize(QtCore.QSize(101, 26))
		self.line_p2_y.setMaximumSize(QtCore.QSize(101, 26))
		self.line_p2_y.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.line_p2_y.setObjectName("line_p2_y")
		self.line_p2_x = QtWidgets.QLineEdit(self.groupBox_2)
		self.line_p2_x.setGeometry(QtCore.QRect(305, 37, 101, 26))
		self.line_p2_x.setMinimumSize(QtCore.QSize(101, 26))
		self.line_p2_x.setMaximumSize(QtCore.QSize(101, 26))
		self.line_p2_x.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.line_p2_x.setObjectName("line_p2_x")
		self.label_6 = QtWidgets.QLabel(self.groupBox_2)
		self.label_6.setGeometry(QtCore.QRect(550, 20, 20, 60))
		self.label_6.setMinimumSize(QtCore.QSize(20, 60))
		self.label_6.setMaximumSize(QtCore.QSize(20, 60))
		font = QtGui.QFont()
		font.setFamily("Calibri")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.label_6.setFont(font)
		self.label_6.setObjectName("label_6")
		self.line_p1_y = QtWidgets.QLineEdit(self.groupBox_2)
		self.line_p1_y.setGeometry(QtCore.QRect(147, 37, 101, 26))
		self.line_p1_y.setMinimumSize(QtCore.QSize(101, 26))
		self.line_p1_y.setMaximumSize(QtCore.QSize(101, 26))
		self.line_p1_y.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.line_p1_y.setObjectName("line_p1_y")
		self.label_7 = QtWidgets.QLabel(self.groupBox_2)
		self.label_7.setGeometry(QtCore.QRect(415, 20, 20, 60))
		self.label_7.setMinimumSize(QtCore.QSize(20, 60))
		self.label_7.setMaximumSize(QtCore.QSize(20, 60))
		font = QtGui.QFont()
		font.setFamily("Calibri")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.label_7.setFont(font)
		self.label_7.setObjectName("label_7")
		self.bresnham_stacked.addWidget(self.bresnham_line)
		self.bresnham_menu = QtWidgets.QGroupBox(self.centralwidget)
		self.bresnham_menu.setGeometry(QtCore.QRect(0, 0, 200, 768))
		self.bresnham_menu.setMinimumSize(QtCore.QSize(200, 768))
		self.bresnham_menu.setMaximumSize(QtCore.QSize(200, 768))
		self.bresnham_menu.setStyleSheet("*{\n"
		"    background-color: #87ffcd;\n"
		"    margin: 0;\n"
		"    width: 100%;\n"
		"    height: 100%\n"
		"}\n"
		"QPushButton {\n"
		"    min-width: 100%;\n"
		"    margin: 0;\n"
		"    padding: 10px;\n"
		"    font: 75 16px \"MS Shell Dlg 2\";\n"
		"    height: auto;\n"
		"    outline: None; \n"
		"    border: None\n"
		"}\n"
		"QPushButton:pressed {\n"
		"    background-color: #5c49d6;\n"
		"    color: #fff\n"
		"}")
		self.bresnham_menu.setTitle("")
		self.bresnham_menu.setObjectName("bresnham_menu")
		self.select_line = QtWidgets.QPushButton(self.bresnham_menu)
		self.select_line.setGeometry(QtCore.QRect(0, 15, 200, 60))
		self.select_line.setMinimumSize(QtCore.QSize(120, 60))
		self.select_line.setMaximumSize(QtCore.QSize(200, 60))
		self.select_line.setStyleSheet("")
		self.select_line.setObjectName("select_line")
		self.select_circle = QtWidgets.QPushButton(self.bresnham_menu)
		self.select_circle.setGeometry(QtCore.QRect(0, 75, 200, 60))
		self.select_circle.setMinimumSize(QtCore.QSize(120, 60))
		self.select_circle.setMaximumSize(QtCore.QSize(200, 60))
		self.select_circle.setStyleSheet("")
		self.select_circle.setObjectName("select_circle")
		self.select_ellipse = QtWidgets.QPushButton(self.bresnham_menu)
		self.select_ellipse.setGeometry(QtCore.QRect(0, 135, 200, 60))
		self.select_ellipse.setMinimumSize(QtCore.QSize(120, 60))
		self.select_ellipse.setMaximumSize(QtCore.QSize(200, 60))
		self.select_ellipse.setStyleSheet("")
		self.select_ellipse.setObjectName("select_ellipse")
		self.select_quit = QtWidgets.QPushButton(self.bresnham_menu)
		self.select_quit.setGeometry(QtCore.QRect(0, 600, 200, 60))
		self.select_quit.setMinimumSize(QtCore.QSize(120, 60))
		self.select_quit.setMaximumSize(QtCore.QSize(200, 60))
		self.select_quit.setStyleSheet("")
		self.select_quit.setObjectName("select_quit")
		BresnhamMainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(BresnhamMainWindow)
		self.bresnham_stacked.setCurrentIndex(2)
		QtCore.QMetaObject.connectSlotsByName(BresnhamMainWindow)

	def retranslateUi(self, BresnhamMainWindow):
		_translate = QtCore.QCoreApplication.translate
		BresnhamMainWindow.setWindowTitle(_translate("BresnhamMainWindow", "Computer Graphics - Bresenham"))
		self.label_37.setText(_translate("BresnhamMainWindow", "C("))
		self.label_38.setText(_translate("BresnhamMainWindow", ","))
		self.label_39.setText(_translate("BresnhamMainWindow", ")"))
		self.label_40.setText(_translate("BresnhamMainWindow", "Rx = "))
		self.label_43.setText(_translate("BresnhamMainWindow", "Ry  ="))
		self.ellipse_ok.setText(_translate("BresnhamMainWindow", "OK"))
		self.label_41.setText(_translate("BresnhamMainWindow", "R    ="))
		self.circle_ok.setText(_translate("BresnhamMainWindow", "OK"))
		self.line_ok.setText(_translate("BresnhamMainWindow", "OK"))
		self.label.setText(_translate("BresnhamMainWindow", "P1("))
		self.label_2.setText(_translate("BresnhamMainWindow", ","))
		self.label_3.setText(_translate("BresnhamMainWindow", ")"))
		self.label_4.setText(_translate("BresnhamMainWindow", "P2("))
		self.label_6.setText(_translate("BresnhamMainWindow", ")"))
		self.label_7.setText(_translate("BresnhamMainWindow", ","))
		self.select_line.setText(_translate("BresnhamMainWindow", "Bresnham Line"))
		self.select_line.clicked.connect(self.line_page)
		self.select_circle.setText(_translate("BresnhamMainWindow", "Bresnham Circle"))
		self.select_circle.clicked.connect(self.circle_page)
		self.select_ellipse.setText(_translate("BresnhamMainWindow", "Bresnham Ellipse"))
		self.select_ellipse.clicked.connect(self.ellipse_page)
		self.select_quit.setText(_translate("BresnhamMainWindow", "Back"))
		self.select_quit.clicked.connect(BresnhamMainWindow.close)
		self.ellipse_keyboard_btn.clicked.connect(lambda: self.showorhide(self.ellipse_keyboard))
		self.line_keyboard_btn.clicked.connect(lambda: self.showorhide(self.line_keyboard))
		self.circle_keyboard_btn.clicked.connect(lambda: self.showorhide(self.circle_keyboard))

	def missing_data_dialog(self, text):
		msg = QMessageBox()
		msg.setIcon(QMessageBox.Warning)
		msg.setText(f"Entrer {text} d'abord!!")
		msg.setWindowTitle("Error!")
		msg.setStandardButtons(QMessageBox.Ok)
		msg.exec_()

	def wrong_expr_dialog(self, text):
		msg = QMessageBox()
		msg.setIcon(QMessageBox.Warning)
		msg.setText(f"Expression de {text} est fausse!!")
		msg.setWindowTitle("Error!")
		msg.setStandardButtons(QMessageBox.Ok)
		msg.exec_()

	def normalize_formula(self, formula, text):
		formula = formula.replace('^', '**')
		formula = formula.replace('π', 'pi')
		try:
			formula = eval(formula)
		except Exception:
			self.wrong_expr_dialog(text)
			return None
		return formula

	def line_graph_plot(self, line_graph):
		p1x, p1y, p2x, p2y = self.line_p1_x.text(), self.line_p1_y.text(), self.line_p2_x.text(), self.line_p2_y.text()
		if (len(p1x) == 0) or (len(p1y) == 0) or (len(p2x) == 0)  or (len(p2y) == 0) :
			self.missing_data_dialog('les Cordonnées')
			return
		p1x = self.normalize_formula(p1x, 'p1x')
		p1y = self.normalize_formula(p1y, 'p1y')
		p2x = self.normalize_formula(p2x, 'p2x')
		p2y = self.normalize_formula(p2y, 'p2y')
		if (p1x != None and p1y != None and p2x != None and p2y != None):
			self.line_keyboard.setMinimumSize(QtCore.QSize(680, 227))
			self.showorhide(self.line_keyboard)	
			line_data = droite_bresenham(p1x, p1y, p2x, p2y)
			line_graph.plot_line(line_data)

	def circle_graph_plot(self, circle_graph):
		r = self.circle_r.text()
		if len(r) == 0:
			self.missing_data_dialog('Rayon')
		r = self.normalize_formula(r, 'R')
		if r != None:
			self.circle_keyboard.setMinimumSize(QtCore.QSize(680, 227))
			self.showorhide(self.circle_keyboard)
			circle_data = circle(r)
			circle_graph.plot_circle(circle_data)

	def ellipse_graph_plot(self, ellipse_graph):
		cx, cy, rx, ry = self.ellipse_c_x.text(), self.ellipse_c_y.text(), self.ellipse_r_x.text(), self.ellipse_r_y.text()
		if (len(cx) == 0) or (len(cy) == 0) or (len(rx) == 0)  or (len(ry) == 0) :
			self.missing_data_dialog('les données')
			return
		cx = self.normalize_formula(cx, 'Cx')
		cy = self.normalize_formula(cy, 'Cy')
		rx = self.normalize_formula(rx, 'Rx')
		ry = self.normalize_formula(ry, 'Ry')
		if (cx != None and cy != None and rx != None and ry != None):
			self.ellipse_keyboard.setMinimumSize(QtCore.QSize(680, 227))
			self.showorhide(self.ellipse_keyboard)	
			ellipse_data = ellipse(cx, cy, rx, ry)
			ellipse_graph.plot_ellipse(ellipse_data)

	def line_page(self):
		self.bresnham_stacked.setCurrentIndex(2)
		self.new = True

	def circle_page(self):
		self.bresnham_stacked.setCurrentIndex(1)
		self.new = True

	def ellipse_page(self):
		self.bresnham_stacked.setCurrentIndex(0)
		self.new = True

	def setFocusOnLast(self):
		widget = QtWidgets.QApplication.instance().inputFocusWidget()
		if widget:
			return widget

	def toinput(self, text, name):
		widget_input = self.setFocusOnLast() if not self.new else None
		self.new = False
		if widget_input is None:
			widget_input = self.ellipse_c_x if (name == self.ellipse_keyboard) else self.line_p1_x if (name == self.line_keyboard) else self.circle_r
		widget_input.setFocus()
		self.input_value(text, widget_input)

	def showorhide(self, widget):
		if widget.height() == 0:
			widget.setGeometry(QtCore.QRect(67, 150, 680, 227))
			widget.setMinimumSize(QtCore.QSize(680, 227))
			widget.setMaximumSize(QtCore.QSize(680, 227))
		else:
			widget.setMinimumSize(QtCore.QSize(0, 0))
			widget.setMaximumSize(QtCore.QSize(0, 0))
			widget.setGeometry(QtCore.QRect(0, 0, 0, 0))

	def input_value(self, v, input):
		input.setText(input.text()[:input.cursorPosition()] + v + input.text()[input.cursorPosition():]) 

	def keyboardf(self, parent, name):
		self.btns = list()
		_translate = QtCore.QCoreApplication.translate
		name = QtWidgets.QGroupBox(parent)
		name.setGeometry(QtCore.QRect(0, 0, 0, 0))
		name.setStyleSheet("*{\n"
"    padding: 20px;\n"
"    background-color: #ccc;\n"
"}\n"
"QPushButton {\n"
"    padding: 0px;\n"
"    background-color: #fdfdfd;\n"
"    border: 1px solid #dcdcdc;\n"
"    border-radius: 8px;\n"
"    font: 20px \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(240, 240, 240);\n"
"}")
		name.setTitle("")
		name.setObjectName("keyboard")
		self.numbers = QtWidgets.QGroupBox(name)
		self.numbers.setGeometry(QtCore.QRect(250, 2, 412, 220))
		self.numbers.setMinimumSize(QtCore.QSize(412, 220))
		self.numbers.setMaximumSize(QtCore.QSize(412, 220))
		self.numbers.setStyleSheet("border: none;")
		self.numbers.setTitle("")
		self.numbers.setObjectName("numbers")
		self.btn_7 = QtWidgets.QPushButton(self.numbers)
		self.btn_7.setGeometry(QtCore.QRect(0, 5, 100, 50))
		self.btn_7.setMinimumSize(QtCore.QSize(100, 50))
		self.btn_7.setMaximumSize(QtCore.QSize(100, 50))
		self.btn_7.setObjectName("btn_7")
		self.btn_7.setText(_translate("BresnhamMainWindow", "7"))
		self.btn_7.clicked.connect(lambda: self.toinput('7', name))
		self.btn_8 = QtWidgets.QPushButton(self.numbers)
		self.btn_8.setGeometry(QtCore.QRect(104, 5, 100, 50))
		self.btn_8.setMinimumSize(QtCore.QSize(100, 50))
		self.btn_8.setMaximumSize(QtCore.QSize(100, 50))
		self.btn_8.setObjectName("btn_8")
		self.btn_8.setText(_translate("BresnhamMainWindow", "8"))
		self.btn_8.clicked.connect(lambda: self.toinput('8', name))
		self.btn_9 = QtWidgets.QPushButton(self.numbers)
		self.btn_9.setGeometry(QtCore.QRect(208, 5, 100, 50))
		self.btn_9.setMinimumSize(QtCore.QSize(100, 50))
		self.btn_9.setMaximumSize(QtCore.QSize(100, 50))
		self.btn_9.setObjectName("btn_9")
		self.btn_9.setText(_translate("BresnhamMainWindow", "9"))
		self.btn_9.clicked.connect(lambda: self.toinput('9', name))
		self.divide_btn = QtWidgets.QPushButton(self.numbers)
		self.divide_btn.setGeometry(QtCore.QRect(312, 5, 100, 50))
		self.divide_btn.setMinimumSize(QtCore.QSize(100, 50))
		self.divide_btn.setMaximumSize(QtCore.QSize(100, 50))
		self.divide_btn.setObjectName("divide_btn")
		self.divide_btn.setText(_translate("BresnhamMainWindow", "/"))
		self.divide_btn.clicked.connect(lambda: self.toinput('/', name))
		self.btn_5 = QtWidgets.QPushButton(self.numbers)
		self.btn_5.setGeometry(QtCore.QRect(104, 60, 100, 50))
		self.btn_5.setMinimumSize(QtCore.QSize(100, 50))
		self.btn_5.setMaximumSize(QtCore.QSize(100, 50))
		self.btn_5.setObjectName("btn_5")
		self.btn_5.setText(_translate("BresnhamMainWindow", "5"))
		self.btn_5.clicked.connect(lambda: self.toinput('5', name))
		self.btn_4 = QtWidgets.QPushButton(self.numbers)
		self.btn_4.setGeometry(QtCore.QRect(0, 60, 100, 50))
		self.btn_4.setMinimumSize(QtCore.QSize(100, 50))
		self.btn_4.setMaximumSize(QtCore.QSize(100, 50))
		self.btn_4.setObjectName("btn_4")
		self.btn_4.setText(_translate("BresnhamMainWindow", "4"))
		self.btn_4.clicked.connect(lambda: self.toinput('4', name))
		self.btn_6 = QtWidgets.QPushButton(self.numbers)
		self.btn_6.setGeometry(QtCore.QRect(208, 60, 100, 50))
		self.btn_6.setMinimumSize(QtCore.QSize(100, 50))
		self.btn_6.setMaximumSize(QtCore.QSize(100, 50))
		self.btn_6.setObjectName("btn_6")
		self.btn_6.setText(_translate("BresnhamMainWindow", "6"))
		self.btn_6.clicked.connect(lambda: self.toinput('6', name))
		self.multiply_btn = QtWidgets.QPushButton(self.numbers)
		self.multiply_btn.setGeometry(QtCore.QRect(312, 60, 100, 50))
		self.multiply_btn.setMinimumSize(QtCore.QSize(100, 50))
		self.multiply_btn.setMaximumSize(QtCore.QSize(100, 50))
		self.multiply_btn.setObjectName("multiply_btn")
		self.multiply_btn.setText(_translate("BresnhamMainWindow", "x"))
		self.multiply_btn.clicked.connect(lambda: self.toinput('*', name))
		self.btn_2 = QtWidgets.QPushButton(self.numbers)
		self.btn_2.setGeometry(QtCore.QRect(104, 115, 100, 50))
		self.btn_2.setMinimumSize(QtCore.QSize(100, 50))
		self.btn_2.setMaximumSize(QtCore.QSize(100, 50))
		self.btn_2.setObjectName("btn_2")
		self.btn_2.setText(_translate("BresnhamMainWindow", "2"))
		self.btn_2.clicked.connect(lambda: self.toinput('2', name))
		self.btn_1 = QtWidgets.QPushButton(self.numbers)
		self.btn_1.setGeometry(QtCore.QRect(0, 115, 100, 50))
		self.btn_1.setMinimumSize(QtCore.QSize(100, 50))
		self.btn_1.setMaximumSize(QtCore.QSize(100, 50))
		self.btn_1.setObjectName("btn_1")
		self.btn_1.setText(_translate("BresnhamMainWindow", "1"))
		self.btn_1.clicked.connect(lambda: self.toinput('1', name))
		self.btn_3 = QtWidgets.QPushButton(self.numbers)
		self.btn_3.setGeometry(QtCore.QRect(208, 115, 100, 50))
		self.btn_3.setMinimumSize(QtCore.QSize(100, 50))
		self.btn_3.setMaximumSize(QtCore.QSize(100, 50))
		self.btn_3.setObjectName("btn_3")
		self.btn_3.setText(_translate("BresnhamMainWindow", "3"))
		self.btn_3.clicked.connect(lambda: self.toinput('3', name))
		self.minus_btn = QtWidgets.QPushButton(self.numbers)
		self.minus_btn.setGeometry(QtCore.QRect(312, 115, 100, 50))
		self.minus_btn.setMinimumSize(QtCore.QSize(100, 50))
		self.minus_btn.setMaximumSize(QtCore.QSize(100, 50))
		self.minus_btn.setObjectName("minus_btn")
		self.minus_btn.setText(_translate("BresnhamMainWindow", "-"))
		self.minus_btn.clicked.connect(lambda: self.toinput('-', name))
		self.btn_0 = QtWidgets.QPushButton(self.numbers)
		self.btn_0.setGeometry(QtCore.QRect(0, 170, 204, 50))
		self.btn_0.setMinimumSize(QtCore.QSize(204, 50))
		self.btn_0.setMaximumSize(QtCore.QSize(204, 50))
		self.btn_0.setObjectName("btn_0")
		self.btn_0.setText(_translate("BresnhamMainWindow", "0"))
		self.btn_0.clicked.connect(lambda: self.toinput('0', name))
		self.comma_btn = QtWidgets.QPushButton(self.numbers)
		self.comma_btn.setGeometry(QtCore.QRect(208, 170, 100, 50))
		self.comma_btn.setMinimumSize(QtCore.QSize(100, 50))
		self.comma_btn.setMaximumSize(QtCore.QSize(100, 50))
		self.comma_btn.setObjectName("comma_btn")
		self.comma_btn.setText(_translate("BresnhamMainWindow", "."))
		self.comma_btn.clicked.connect(lambda: self.toinput('.', name))
		self.plus_btn = QtWidgets.QPushButton(self.numbers)
		self.plus_btn.setGeometry(QtCore.QRect(312, 170, 100, 50))
		self.plus_btn.setMinimumSize(QtCore.QSize(100, 50))
		self.plus_btn.setMaximumSize(QtCore.QSize(100, 50))
		self.plus_btn.setObjectName("plus_btn")
		self.plus_btn.setText(_translate("BresnhamMainWindow", "+"))
		self.plus_btn.clicked.connect(lambda: self.toinput('+', name))
		self.characters = QtWidgets.QGroupBox(name)
		self.characters.setGeometry(QtCore.QRect(10, 2, 212, 220))
		self.characters.setMinimumSize(QtCore.QSize(212, 220))
		self.characters.setMaximumSize(QtCore.QSize(212, 220))
		self.characters.setStyleSheet("border: none;")
		self.characters.setTitle("")
		self.characters.setObjectName("characters")
		self.pi_btn = QtWidgets.QPushButton(self.characters)
		self.pi_btn.setGeometry(QtCore.QRect(0, 5, 104, 50))
		self.pi_btn.setMinimumSize(QtCore.QSize(104, 50))
		self.pi_btn.setMaximumSize(QtCore.QSize(104, 50))
		self.pi_btn.setObjectName("pi_btn")
		self.pi_btn.setText(_translate("BresnhamMainWindow", "π"))
		self.pi_btn.clicked.connect(lambda: self.toinput('π', name))
		self.square_btn = QtWidgets.QPushButton(self.characters)
		self.square_btn.setGeometry(QtCore.QRect(108, 5, 104, 50))
		self.square_btn.setMinimumSize(QtCore.QSize(104, 50))
		self.square_btn.setMaximumSize(QtCore.QSize(104, 50))
		self.square_btn.setObjectName("square_btn")
		self.square_btn.setText(_translate("BresnhamMainWindow", "a²"))
		self.square_btn.clicked.connect(lambda: self.toinput('^2', name))
		self.sqrt_btn = QtWidgets.QPushButton(self.characters)
		self.sqrt_btn.setGeometry(QtCore.QRect(0, 60, 104, 50))
		self.sqrt_btn.setMinimumSize(QtCore.QSize(104, 50))
		self.sqrt_btn.setMaximumSize(QtCore.QSize(104, 50))
		self.sqrt_btn.setObjectName("sqrt_btn")
		self.sqrt_btn.setText(_translate("BresnhamMainWindow", "√"))
		self.sqrt_btn.clicked.connect(lambda: self.toinput('sqrt(', name))
		self.power_btn = QtWidgets.QPushButton(self.characters)
		self.power_btn.setGeometry(QtCore.QRect(108, 60, 104, 50))
		self.power_btn.setMinimumSize(QtCore.QSize(104, 50))
		self.power_btn.setMaximumSize(QtCore.QSize(104, 50))
		self.power_btn.setObjectName("power_btn")
		self.power_btn.setText(_translate("BresnhamMainWindow", "aⁿ"))
		self.power_btn.clicked.connect(lambda: self.toinput('^', name))
		self.left_btn = QtWidgets.QPushButton(self.characters)
		self.left_btn.setGeometry(QtCore.QRect(0, 115, 104, 50))
		self.left_btn.setMinimumSize(QtCore.QSize(104, 50))
		self.left_btn.setMaximumSize(QtCore.QSize(104, 50))
		self.left_btn.setObjectName("left_btn")
		self.left_btn.setText(_translate("BresnhamMainWindow", "("))
		self.left_btn.clicked.connect(lambda: self.toinput('(', name))
		self.right_btn = QtWidgets.QPushButton(self.characters)
		self.right_btn.setGeometry(QtCore.QRect(108, 115, 104, 50))
		self.right_btn.setMinimumSize(QtCore.QSize(104, 50))
		self.right_btn.setMaximumSize(QtCore.QSize(104, 50))
		self.right_btn.setObjectName("right_btn")
		self.right_btn.clicked.connect(lambda: self.toinput(')', name))
		self.right_btn.setText(_translate("BresnhamMainWindow", ")"))
		self.exp_btn = QtWidgets.QPushButton(self.characters)
		self.exp_btn.setGeometry(QtCore.QRect(0, 170, 104, 50))
		self.exp_btn.setMinimumSize(QtCore.QSize(104, 50))
		self.exp_btn.setMaximumSize(QtCore.QSize(104, 50))
		self.exp_btn.setObjectName("exp_btn")
		self.exp_btn.setText(_translate("BresnhamMainWindow", "eⁿ"))
		self.exp_btn.clicked.connect(lambda: self.toinput('exp(', name))
		self.pof10_btn = QtWidgets.QPushButton(self.characters)
		self.pof10_btn.setGeometry(QtCore.QRect(108, 170, 104, 50))
		self.pof10_btn.setMinimumSize(QtCore.QSize(104, 50))
		self.pof10_btn.setMaximumSize(QtCore.QSize(104, 50))
		self.pof10_btn.setObjectName("pof10_btn")
		self.pof10_btn.setText(_translate("BresnhamMainWindow", "10ⁿ"))
		self.pof10_btn.clicked.connect(lambda: self.toinput('10^', name))
		return name

import resources


if __name__ == "__main__":
	import sys
	app = MyApplication(sys.argv)
	BresnhamMainWindow = QtWidgets.QMainWindow()
	ui = Ui_BresnhamMainWindow()
	ui.setupUi(BresnhamMainWindow)
	BresnhamMainWindow.show()
	sys.exit(app.exec_())

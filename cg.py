#coding: utf-8


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1024, 768)
		MainWindow.setMinimumSize(QtCore.QSize(1024, 768))
		MainWindow.setMaximumSize(QtCore.QSize(1024, 768))
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("cg.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
		MainWindow.setWindowIcon(icon)
		MainWindow.setStyleSheet("*{background-color:rgb(253,253,253);\n"
		"color: #000}\n"
		"QPushButton{\nborder: 3px solid black;\nborder-radius:5px}")
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(430, 90, 411, 151))
		self.label.setStyleSheet("margin: 0 auto;\n"
"font: 75 italic 24pt \"MS Sans Serif\";")
		self.label.setObjectName("label")
		self.frame = QtWidgets.QFrame(self.centralwidget)
		self.frame.setGeometry(QtCore.QRect(260, 70, 211, 191))
		self.frame.setStyleSheet("background:url(:/newPrefix/cg.jpg)")
		self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame.setObjectName("frame")
		self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(260, 330, 511, 361))
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
		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Computer Graphics"))
		self.label.setText(_translate("MainWindow", "Computer Graphics"))
		self.bresnham_btn.setText(_translate("MainWindow", "Traçage des objets"))
		self.fenetrage_btn.setText(_translate("MainWindow", "Fenêtrage"))
		self.remplissage_btn.setText(_translate("MainWindow", "Remplissage"))
		self.courbes_btn.setText(_translate("MainWindow", "Courbes"))
import resources


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())

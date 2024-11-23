from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *
import smtplib
import pyttsx3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1253, 1000)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/click.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QTabWidget::pane {\n"
"    background: white;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:top {\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:bottom {\n"
"    bottom: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:left {\n"
"    right: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:right {\n"
"    left: 1px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    width:85px;\n"
"    border-radius:2px;\n"
"    margin-left:4px;\n"
"    height:20px\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: rgb(134, 134, 134);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background: silver;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    background: #999;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected {\n"
"    margin-top: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected {\n"
"    margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8ex;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    border-bottom-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"    border-top-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected {\n"
"    margin-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected {\n"
"    margin-left: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right {\n"
"    min-height: 8ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"    border-left-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"    border-right-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {\n"
"    margin-bottom: 0;\n"
"}\n"
"QMainWindow{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"/* VERTICAL SCROLLBAR */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: rgb(80, 80, 122);\n"
"    min-height: 30px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:vertical:pressed {    \n"
"    background-color: rgb(39, 17, 109);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(59, 59, 90);\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {    \n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {    \n"
"    background-color: rgb(54, 213, 213);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(59, 59, 90);\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {    \n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {    \n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.Home_page = QtWidgets.QWidget()
        self.Home_page.setObjectName("Home_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Home_page)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.Home_page)
        self.frame.setStyleSheet("background-color: rgb(184, 184, 184);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.verticalLayout_3.addWidget(self.frame_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.verticalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignTop)
        self.frame_2 = QtWidgets.QFrame(self.Home_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("border:none;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setStyleSheet("Background-color:rgb(38, 88, 206)")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Home_btn_menu_frame = QtWidgets.QFrame(self.frame_4)
        self.Home_btn_menu_frame.setStyleSheet("Background-color:rgb(38, 88, 206)")
        self.Home_btn_menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Home_btn_menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Home_btn_menu_frame.setObjectName("Home_btn_menu_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Home_btn_menu_frame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Home_Home_btn = QtWidgets.QPushButton(self.Home_btn_menu_frame)
        self.Home_Home_btn.setMinimumSize(QtCore.QSize(0, 200))
        self.Home_Home_btn.setStyleSheet("QPushButton{\n"
"font: 75 48pt \"MS Shell Dlg 2\";\n"
"color: white;\n"
"border-radius:3px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(35, 130, 255);\n"
"}\n"
"QPushButton:Pressed{\n"
"border:3px solid white;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Home_Home_btn.setIcon(icon1)
        self.Home_Home_btn.setIconSize(QtCore.QSize(50, 50))
        self.Home_Home_btn.setObjectName("Home_Home_btn")
        self.verticalLayout_5.addWidget(self.Home_Home_btn)
        self.Home_Feedback_btn = QtWidgets.QPushButton(self.Home_btn_menu_frame)
        self.Home_Feedback_btn.setMinimumSize(QtCore.QSize(0, 200))
        self.Home_Feedback_btn.setStyleSheet("QPushButton{\n"
"font: 75 48pt \"MS Shell Dlg 2\";\n"
"color: white;\n"
"border-radius:3px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(35, 130, 255);\n"
"}\n"
"QPushButton:Pressed{\n"
"border:3px solid white;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/feedback.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Home_Feedback_btn.setIcon(icon2)
        self.Home_Feedback_btn.setIconSize(QtCore.QSize(50, 50))
        self.Home_Feedback_btn.setObjectName("Home_Feedback_btn")
        self.verticalLayout_5.addWidget(self.Home_Feedback_btn)
        self.frame_7 = QtWidgets.QFrame(self.Home_btn_menu_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setStyleSheet("height:20px;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_5.addWidget(self.frame_7)
        self.horizontalLayout_2.addWidget(self.Home_btn_menu_frame)
        self.horizontalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setStyleSheet("background-color: rgb(112, 112, 112);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Home_welcomToMGBPoint_btn = QtWidgets.QPushButton(self.frame_5)
        self.Home_welcomToMGBPoint_btn.setMinimumSize(QtCore.QSize(0, 200))
        self.Home_welcomToMGBPoint_btn.setStyleSheet("QPushButton{\n"
"font: 36pt \"MS Shell Dlg 2\";\n"
"border-radius:2px;\n"
"height:100px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(185, 185, 185);\n"
"}\n"
"QPushButton:Pressed{\n"
"background-color: rgb(182, 182, 182);\n"
"border:2px slod white;\n"
"}\n"
"")
        self.Home_welcomToMGBPoint_btn.setObjectName("Home_welcomToMGBPoint_btn")
        self.verticalLayout_6.addWidget(self.Home_welcomToMGBPoint_btn)
        self.Home_Blank_page_btn = QtWidgets.QPushButton(self.frame_5)
        self.Home_Blank_page_btn.setMinimumSize(QtCore.QSize(0, 200))
        self.Home_Blank_page_btn.setStyleSheet("QPushButton{\n"
"font: 36pt \"MS Shell Dlg 2\";\n"
"border-radius:2px;\n"
"height:100px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(185, 185, 185);\n"
"}\n"
"QPushButton:Pressed{\n"
"background-color: rgb(182, 182, 182);\n"
"border:2px slod white;\n"
"}\n"
"")
        self.Home_Blank_page_btn.setObjectName("Home_Blank_page_btn")
        self.verticalLayout_6.addWidget(self.Home_Blank_page_btn)
        self.Home_OpenExisting_btn = QtWidgets.QPushButton(self.frame_5)
        self.Home_OpenExisting_btn.setMinimumSize(QtCore.QSize(0, 200))
        self.Home_OpenExisting_btn.setStyleSheet("QPushButton{\n"
"font: 36pt \"MS Shell Dlg 2\";\n"
"border-radius:2px;\n"
"height:100px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(185, 185, 185);\n"
"}\n"
"QPushButton:Pressed{\n"
"background-color: rgb(182, 182, 182);\n"
"border:2px slod white;\n"
"}\n"
"")
        self.Home_OpenExisting_btn.setObjectName("Home_OpenExisting_btn")
        self.verticalLayout_6.addWidget(self.Home_OpenExisting_btn)
        self.horizontalLayout.addWidget(self.frame_5)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.stackedWidget.addWidget(self.Home_page)
        self.Main_point_page = QtWidgets.QWidget()
        self.Main_point_page.setObjectName("Main_point_page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Main_point_page)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_6 = QtWidgets.QFrame(self.Main_point_page)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_6.setStyleSheet("background-color: rgb(59, 92, 162);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tabWidget = QtWidgets.QTabWidget(self.frame_6)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 150))
        self.tabWidget.setObjectName("tabWidget")
        self.File_tab = QtWidgets.QWidget()
        self.File_tab.setObjectName("File_tab")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.File_tab)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.File_tab)
        self.pushButton.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"font: 36pt \"MS Shell Dlg 2\";\n"
"width:50px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:Pressed{\n"
"border:2px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(171, 171, 171);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.File_tab)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"font: 36pt \"MS Shell Dlg 2\";\n"
"width:50px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:Pressed{\n"
"border:2px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(171, 171, 171);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.pushButton_7 = QtWidgets.QPushButton(self.File_tab)
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"font: 36pt \"MS Shell Dlg 2\";\n"
"width:50px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:Pressed{\n"
"border:2px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(171, 171, 171);\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_4.addWidget(self.pushButton_7)
        self.pushButton_3 = QtWidgets.QPushButton(self.File_tab)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"font: 30pt \"MS Shell Dlg 2\";\n"
"width:50px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:Pressed{\n"
"border:2px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(171, 171, 171);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.File_tab)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"font: 36pt \"MS Shell Dlg 2\";\n"
"width:50px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:Pressed{\n"
"border:2px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(171, 171, 171);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.tabWidget.addTab(self.File_tab, "")
        self.Edit_tab = QtWidgets.QWidget()
        self.Edit_tab.setObjectName("Edit_tab")
        self.frame_10 = QtWidgets.QFrame(self.Edit_tab)
        self.frame_10.setGeometry(QtCore.QRect(0, 0, 220, 114))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.Edit_paste_btn = QtWidgets.QPushButton(self.frame_10)
        self.Edit_paste_btn.setMinimumSize(QtCore.QSize(200, 0))
        self.Edit_paste_btn.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"font: 36pt \"MS Shell Dlg 2\";\n"
"width:50px;\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton:Pressed{\n"
"border:2px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(171, 171, 171);\n"
"}")
        self.Edit_paste_btn.setObjectName("Edit_paste_btn")
        self.verticalLayout_11.addWidget(self.Edit_paste_btn)
        self.Edit_font_frame = QtWidgets.QFrame(self.Edit_tab)
        self.Edit_font_frame.setGeometry(QtCore.QRect(240, 10, 231, 101))
        self.Edit_font_frame.setStyleSheet("border:3px solid black;\n"
"border-radius:10px;")
        self.Edit_font_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Edit_font_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Edit_font_frame.setObjectName("Edit_font_frame")
        self.Edit_font_btn = QtWidgets.QPushButton(self.Edit_font_frame)
        self.Edit_font_btn.setGeometry(QtCore.QRect(15, 20, 201, 61))
        self.Edit_font_btn.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"font: 36pt \"MS Shell Dlg 2\";\n"
"width:50px;\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton:Pressed{\n"
"border:2px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(171, 171, 171);\n"
"}")
        self.Edit_font_btn.setObjectName("Edit_font_btn")
        self.Edit_Edit_frame = QtWidgets.QFrame(self.Edit_tab)
        self.Edit_Edit_frame.setGeometry(QtCore.QRect(510, 10, 500, 101))
        self.Edit_Edit_frame.setStyleSheet("border:3px solid black;\n"
"border-radius:10px;")
        self.Edit_Edit_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Edit_Edit_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Edit_Edit_frame.setObjectName("Edit_Edit_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Edit_Edit_frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Edit_color_btn = QtWidgets.QPushButton(self.Edit_Edit_frame)
        self.Edit_color_btn.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"font: 36pt \"MS Shell Dlg 2\";\n"
"width:50px;\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton:Pressed{\n"
"border:2px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(171, 171, 171);\n"
"}")
        self.Edit_color_btn.setObjectName("Edit_color_btn")
        self.horizontalLayout_5.addWidget(self.Edit_color_btn)
        self.Edit_copy_btn = QtWidgets.QPushButton(self.Edit_Edit_frame)
        self.Edit_copy_btn.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"font: 36pt \"MS Shell Dlg 2\";\n"
"width:50px;\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton:Pressed{\n"
"border:2px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(171, 171, 171);\n"
"}")
        self.Edit_copy_btn.setObjectName("Edit_copy_btn")
        self.horizontalLayout_5.addWidget(self.Edit_copy_btn)
        self.Edit_cut_btn = QtWidgets.QPushButton(self.Edit_Edit_frame)
        self.Edit_cut_btn.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"font: 36pt \"MS Shell Dlg 2\";\n"
"width:50px;\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton:Pressed{\n"
"border:2px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(171, 171, 171);\n"
"}")
        self.Edit_cut_btn.setObjectName("Edit_cut_btn")
        self.horizontalLayout_5.addWidget(self.Edit_cut_btn)
        self.Edit_clear_btn = QtWidgets.QPushButton(self.Edit_Edit_frame)
        self.Edit_clear_btn.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"font: 36pt \"MS Shell Dlg 2\";\n"
"width:50px;\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton:Pressed{\n"
"border:2px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(171, 171, 171);\n"
"}")
        self.Edit_clear_btn.setObjectName("Edit_clear_btn")
        self.horizontalLayout_5.addWidget(self.Edit_clear_btn)
        self.tabWidget.addTab(self.Edit_tab, "")
        self.Remind_tab = QtWidgets.QWidget()
        self.Remind_tab.setObjectName("Remind_tab")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.Remind_tab)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Remind_label = QtWidgets.QLabel(self.Remind_tab)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Remind_label.setFont(font)
        self.Remind_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.Remind_label.setObjectName("Remind_label")
        self.horizontalLayout_6.addWidget(self.Remind_label)
        self.Remind_lineEdit = QtWidgets.QLineEdit(self.Remind_tab)
        self.Remind_lineEdit.setStyleSheet("border-radius:5px;\n"
"font: 36pt \"MS Shell Dlg 2\";\n"
"border:2px solid blue;")
        self.Remind_lineEdit.setObjectName("Remind_lineEdit")
        self.horizontalLayout_6.addWidget(self.Remind_lineEdit)
        self.tabWidget.addTab(self.Remind_tab, "")
        self.Chngae_background_color_tab = QtWidgets.QWidget()
        self.Chngae_background_color_tab.setObjectName("Chngae_background_color_tab")
        self.Change_bacground_color_btn = QtWidgets.QPushButton(self.Chngae_background_color_tab)
        self.Change_bacground_color_btn.setGeometry(QtCore.QRect(370, 30, 551, 61))
        self.Change_bacground_color_btn.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"font: 36pt \"MS Shell Dlg 2\";\n"
"width:50px;\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton:Pressed{\n"
"border:2px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(171, 171, 171);\n"
"}")
        self.Change_bacground_color_btn.setObjectName("Change_bacground_color_btn")
        self.tabWidget.addTab(self.Chngae_background_color_tab, "")
        self.Time_tab = QtWidgets.QWidget()
        self.Time_tab.setObjectName("Time_tab")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.Time_tab)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_11 = QtWidgets.QFrame(self.Time_tab)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_12 = QtWidgets.QFrame(self.frame_11)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.Time_show_time_btn = QtWidgets.QPushButton(self.frame_12)
        self.Time_show_time_btn.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"font: 36pt \"MS Shell Dlg 2\";\n"
"width:50px;\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton:Pressed{\n"
"border:2px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(171, 171, 171);\n"
"}")
        self.Time_show_time_btn.setObjectName("Time_show_time_btn")
        self.verticalLayout_13.addWidget(self.Time_show_time_btn)
        self.horizontalLayout_7.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.frame_11)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.Time_Time_label = QtWidgets.QLabel(self.frame_13)
        self.Time_Time_label.setStyleSheet("font: 48pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.Time_Time_label.setObjectName("Time_Time_label")
        self.horizontalLayout_8.addWidget(self.Time_Time_label)
        self.Time_Display_label = QtWidgets.QLabel(self.frame_13)
        self.Time_Display_label.setStyleSheet("font: 48pt \"MS Shell Dlg 2\";")
        self.Time_Display_label.setText("")
        self.Time_Display_label.setObjectName("Time_Display_label")
        self.horizontalLayout_8.addWidget(self.Time_Display_label)
        self.horizontalLayout_7.addWidget(self.frame_13)
        self.verticalLayout_12.addWidget(self.frame_11)
        self.tabWidget.addTab(self.Time_tab, "")
        self.Pronounce_tab = QtWidgets.QWidget()
        self.Pronounce_tab.setObjectName("Pronounce_tab")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.Pronounce_tab)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.frame_19 = QtWidgets.QFrame(self.Pronounce_tab)
        self.frame_19.setMinimumSize(QtCore.QSize(500, 0))
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_19)
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"font: 36pt \"MS Shell Dlg 2\";\n"
"width:50px;\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton:Pressed{\n"
"border:2px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(171, 171, 171);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_19.addWidget(self.pushButton_6)
        self.verticalLayout_18.addWidget(self.frame_19, 0, QtCore.Qt.AlignHCenter)
        self.tabWidget.addTab(self.Pronounce_tab, "")
        self.verticalLayout_8.addWidget(self.tabWidget)
        self.verticalLayout_7.addWidget(self.frame_6, 0, QtCore.Qt.AlignTop)
        self.frame_8 = QtWidgets.QFrame(self.Main_point_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_9)
        self.scrollArea.setMinimumSize(QtCore.QSize(1200, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1198, 800))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:5px;\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_3.addWidget(self.textEdit)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_10.addWidget(self.scrollArea)
        self.verticalLayout_9.addWidget(self.frame_9, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_7.addWidget(self.frame_8)
        self.stackedWidget.addWidget(self.Main_point_page)
        self.Feedback_page = QtWidgets.QWidget()
        self.Feedback_page.setObjectName("Feedback_page")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.Feedback_page)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_14 = QtWidgets.QFrame(self.Feedback_page)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_16 = QtWidgets.QFrame(self.frame_14)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_2 = QtWidgets.QLabel(self.frame_16)
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_15.addWidget(self.label_2)
        self.horizontalLayout_9.addWidget(self.frame_16, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_14.addWidget(self.frame_14, 0, QtCore.Qt.AlignTop)
        self.frame_15 = QtWidgets.QFrame(self.Feedback_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame_17 = QtWidgets.QFrame(self.frame_15)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_3 = QtWidgets.QLabel(self.frame_17)
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_10.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_17)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit.setStyleSheet("font: 36pt \"MS Shell Dlg 2\";\n"
"border:4px solid rgb(29, 138, 255);\n"
"border-radius:5px;")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_10.addWidget(self.lineEdit)
        self.verticalLayout_16.addWidget(self.frame_17)
        self.frame_18 = QtWidgets.QFrame(self.frame_15)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_18)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"border:3px solid rgb(51, 133, 255);\n"
"font: 36pt \"MS Shell Dlg 2\";\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"border:3px solid rgb(25, 101, 199)\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_17.addWidget(self.pushButton_5)
        self.Feedback_send_btn = QtWidgets.QPushButton(self.frame_18)
        self.Feedback_send_btn.setStyleSheet("QPushButton{\n"
"border:3px solid rgb(51, 133, 255);\n"
"font: 36pt \"MS Shell Dlg 2\";\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"border:3px solid rgb(25, 101, 199)\n"
"}")
        self.Feedback_send_btn.setObjectName("Feedback_send_btn")
        self.verticalLayout_17.addWidget(self.Feedback_send_btn)
        self.label_4 = QtWidgets.QLabel(self.frame_18)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_17.addWidget(self.label_4)
        self.Feedback_message_lineedit = QtWidgets.QLineEdit(self.frame_18)
        self.Feedback_message_lineedit.setMinimumSize(QtCore.QSize(0, 300))
        self.Feedback_message_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 36pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"border-radius:5px;")
        self.Feedback_message_lineedit.setObjectName("Feedback_message_lineedit")
        self.verticalLayout_17.addWidget(self.Feedback_message_lineedit)
        self.verticalLayout_16.addWidget(self.frame_18)
        self.verticalLayout_14.addWidget(self.frame_15)
        self.stackedWidget.addWidget(self.Feedback_page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.frame_20 = QtWidgets.QFrame(self.page_3)
        self.frame_20.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"border:none;")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_20)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_5 = QtWidgets.QLabel(self.frame_20)
        self.label_5.setStyleSheet("font: 75 26pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_21.addWidget(self.label_5)
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame_20)
        self.textEdit_2.setStyleSheet("font: 75 26pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(46, 185, 255);\n"
"border-radius:5px;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_21.addWidget(self.textEdit_2)
        self.verticalLayout_20.addWidget(self.frame_20)
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


#########################################################################################
################################Connections##############################################
#########################################################################################


        self.pushButton_3.clicked.connect(self.open_new)
        self.Edit_clear_btn.clicked.connect(self.clearall)
        self.Edit_color_btn.clicked.connect(self.change_color)
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Home_page))
        self.pushButton_2.clicked.connect(self.save_pdf)
        self.pushButton_4.clicked.connect(self.printpreview)
        self.Home_Blank_page_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Main_point_page))
        self.Home_welcomToMGBPoint_btn.clicked.connect(self.welcome)
        self.Edit_font_btn.clicked.connect(self.fontfor)
        self.Edit_copy_btn.clicked.connect(self.textEdit.copy)
        self.Edit_cut_btn.clicked.connect(self.textEdit.cut)
        self.Edit_paste_btn.clicked.connect(self.textEdit.paste)
        self.Time_show_time_btn.clicked.connect(self.time)
        self.Change_bacground_color_btn.clicked.connect(self.change_color_back2)
        self.Home_welcomToMGBPoint_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Main_point_page))
        self.Home_Feedback_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Feedback_page))
        self.pushButton_5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Main_point_page))
        self.Home_Blank_page_btn.clicked.connect(self.clearall)
        self.Home_OpenExisting_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Main_point_page))
        self.Feedback_send_btn.clicked.connect(self.email)
        self.pushButton_6.clicked.connect(self.pronounce)
        self.pushButton_7.clicked.connect(self.openFile)


#########################################################################################
#################################Connections End#########################################
#########################################################################################



#########################################################################################
###################################Functions#############################################
#########################################################################################



    def pronounce(self):
            friend =pyttsx3.init()
            friend.say(self.textEdit.toPlainText())
            friend.runAndWait()

    def email(self):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('', '')
            server.sendmail("", '',self.lineEdit.text()+'\n'+ self.Feedback_message_lineedit.text())

    def change_color_back2(self):
            color2= QColorDialog.getColor()
            self.textEdit.setTextBackgroundColor(color2)


    def open_new(self):
            self.window=QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()


    def clearall(self):
            self.textEdit.clear()


    def welcome(self):
            self.textEdit.setFontPointSize(65)
            self.textEdit.setText("Welcome to the MGB Point ")
        
    def fontfor(self):
            font2, ok2=QFontDialog.getFont()
            if ok2:
                    self.textEdit.setFont(font2)


    def change_color(self):
            color= QColorDialog.getColor()
            self.textEdit.setTextColor(color)


    def remnind_font(self):
            font, ok=QFontDialog.getFont()
            if ok:
                    self.Remind_remind_linedit_4.setFont(font)


    def back_color(self):
            color= QColorDialog.getColor()
            self.Word_main.setTextBackgroundColor(color)


    def time(self):
            while True:
                QtWidgets.QApplication.processEvents()
                dt= datetime.datetime.now()
                self.Time_Display_label.setText('%s:%s:%s' % (dt.hour, dt.minute, dt.second))


    def printpreview(self):
            printer = QPrinter(QPrinter.HighResolution)
            previewDialog = QPrintPreviewDialog(printer)
            previewDialog.paintRequested.connect(self.Print_preview2)
            previewDialog.exec_()

    def Print_preview2(self,printer):
            self.textEdit.print_(printer)


    def save_pdf(self):
        f_name, _ = QFileDialog.getSaveFileName()
        File = open(f_name+".mgt","w")
        File.write(self.textEdit.toPlainText())
        File.close()

    def openFile(self):
        OpenFile, _ = QFileDialog.getOpenFileNames()
        File_Read = open("OpenFile","r")
        self.textEdit.setText(File_Read.read())
        File_Read.close()

########################################################################################
#####################################Functions End######################################
########################################################################################


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MGB Point"))
        self.label.setText(_translate("MainWindow", "Welcome"))
        self.Home_Home_btn.setText(_translate("MainWindow", "Home"))
        self.Home_Feedback_btn.setText(_translate("MainWindow", "Feedback"))
        self.Home_welcomToMGBPoint_btn.setText(_translate("MainWindow", "Welcome to MGB Point"))
        self.Home_Blank_page_btn.setText(_translate("MainWindow", "Blank page"))
        self.Home_OpenExisting_btn.setText(_translate("MainWindow", "Open Existing"))
        self.pushButton.setText(_translate("MainWindow", "Home"))
        self.pushButton_2.setText(_translate("MainWindow", "Save as"))
        self.pushButton_7.setText(_translate("MainWindow", "Open"))
        self.pushButton_3.setText(_translate("MainWindow", "New window"))
        self.pushButton_4.setText(_translate("MainWindow", "Print"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.File_tab), _translate("MainWindow", "File"))
        self.Edit_paste_btn.setText(_translate("MainWindow", "Paste"))
        self.Edit_font_btn.setText(_translate("MainWindow", "Font"))
        self.Edit_color_btn.setText(_translate("MainWindow", "Color"))
        self.Edit_copy_btn.setText(_translate("MainWindow", "Copy"))
        self.Edit_cut_btn.setText(_translate("MainWindow", "Cut"))
        self.Edit_clear_btn.setText(_translate("MainWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Edit_tab), _translate("MainWindow", "Edit"))
        self.Remind_label.setText(_translate("MainWindow", "Remind:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Remind_tab), _translate("MainWindow", "Reminder"))
        self.Change_bacground_color_btn.setText(_translate("MainWindow", "Change Background color"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Chngae_background_color_tab), _translate("MainWindow", "Background"))
        self.Time_show_time_btn.setText(_translate("MainWindow", "Show Time"))
        self.Time_Time_label.setText(_translate("MainWindow", "    Time:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Time_tab), _translate("MainWindow", "Time"))
        self.pushButton_6.setText(_translate("MainWindow", "Pronounce all the text"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Pronounce_tab), _translate("MainWindow", "Speech"))
        self.label_2.setText(_translate("MainWindow", "Give FeedBack"))
        self.label_3.setText(_translate("MainWindow", "Name:"))
        self.pushButton_5.setText(_translate("MainWindow", "Go to the main page"))
        self.Feedback_send_btn.setText(_translate("MainWindow", "Send"))
        self.label_4.setText(_translate("MainWindow", "Feedback massage:"))
        self.label_5.setText(_translate("MainWindow", "Type the File name:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

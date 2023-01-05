
# from PyQt5 import QtWidgets, QtGui, QtCore

# class MainWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()

#         # Create QTabWidget and add some tabs
#         self.tab_widget = QtWidgets.QTabWidget()
#         self.tab_widget.addTab(QtWidgets.QLabel("Tab 1"), "Tab 1")
#         self.tab_widget.addTab(QtWidgets.QLabel("Tab 2"), "Tab 2")
#         self.tab_widget.addTab(QtWidgets.QLabel("Tab 3"), "Tab 3")

#         # Create right-click menu for QTabWidget
#         self.tab_menu = QtWidgets.QMenu()
#         self.tab_menu.addAction("Close Tab", self.close_tab)
#         self.tab_menu.addAction("Close Other Tabs", self.close_other_tabs)
#         self.tab_widget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
#         self.tab_widget.customContextMenuRequested.connect(self.show_tab_menu)

#         # Set QTabWidget as central widget
#         self.setCentralWidget(self.tab_widget)

#     def show_tab_menu(self, pos):
#         self.tab_menu.exec_(self.tab_widget.mapToGlobal(pos))

#     def close_tab(self):
#         current_index = self.tab_widget.currentIndex()
#         self.tab_widget.removeTab(current_index)

#     def close_other_tabs(self):
#         current_index = self.tab_widget.currentIndex()
#         for i in range(self.tab_widget.count()):
#             if i != current_index:
#                 self.tab_widget.removeTab(i)

# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])
#     window = MainWindow()
#     window.show()
#     app.exec_()
# exit()
# import sys
# from PyQt5.QtWidgets import QApplication, QTabWidget, QShortcut, QMainWindow, QLabel
# from PyQt5.QtGui import QKeySequence

# # create the main window
# app = QApplication(sys.argv)
# window = QMainWindow()

# # create a tab widget and add some tabs to it
# tab_widget = QTabWidget(window)
# tab_widget.addTab(QLabel("Tab 1"), "Tab 1")
# tab_widget.addTab(QLabel("Tab 2"), "Tab 2")
# tab_widget.addTab(QLabel("Tab 3"), "Tab 3")

# # set the tab widget as the central widget of the main window
# window.setCentralWidget(tab_widget)

# # create a shortcut key for the Ctrl+W key combination
# close_shortcut = QShortcut(QKeySequence("Ctrl+W"), tab_widget)

# # define a slot function for the triggered signal of the shortcut key
# def close_current_tab():
#     current_index = tab_widget.currentIndex()
#     tab_widget.removeTab(current_index)

# # connect the triggered signal of the shortcut key to the close_current_tab slot function
# close_shortcut.activated.connect(close_current_tab)

# # show the main window
# window.show()

# # run the application
# sys.exit(app.exec_())

# exit()
# import pandas
# sets = {123,"hello","rate",123123123,"houses"}
# df = pandas.DataFrame(sets)
# df

import sys
import platform
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *
from ui_splash_screen import Ui_SplashScreen
from PyQt5 import QtCore
# import playsound
# from playsound import playsound

# import requests
# import pyautogui as g
# import vlc , pafy, time

counter = 0

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setStyleSheet('''*{
                                        background:#121019;
                                    }
                                    QTabBar::tab {
                                        border-bottom: none;
                                        padding: 1px 3px;
                                        margin-left: 3px;
                                        width: 80px;
                                        color: #a4a4a4;
                                        height: 20px;
                                        border-top-left-radius:9px;
                                        margin-bottom: 0px;

                                        }
                                    QTabBar::tab:hover{
                                        background: #450d1d;
                                        color: #a4a4a4;

                                        }
                                    QTabBar::tab:selected {
                                        background-color: #121019;
                                        border: 1px solid #fa1e4e;
                                        border-bottom-style: none;
                                        margin-bottom: 0px;
                                        border-left-color: #fa1e4e;
                                        color: white;

                                        }
                                    QTabBar::close-button {
                                        image: url(C:/Users/Black/close.png);
                                        subcontrol-position: right;
                                        }
                                    QTabBar::close-button:hover {
                                        border: 1px solid #2b3548;
                                        }
                                     ''')#181b28; border-top-left-radius: 4px; # border-top-right-radius: 4px; border-bottom-color: #fa1e4e;
                                        
                                        # margin-bottom: 1px;
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)

        
        # self.addtab = QWidget(self)
        # self.addtab.mouseDoubleClickEvent(QMouseEvent.buttons(Qt.MouseButton("left")))
        # self.tabs.setCornerWidget(self.addtab)  
        # if e.button() == Qt.RightButton:
        #     print("lefy") 
        # self.tabs.setTabShape(QTabWidget.TabShape("Triangular"))

        # self.tabs.setOverrideCursor(Qt.CursorShape.IBeamCursor)
        # self.tabs.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    

        # self.tabs.showEvent(QShowEvent("tab"))
        self.tabs.setMovable(True)
        # self.tabs.setTabBarAutoHide(True)
        self.tabs.setToolTip("Double Click On This👆")
        # self.tabs.setTabPosition(QTabWidget.West)
        self.tabs.currentChanged.connect(self.current_tab_changed)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)
        self.setCentralWidget(self.tabs)
        close_shortcut = QShortcut(QKeySequence("Ctrl+W"), self.tabs)
        close_shortcut.activated.connect(self.close_current_tab)
        self.tab_menu = QMenu()
        self.tab_menu.addAction("Close Tab", self.close_current_tab)
        self.tabs.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tabs.customContextMenuRequested.connect(self.show_tab_menu)
        # self.tabbars.setShape(self.tabbars.Shape(1))
        # self.tabbars.sizeHint(QSize.setWidth(self.tabbars,12))
        # self.tabbars.Shape.TriangularWest

        # self.tabs.setTabBar(self.tabbars)
        # self.tabs.setTabShape(self.tabs.TabShape(1))
        navtb = QToolBar("Navigation")
        navtb.setToolTip('tools ⚙')
        self.tabs.setStatusTip("Do You Want To Open New Tab? press ''ctrl+t")
        # shortcut = QShortcut(QKeySequence("Ctrl+w"), self)
        # shortcut.activated.connect(self.close_current_tab)


        navtb.setMovable(False)
        self.addToolBar(navtb)
        self.tabbtn = QPushButton(self)
        self.tabbtn.setGeometry(1670,40,30,18)
        self.tabbtn.setShortcut("ctrl+t")
        self.tabbtn.clicked.connect(self.new_tab)
        
        self.fullbtn = QCheckBox(self)
        self.fullbtn.setGeometry(1670,40,30,18)
        self.fullbtn.setShortcut("F11")
        self.fullbtn.clicked.connect(self.shownorful)
            # self.tabs.setTabBarAutoHide(False)
        self.hidebtn = QCheckBox(self.tabs)
        self.hidebtn.setGeometry(1670,40,30,18)
        self.hidebtn.setShortcut("ctrl+m")
        self.hidebtn.clicked.connect(self.tab_bar_hide_or_no)


        self.hidetabbtn = QCheckBox(self)
        self.hidetabbtn.setGeometry(1670,40,30,18)
        self.hidetabbtn.setShortcut("ctrl+n")
        self.hidetabbtn.clicked.connect(self.tab_bar_hidetab_or_no)

        # self.btn = QPushButton(self.tabs)
        # self.btn.setGeometry(160,40,30,18)
        # # self.btn.setShortcut("ctrl+m")
        # self.btn.clicked.connect(self.tabremoved)

        # self.ctabbtn = QShortcut(QKeySequence("ctrl+w"),self)
        
        # # self.ctabbtn.setGeometry(1570,40,30,18)
        # self.ctabbtn.activated.connect(self.close_current_tab)
        # cltabbtn = QAction(QIcon("right.png"),"➡", self)
        # cltabbtn.triggered.connect(self)
        # cltabbtn.setShortcut("ctrl+w")l
        # navtb.addAction(cltabbtn)
        # tabs = self.tabs
        # self.addtabbtn = QPushButton(self)
        # self.addtabbtn.setGeometry(160,40,15,18)
        # self.addtabbtn.setShortcut("ctrl+w")
        # self.addtabbtn.clicked.connect(self

        back_btn = QAction(QIcon(r'C:\MacKloud\resources\leftarrow.png'),"Go Back (alt+ ← arrow)",self)
        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
        back_btn.setToolTip("Go Back (alt+ ← arrow)")
        
        back_btn.setStatusTip("Do You Want To Go Back?  press 'alt+left arrow'")
        back_btn.setShortcut("alt+left")
        navtb.addAction(back_btn)


        forward_btn = QAction(QIcon('C:\\MacKloud\\resources\\rightarrow.png'),"Go Forward (alt+ → arrow)", self)
        forward_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
        forward_btn.setToolTip("Go Forward (alt+ → arrow)")
        forward_btn.setStatusTip("Do You Want To Go Forward?  press 'alt+right arrow'")
        forward_btn.setShortcut("alt+right")
        navtb.addAction(forward_btn)
        # self.tabs.addAction(forward_btn)

        reload_btn = QAction(QIcon('circular-arrow.png'), '🔄', self)
        reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
        # print(self.tabs.currentWidget().reload())
        # ss = QWebEngineHistory().count()
        # print(ss)
        reload_btn.setToolTip("Reload (ctrl+ ֎ r)")
        reload_btn.setStatusTip("Do You Want To Reload?  press 'ctrl+r'")
        reload_btn.setShortcut("ctrl+r")
        navtb.addAction(reload_btn)

        navtb.addSeparator()

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        
            
        self.url_bar.setStyleSheet("""
                                *{
                                    margin-top: 3px;
                                    color: white;
                                    font:bold;
                                    height: 30px;
                                    border-style: solid;
                                    background-color:#121019;
                                    border-radius:4px;
                                    selection-background-color: #fa1e4e;
                                }
                                *:hover{
                                    background-color:#4c1326;
                                    border-color:#00dfff;
                                    
                                }
                                *:focus{
                                    background-color: #251f33;
                                }
                                QLineEdit QMenu{
                                    color:white;
                                    font:bold;
                                    height: 180px;
                                    background: #1c1726;
                                }
                                QLineEdit QMenu::item:selected{
                                    background:#8b1b3a;
                                }""")

        navtb.addWidget(self.url_bar)
#         self.url_bar.setStyleSheet("""
#                                     QMenu {
#                                         background-color: transparent;
#                                         border: transparent;
#                                         }
# """)


        stop_btn = QAction('🛑', self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
        navtb.addAction(stop_btn)

        self.add_new_tab(QUrl('https://www.bing.com/'), 'homepage')
        self.show()
        self.setWindowTitle('MacKloud')
        self.setWindowIcon(QIcon("icon2.png"))
        self.setStyleSheet("background: #121019;color:white")  # 161219
        self.setToolTip("Browser🌐")

        # self.setWindowOpacity(0.96)
        self.screen()
        self.nav = navtb
        self.tabs.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tabs.customContextMenuRequested.connect(self.contextMenuEvent)
        
    # def tabremoved(self,i):
    #     self.tabs.setTabIcon(i,QIcon("C:\\MacKloud\\resources\\rightarrow.png"))
        # self.tabs.setTabIcon(i,QIcon("C:\\MacKloud\\resources\\rightarrow.png"))
# 
    def contextMenuEvent(self,event):
        menu = QMenu(self)
        copy_action = menu.addAction("Copy")
        paste_action = menu.addAction("Paste")
        action = menu.exec_(self.mapToGlobal(event.pos()))
        if action == copy_action:
            self.triggerPageAction(QWebEnginePage.Copy)
        elif action == paste_action:
            self.triggerPageAction(QWebEnginePage.Paste)
        print("right click on context menu")


    def show_tab_menu(self, pos):
        self.tab_menu.exec_(self.tabs.mapToGlobal(pos))

    def tab_bar_hide_or_no(self):
        if self.hidebtn.isChecked():
            self.nav.setHidden(True)
        elif self.hidebtn.isChecked()==False:
            self.nav.setHidden(False)


    def tab_bar_hidetab_or_no(self):
        if self.hidetabbtn.isChecked():
            self.tabs.setTabBarAutoHide(True)
        elif self.hidetabbtn.isChecked()==False:
            self.tabs.setTabBarAutoHide(False)


    def add_new_tab(self, qurl=None, label="New tab"):
        if qurl is None:
            qurl = QUrl('https://www.bing.com/')
        browser = QWebEngineView()
        browser.setUrl(qurl)
        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)
        # self.tabs.setTabToolTip(1, browser.page().title)
        
        browser.urlChanged.connect(
            lambda qurl, browser=browser: self.update_urlbar(qurl, browser))

        browser.loadFinished.connect(
            lambda _, i=i, browser=browser: self.tabs.setTabText(i, browser.page().title()[0:20]))

        # browser.setToolTip.connect(lambda: self.tabs.setTabToolTip(i, browser.page().title) )

    def tab_open_doubleclick(self, i):

        # playsound('C:/Users/BAREERA/Downloads/newtab.wav')
        if i == -1:
            self.add_new_tab()
            # self.tabs.setTabIcon(i,QIcon("Captures.PNG"))

            # sleep(0.25)

    def current_tab_changed(self, i):
        qurl = self.tabs.currentWidget().url()
        self.update_urlbar(qurl, self.tabs.currentWidget())
        self.update_title(self.tabs.currentWidget())

    
    def close_current_tab(self):
        if self.tabs.count() > 1:
            current_index = self.tabs.currentIndex()
            self.tabs.removeTab(current_index)

 
    def update_title(self, browser):
        if browser != self.tabs.currentWidget():
            return

        # title = self.tabs.currentWidget().page().title()
        self.setWindowTitle("% s - MacKloud"% self.tabs.currentWidget().page().title())


    def new_tab(self):
        self.add_new_tab()
        # sleep(0.25)
        # playsound('C:/Users/BAREERA/Downloads/newtab.wav')

    def navigate_to_url(self):
        navbar = QProgressBar(self)
        
        navbar.setGeometry(0,115,100,100)
        q = QUrl(self.url_bar.text())
        s = "youtube.com storror"
        s = s.replace("storror", self.url_bar.text()[12::])
        goo = "google.com storror"
        goo = goo.replace("storror", self.url_bar.text()[11::])
        search = self.url_bar.text().replace(" ","+")
        # checking for youtube search
        # print(s) 
        if q.scheme() == "":
            q.setScheme("http")
        if self.url_bar.text() == s:
            # checking again for youtube search
            # print(s)
            q = QUrl(f"https://www.youtube.com/results?search_query={search[12::]}")
            # self.tabs.setTabText(i,self.url_bar.text()[12::])
        elif self.url_bar.text() == goo:
            q = QUrl(f"https://www.google.com/search?q={search[11::]}")
        
        elif ".com" not in self.url_bar.text():
            q = QUrl(f"https://www.bing.com/search?q={search[0::]}")

        self.tabs.currentWidget().setUrl(q)

        

    def update_urlbar(self, q, browser=None):
        if browser != self.tabs.currentWidget():
            return

        self.url_bar.setText(q.toString())
        self.url_bar.setCursorPosition(0)
    
    def shownorful(self):
        if self.fullbtn.isChecked():
            self.showFullScreen()
        elif self.fullbtn.isChecked()==False:
            self.showMaximized()
            # QMessageBox.information(self, "No Closed Tabs", "There are no closed tabs to reopen.")



# def abb():
#     app = QApplication(sys.argv)
#     win = QWidget()
#     # QApplication.setWindowIcon(QIcon("D:/alldownloadafterdownload/macklogo.png"))
#     win.setToolTip("Browser")
#     window = MainWindow()
#     sys.exit(app.exec_())
# abb()
# SPLASH SCREEN

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME</strong> TO BROWSER")

        # Change Texts
        QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QTimer.singleShot(2300, lambda: self.ui.label_description.setText("<strong>LOADING...</strong>"))
        QTimer.singleShot(2500, lambda: self.ui.label_description.setText("<strong>LOADING..</strong>"))
        QTimer.singleShot(2800, lambda: self.ui.label_description.setText("<strong>LOADING.</strong>"))
        QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong>"))
        QTimer.singleShot(3500, lambda: self.ui.label_description.setText("<strong>LOADING.</strong>"))
        QTimer.singleShot(3800, lambda: self.ui.label_description.setText("<strong>LOADING..</strong>"))
        QTimer.singleShot(4000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())

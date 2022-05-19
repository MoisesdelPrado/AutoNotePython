from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys, os, time


class Ui_AutoNotepad(object):
    def setupUi(self, AutoNotepad):
        AutoNotepad.setObjectName("AutoNotepad")
        AutoNotepad.resize(709, 795)
        self.centralwidget = QtWidgets.QWidget(AutoNotepad)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 110, 621, 55))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.profile_link_buttons_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.profile_link_buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.profile_link_buttons_layout.setObjectName("profile_link_buttons_layout")
        self.copy_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.copy_button.setObjectName("copy_button")
        self.profile_link_buttons_layout.addWidget(self.copy_button)
        self.search_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.search_button.setObjectName("search_button")
        self.profile_link_buttons_layout.addWidget(self.search_button)
        self.reset_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.reset_button.setObjectName("reset_button")
        self.profile_link_buttons_layout.addWidget(self.reset_button)
        self.scroll_Area = QtWidgets.QScrollArea(self.centralwidget)
        self.scroll_Area.setGeometry(QtCore.QRect(30, 170, 661, 511))
        self.scroll_Area.setWidgetResizable(True)
        self.scroll_Area.setObjectName("scroll_Area")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 636, 1275))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.romanised_name = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.romanised_name.setObjectName("romanised_name")
        self.horizontalLayout_2.addWidget(self.romanised_name)
        self.original_name = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.original_name.sizePolicy().hasHeightForWidth())
        self.original_name.setSizePolicy(sizePolicy)
        self.original_name.setMaximumSize(QtCore.QSize(200, 16777215))
        self.original_name.setObjectName("original_name")
        self.horizontalLayout_2.addWidget(self.original_name)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.affiliations_text = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.affiliations_text.sizePolicy().hasHeightForWidth())
        self.affiliations_text.setSizePolicy(sizePolicy)
        self.affiliations_text.setObjectName("affiliations_text")
        self.verticalLayout.addWidget(self.affiliations_text)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.keywords_text = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.keywords_text.setObjectName("keywords_text")
        self.verticalLayout.addWidget(self.keywords_text)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.namesakes_text = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.namesakes_text.sizePolicy().hasHeightForWidth())
        self.namesakes_text.setSizePolicy(sizePolicy)
        self.namesakes_text.setMinimumSize(QtCore.QSize(0, 500))
        self.namesakes_text.setMaximumSize(QtCore.QSize(2000, 500))
        self.namesakes_text.setObjectName("namesakes_text")
        self.verticalLayout.addWidget(self.namesakes_text)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.notes_text = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notes_text.sizePolicy().hasHeightForWidth())
        self.notes_text.setSizePolicy(sizePolicy)
        self.notes_text.setObjectName("notes_text")
        self.verticalLayout.addWidget(self.notes_text)
        self.scroll_Area.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 690, 661, 55))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.reverse_email = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.reverse_email.setObjectName("reverse_email")
        self.horizontalLayout.addWidget(self.reverse_email)
        self.reverse_email_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.reverse_email_button.setToolTip("")
        self.reverse_email_button.setObjectName("reverse_email_button")
        self.horizontalLayout.addWidget(self.reverse_email_button)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 20, 301, 37))
        self.label_6.setObjectName("label_6")
        self.profile_link = QtWidgets.QLineEdit(self.centralwidget)
        self.profile_link.setGeometry(QtCore.QRect(60, 60, 601, 51))
        self.profile_link.setObjectName("profile_link")
        self.scroll_Area.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.label_6.raise_()
        self.profile_link.raise_()
        AutoNotepad.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AutoNotepad)
        self.statusbar.setObjectName("statusbar")
        AutoNotepad.setStatusBar(self.statusbar)

        self.retranslateUi(AutoNotepad)
        QtCore.QMetaObject.connectSlotsByName(AutoNotepad)

        self.copy_button.clicked.connect(self.copy)
        self.search_button.clicked.connect(self.search)
        self.reset_button.clicked.connect(self.reset)
        self.reverse_email_button.clicked.connect(self.reverse)

    def retranslateUi(self, AutoNotepad):
        _translate = QtCore.QCoreApplication.translate
        AutoNotepad.setWindowTitle(_translate("AutoNotepad", "Auto Notepad"))
        self.copy_button.setToolTip(_translate("AutoNotepad", "Copy KP information from CLean"))
        self.copy_button.setText(_translate("AutoNotepad", "Copy"))
        self.search_button.setToolTip(_translate("AutoNotepad", "Send google search query tabs based on KP information"))
        self.search_button.setText(_translate("AutoNotepad", "Search"))
        self.reset_button.setToolTip(_translate("AutoNotepad", "Reset KP information to blank"))
        self.reset_button.setText(_translate("AutoNotepad", "Reset"))
        self.label.setText(_translate("AutoNotepad", "Name:"))
        self.label_2.setText(_translate("AutoNotepad", "Past/Present Affiliations:"))
        self.label_3.setText(_translate("AutoNotepad", "Keywords:"))
        self.label_4.setText(_translate("AutoNotepad", "Namesakes:"))
        self.label_5.setText(_translate("AutoNotepad", "Additional notes:"))
        self.reverse_email_button.setText(_translate("AutoNotepad", "Reverse Email"))
        self.label_6.setText(_translate("AutoNotepad", "Insert profile link here:"))


    def copy(self):
        target = self.profile_link.text()
        
        #option = Options()
        #option.add_experimental_option('/usr/share/applications','localhost:9000')
        driver= webdriver.Chrome()
        driver.get(target)
        try:
            original = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/dirt/dirt-profile/div/section/dirt-profile-detail/section/div/div[1]/div/div[1]/div[1]/h6'))
            )

            romanised1 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/dirt/dirt-profile/div/section/dirt-profile-detail/section/div/div[1]/div/div[1]/div[1]/h4/a/span[2]'))
            )

            romanised2 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/dirt/dirt-profile/div/section/dirt-profile-detail/section/div/div[1]/div/div[1]/div[1]/h4/a/span[1]'))
            )

            affiliation1 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/dirt/dirt-profile/div/section/dirt-profile-detail/section/div/div[1]/div/div[3]/div[3]/div/span[2]'))
            )


            affiliation2 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/dirt/dirt-profile/div/section/dirt-profile-detail/section/div/div[1]/div/div[3]/div[3]/div/span[3]'))
            )

            affiliation3 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/dirt/dirt-profile/div/section/dirt-profile-detail/section/div/div[1]/div/div[3]/div[4]/div/span[2]'))
            )

            affiliation4 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/dirt/dirt-profile/div/section/dirt-profile-detail/section/div/div[1]/div/div[3]/div[4]/div/span[3]'))
            )

            keyword1 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/dirt/dirt-profile/div/section/dirt-profile-detail/section/div/div[1]/div/div[1]/div[2]/div[1]/span[1]'))
            )

            keyword2 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/dirt/dirt-profile/div/section/dirt-profile-detail/section/div/div[1]/div/div[1]/div[2]/div[1]/span[2]'))
            )


            self.original_name.setText(original.text)
            self.romanised_name.setText(romanised1.text + ' ' + romanised2.text)
            self.affiliations_text.setText(affiliation1.text + ' ' + affiliation2.text + ' ' + '\n' + affiliation3.text + ' ' + affiliation4.text)
            self.keywords_text.setText(keyword1.text + '\n' + keyword2.text)

        except:
            print('Error')
            time.sleep(20) 


    #Send search data to google search
    def search(self):
        name = ''

        if self.original_name.text() == '':
            name = self.romanised_name.text()
        else:
            name = self.original_name.text()

        os.environ['webdriver.chrome.driver'] = '/usr/bin'
        #s= Service(executable_path='/usr/bin/google-chrome-stable')
        driver = webdriver.Chrome()
        driver.get('https://google.com')

        try:
            searchbox = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'))
            )

            searchbox.send_keys(name + ' 病院')
            searchbox.send_keys(Keys.RETURN)
            time.sleep(20)

        except:
            print('Error')
            time.sleep(20)


    #Resets all info boxes to blank
    def reset(self):
        self.profile_link.setText('')
        self.romanised_name.setText('')
        self.original_name.setText('')
        self.affiliations_text.setText('')
        self.keywords_text.setText('')
        self.namesakes_text.setText('')
        self.reverse_email.setText('')


        
    #Reverses email 
    def reverse(self):
        corrected_email = self.reverse_email.text()[::-1]
        self.reverse_email.setText(corrected_email)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AutoNotepad = QtWidgets.QMainWindow()
    ui = Ui_AutoNotepad()
    ui.setupUi(AutoNotepad)
    AutoNotepad.show()
    sys.exit(app.exec_())

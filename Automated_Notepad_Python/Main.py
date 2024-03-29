# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AutoNotepad(object):
    def setupUi(self, AutoNotepad):
        AutoNotepad.setObjectName("AutoNotepad")
        AutoNotepad.resize(709, 860)
        self.centralwidget = QtWidgets.QWidget(AutoNotepad)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(130, 80, 481, 41))
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
        self.scroll_Area.setGeometry(QtCore.QRect(30, 130, 661, 521))
        self.scroll_Area.setWidgetResizable(True)
        self.scroll_Area.setObjectName("scroll_Area")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 636, 1375))
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
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.KOL_ID = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.KOL_ID.setObjectName("KOL_ID")
        self.verticalLayout.addWidget(self.KOL_ID)
        self.scroll_Area.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 660, 661, 41))
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
        self.profile_link = QtWidgets.QLineEdit(self.centralwidget)
        self.profile_link.setGeometry(QtCore.QRect(70, 30, 601, 41))
        self.profile_link.setWhatsThis("")
        self.profile_link.setText("")
        self.profile_link.setObjectName("profile_link")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 710, 661, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.search_email = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_email.sizePolicy().hasHeightForWidth())
        self.search_email.setSizePolicy(sizePolicy)
        self.search_email.setText("")
        self.search_email.setObjectName("search_email")
        self.horizontalLayout_3.addWidget(self.search_email)
        self.search_email_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_email_button.sizePolicy().hasHeightForWidth())
        self.search_email_button.setSizePolicy(sizePolicy)
        self.search_email_button.setMinimumSize(QtCore.QSize(0, 0))
        self.search_email_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.search_email_button.setObjectName("search_email_button")
        self.horizontalLayout_3.addWidget(self.search_email_button)
        self.JT_crosscheck_button = QtWidgets.QPushButton(self.centralwidget)
        self.JT_crosscheck_button.setGeometry(QtCore.QRect(450, 760, 241, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.JT_crosscheck_button.sizePolicy().hasHeightForWidth())
        self.JT_crosscheck_button.setSizePolicy(sizePolicy)
        self.JT_crosscheck_button.setMinimumSize(QtCore.QSize(0, 0))
        self.JT_crosscheck_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.JT_crosscheck_button.setObjectName("JT_crosscheck_button")
        self.scroll_Area.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.profile_link.raise_()
        self.horizontalLayoutWidget_3.raise_()
        self.JT_crosscheck_button.raise_()
        AutoNotepad.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AutoNotepad)
        self.statusbar.setObjectName("statusbar")
        AutoNotepad.setStatusBar(self.statusbar)

        self.retranslateUi(AutoNotepad)
        QtCore.QMetaObject.connectSlotsByName(AutoNotepad)

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
        self.romanised_name.setPlaceholderText(_translate("AutoNotepad", "Romanised/English Name"))
        self.original_name.setPlaceholderText(_translate("AutoNotepad", "Original Name"))
        self.label_2.setText(_translate("AutoNotepad", "Past/Present Affiliations:"))
        self.label_3.setText(_translate("AutoNotepad", "Keywords:"))
        self.label_4.setText(_translate("AutoNotepad", "Namesakes:"))
        self.label_5.setText(_translate("AutoNotepad", "Additional notes:"))
        self.label_6.setText(_translate("AutoNotepad", "KOL ID:"))
        self.reverse_email.setPlaceholderText(_translate("AutoNotepad", "Insert reversed email"))
        self.reverse_email_button.setText(_translate("AutoNotepad", "Un-Reverse Email"))
        self.profile_link.setPlaceholderText(_translate("AutoNotepad", "Insert profile link here"))
        self.search_email.setPlaceholderText(_translate("AutoNotepad", "Insert PA url here"))
        self.search_email_button.setToolTip(_translate("AutoNotepad", "Send google search query to find email"))
        self.search_email_button.setText(_translate("AutoNotepad", " Search for Email "))
        self.JT_crosscheck_button.setToolTip(_translate("AutoNotepad", "Send google search query to find email"))
        self.JT_crosscheck_button.setText(_translate("AutoNotepad", "JT Cross-check"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AutoNotepad = QtWidgets.QMainWindow()
    ui = Ui_AutoNotepad()
    ui.setupUi(AutoNotepad)
    AutoNotepad.show()
    sys.exit(app.exec_())

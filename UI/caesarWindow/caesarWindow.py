# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'caesarWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDial, QFrame, QGridLayout,
    QLabel, QLayout, QSizePolicy, QTextEdit,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridFrame = QFrame(Form)
        self.gridFrame.setObjectName(u"gridFrame")
        self.gridFrame.setGeometry(QRect(0, 0, 400, 600))
        sizePolicy.setHeightForWidth(self.gridFrame.sizePolicy().hasHeightForWidth())
        self.gridFrame.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.gridFrame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout.setContentsMargins(50, 50, 150, 50)
        self.label_2 = QLabel(self.gridFrame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(2)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(50, 25))
        self.label_2.setMaximumSize(QSize(50, 25))

        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1, Qt.AlignHCenter)

        self.dial = QDial(self.gridFrame)
        self.dial.setObjectName(u"dial")
        sizePolicy.setHeightForWidth(self.dial.sizePolicy().hasHeightForWidth())
        self.dial.setSizePolicy(sizePolicy)
        self.dial.setMinimumSize(QSize(100, 100))
        self.dial.setMaximumSize(QSize(100, 100))

        self.gridLayout.addWidget(self.dial, 0, 0, 1, 1)

        self.textEdit_3 = QTextEdit(self.gridFrame)
        self.textEdit_3.setObjectName(u"textEdit_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textEdit_3.sizePolicy().hasHeightForWidth())
        self.textEdit_3.setSizePolicy(sizePolicy2)
        self.textEdit_3.setMinimumSize(QSize(300, 100))
        self.textEdit_3.setMaximumSize(QSize(300, 100))
        self.textEdit_3.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.489, fy:0.511364, stop:0.189944 rgba(162, 165, 168, 255), stop:1 rgba(185, 188, 191, 255));\n"
"border-radius: 20px;")

        self.gridLayout.addWidget(self.textEdit_3, 8, 0, 1, 1, Qt.AlignHCenter)

        self.textEdit = QTextEdit(self.gridFrame)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QSize(200, 100))
        self.textEdit.setMaximumSize(QSize(200, 100))
        self.textEdit.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.489, fy:0.511364, stop:0.189944 rgba(162, 165, 168, 255), stop:1 rgba(185, 188, 191, 255));\n"
"border-radius: 20px;")

        self.gridLayout.addWidget(self.textEdit, 0, 1, 1, 1)

        self.textEdit_2 = QTextEdit(self.gridFrame)
        self.textEdit_2.setObjectName(u"textEdit_2")
        sizePolicy.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy)
        self.textEdit_2.setMinimumSize(QSize(200, 100))
        self.textEdit_2.setMaximumSize(QSize(200, 100))
        self.textEdit_2.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.489, fy:0.511364, stop:0.189944 rgba(162, 165, 168, 255), stop:1 rgba(185, 188, 191, 255));\n"
"border-radius: 20px;")

        self.gridLayout.addWidget(self.textEdit_2, 4, 1, 1, 1)

        self.label = QLabel(self.gridFrame)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(50, 25))
        self.label.setMaximumSize(QSize(50, 25))
        self.label.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1, Qt.AlignHCenter)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi


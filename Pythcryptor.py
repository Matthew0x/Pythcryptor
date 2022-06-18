# * Formatted using Black with camelCase + Qt naming convention.
# * Yes, camelCase is the best in the universe and doesn't add 99384573 additional signs in the names.

# TIPS:
# To pass an argument in the slot you need to construct a lambda expression:
# self.filmButton.clicked.connect(lambda: openWebpage("http://some.web.adress"))
# Remember to put signal listeners in persistent objects

# Obtaining window size
# self.shiftDial.setFixedWidth(int(window.frameSize().width() * 1 / 4))
# self.shiftDial.setFixedHeight(int(window.frameSize().width() * 1 / 4))

from PySide6.QtWidgets import (
    QApplication,
    QDial,
    QFrame,
    QGridLayout,
    QLabel,
    QLayout,
    QSizePolicy,
    QTextEdit,
    QWidget,
    QFormLayout,
    QComboBox,
    QBoxLayout,
    QStyleFactory,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
    QTextCursor,
    QCursor,
)
from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from functools import partial
import sys, os

# * Global functions

# *Yada yada, yes I found it on the internet
def getRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    roman = ""
    while number:
        div = number // num[i]
        number %= num[i]
        while div:
            roman += sym[i]
            div -= 1
        i -= 1
    return roman


# * Modifies text by operating on a copy
def changeAlignment(textEdit: QTextEdit, textAlignment: Qt.Alignment):
    tempTextEdit = textEdit
    tempTextEdit.moveCursor(QTextCursor.Start)
    lastPosition = -1
    currentPosition = tempTextEdit.textCursor().position()
    while lastPosition != currentPosition:
        tempTextEdit.setAlignment(textAlignment)
        tempTextEdit.moveCursor(QTextCursor.Down)
        lastPosition = currentPosition
        currentPosition = tempTextEdit.textCursor().position()
    textEdit = tempTextEdit
    del tempTextEdit
    textEdit.moveCursor(QTextCursor.End)


sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
sizePolicy.setHorizontalStretch(0)
sizePolicy.setVerticalStretch(0)


class MainWindow(QWidget):
    programName: str = "Pythcryptor"
    welcomeLabel: str = "Welcome to Pythcryptor\n\n"
    defaultWindowSize: list = [int(400), int(600)]
    previousCipher: str = "Null"
    darkBackgroundColor: str = "background-color: rgba(46,33,27, 250)"
    lightBackgroundGradient: str = "background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.8, fx:0.5, fy:0.5, stop:0.2 rgba(162, 165, 168, 50), stop:1 rgba(221, 221, 221, 250))"
    lightBackgroundColor: str = "background-color: rgba(221, 221, 221, 250)"
    lightSelectionBackgroundColor: str = "selection-background-color: lightGray;"
    lightSelectionColor: str = "selection-background-color: black;"
    lightHoverColor: str = "background: lightGray;"
    borderRadius: str = "border-radius: 10px;"

    def __init__(self, parent=None):
        super().__init__(parent)
        self.infoLabel = QLabel()
        self.spacerLabel = QLabel()
        self.cipherComboBox = QComboBox()
        self.windowLayout = QFormLayout()
        self.setSizePolicy(sizePolicy)
        self.setWindowTitle(self.programName)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setFixedSize(self.defaultWindowSize[0], self.defaultWindowSize[1])

        # The problem here is that the app runs QStyles rather than default CSS. Using own CSS will overwrite the old Style and you need to declare full CSS or the app looks like crap.
        # So far the CSS producted by QApplication object is empty...
        # TODO: WORK ON WINDOW GRAPHICAL FORMATTING
        # self.setStyleSheet("QApplication {background-color: cyan} QLabel {border-radius: 5px;}")
        # self.setStyleSheet("background-color: rgba(150, 150, 20, 100)")
        self.initUI()

    def initUI(self):
        # e1 = QListWidget(self)
        # e1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # e1.setFont(QFont("Arial",20))
        self.spacerLabel.setText("\n\n")
        self.spacerLabel.setFrameStyle(QFrame.HLine | QFrame.Raised)  # type: ignore
        # self.spacerLabel.setFrameShape(QFrame.HLine)
        # self.spacerLabel.setFrameShadow(QFrame.Raised)
        self.spacerLabel.setAlignment(Qt.AlignCenter)  # type: ignore

        self.infoLabel.setFrameStyle(int(QFrame.HLine | QFrame.Raised))  # type: ignore
        self.infoLabel.setText(self.welcomeLabel)
        self.infoLabel.setAlignment(Qt.AlignCenter)  # type: ignore

        self.cipherComboBox.setFixedWidth(200)
        self.cipherComboBox.addItem("Monoalphabetic")
        self.cipherComboBox.addItem("Caesar")
        self.cipherComboBox.setStyleSheet(
            f"{MainWindow.lightBackgroundColor};"
            f"{MainWindow.lightSelectionBackgroundColor};"
            f"{MainWindow.borderRadius};"
            "QComboBox::hover"
            "{"
            f"{MainWindow.lightHoverColor};"
            "}"
        )

        self.windowLayout.setAlignment(Qt.AlignCenter)  # type: ignore
        self.windowLayout.addRow(self.infoLabel)
        self.windowLayout.addRow(self.cipherComboBox)
        self.windowLayout.addRow(self.spacerLabel)

        # Doesn't work really. Produces an empty stylesheet. I wonder where I can find the stupid CSS template example...
        test = str(self.styleSheet())
        file = open(os.path.join(os.getcwd(), "stylesheet.css"), "w")
        file.write("Writing stylesheet: \n\n" + str(test))
        file.close()

        # Basically my old trash code, that I might want to analyze the other day.
        # So far I realized that event listeners are rigged and don't accept arguments in called functions.
        # Makes much sense, because what kind of function accepts arguments? ./s

        # This one doesn't work. /Edit - yeah, explained above
        # self.cipherComboBox.textActivated.connect(self.buildChanges(
        #     self.cipherComboBox.currentText(), self.previousCipher))

        # This one won't pass the updated arguments. I think that the arg0 and arg1 are static and not updated dynamically when events are signalled.
        # I guess the arg0, arg1 are static and won't really care about currentText() changing.
        # self.cipherComboBox.textActivated.connect(lambda arg0 = self.cipherComboBox.currentText(), arg1 = self.previousCipher : self.buildChanges(arg0, arg1))

        # This one says that it gives too many arguments? Uwotm8? /Edit - I kicked that library out for now.
        # self.cipherComboBox.textActivated.connect(partial(
        #    self.buildChanges, self.cipherComboBox.currentText(), self.previousCipher))

        # This one works!
        # It works, but it's also a bit stupid. It's like a pointer to a function, but with arguments...
        # buildLambda = lambda: self.buildChanges(self.cipherComboBox.currentText(), self.previousCipher)
        # self.cipherComboBox.textActivated.connect(buildLambda)

        # This one works and was produced by PEP8 plugin... No idea what's the difference. The return isn't even necessary I guess?
        # def buildLambda(): return self.buildChanges(
        #     self.cipherComboBox.currentText(), self.previousCipher)

        # Some sample code. Will see if I can scrap something from that.
        # e2 = QLineEdit()
        # e2.setValidator(QDoubleValidator(0.99,99.99,2))
        # e3 = QLineEdit()
        # e3.setInputMask("+99_9999_999999")
        # e4 = QLineEdit()
        # e4.textChanged.connect(self.textchanged)
        # e5 = QLineEdit()
        # e5.setEchoMode(QLineEdit.Password)
        # e6 = QLineEdit("Hello PyQt5")
        # e6.setReadOnly(True)
        # e5.editingFinished.connect(self.enterPress)

        self.setLayout(self.windowLayout)

    def buildChanges(self) -> None:
        # Tell me what cipher we're talking about
        print(
            "buildChanges says:",
            "\n\tprevious cipher: ",
            self.previousCipher,
            "\n\tcurrent cipher: ",
            self.cipherComboBox.currentText(),
        )

        if (
            self.cipherComboBox.currentText() == "Monoalphabetic"
            and self.previousCipher != self.cipherComboBox.currentText()
        ):
            self.changeWindow("Monoalphabetic")
        if self.cipherComboBox.currentText() == "Caesar" and self.previousCipher != self.cipherComboBox.currentText():
            self.changeWindow("Caesar")
            # Yes, global is pretty stupid, but I don't know how to fix it for now
            global caesarWindow
            caesarWindow = Caesar(self)
            caesarWindow.shiftDial.valueChanged.connect(caesarWindow.caesarShowValue)  # type: ignore
            caesarWindow.shiftDial.valueChanged.connect(caesarWindow.caesarShowMessage)  # type: ignore
            caesarWindow.messageInput.textChanged.connect(caesarWindow.caesarShowMessage)  # type: ignore

            def messageInputFormat():
                caesarWindow.messageInput.textChanged.disconnect(messageInputFormat),  # type: ignore
                changeAlignment(caesarWindow.messageInput, Qt.AlignCenter),  # type: ignore
                caesarWindow.messageInput.textChanged.connect(messageInputFormat)  # type: ignore

            caesarWindow.messageInput.textChanged.connect(messageInputFormat)  # type: ignore

    def buildSpacer(self, frameWidth, frameHeight):
        spacerLabel = QLabel()
        spacerLabel.setFixedWidth(frameWidth)
        spacerLabel.setFixedHeight(frameHeight)
        spacerLabel.setFrameStyle(QFrame.NoFrame)  # type: ignore
        spacerLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # type: ignore
        sizePolicy.setHeightForWidth(spacerLabel.sizePolicy().hasHeightForWidth())
        spacerLabel.setSizePolicy(sizePolicy)
        return spacerLabel

    def changeWindow(self, currentCipher: str) -> None:
        if currentCipher != self.previousCipher and currentCipher != "Null":
            if self.windowLayout.rowCount() > 3:
                self.windowLayout.removeRow(self.windowLayout.rowCount() - 1)
        self.previousCipher = currentCipher


class Caesar:
    def __init__(self, window: MainWindow, parent=MainWindow):
        # Caesar CONTROLS
        self.shiftDial = QDial()
        self.shiftDial.setSingleStep(1)
        self.shiftDial.setPageStep(1)
        self.shiftDial.setValue(1)
        self.shiftDial.setMinimum(1)
        self.shiftDial.setMaximum(26)
        self.shiftDial.setTracking(True)
        self.shiftDial.setNotchTarget(True)
        self.shiftDial.setNotchesVisible(False)
        self.shiftDial.setWrapping(False)
        self.shiftDial.setFixedWidth(100)
        self.shiftDial.setFixedHeight(100)
        sizePolicy.setHeightForWidth(self.shiftDial.sizePolicy().hasHeightForWidth())
        self.shiftDial.setSizePolicy(sizePolicy)
        self.shiftDial.setStyleSheet(
            f"{MainWindow.lightBackgroundColor};"
            f"{MainWindow.lightSelectionBackgroundColor};"
            f"{MainWindow.borderRadius};"
        )
        #
        # No idea what it's supposed to do. I tried playing around with dynamically expanding elements.
        # So far it turns out to be stupidly messed up. I will write own listener for this.
        # TODO: DYNAMICALLY EXPANDING WINDOWS
        # shiftDial.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.valueLabel = QLabel()
        self.valueLabel.setText(str(self.shiftDial.value()))
        self.valueLabel.setAlignment(Qt.AlignCenter)  # type: ignore
        self.valueLabel.setFixedWidth(50)
        self.valueLabel.setFixedHeight(25)
        print(
            "buildChanges says:",
            "\n\tshiftDial.height(): ",
            self.shiftDial.height(),
            "\n\tshiftDial.width(): ",
            self.shiftDial.width(),
            "\n\tvalueLabel.height(): ",
            self.valueLabel.height(),
            "\n\tvalueLabel.width(): ",
            self.valueLabel.width(),
        )
        self.valueLabel.setFrameStyle(QFrame.Box | QFrame.Raised)  # type: ignore
        sizePolicy.setHeightForWidth(self.valueLabel.sizePolicy().hasHeightForWidth())
        self.valueLabel.setSizePolicy(sizePolicy)

        # Caesar DATA INPUT/OUTPUT
        self.messageInput = QTextEdit("Your message")
        self.messageInput.setFixedWidth(200)
        self.messageInput.setFixedHeight(100)
        self.messageInput.setFrameStyle(QFrame.Panel | QFrame.Raised)  # type: ignore
        self.messageInput.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # type: ignore
        self.messageInput.setAcceptRichText(False)
        sizePolicy.setHeightForWidth(self.messageInput.sizePolicy().hasHeightForWidth())
        self.messageInput.setSizePolicy(sizePolicy)
        self.messageInput.setStyleSheet(
            f"{MainWindow.lightBackgroundGradient};"
            f"{MainWindow.lightSelectionBackgroundColor};"
            f"{MainWindow.borderRadius};"
        )
        # self.messageInput.setClearButtonEnabled(True)

        self.messageOutput = QTextEdit("Your encrypted message")
        self.messageOutput.setFixedWidth(200)
        self.messageOutput.setFixedHeight(100)
        self.messageOutput.setFrameStyle(QFrame.Panel | QFrame.Raised)  # type: ignore
        self.messageOutput.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # type: ignore
        self.messageOutput.setAcceptRichText(False)
        sizePolicy.setHeightForWidth(self.messageOutput.sizePolicy().hasHeightForWidth())
        self.messageOutput.setSizePolicy(sizePolicy)
        self.messageOutput.setStyleSheet(
            f"{MainWindow.lightBackgroundGradient};"
            f"{MainWindow.lightSelectionBackgroundColor};"
            f"{MainWindow.borderRadius};"
        )

        self.cipherInfo = QTextEdit(
            """
                Caesar cipher is also known as shift cipher.
                ...
                It is a type of cipher that belongs into substitution ciphers category.
                Caesar cipher replaces each letter of the encrypted word with another letter, shifted by a specified value
                in modulo space of alphabet. In different words, the alphabet has 26 letters, hence the modulo space is 26, with shift values
                varying from 0 to 26
            """
        )
        self.cipherInfo.setFixedWidth(300)
        self.cipherInfo.setFixedHeight(150)
        self.cipherInfo.setFrameStyle(QFrame.Panel | QFrame.Raised)  # type: ignore
        self.cipherInfo.setAlignment(Qt.AlignJustify)  # type: ignore
        self.cipherInfo.setTextInteractionFlags(Qt.NoTextInteraction)  # type: ignore
        sizePolicy.setHeightForWidth(self.cipherInfo.sizePolicy().hasHeightForWidth())
        self.cipherInfo.setSizePolicy(sizePolicy)
        self.cipherInfo.setStyleSheet(
            f"{MainWindow.lightBackgroundGradient};"
            f"{MainWindow.lightSelectionBackgroundColor};"
            f"{MainWindow.borderRadius};"
        )

        # Caesar MAIN LAYOUT
        self.gridCaesar = QGridLayout()
        # self.gridCaesar.setGeometry(QRect(0, 0, 400, 600))
        self.gridCaesar.setSpacing(0)
        self.gridCaesar.setSizeConstraint(QLayout.SetFixedSize)
        self.gridCaesar.setContentsMargins(40, 0, 140, 0)

        # ! Tried providing arguments with names, not to get lost in a series of 10 thousands numerical values.
        # ! Turns out that the function doesn't agree with me. It prefers the most primitive and stupid way instead.

        # TODO: add aliases to arguments
        # * BTW did you know about:
        # Edit: Positional-only parameters are possible in Python 3.8 by a new function parameter syntax / to indicate that some function parameters must be specified positionally and cannot be used as keyword arguments.
        # def somefunc(a, b, /):
        #   print(a, b)
        # * POV: you're a python programmer trying to use arguments with keywords
        # addWidget(arg__1: QWidget, row: int, column: int, rowSpan: int, columnSpan: int, alignment: Alignment = ...)
        # ?self.gridCaesar.addWidget(self.shiftDial, row=0, column=0, rowSpan=1, columnSpan=1, alignment=Qt.AlignCenter)  # type: ignore
        # ?AttributeError: PySide6.QtWidgets.QGridLayout.addWidget(): unsupported keyword 'row'

        # self.gridCaesar.addWidget(self.shiftDial, row=0, column=0, rowSpan=1, columnSpan=1, alignment=Qt.AlignCenter)  # type: ignore
        self.gridCaesar.addWidget(self.shiftDial, 0, 0, 1, 1, Qt.AlignCenter)  # type: ignore
        self.gridCaesar.addWidget(self.valueLabel, 1, 0, 1, 1, Qt.AlignCenter)  # type: ignore
        self.gridCaesar.addWidget(self.messageInput, 0, 1, 1, 1, Qt.AlignCenter)  # type: ignore
        self.gridCaesar.addWidget(self.messageOutput, 4, 1, 1, 1, Qt.AlignCenter)  # type: ignore
        self.gridCaesar.addWidget(
            window.buildSpacer((int(window.frameSize().width() * 1 / 8)), (int(window.frameSize().width() * 1 / 16))),
            5,
            0,
            1,
            1,
            Qt.AlignCenter,  # type: ignore
        )
        self.gridCaesar.addWidget(self.cipherInfo, 8, 0, 1, 1, Qt.AlignCenter)  # type: ignore
        window.windowLayout.addRow(self.gridCaesar)

    # Let's define some things
    def caesarShowValue(self) -> None:
        """print(
            "caesarShowValue says:",
            "\n\tvalueLabel.text(): ",
            self.valueLabel.text(),
            "\n\tshiftDial.value(): ",
            self.shiftDial.value(),
        )"""
        self.valueLabel.setText(str(self.shiftDial.value()) + "-" + str(getRoman(self.shiftDial.value())))

    def caesarShowMessage(self) -> None:
        array = ""
        for index in range(len(self.messageInput.toPlainText())):
            char = self.messageInput.toPlainText()[index]
            if ord(char) >= 65 and ord(char) <= 90:
                array = array + chr((ord(char) + self.shiftDial.value() - 65) % 26 + 65)
            elif ord(char) >= 97 and ord(char) <= 122:
                array = array + chr((ord(char) + self.shiftDial.value() - 97) % 26 + 97)
            else:
                array = array + char
        self.messageOutput.setText(array)
        changeAlignment(self.messageOutput, Qt.AlignCenter)  # type: ignore


def render():
    sys.argv += ["--style", "Material"]
    app = QApplication(sys.argv)

    # Basically tried to utilize Qt styles. Like Macintosh, Windows (old ones), or new ones like Material etc.
    # * OK, they seem to work, but only chosen ones? I found info that they are available basing on the OS, so what the 0ck is the point of having multiple themes,
    # * if they are OS dependent and do not provide a universal GUI style?
    # https://doc.qt.io/qt-6/qtquickcontrols2-styles.html

    # app.setStyle(QStyleFactory.create("macOS"))
    # app.setStyle(QStyleFactory.create("Fusion"))

    mainWindow = MainWindow()
    mainWindow.show()

    # Signal listeners handled from "main", as this seems to be one of few persistent ways to do so
    mainWindow.cipherComboBox.textActivated.connect(mainWindow.buildChanges)  # type: ignore
    sys.exit(app.exec())


if __name__ == "__main__":
    render()

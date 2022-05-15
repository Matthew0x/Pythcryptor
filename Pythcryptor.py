from PySide6.QtWidgets import QApplication, QStyleFactory, QLineEdit, QWidget, QFormLayout, QListWidget, QComboBox, QLabel, QFrame, QDial, QColumnView, QVBoxLayout, QHBoxLayout, QInputDialog, QBoxLayout, QGridLayout, QSpacerItem, QSizePolicy
from PySide6.QtGui import QIntValidator, QDoubleValidator, QFont
from PySide6.QtCore import Qt
from functools import partial
import sys, os


class mainWindow(QWidget):
        programName: str = "Pythcryptor"
        welcomeLabel: str = "Welcome to Pythcryptor\n\n"
        defaultWindowSize: list = [int(400), int(600)]
        previousCipher: str = "Null"

        def __init__(self, parent=None):
                super().__init__(parent)
                self.infoLabel = QLabel()
                self.spacerLabel = QLabel()
                self.cipherComboBox = QComboBox()
                self.windowLayout = QFormLayout()
                self.setWindowTitle(self.programName)
                self.setFixedSize(self.defaultWindowSize[0], self.defaultWindowSize[1])

                # The problem here is that the app runs QStyles rather than default CSS. Using own CSS will overwrite the old Style and you need to declare full CSS or the app looks like crap.
                # So far the CSS producted by QApplication object is empty...
                #self.setStyleSheet("QApplication {background-color: cyan} QLabel {border-radius: 5px;}")
                #self.setStyleSheet("background-color: rgba(150, 150, 20, 100)")
                self.initUI()

        def initUI(self):
                # e1 = QListWidget(self)
                # e1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                # e1.setFont(QFont("Arial",20))
                self.spacerLabel.setText("\n\n")
                self.spacerLabel.setFrameStyle(QFrame.HLine | QFrame.Raised)
                self.spacerLabel.setAlignment(Qt.AlignCenter)

                self.infoLabel.setFrameStyle(QFrame.HLine | QFrame.Raised)
                self.infoLabel.setText(self.welcomeLabel)
                self.infoLabel.setAlignment(Qt.AlignCenter)

                self.cipherComboBox.setFixedWidth(self.frameSize().toTuple()[0]*2/4)
                self.cipherComboBox.addItem("Monoalphabetic")
                self.cipherComboBox.addItem("Caesar")

                self.windowLayout.setAlignment(Qt.AlignCenter)
                self.windowLayout.addRow(self.infoLabel)
                self.windowLayout.addRow(self.cipherComboBox)
                self.windowLayout.addRow(self.spacerLabel)

                # Doesn't work really. Produces an empty stylesheet. I wonder where I can find the stupid CSS template example...
                test = self.styleSheet()
                file = open(os.path.join(os.getcwd(), "stylesheet.css"), 'w')
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
                self.cipherComboBox.textActivated.connect(self.buildChanges)


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
                print("buildChanges says:", "\n\tprevious cipher: ", self.previousCipher, "\n\tcurrent cipher: ", self.cipherComboBox.currentText())
                if self.cipherComboBox.currentText() == "Monoalphabetic" and self.previousCipher != self.cipherComboBox.currentText():
                        self.trackChanges("Monoalphabetic")
                if self.cipherComboBox.currentText() == "Caesar" and self.previousCipher != self.cipherComboBox.currentText():
                        self.trackChanges("Caesar")

                        # One liner global variable with initialization is not available. Top "Frog God"
                        # I might want to rewrite those things into classes to build objects instead.
                        # It just doesn't make much sense to build objects to hold one or two variables, right?
                        # global shiftDial = QDial() 

                        global dialValue, shiftDial, messageInput, messageOutput

                        # Caesar CONTROLS
                        shiftDial = QDial()
                        shiftDial.setSingleStep(1)
                        shiftDial.setPageStep(1)
                        shiftDial.setMinimum(1)
                        shiftDial.setMaximum(26)
                        shiftDial.setTracking(1)
                        shiftDial.setNotchTarget(True)
                        shiftDial.setNotchesVisible(True)
                        shiftDial.setWrapping(False)
                        shiftDial.setFixedWidth(self.frameSize().toTuple()[0]*1/4)
                        shiftDial.setFixedHeight(self.frameSize().toTuple()[0]*1/4)

                        # No idea what it's supposed to do. I tried playing around with dynamically expanding elements.
                        # So far it turns out to be stupidly messed up. I will write own listener for this.
                        # Learning about how Qt handles this is a waste of my time.
                        # shiftDial.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

                        dialValue = QLabel()
                        dialValue.setText("0")
                        dialValue.setAlignment(Qt.AlignCenter)
                        dialValue.setFixedWidth(shiftDial.width()*1/2)
                        dialValue.setFixedHeight(shiftDial.height()*1/4)
                        print("buildChanges says:", "\n\tshiftDial.height(): ", shiftDial.height(), "\n\tshiftDial.width(): ", shiftDial.width(), "\n\tdialValue.height(): ", dialValue.height(), "\n\tdialValue.width(): ", dialValue.width())
                        dialValue.setFrameStyle(QFrame.Box | QFrame.Raised)
                        # dialValue.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

                        layoutDials = QBoxLayout(QBoxLayout.TopToBottom, parent = None)
                        # Same. Related to layout/widget stretching/expanding. Makes 0 difference.
                        # layoutDials.setStretch(1, 1)
                        layoutDials.addWidget(shiftDial)
                        layoutDials.addWidget(dialValue)

                        # Caesar DATA INPUT/OUTPUT
                        messageInput = QLineEdit("Your message")
                        messageInput.setFixedWidth(self.frameSize().toTuple()[0]*2/4)
                        messageInput.setFixedHeight(self.frameSize().toTuple()[0]*1/4)

                        messageOutput = QLabel("Your encrypted message")
                        messageOutput.setFrameStyle(QFrame.Box | QFrame.Raised)
                        messageOutput.setFixedWidth(self.frameSize().toTuple()[0]*2/4)
                        messageOutput.setFixedHeight(self.frameSize().toTuple()[0]*1/4)

                        layoutData = QBoxLayout(QBoxLayout.TopToBottom, parent = None)
                        # layoutData.setStretch(1, 1)
                        layoutData.addWidget(messageInput)
                        layoutData.addWidget(messageOutput)

                        # Caesar MAIN LAYOUT
                        layoutCaesar = QBoxLayout(QBoxLayout.LeftToRight, parent = None)
                        layoutCaesar.addLayout(layoutDials)
                        layoutCaesar.addLayout(layoutData)
                        gridCaesar = QGridLayout()

                        # Tried providing arguments with names, not to get lost in a series of 10 thousands numerical values.
                        # Turns out that the function doesn't agree with me. It prefers the most primitive and stupid way instead.
                        # The issue it has is that I provide "too many" arguments, but the constructors disagree otherwise (shown below).
                        # gridCaesar.addWidget(self = self, arg__1 = shiftDial, row = 0, column = 0, rowSpan = 1, columnSpan = 1, alignment = Qt.AlignCenter)


                        # def addItem(self, arg__1:PySide6.QtWidgets.QLayoutItem) -> None: ...
                        # @overload
                        # def addItem(self, item:PySide6.QtWidgets.QLayoutItem, row:int, column:int, rowSpan:int=..., columnSpan:int=..., alignment:PySide6.QtCore.Qt.Alignment=...) -> None: ...
                        # @overload
                        # def addLayout(self, arg__1:PySide6.QtWidgets.QLayout, row:int, column:int, alignment:PySide6.QtCore.Qt.Alignment=...) -> None: ...
                        # @overload
                        # def addLayout(self, arg__1:PySide6.QtWidgets.QLayout, row:int, column:int, rowSpan:int, columnSpan:int, alignment:PySide6.QtCore.Qt.Alignment=...) -> None: ...
                        # @overload
                        # def addWidget(self, arg__1:PySide6.QtWidgets.QWidget, row:int, column:int, alignment:PySide6.QtCore.Qt.Alignment=...) -> None: ...
                        
                        gridCaesar.addWidget(shiftDial, 0, 0, 1, 1, Qt.AlignCenter)
                        gridCaesar.addWidget(dialValue, 1, 0, 1, 1, Qt.AlignCenter)
                        gridCaesar.addWidget(messageInput, 0, 1, 1, 3, Qt.AlignCenter)
                        gridCaesar.addWidget(messageOutput, 2, 1, 1, 3, Qt.AlignCenter)
                        self.windowLayout.addRow(gridCaesar)

                        # Caesar EVENT LISTENERS
                        def showValue(): dialValue.setText(str(shiftDial.value()))
                        shiftDial.valueChanged.connect(showValue)
                        def showMessage(): 
                                array = ""
                                for index in range(len(messageInput.text())):
                                        char = messageInput.text()[index]
                                        if (ord(char) >=65 and ord(char) <=90):
                                                array = array + chr((ord(char) + shiftDial.value() - 67) % 26 + 65)
                                        elif (ord(char) >=97 and ord(char) <=122):
                                                array = array + chr((ord(char) + shiftDial.value() - 97) % 26 + 97)
                                        else:
                                                array = array + char
                                messageOutput.setText(array)
                        shiftDial.valueChanged.connect(showMessage)
                        messageInput.textChanged.connect(showMessage)

        def trackChanges(self, currentCipher:str) -> None:
                if(currentCipher != self.previousCipher and currentCipher != "Null"):
                        if (self.windowLayout.rowCount() > 3): 
                                self.windowLayout.removeRow(self.windowLayout.rowCount()-1)
                self.previousCipher = currentCipher


def render():
        sys.argv += ['--style', 'Material']
        app = QApplication(sys.argv)

        # Basically tried to utilize Qt styles. Like Macintosh, Windows (old ones), or new ones like Material etc.
        # Nope, the program doesn't really care. Here we go Qt guides, so much useful once again... (still better than UWP lmao)
        # app.setStyle(QStyleFactory.create("Material"))

        win = mainWindow()
        win.show()
        sys.exit(app.exec())


if __name__ == "__main__":
        render()

from PySide6.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout, QListWidget, QComboBox, QLabel, QFrame, QDial, QColumnView, QVBoxLayout
from PySide6.QtGui import QIntValidator, QDoubleValidator, QFont
from PySide6.QtCore import Qt
from functools import partial
import sys


class mainWindow(QWidget):
        programName: str = "Pythcryptor"
        infoLabel: str = "Welcome to Pythcryptor\n\n"
        defaultWindowSize: list = [int(400), int(600)]
        previousCipher: str = "Null"

        def __init__(self, parent=None):
                super().__init__(parent)
                self.cipherTypeLabel = QLabel()
                self.cipherComboBox = QComboBox()
                self.windowLayout = QFormLayout()
                self.setWindowTitle(self.programName)
                self.resize(self.defaultWindowSize[0], self.defaultWindowSize[1])
                self.initUI()

        def initUI(self):
                # e1 = QListWidget(self)
                # e1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                # e1.setFont(QFont("Arial",20))
                self.cipherTypeLabel.setFrameStyle(QFrame.HLine | QFrame.Raised)
                self.cipherTypeLabel.setText(self.infoLabel)
                self.cipherTypeLabel.setAlignment(Qt.AlignCenter)

                self.cipherComboBox.setFixedWidth(self.frameSize().toTuple()[0]/4)
                self.cipherComboBox.addItem("Monoalphabetic")
                self.cipherComboBox.addItem("Caesar")

                self.windowLayout.addRow(self.cipherTypeLabel)
                self.windowLayout.addRow(self.cipherComboBox)

                # This one doesn't work lol
                # self.cipherComboBox.textActivated.connect(self.buildChanges(
                #     self.cipherComboBox.currentText(), self.previousCipher))

                # This one won't pass the updated arguments. I think that the arg0 and arg1 are static and not updated dynamically when events are signalled. Weird
                # self.cipherComboBox.textActivated.connect(lambda arg0 = self.cipherComboBox.currentText(), arg1 = self.previousCipher : self.buildChanges(arg0, arg1)) #Lambda is broken in this example

                # This one says that it gives too many arguments? WTF?
                # self.cipherComboBox.textActivated.connect(partial(
                #    self.buildChanges, self.cipherComboBox.currentText(), self.previousCipher))

                # This one works!
                # buildLambda = lambda: self.buildChanges(self.cipherComboBox.currentText(), self.previousCipher)
                # self.cipherComboBox.textActivated.connect(buildLambda)

                # This one works and was produced by PEP8 plugin... what the hell is going on with Python?
                # def buildLambda(): return self.buildChanges(
                #     self.cipherComboBox.currentText(), self.previousCipher)
                self.cipherComboBox.textActivated.connect(self.buildChanges)

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

                        global dialValue  # global shiftDial = QDial() #ecs dee, the one liner global variable with initialization is not available. Prase Kek
                        global shiftDial
                        shiftDial = QDial()
                        shiftDial.setSingleStep(1)
                        shiftDial.setMinimum(1)
                        shiftDial.setMaximum(26)
                        shiftDial.setTracking(1)
                        shiftDial.setNotchTarget(True)
                        shiftDial.setNotchesVisible(True)
                        shiftDial.setWrapping(False)
                        shiftDial.setFixedWidth(self.frameSize().toTuple()[0]/4)
                        shiftDial.setFixedHeight(self.frameSize().toTuple()[0]/4)

                        dialValue = QLabel()
                        dialValue.setText("0")
                        dialValue.setAlignment(Qt.AlignCenter)

                        dialValue.setFixedWidth(self.frameSize().toTuple()[0]/4)

                        dialValue.setFrameStyle(QFrame.Box | QFrame.Raised)

                        layoutCaesar = QVBoxLayout()
                        layoutCaesar.addWidget(shiftDial)
                        layoutCaesar.addWidget(dialValue)
                        self.windowLayout.addRow(layoutCaesar)

                        def showValue(): return dialValue.setText(str(shiftDial.value()))
                        shiftDial.valueChanged.connect(showValue)

        def trackChanges(self, currentCipher:str) -> None:
                if(currentCipher != self.previousCipher and currentCipher != "Null"):
                        if (self.windowLayout.rowCount() > 2): 
                                self.windowLayout.removeRow(self.windowLayout.rowCount()-1)
                self.previousCipher = currentCipher


def render():
        app = QApplication(sys.argv)
        win = mainWindow()
        win.show()
        sys.exit(app.exec())


if __name__ == "__main__":
        render()

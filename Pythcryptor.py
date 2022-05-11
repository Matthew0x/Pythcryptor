from PySide6.QtWidgets import QApplication,QLineEdit,QWidget,QFormLayout, QListWidget, QComboBox, QLabel, QFrame, QDial, QColumnView
from PySide6.QtGui import QIntValidator,QDoubleValidator,QFont
from PySide6.QtCore import Qt
import sys

class pythCrypt(QWidget):
        programName = "Pythcryptor"
        infoLabel = "Welcome to Pythcryptor\n\n"
        defaultWindowSize = [int(400), int(600)]
        def __init__(self, parent = None):
                super().__init__(parent)
                self.encryptTypeLabel = QLabel()
                self.encryptComboBox = QComboBox()
                self.windowLayout = QFormLayout()
                self.setWindowTitle(self.programName)
                self.resize(self.defaultWindowSize[0], self.defaultWindowSize[1])
                self.initUI()
                
        def initUI(self):
                #e1 = QListWidget(self)
                #e1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                #e1.setFont(QFont("Arial",20))
                self.encryptTypeLabel.setFrameStyle(QFrame.HLine | QFrame.Raised)
                self.encryptTypeLabel.setText(self.infoLabel)
                self.encryptTypeLabel.setAlignment(Qt.AlignCenter)
                                
                self.encryptComboBox.addItem("Null")
                self.encryptComboBox.addItem("Ceasar")

                self.windowLayout.addRow(self.encryptTypeLabel)
                self.windowLayout.addRow(self.encryptComboBox)
                
                #encryptComboBox.textActivated.connect(self.encryptCombotBox.trackChanges)

                e2 = QLineEdit()
                e2.setValidator(QDoubleValidator(0.99,99.99,2))
                e3 = QLineEdit()
                e3.setInputMask("+99_9999_999999")

                e4 = QLineEdit()
                e4.textChanged.connect(self.textchanged)

                e5 = QLineEdit()
                e5.setEchoMode(QLineEdit.Password)

                e6 = QLineEdit("Hello PyQt5")
                e6.setReadOnly(True)
                e5.editingFinished.connect(self.enterPress)

                self.setLayout(self.windowLayout)

        def trackChanges(self):
            if encryptComboBox.currentText() == "Ceasar":
                global dialValue #ecs dee, the one liner global variable with initialization is not available. Prase Kek
                global shiftDial
                shiftDial = QDial()
                shiftDial.setSingleStep(1)
                shiftDial.setMinimum(1)
                shiftDial.setMaximum(26)
                shiftDial.setTracking(1)
                shiftDial.setNotchTarget(True)
                shiftDial.setNotchesVisible(True)
                shiftDial.setWrapping(False)

                dialValue = QLabel("0")
                dialValue.setFrameStyle(QFrame.Box | QFrame.Raised)
                
                layout.addRow(dialValue, shiftDial)
                #if shiftDial.valueChanged():
                #    dialValue = shiftDial.value()

        def textchanged(self,text):
                print("Changed: " + text)

        def enterPress(self):
                print("Enter pressed")

def window():
        app = QApplication(sys.argv)
        win = pythCrypt()
        win.show()
        sys.exit(app.exec())
    
if __name__ == "__main__":
        window()

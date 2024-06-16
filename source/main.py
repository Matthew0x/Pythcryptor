"""
# Obtaining window size
self.shiftDial.setFixedWidth(int(window.frameSize().width() * 1 / 4))
self.shiftDial.setFixedHeight(int(window.frameSize().width() * 1 / 4))
# type: ignore
"""

# Standard
import sys, os

# 3d Party
# import yaml #https://pyyaml.org/wiki/PyYAMLDocumentation

# Custom
# import (os.path.join(os.path.dirname(__file__), "ciphers", "caesar"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "ciphers"))
import caesar

# Frameworks
from PySide6 import QtGui, QtCore, QtWidgets

DEBUG = 0


def list_fonts():
    fonts = QtGui.QFontDatabase()
    with open("fonts.txt", "w") as file:
        file.write(str(fonts.families()))


"""
def changeAlignment(
    textEdit: QtWidgets.QTextEdit, textAlignment: QtCore.Qt.AlignmentFlag
):
    tempTextEdit = textEdit
    tempTextEdit.moveCursor(QtGui.QTextCursor.MoveOperation.Start)
    lastPosition = -1
    currentPosition = tempTextEdit.textCursor().position()
    while lastPosition != currentPosition:
        tempTextEdit.setAlignment(textAlignment)
        tempTextEdit.moveCursor(QtGui.QTextCursor.MoveOperation.Down)
        lastPosition = currentPosition
        currentPosition = tempTextEdit.textCursor().position()
    textEdit = tempTextEdit
    del tempTextEdit
    textEdit.moveCursor(QtGui.QTextCursor.MoveOperation.End)
"""


# MainWindow() -> set_ui()
class MainWindow(QtWidgets.QWidget):
    # Class variables (constants)
    text_title: str = "aCipher"
    text_information: str = "Version 1.0.0\n\n"
    size_window: list = [int(900), int(700)]
    size_button: list = [int(300), int(150)]
    text_selection: str = "Null"
    # color_background_dark: str = "background-color: rgba(46,33,27, 250)"
    # color_selection_background_dark: str = "selection-background-color: black;"
    # gradient_background_light: str = (
    #    "background-color: radialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.8, fx:0.5, fy:0.5, stop:0.2 rgba(162, 165, 168, 50), stop:1 rgba(221, 221, 221, 250))"
    # )
    color_background_light: str = "background-color: rgba(221, 221, 221, 250)"
    color_selection_background_light: str = "selection-background-color: lightGray;"
    color_hover_light: str = "background: lightGray;"
    radius_border: str = "border-radius: 10px;"

    def __init__(self, parent=None):
        super().__init__(parent)
        # Instance variables (objects)
        """
        self.label_theme_option = QtWidgets.QToolButton()
        self.label_theme_option.setObjectName("label_theme_option")
        self.tool_button_theme = QtWidgets.QToolBar("tool_button_theme")  # Top Right
        self.tool_button_theme.addWidget(self.label_theme_option)
        self.tool_button_theme.show()
        self.tool_button_theme.setGeometry(QtCore.QRect(220, 120, 41, 41))
        """
        self.label_spacer = QtWidgets.QLabel()  # Bottom
        self.push_button_cipher_substitution_monoalphabetic = QtWidgets.QPushButton(
            text="Monoalphabetic\nSubstitution Ciphers"
        )
        self.push_button_cipher_substitution_polyalphabetic = QtWidgets.QPushButton(
            text="Polyalphabetic\nSubstitution Ciphers"
        )
        self.push_button_encoding = QtWidgets.QPushButton(text="Encodings")
        self.push_button_hash = QtWidgets.QPushButton(text="Hash Functions")
        self.combo_box_options = QtWidgets.QComboBox()  # Will be moved
        # Window layouts
        self.vertical_layout_ui_main = QtWidgets.QVBoxLayout()
        self.horizontal_layout_ui_bar = QtWidgets.QHBoxLayout()
        self.stacked_layout_ui_container = QtWidgets.QStackedLayout()
        self.widget_ui_main = QtWidgets.QWidget()
        # self.widget_ui_main.setDirection(QtWidgets.QVBoxLayout.Direction.TopToBottom)  # Container
        self.horizontal_layout_ui_options = QtWidgets.QHBoxLayout()  # Container
        self.vertical_layout_ui_options_left = QtWidgets.QVBoxLayout()  #  Left
        self.vertical_layout_ui_options_right = QtWidgets.QVBoxLayout()  # Right
        self.setLayout(self.vertical_layout_ui_main)  # Set top level layout
        self.vertical_layout_ui_main.addLayout(self.horizontal_layout_ui_bar)
        self.vertical_layout_ui_main.addLayout(self.stacked_layout_ui_container)
        # self.horizontal_layout_ui_bar.addWidget(self.tool_button_theme)
        self.stacked_layout_ui_container.addWidget(self.widget_ui_main)
        self.widget_ui_main.setLayout(self.horizontal_layout_ui_options)
        self.horizontal_layout_ui_options.addLayout(
            self.vertical_layout_ui_options_left
        )
        self.horizontal_layout_ui_options.addLayout(
            self.vertical_layout_ui_options_right
        )
        self.vertical_layout_ui_options_left.addWidget(
            self.push_button_cipher_substitution_monoalphabetic
        )
        self.vertical_layout_ui_options_left.addWidget(
            self.push_button_cipher_substitution_polyalphabetic,
        )
        self.vertical_layout_ui_options_right.addWidget(self.push_button_encoding)
        self.vertical_layout_ui_options_right.addWidget(self.push_button_hash)
        # self.widget_ui_main.addWidget(self.combo_box_options)
        # self.widget_ui_main.addWidget(self.label_spacer)
        # Window styles
        self.setWindowTitle(self.text_title)
        policy_size = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.MinimumExpanding,
            QtWidgets.QSizePolicy.Policy.MinimumExpanding,
        )
        # policy_size.setHeightForWidth(True)
        self.setSizePolicy(policy_size)
        self.push_button_cipher_substitution_monoalphabetic.setSizePolicy(policy_size)
        self.push_button_cipher_substitution_polyalphabetic.setSizePolicy(policy_size)
        self.push_button_encoding.setSizePolicy(policy_size)
        self.push_button_hash.setSizePolicy(policy_size)
        # Runtime
        self.resize(self.size_window[0], self.size_window[1])
        self.set_ui()

    # get_stylesheet()
    def get_stylesheet(self, path: str) -> str:
        with open(path, "r") as file:
            style = file.read()
            if DEBUG == 1:
                print(style)
            return style

    # set_ui() -> get_stylesheet()
    def set_ui(self) -> None:
        # UI styles
        self.setStyleSheet(
            self.get_stylesheet("config/theme/dark/window_stylesheet.qss")
        )
        self.label_spacer.setText("\n\n")
        self.label_spacer.setFrameStyle(
            QtWidgets.QFrame.Shape.StyledPanel
            if DEBUG == 1
            else QtWidgets.QFrame.Shape.Panel | QtWidgets.QFrame.Shadow.Raised
        )
        self.label_spacer.setLineWidth(2)
        self.label_spacer.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        """
        self.tool_button_theme.setText(self.text_information)
        self.tool_button_theme.setFrameStyle(
            QtWidgets.QFrame.Shape.StyledPanel
            if DEBUG == 1
            else QtWidgets.QFrame.Shape.HLine | QtWidgets.QFrame.Shadow.Raised
        )
        self.tool_button_theme.setLineWidth(2)
        self.tool_button_theme.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        """
        self.push_button_cipher_substitution_monoalphabetic.setMinimumSize(
            self.size_button[0], self.size_button[1]
        )
        self.push_button_cipher_substitution_monoalphabetic.setMaximumSize(
            self.size_button[0] * 1.5, self.size_button[1] * 1.5
        )
        self.push_button_cipher_substitution_monoalphabetic.setStyleSheet(
            self.get_stylesheet("config/theme/dark/button_stylesheet.qss")
            + """
                QPushButton {
                    background-color: qlineargradient(x1: 2, y1: 0, x2: 0, y2: 2, stop: 0 #1CB5E0, stop: 1 #000851);
                }
            """
        )
        self.push_button_cipher_substitution_polyalphabetic.setMinimumSize(
            self.size_button[0], self.size_button[1]
        )
        self.push_button_cipher_substitution_polyalphabetic.setMaximumSize(
            self.size_button[0] * 1.5, self.size_button[1] * 1.5
        )
        self.push_button_cipher_substitution_polyalphabetic.setStyleSheet(
            self.get_stylesheet("config/theme/dark/button_stylesheet.qss")
            + """
                QPushButton {
                    background-color: qlineargradient(x1: 2, y1: 0, x2: 0, y2: 2, stop: 0 #ff702c, stop: 1 #deb700);
                }
            """
        )
        self.push_button_encoding.setMinimumSize(
            self.size_button[0], self.size_button[1]
        )
        self.push_button_encoding.setMaximumSize(
            self.size_button[0] * 1.5, self.size_button[1] * 1.5
        )
        self.push_button_encoding.setStyleSheet(
            self.get_stylesheet("config/theme/dark/button_stylesheet.qss")
            + """
                QPushButton {
                    background-color: qlineargradient(x1: 2, y1: 0, x2: 0, y2: 2, stop: 0 #d53369, stop: 1 #daae51);
                }
            """
        )
        self.push_button_hash.setMinimumSize(self.size_button[0], self.size_button[1])
        self.push_button_hash.setMaximumSize(
            self.size_button[0] * 1.5, self.size_button[1] * 1.5
        )
        self.push_button_hash.setStyleSheet(
            self.get_stylesheet("config/theme/dark/button_stylesheet.qss")
            + """
                QPushButton {
                    background-color: qlineargradient(x1: 2, y1: 0, x2: 0, y2: 2, stop: 0 #009fab, stop: 1 #cede00);
                }
            """
        )
        self.combo_box_options.setFixedWidth(200)
        self.combo_box_options.addItem("Monoalphabetic")
        self.combo_box_options.addItem("Caesar")
        self.combo_box_options.setStyleSheet(
            f"font-size: 24px;font-family: QTEurotype;"
            f"{MainWindow.color_background_light};"
            f"{MainWindow.color_selection_background_light};"
            f"{MainWindow.radius_border};"
            "QtWidgets.QComboBox::hover"
            "{"
            f"{MainWindow.color_hover_light};"
            "}"
        )
        # self.stacked_layout_ui_container.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.widget_ui_main.setContentsMargins(16, 16, 16, 16)
        self.horizontal_layout_ui_options.setSpacing(16)
        self.horizontal_layout_ui_options.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        test = str(self.combo_box_options.styleSheet())
        file = open(os.path.join(os.getcwd(), "stylesheet.css"), "w")
        file.write("Writing stylesheet: \n\n" + str(test))
        file.close()

    def get_spacer(self, width_frame, height_frame) -> QtWidgets.QLabel:
        label_spacer = QtWidgets.QLabel()
        label_spacer.setFixedWidth(width_frame)
        label_spacer.setFixedHeight(height_frame)
        label_spacer.setFrameStyle(QtWidgets.QFrame.Shape.NoFrame)
        label_spacer.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        policy_size = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        policy_size.setHorizontalStretch(0)
        policy_size.setVerticalStretch(0)
        policy_size.setHeightForWidth(label_spacer.sizePolicy().hasHeightForWidth())
        label_spacer.setSizePolicy(policy_size)
        return label_spacer

    """
    def set_option(self, option: str) -> None:
        if option != self.text_selection and option != "Null":
            if self.horizontal_layout_ui_options.rowCount() > 3:
                self.horizontal_layout_ui_options.removeRow(
                    self.horizontal_layout_ui_options.rowCount() - 1
                )
        self.text_selection = option
    """

    # handle_events() -> set_option()
    def handle_events(self, widget) -> None:
        if isinstance(widget, QtWidgets.QComboBox):
            print(
                "handle_events reports:",
                "\n\tcurrent option: ",
                widget.currentText(),
                widget.currentIndex(),
            )
            if widget.currentText() == "Monoalphabetic":
                self.set_option("Monoalphabetic")
            if widget.currentText() == "Caesar":
                self.set_option("Caesar")
                """
                global caesarWindow
                caesarWindow = Caesar(self)
                caesarWindow.shiftDial.valueChanged.connect(caesarWindow.caesarShowValue)
                caesarWindow.shiftDial.valueChanged.connect(caesarWindow.caesarShowMessage)
                caesarWindow.messageInput.textChanged.connect(caesarWindow.caesarShowMessage)

                def messageInputFormat():
                    caesarWindow.messageInput.textChanged.disconnect(messageInputFormat),
                    changeAlignment(caesarWindow.messageInput, QtCore.Qt.AlignmentFlag.AlignCenter),
                    caesarWindow.messageInput.textChanged.connect(messageInputFormat)

                caesarWindow.messageInput.textChanged.connect(messageInputFormat)
                """

    # render() -> handle_events()
    def render(self) -> None:
        self.show()
        # Need to specify receiver without arguments or use lambda as wrapper
        self.combo_box_options.currentIndexChanged.connect(
            lambda x: self.handle_events((self.combo_box_options))
        )


# Entrypoint -> MainWindow() -> render()
if __name__ == "__main__":
    sys.argv += ["--style", "Fusion"]
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.render()
    if DEBUG == 1:
        list_fonts()
    sys.exit(app.exec())

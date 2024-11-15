from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit
import sys

def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("Pascal_Triangle")
    window.setGeometry(100, 100, 600, 400)

    # Adaugam un buton
    button = QPushButton(window)
    button.setText("GENERATE")
    button.move(250, 180)

    # Adăugăm o bară de căutare (QLineEdit)
    search_bar = QLineEdit(window)
    search_bar.setPlaceholderText("Search...")
    search_bar.setGeometry(200, 100, 200, 30)

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

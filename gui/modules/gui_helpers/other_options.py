from gui.gui import Ui_MainWindow
from PySide6 import QtCore


def on_other_clicked(ui: Ui_MainWindow):
    ui.expand_other_options_button.hide()

    Ui_MainWindow.other_animation = QtCore.QPropertyAnimation(ui.other_properties_widget, b"maximumHeight")
    Ui_MainWindow.other_animation.setDuration(300)

    Ui_MainWindow.other_animation.setStartValue(0)
    Ui_MainWindow.other_animation.setEndValue(500)

    Ui_MainWindow.other_animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

    Ui_MainWindow.other_animation.start()

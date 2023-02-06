import os.path
import sys
from PySide6.QtWidgets import QCalendarWidget
from gui.gui import Ui_MainWindow
from gui.modules.initialize import styles
from gui.modules.initialize.handlers import register_handlers
from PySide6 import QtWidgets


def on_load(ui: Ui_MainWindow, MainWindow: QtWidgets.QMainWindow):
    ui.dateandtime_created_box.calendarWidget().setHorizontalHeaderFormat(
        QCalendarWidget.HorizontalHeaderFormat.NoHorizontalHeader
    )
    ui.dateandtime_created_box.calendarWidget().setVerticalHeaderFormat(
        QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader
    )
    ui.dateandtime_edited_box.calendarWidget().setHorizontalHeaderFormat(
        QCalendarWidget.HorizontalHeaderFormat.NoHorizontalHeader
    )
    ui.dateandtime_edited_box.calendarWidget().setVerticalHeaderFormat(
        QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader
    )

    if '1337' in sys.executable or '1337' in sys.argv:
        ui.centralwidget.setStyleSheet(styles.centralwidget_h4ck3r)
    else:
        ui.centralwidget.setStyleSheet(styles.centralwidget_g)

    register_handlers(ui, MainWindow)
    ui.remove_objects = list()
    ui.save_button.setEnabled(False)

    for arg in sys.argv:
        if arg.split('.')[-1] in ['docx', 'pptx', 'xlsx'] and os.path.isfile(arg):
            ui.path_to_original_box.setText(arg)
            break

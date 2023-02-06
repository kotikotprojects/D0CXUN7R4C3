from gui.gui import Ui_MainWindow
from modules.document.document_file import ExtractedDocument
from modules.document.document_properties import DocumentProps
from gui.modules.document_loader import to_gui, from_gui
from PySide6 import QtWidgets
from gui.modules.gui_helpers import other_options
from PySide6.QtWidgets import QFileDialog
from modules.time_tools import time_diff


def remobjects(ui: Ui_MainWindow):
    for obj in ui.remove_objects:
        try:
            obj.remove()
        except Exception as e:
            assert e


def register_handlers(ui: Ui_MainWindow, MainWindow: QtWidgets.QMainWindow):
    ui.path_to_original_box.textChanged.connect(
        lambda: to_gui.fill_gui(ui, DocumentProps(ExtractedDocument(ui.path_to_original_box.text())))
    )
    MainWindow.closeEvent = lambda _: (remobjects(ui))
    ui.expand_other_options_button.clicked.connect(
        lambda: other_options.on_other_clicked(ui)
    )
    ui.creator_box.textEdited.connect(
        lambda: ui.last_modified_by_box.setText(ui.creator_box.text())
    )
    ui.save_button.clicked.connect(
        lambda: from_gui.write_document(ui, ui.document)
    )
    ui.open_document_button.clicked.connect(
        lambda: ui.path_to_original_box.setText(
            QFileDialog.getOpenFileName(None, caption='Choose file to edit')[0]
        )
    )

    ui.dateandtime_created_box.dateTimeChanged.connect(
        lambda: ui.custom_edit_time_box.setValue(time_diff.compute_time_diff(
            ui.dateandtime_created_box.date().toPython(), ui.dateandtime_created_box.time().toPython(),
            ui.dateandtime_edited_box.date().toPython(), ui.dateandtime_edited_box.time().toPython()
        ))
    )
    ui.dateandtime_edited_box.dateTimeChanged.connect(
        lambda: ui.custom_edit_time_box.setValue(time_diff.compute_time_diff(
            ui.dateandtime_created_box.date().toPython(), ui.dateandtime_created_box.time().toPython(),
            ui.dateandtime_edited_box.date().toPython(), ui.dateandtime_edited_box.time().toPython()
        ))
    )

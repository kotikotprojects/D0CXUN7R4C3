from PySide6 import QtCore
from gui.gui import Ui_MainWindow
from modules.document.document_properties import DocumentProps


def fill_gui(ui: Ui_MainWindow, document_props: DocumentProps):
    if not document_props.parsed_:
        return

    ui.remove_objects.append(document_props.extracted_document)

    ui.save_to_box.setText(ui.path_to_original_box.text())

    ui.creator_box.setText(document_props.creator)
    ui.last_modified_by_box.setText(document_props.last_modified_by)

    ui.dateandtime_created_box.setDateTime(
        QtCore.QDateTime(QtCore.QDate(document_props.created.date()), QtCore.QTime(document_props.created.time()))
    )
    ui.dateandtime_edited_box.setDateTime(
        QtCore.QDateTime(QtCore.QDate(document_props.modified.date()), QtCore.QTime(document_props.modified.time()))
    )

    ui.revision_box.setText(document_props.revision)
    ui.template_box.setText(document_props.template)
    ui.pages_box.setValue(document_props.pages)
    ui.words_box.setValue(document_props.words)
    ui.symbols_box.setValue(document_props.characters)
    ui.lines_box.setValue(document_props.lines)
    ui.paragraphs_box.setValue(document_props.paragraphs)
    ui.application_name_box.setText(document_props.application)
    ui.custom_edit_time_box.setValue(document_props.total_time)

    ui.document = document_props
    ui.save_button.setEnabled(True)

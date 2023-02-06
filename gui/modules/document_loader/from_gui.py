import time
from gui.gui import Ui_MainWindow
from modules.document.document_properties import DocumentProps
from modules.helpers import xml
import datetime
from ezzthread import threaded


@threaded
def update_button(ui: Ui_MainWindow):
    ui.save_button.setText('Success')
    time.sleep(3)
    ui.save_button.setText('Save')


def write_document(ui: Ui_MainWindow, document_props: DocumentProps):
    if not document_props.parsed_:
        return

    xml.set_value(document_props.app_xml, '//Application', ui.application_name_box.text())
    xml.set_value(document_props.app_xml, '//Paragraphs', ui.paragraphs_box.value())
    xml.set_value(document_props.app_xml, '//Lines', ui.lines_box.value())
    xml.set_value(document_props.app_xml, '//Characters', ui.symbols_box.value())
    xml.set_value(document_props.app_xml, '//Words', ui.words_box.value())
    xml.set_value(document_props.app_xml, '//Pages', ui.pages_box.value())
    xml.set_value(document_props.app_xml, '//TotalTime', ui.custom_edit_time_box.value())
    xml.set_value(document_props.app_xml, '//Template', ui.template_box.text())
    xml.set_value(
        document_props.core_xml, 'dcterms:modified',
        datetime.datetime.combine(ui.dateandtime_edited_box.date().toPython(),
                                  ui.dateandtime_edited_box.time().toPython()
                                  ).strftime('%Y-%m-%dT%H:%M:%SZ')
    )
    xml.set_value(
        document_props.core_xml, 'dcterms:created',
        datetime.datetime.combine(ui.dateandtime_created_box.date().toPython(),
                                  ui.dateandtime_created_box.time().toPython()
                                  ).strftime('%Y-%m-%dT%H:%M:%SZ')
    )
    xml.set_value(document_props.core_xml, 'cp:revision', ui.revision_box.text())
    xml.set_value(document_props.core_xml, 'cp:lastModifiedBy', ui.last_modified_by_box.text())
    xml.set_value(document_props.core_xml, 'dc:creator', ui.creator_box.text())

    document_props.core_xml.write(document_props.extracted_document.core)
    document_props.app_xml.write(document_props.extracted_document.app)

    document_props.extracted_document.pack(ui.save_to_box.text())

    update_button(ui)

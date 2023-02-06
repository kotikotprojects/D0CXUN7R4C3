import os.path
import lxml
from lxml import etree
from modules.document.document_file import ExtractedDocument
from modules.helpers import xml
from modules.helpers.convert import Int
from datetime import datetime


class DocumentProps:
    def __init__(self, extracted_document: ExtractedDocument):
        if not extracted_document.documentroot or not os.path.isdir(extracted_document.documentroot):
            self.parsed_ = False
            return

        self.parsed_ = True

        core_xml = etree.parse(extracted_document.core)
        app_xml = etree.parse(extracted_document.app)

        self.extracted_document = extracted_document
        self.application = xml.get_value(app_xml, '//Application')
        self.paragraphs = Int(xml.get_value(app_xml, '//Paragraphs'))
        self.lines = Int(xml.get_value(app_xml, '//Lines'))
        self.characters = Int(xml.get_value(app_xml, '//Characters'))
        self.words = Int(xml.get_value(app_xml, '//Words'))
        self.pages = Int(xml.get_value(app_xml, '//Pages'))
        self.total_time = Int(xml.get_value(app_xml, '//TotalTime'))
        self.template = xml.get_value(app_xml, '//Template')
        self.modified = datetime.strptime(xml.get_value(core_xml, 'dcterms:modified'), '%Y-%m-%dT%H:%M:%SZ')
        self.created = datetime.strptime(xml.get_value(core_xml, 'dcterms:created'), '%Y-%m-%dT%H:%M:%SZ')
        self.revision = xml.get_value(core_xml, 'cp:revision')
        self.last_modified_by = xml.get_value(core_xml, 'cp:lastModifiedBy')
        self.creator = xml.get_value(core_xml, 'dc:creator')
        self.core_xml = core_xml
        self.app_xml = app_xml

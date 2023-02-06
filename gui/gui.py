# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from  . import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 570)
        icon = QIcon()
        icon.addFile(u":/img/img/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.docxuntracelabel = QLabel(self.centralwidget)
        self.docxuntracelabel.setObjectName(u"docxuntracelabel")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.docxuntracelabel.sizePolicy().hasHeightForWidth())
        self.docxuntracelabel.setSizePolicy(sizePolicy)
        self.docxuntracelabel.setStyleSheet(u"font: 87 30pt \"Segoe UI Black\";")
        self.docxuntracelabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.docxuntracelabel)

        self.line_name_top_openfile = QFrame(self.centralwidget)
        self.line_name_top_openfile.setObjectName(u"line_name_top_openfile")
        self.line_name_top_openfile.setFrameShape(QFrame.HLine)
        self.line_name_top_openfile.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_name_top_openfile)

        self.path_to_original_widget = QWidget(self.centralwidget)
        self.path_to_original_widget.setObjectName(u"path_to_original_widget")
        self.horizontalLayout = QHBoxLayout(self.path_to_original_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.path_to_original_box = QLineEdit(self.path_to_original_widget)
        self.path_to_original_box.setObjectName(u"path_to_original_box")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.path_to_original_box.sizePolicy().hasHeightForWidth())
        self.path_to_original_box.setSizePolicy(sizePolicy1)
        self.path_to_original_box.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.path_to_original_box)

        self.open_document_button = QPushButton(self.path_to_original_widget)
        self.open_document_button.setObjectName(u"open_document_button")
        self.open_document_button.setMinimumSize(QSize(80, 30))

        self.horizontalLayout.addWidget(self.open_document_button)


        self.verticalLayout.addWidget(self.path_to_original_widget)

        self.line_openfile_authors = QFrame(self.centralwidget)
        self.line_openfile_authors.setObjectName(u"line_openfile_authors")
        self.line_openfile_authors.setFrameShape(QFrame.HLine)
        self.line_openfile_authors.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_openfile_authors)

        self.authors_widget = QWidget(self.centralwidget)
        self.authors_widget.setObjectName(u"authors_widget")
        self.verticalLayout_2 = QVBoxLayout(self.authors_widget)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.authors_label = QLabel(self.authors_widget)
        self.authors_label.setObjectName(u"authors_label")

        self.verticalLayout_2.addWidget(self.authors_label)

        self.creator_label = QLabel(self.authors_widget)
        self.creator_label.setObjectName(u"creator_label")

        self.verticalLayout_2.addWidget(self.creator_label)

        self.creator_box = QLineEdit(self.authors_widget)
        self.creator_box.setObjectName(u"creator_box")
        self.creator_box.setMinimumSize(QSize(0, 30))

        self.verticalLayout_2.addWidget(self.creator_box)

        self.last_modified_by_label = QLabel(self.authors_widget)
        self.last_modified_by_label.setObjectName(u"last_modified_by_label")

        self.verticalLayout_2.addWidget(self.last_modified_by_label)

        self.last_modified_by_box = QLineEdit(self.authors_widget)
        self.last_modified_by_box.setObjectName(u"last_modified_by_box")
        self.last_modified_by_box.setMinimumSize(QSize(0, 30))

        self.verticalLayout_2.addWidget(self.last_modified_by_box)


        self.verticalLayout.addWidget(self.authors_widget)

        self.line_authors_datetime = QFrame(self.centralwidget)
        self.line_authors_datetime.setObjectName(u"line_authors_datetime")
        self.line_authors_datetime.setFrameShape(QFrame.HLine)
        self.line_authors_datetime.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_authors_datetime)

        self.date_edit_widget = QWidget(self.centralwidget)
        self.date_edit_widget.setObjectName(u"date_edit_widget")
        self.verticalLayout_3 = QVBoxLayout(self.date_edit_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.dateandtime_label = QLabel(self.date_edit_widget)
        self.dateandtime_label.setObjectName(u"dateandtime_label")

        self.verticalLayout_3.addWidget(self.dateandtime_label)

        self.dateandtime_created_label = QLabel(self.date_edit_widget)
        self.dateandtime_created_label.setObjectName(u"dateandtime_created_label")

        self.verticalLayout_3.addWidget(self.dateandtime_created_label)

        self.dateandtime_created_box = QDateTimeEdit(self.date_edit_widget)
        self.dateandtime_created_box.setObjectName(u"dateandtime_created_box")
        self.dateandtime_created_box.setMinimumSize(QSize(0, 30))
        self.dateandtime_created_box.setCalendarPopup(True)

        self.verticalLayout_3.addWidget(self.dateandtime_created_box)

        self.dateandtime_edited_label = QLabel(self.date_edit_widget)
        self.dateandtime_edited_label.setObjectName(u"dateandtime_edited_label")

        self.verticalLayout_3.addWidget(self.dateandtime_edited_label)

        self.dateandtime_edited_box = QDateTimeEdit(self.date_edit_widget)
        self.dateandtime_edited_box.setObjectName(u"dateandtime_edited_box")
        self.dateandtime_edited_box.setMinimumSize(QSize(0, 30))
        self.dateandtime_edited_box.setCalendarPopup(True)

        self.verticalLayout_3.addWidget(self.dateandtime_edited_box)


        self.verticalLayout.addWidget(self.date_edit_widget)

        self.line_datetime_other = QFrame(self.centralwidget)
        self.line_datetime_other.setObjectName(u"line_datetime_other")
        self.line_datetime_other.setFrameShape(QFrame.HLine)
        self.line_datetime_other.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_datetime_other)

        self.other_properties_widget = QWidget(self.centralwidget)
        self.other_properties_widget.setObjectName(u"other_properties_widget")
        self.other_properties_widget.setMaximumSize(QSize(16777215, 0))
        self.verticalLayout_4 = QVBoxLayout(self.other_properties_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.other_label = QLabel(self.other_properties_widget)
        self.other_label.setObjectName(u"other_label")

        self.verticalLayout_4.addWidget(self.other_label)

        self.revision_label = QLabel(self.other_properties_widget)
        self.revision_label.setObjectName(u"revision_label")

        self.verticalLayout_4.addWidget(self.revision_label)

        self.revision_box = QLineEdit(self.other_properties_widget)
        self.revision_box.setObjectName(u"revision_box")
        self.revision_box.setMinimumSize(QSize(0, 30))

        self.verticalLayout_4.addWidget(self.revision_box)

        self.template_label = QLabel(self.other_properties_widget)
        self.template_label.setObjectName(u"template_label")

        self.verticalLayout_4.addWidget(self.template_label)

        self.template_box = QLineEdit(self.other_properties_widget)
        self.template_box.setObjectName(u"template_box")
        self.template_box.setMinimumSize(QSize(0, 30))

        self.verticalLayout_4.addWidget(self.template_box)

        self.pages_words_symbols_label = QLabel(self.other_properties_widget)
        self.pages_words_symbols_label.setObjectName(u"pages_words_symbols_label")

        self.verticalLayout_4.addWidget(self.pages_words_symbols_label)

        self.pages_words_symbols_widget = QWidget(self.other_properties_widget)
        self.pages_words_symbols_widget.setObjectName(u"pages_words_symbols_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.pages_words_symbols_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pages_box = QSpinBox(self.pages_words_symbols_widget)
        self.pages_box.setObjectName(u"pages_box")

        self.horizontalLayout_2.addWidget(self.pages_box)

        self.words_box = QSpinBox(self.pages_words_symbols_widget)
        self.words_box.setObjectName(u"words_box")

        self.horizontalLayout_2.addWidget(self.words_box)

        self.symbols_box = QSpinBox(self.pages_words_symbols_widget)
        self.symbols_box.setObjectName(u"symbols_box")

        self.horizontalLayout_2.addWidget(self.symbols_box)

        self.lines_box = QSpinBox(self.pages_words_symbols_widget)
        self.lines_box.setObjectName(u"lines_box")

        self.horizontalLayout_2.addWidget(self.lines_box)

        self.paragraphs_box = QSpinBox(self.pages_words_symbols_widget)
        self.paragraphs_box.setObjectName(u"paragraphs_box")

        self.horizontalLayout_2.addWidget(self.paragraphs_box)


        self.verticalLayout_4.addWidget(self.pages_words_symbols_widget)

        self.application_name_label = QLabel(self.other_properties_widget)
        self.application_name_label.setObjectName(u"application_name_label")

        self.verticalLayout_4.addWidget(self.application_name_label)

        self.application_name_box = QLineEdit(self.other_properties_widget)
        self.application_name_box.setObjectName(u"application_name_box")
        self.application_name_box.setMinimumSize(QSize(0, 30))

        self.verticalLayout_4.addWidget(self.application_name_box)

        self.custom_edit_time_label = QLabel(self.other_properties_widget)
        self.custom_edit_time_label.setObjectName(u"custom_edit_time_label")

        self.verticalLayout_4.addWidget(self.custom_edit_time_label)

        self.custom_edit_time_box = QSpinBox(self.other_properties_widget)
        self.custom_edit_time_box.setObjectName(u"custom_edit_time_box")
        self.custom_edit_time_box.setMinimumSize(QSize(0, 30))
        self.custom_edit_time_box.setMinimum(-2147483647)
        self.custom_edit_time_box.setMaximum(2147483647)

        self.verticalLayout_4.addWidget(self.custom_edit_time_box)


        self.verticalLayout.addWidget(self.other_properties_widget)

        self.expand_other_options_button = QPushButton(self.centralwidget)
        self.expand_other_options_button.setObjectName(u"expand_other_options_button")
        self.expand_other_options_button.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.expand_other_options_button)

        self.spacer_content_to_save = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.spacer_content_to_save)

        self.line_options_save = QFrame(self.centralwidget)
        self.line_options_save.setObjectName(u"line_options_save")
        self.line_options_save.setFrameShape(QFrame.HLine)
        self.line_options_save.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_options_save)

        self.save_to_label = QLabel(self.centralwidget)
        self.save_to_label.setObjectName(u"save_to_label")

        self.verticalLayout.addWidget(self.save_to_label)

        self.save_to_box = QLineEdit(self.centralwidget)
        self.save_to_box.setObjectName(u"save_to_box")
        self.save_to_box.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.save_to_box)

        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setMinimumSize(QSize(0, 50))
        self.save_button.setStyleSheet(u"font: 20pt \"Segoe UI Black\";")

        self.verticalLayout.addWidget(self.save_button)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"D0CXUN7R4C3", None))
        self.docxuntracelabel.setText(QCoreApplication.translate("MainWindow", u"D0CXUN7R4C3", None))
        self.path_to_original_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Path to document", None))
        self.open_document_button.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.authors_label.setText(QCoreApplication.translate("MainWindow", u"Authors", None))
        self.creator_label.setText(QCoreApplication.translate("MainWindow", u"Creator", None))
        self.creator_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"BarsTiger", None))
        self.last_modified_by_label.setText(QCoreApplication.translate("MainWindow", u"Last modified by", None))
        self.last_modified_by_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"BarsTiger", None))
        self.dateandtime_label.setText(QCoreApplication.translate("MainWindow", u"Date and time (in global time)", None))
        self.dateandtime_created_label.setText(QCoreApplication.translate("MainWindow", u"Created", None))
        self.dateandtime_edited_label.setText(QCoreApplication.translate("MainWindow", u"Last edited", None))
        self.other_label.setText(QCoreApplication.translate("MainWindow", u"Other", None))
        self.revision_label.setText(QCoreApplication.translate("MainWindow", u"Revision", None))
        self.revision_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.template_label.setText(QCoreApplication.translate("MainWindow", u"Template", None))
        self.template_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Normal.dotm", None))
        self.pages_words_symbols_label.setText(QCoreApplication.translate("MainWindow", u"Pages - Words - Symbols - Lines - Paragraphs", None))
        self.application_name_label.setText(QCoreApplication.translate("MainWindow", u"Application", None))
        self.application_name_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Microsoft Office Word", None))
        self.custom_edit_time_label.setText(QCoreApplication.translate("MainWindow", u"Custom edit time (min)", None))
        self.expand_other_options_button.setText(QCoreApplication.translate("MainWindow", u"Other options", None))
        self.save_to_label.setText(QCoreApplication.translate("MainWindow", u"Save to", None))
        self.save_to_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Path to new document", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi


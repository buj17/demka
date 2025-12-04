# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'order_list_manager_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            )
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout, QLabel,
                               QPushButton, QScrollArea, QVBoxLayout,
                               QWidget, )


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(810, 714)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.logout_button = QPushButton(Form)
        self.logout_button.setObjectName(u"logout_button")

        self.horizontalLayout_2.addWidget(self.logout_button)

        self.full_name_label = QLabel(Form)
        self.full_name_label.setObjectName(u"full_name_label")

        self.horizontalLayout_2.addWidget(self.full_name_label)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.orders_scroll_area = QScrollArea(Form)
        self.orders_scroll_area.setObjectName(u"orders_scroll_area")
        self.orders_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(
            u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setEnabled(True)
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 784, 642))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.order_cards_layout = QVBoxLayout()
        self.order_cards_layout.setObjectName(u"order_cards_layout")

        self.verticalLayout_4.addLayout(self.order_cards_layout)

        self.orders_scroll_area.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout.addWidget(self.orders_scroll_area)

        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.logout_button.setText(QCoreApplication.translate("Form",
                                                              u"\u0412\u044b\u0445\u043e\u0434",
                                                              None))
        self.full_name_label.setText(QCoreApplication.translate("Form",
                                                                u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f \u0418\u043c\u044f \u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e",
                                                                None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item_list_administrator_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            )
from PySide6.QtWidgets import (QComboBox, QGridLayout,
                               QHBoxLayout,
                               QLabel, QLineEdit, QPushButton, QScrollArea,
                               QSizePolicy, QVBoxLayout, QWidget, )


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
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.search_suppliers_combo_box = QComboBox(Form)
        self.search_suppliers_combo_box.setObjectName(
            u"search_suppliers_combo_box")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding,
                                 QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.search_suppliers_combo_box.sizePolicy().hasHeightForWidth())
        self.search_suppliers_combo_box.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.search_suppliers_combo_box)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_8.addWidget(self.label_3)

        self.sort_by_stock_quantity_combo_box = QComboBox(Form)
        self.sort_by_stock_quantity_combo_box.addItem("")
        self.sort_by_stock_quantity_combo_box.addItem("")
        self.sort_by_stock_quantity_combo_box.setObjectName(
            u"sort_by_stock_quantity_combo_box")
        sizePolicy.setHeightForWidth(
            self.sort_by_stock_quantity_combo_box.sizePolicy().hasHeightForWidth())
        self.sort_by_stock_quantity_combo_box.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(
            self.sort_by_stock_quantity_combo_box)

        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.search_items_line_edit = QLineEdit(Form)
        self.search_items_line_edit.setObjectName(u"search_items_line_edit")

        self.horizontalLayout.addWidget(self.search_items_line_edit)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.items_scroll_area = QScrollArea(Form)
        self.items_scroll_area.setObjectName(u"items_scroll_area")
        self.items_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(
            u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setEnabled(True)
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 784, 519))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.item_cards_layout = QVBoxLayout()
        self.item_cards_layout.setObjectName(u"item_cards_layout")

        self.verticalLayout_4.addLayout(self.item_cards_layout)

        self.items_scroll_area.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout.addWidget(self.items_scroll_area)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.go_to_orders_button = QPushButton(Form)
        self.go_to_orders_button.setObjectName(u"go_to_orders_button")

        self.horizontalLayout_4.addWidget(self.go_to_orders_button)

        self.add_item_button = QPushButton(Form)
        self.add_item_button.setObjectName(u"add_item_button")

        self.horizontalLayout_4.addWidget(self.add_item_button)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

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
        self.label_2.setText(QCoreApplication.translate("Form",
                                                        u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a:",
                                                        None))
        self.label_3.setText(QCoreApplication.translate("Form",
                                                        u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430 \u043f\u043e \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0443 \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435",
                                                        None))
        self.sort_by_stock_quantity_combo_box.setItemText(0,
                                                          QCoreApplication.translate(
                                                              "Form",
                                                              u"\u041f\u043e \u0432\u043e\u0437\u0440\u0430\u0441\u0442\u0430\u043d\u0438\u044e",
                                                              None))
        self.sort_by_stock_quantity_combo_box.setItemText(1,
                                                          QCoreApplication.translate(
                                                              "Form",
                                                              u"\u041f\u043e \u0443\u0431\u044b\u0432\u0430\u043d\u0438\u044e",
                                                              None))

        self.label.setText(QCoreApplication.translate("Form",
                                                      u"\u0418\u0441\u043a\u0430\u0442\u044c:",
                                                      None))
        self.go_to_orders_button.setText(QCoreApplication.translate("Form",
                                                                    u"\u041f\u0435\u0440\u0435\u0439\u0442\u0438 \u043a \u0437\u0430\u043a\u0430\u0437\u0430\u043c",
                                                                    None))
        self.add_item_button.setText(QCoreApplication.translate("Form",
                                                                u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u043e\u0432\u0430\u0440",
                                                                None))
    # retranslateUi

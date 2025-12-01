# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item_card_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, )
from PySide6.QtGui import (QPixmap, )
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QSizePolicy,
                               QVBoxLayout, )


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(616, 180)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.item_image_label = QLabel(Form)
        self.item_image_label.setObjectName(u"item_image_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed,
                                 QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.item_image_label.sizePolicy().hasHeightForWidth())
        self.item_image_label.setSizePolicy(sizePolicy)
        self.item_image_label.setPixmap(QPixmap(u"../../../media/picture.png"))

        self.horizontalLayout.addWidget(self.item_image_label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.item_category_name_label = QLabel(Form)
        self.item_category_name_label.setObjectName(
            u"item_category_name_label")

        self.verticalLayout.addWidget(self.item_category_name_label)

        self.item_description_label = QLabel(Form)
        self.item_description_label.setObjectName(u"item_description_label")
        self.item_description_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.item_description_label)

        self.item_producer_label = QLabel(Form)
        self.item_producer_label.setObjectName(u"item_producer_label")

        self.verticalLayout.addWidget(self.item_producer_label)

        self.item_supplier_label = QLabel(Form)
        self.item_supplier_label.setObjectName(u"item_supplier_label")

        self.verticalLayout.addWidget(self.item_supplier_label)

        self.item_price_label = QLabel(Form)
        self.item_price_label.setObjectName(u"item_price_label")

        self.verticalLayout.addWidget(self.item_price_label)

        self.item_measure_label = QLabel(Form)
        self.item_measure_label.setObjectName(u"item_measure_label")

        self.verticalLayout.addWidget(self.item_measure_label)

        self.item_stock_quantity_label = QLabel(Form)
        self.item_stock_quantity_label.setObjectName(
            u"item_stock_quantity_label")

        self.verticalLayout.addWidget(self.item_stock_quantity_label)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.item_current_discount_label = QLabel(Form)
        self.item_current_discount_label.setObjectName(
            u"item_current_discount_label")

        self.horizontalLayout.addWidget(self.item_current_discount_label)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.item_image_label.setText("")
        self.item_category_name_label.setText(
            QCoreApplication.translate("Form",
                                       u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0442\u043e\u0432\u0430\u0440\u0430 | \u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430",
                                       None))
        self.item_description_label.setText(QCoreApplication.translate("Form",
                                                                       u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430",
                                                                       None))
        self.item_producer_label.setText(QCoreApplication.translate("Form",
                                                                    u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c",
                                                                    None))
        self.item_supplier_label.setText(QCoreApplication.translate("Form",
                                                                    u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a",
                                                                    None))
        self.item_price_label.setText(
            QCoreApplication.translate("Form", u"\u0426\u0435\u043d\u0430",
                                       None))
        self.item_measure_label.setText(QCoreApplication.translate("Form",
                                                                   u"\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f",
                                                                   None))
        self.item_stock_quantity_label.setText(
            QCoreApplication.translate("Form",
                                       u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435",
                                       None))
        self.item_current_discount_label.setText(
            QCoreApplication.translate("Form",
                                       u"\u0414\u0435\u0439\u0441\u0442\u0432\u0443\u044e\u0449\u0430\u044f \u0441\u043a\u0438\u0434\u043a\u0430",
                                       None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item_add_form_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt, )
from PySide6.QtGui import (QPixmap, )
from PySide6.QtWidgets import (QComboBox, QDoubleSpinBox,
                               QHBoxLayout,
                               QLabel, QLineEdit, QPlainTextEdit, QPushButton,
                               QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
                               )


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed,
                                 QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum,
                                  QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.item_image_label = QLabel(Form)
        self.item_image_label.setObjectName(u"item_image_label")
        self.item_image_label.setPixmap(QPixmap(u"../../../media/picture.png\n"
                                                "                                        "))
        self.item_image_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.item_image_label)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.item_upload_photo_button = QPushButton(Form)
        self.item_upload_photo_button.setObjectName(
            u"item_upload_photo_button")

        self.horizontalLayout_12.addWidget(self.item_upload_photo_button)

        self.horizontalSpacer = QSpacerItem(40, 20,
                                            QSizePolicy.Policy.Expanding,
                                            QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer)

        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.item_name_line_edit = QLineEdit(Form)
        self.item_name_line_edit.setObjectName(u"item_name_line_edit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding,
                                  QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.item_name_line_edit.sizePolicy().hasHeightForWidth())
        self.item_name_line_edit.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.item_name_line_edit)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.item_category_combo_box = QComboBox(Form)
        self.item_category_combo_box.setObjectName(u"item_category_combo_box")
        sizePolicy2.setHeightForWidth(
            self.item_category_combo_box.sizePolicy().hasHeightForWidth())
        self.item_category_combo_box.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.item_category_combo_box)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.item_description_plain_text_edit = QPlainTextEdit(Form)
        self.item_description_plain_text_edit.setObjectName(
            u"item_description_plain_text_edit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding,
                                  QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.item_description_plain_text_edit.sizePolicy().hasHeightForWidth())
        self.item_description_plain_text_edit.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(
            self.item_description_plain_text_edit)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.item_producer_combo_box = QComboBox(Form)
        self.item_producer_combo_box.setObjectName(u"item_producer_combo_box")
        sizePolicy2.setHeightForWidth(
            self.item_producer_combo_box.sizePolicy().hasHeightForWidth())
        self.item_producer_combo_box.setSizePolicy(sizePolicy2)

        self.horizontalLayout_6.addWidget(self.item_producer_combo_box)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.item_supplier_line_edit = QLineEdit(Form)
        self.item_supplier_line_edit.setObjectName(u"item_supplier_line_edit")

        self.horizontalLayout_7.addWidget(self.item_supplier_line_edit)

        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.item_price_double_spin_box = QDoubleSpinBox(Form)
        self.item_price_double_spin_box.setObjectName(
            u"item_price_double_spin_box")
        sizePolicy2.setHeightForWidth(
            self.item_price_double_spin_box.sizePolicy().hasHeightForWidth())
        self.item_price_double_spin_box.setSizePolicy(sizePolicy2)
        self.item_price_double_spin_box.setMaximum(100000000.000000000000000)
        self.item_price_double_spin_box.setValue(0.000000000000000)

        self.horizontalLayout_8.addWidget(self.item_price_double_spin_box)

        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.item_measure_line_edit = QLineEdit(Form)
        self.item_measure_line_edit.setObjectName(u"item_measure_line_edit")

        self.horizontalLayout_9.addWidget(self.item_measure_line_edit)

        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_10.addWidget(self.label_9)

        self.item_stock_quantity_spin_box = QSpinBox(Form)
        self.item_stock_quantity_spin_box.setObjectName(
            u"item_stock_quantity_spin_box")
        sizePolicy2.setHeightForWidth(
            self.item_stock_quantity_spin_box.sizePolicy().hasHeightForWidth())
        self.item_stock_quantity_spin_box.setSizePolicy(sizePolicy2)
        self.item_stock_quantity_spin_box.setMaximum(100000000)

        self.horizontalLayout_10.addWidget(self.item_stock_quantity_spin_box)

        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_11.addWidget(self.label_10)

        self.item_current_discount_spin_box = QSpinBox(Form)
        self.item_current_discount_spin_box.setObjectName(
            u"item_current_discount_spin_box")
        sizePolicy2.setHeightForWidth(
            self.item_current_discount_spin_box.sizePolicy().hasHeightForWidth())
        self.item_current_discount_spin_box.setSizePolicy(sizePolicy2)
        self.item_current_discount_spin_box.setMaximum(100)

        self.horizontalLayout_11.addWidget(self.item_current_discount_spin_box)

        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.submit_button = QPushButton(Form)
        self.submit_button.setObjectName(u"submit_button")

        self.horizontalLayout_13.addWidget(self.submit_button)

        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form",
                                                      u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435",
                                                      None))
        self.item_image_label.setText("")
        self.item_upload_photo_button.setText(
            QCoreApplication.translate("Form",
                                       u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435",
                                       None))
        self.label_2.setText(QCoreApplication.translate("Form",
                                                        u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430",
                                                        None))
        self.label_3.setText(QCoreApplication.translate("Form",
                                                        u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0442\u043e\u0432\u0430\u0440\u0430",
                                                        None))
        self.label_4.setText(QCoreApplication.translate("Form",
                                                        u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430",
                                                        None))
        self.item_description_plain_text_edit.setPlainText("")
        self.label_5.setText(QCoreApplication.translate("Form",
                                                        u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c",
                                                        None))
        self.label_6.setText(QCoreApplication.translate("Form",
                                                        u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a",
                                                        None))
        self.label_7.setText(
            QCoreApplication.translate("Form", u"\u0426\u0435\u043d\u0430",
                                       None))
        self.label_8.setText(QCoreApplication.translate("Form",
                                                        u"\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f",
                                                        None))
        self.label_9.setText(QCoreApplication.translate("Form",
                                                        u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435",
                                                        None))
        self.label_10.setText(QCoreApplication.translate("Form",
                                                         u"\u0414\u0435\u0439\u0441\u0442\u0432\u0443\u044e\u0449\u0430\u044f \u0441\u043a\u0438\u0434\u043a\u0430",
                                                         None))
        self.submit_button.setText(QCoreApplication.translate("Form",
                                                              u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c",
                                                              None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'order_add_form_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt, )
from PySide6.QtWidgets import (QComboBox, QDateEdit, QHBoxLayout,
                               QLabel, QLineEdit, QPushButton, QSizePolicy,
                               QVBoxLayout, )


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(285, 301)
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

        self.order_article_line_edit = QLineEdit(Form)
        self.order_article_line_edit.setObjectName(u"order_article_line_edit")

        self.horizontalLayout.addWidget(self.order_article_line_edit)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.order_status_combo_box = QComboBox(Form)
        self.order_status_combo_box.addItem("")
        self.order_status_combo_box.addItem("")
        self.order_status_combo_box.setObjectName(u"order_status_combo_box")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding,
                                  QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.order_status_combo_box.sizePolicy().hasHeightForWidth())
        self.order_status_combo_box.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.order_status_combo_box)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.order_pickup_point_combo_box = QComboBox(Form)
        self.order_pickup_point_combo_box.setObjectName(
            u"order_pickup_point_combo_box")
        sizePolicy2.setHeightForWidth(
            self.order_pickup_point_combo_box.sizePolicy().hasHeightForWidth())
        self.order_pickup_point_combo_box.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.order_pickup_point_combo_box)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.order_date_edit = QDateEdit(Form)
        self.order_date_edit.setObjectName(u"order_date_edit")

        self.horizontalLayout_5.addWidget(self.order_date_edit)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.deliver_date_edit = QDateEdit(Form)
        self.deliver_date_edit.setObjectName(u"deliver_date_edit")

        self.horizontalLayout_6.addWidget(self.deliver_date_edit)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

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
                                                      u"\u0410\u0440\u0442\u0438\u043a\u0443\u043b",
                                                      None))
        self.label_2.setText(QCoreApplication.translate("Form",
                                                        u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0437\u0430\u043a\u0430\u0437\u0430",
                                                        None))
        self.order_status_combo_box.setItemText(0, QCoreApplication.translate(
            "Form", u"\u041d\u043e\u0432\u044b\u0439", None))
        self.order_status_combo_box.setItemText(1, QCoreApplication.translate(
            "Form", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0435\u043d", None))

        self.label_3.setText(QCoreApplication.translate("Form",
                                                        u"\u0410\u0434\u0440\u0435\u0441 \u043f\u0443\u043d\u043a\u0442\u0430 \u0432\u044b\u0434\u0430\u0447\u0438",
                                                        None))
        self.label_4.setText(QCoreApplication.translate("Form",
                                                        u"\u0414\u0430\u0442\u0430 \u0437\u0430\u043a\u0430\u0437\u0430",
                                                        None))
        self.label_5.setText(QCoreApplication.translate("Form",
                                                        u"\u0414\u0430\u0442\u0430 \u0432\u044b\u0434\u0430\u0447\u0438",
                                                        None))
        self.submit_button.setText(QCoreApplication.translate("Form",
                                                              u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c",
                                                              None))
    # retranslateUi

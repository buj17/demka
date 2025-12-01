# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, )
from PySide6.QtWidgets import (QFormLayout, QGridLayout, QLabel,
                               QLineEdit, QPushButton, )


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(381, 253)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.login_label = QLabel(Form)
        self.login_label.setObjectName(u"login_label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole,
                                  self.login_label)

        self.login_line_edit = QLineEdit(Form)
        self.login_line_edit.setObjectName(u"login_line_edit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole,
                                  self.login_line_edit)

        self.password_label = QLabel(Form)
        self.password_label.setObjectName(u"password_label")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole,
                                  self.password_label)

        self.password_line_Edit = QLineEdit(Form)
        self.password_line_Edit.setObjectName(u"password_line_Edit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole,
                                  self.password_line_Edit)

        self.login_button = QPushButton(Form)
        self.login_button.setObjectName(u"login_button")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole,
                                  self.login_button)

        self.login_as_guest_button = QPushButton(Form)
        self.login_as_guest_button.setObjectName(u"login_as_guest_button")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole,
                                  self.login_as_guest_button)

        self.gridLayout.addLayout(self.formLayout, 1, 1, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.login_label.setText(QCoreApplication.translate("Form",
                                                            u"\u041b\u043e\u0433\u0438\u043d",
                                                            None))
        self.password_label.setText(QCoreApplication.translate("Form",
                                                               u"\u041f\u0430\u0440\u043e\u043b\u044c",
                                                               None))
        self.login_button.setText(QCoreApplication.translate("Form",
                                                             u"\u0412\u043e\u0439\u0442\u0438",
                                                             None))
        self.login_as_guest_button.setText(QCoreApplication.translate("Form",
                                                                      u"\u0412\u043e\u0439\u0442\u0438 \u043a\u0430\u043a \u0433\u043e\u0441\u0442\u044c",
                                                                      None))
    # retranslateUi

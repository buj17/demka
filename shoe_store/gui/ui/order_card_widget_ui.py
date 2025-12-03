# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'order_card_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt, )
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QVBoxLayout, )


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(616, 212)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.order_article_label = QLabel(Form)
        self.order_article_label.setObjectName(u"order_article_label")

        self.verticalLayout.addWidget(self.order_article_label)

        self.order_status_label = QLabel(Form)
        self.order_status_label.setObjectName(u"order_status_label")
        self.order_status_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.order_status_label)

        self.order_address_label = QLabel(Form)
        self.order_address_label.setObjectName(u"order_address_label")

        self.verticalLayout.addWidget(self.order_address_label)

        self.order_date_label = QLabel(Form)
        self.order_date_label.setObjectName(u"order_date_label")

        self.verticalLayout.addWidget(self.order_date_label)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.deliver_date_label = QLabel(Form)
        self.deliver_date_label.setObjectName(u"deliver_date_label")
        self.deliver_date_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.deliver_date_label)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.order_article_label.setText(QCoreApplication.translate("Form",
                                                                    u"\u0410\u0440\u0442\u0438\u043a\u0443\u043b \u0437\u0430\u043a\u0430\u0437\u0430",
                                                                    None))
        self.order_status_label.setText(QCoreApplication.translate("Form",
                                                                   u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0437\u0430\u043a\u0430\u0437\u0430",
                                                                   None))
        self.order_address_label.setText(QCoreApplication.translate("Form",
                                                                    u"\u0410\u0434\u0440\u0435\u0441 \u043f\u0443\u043d\u043a\u0442\u0430 \u0432\u044b\u0434\u0430\u0447\u0438",
                                                                    None))
        self.order_date_label.setText(QCoreApplication.translate("Form",
                                                                 u"\u0414\u0430\u0442\u0430 \u0437\u0430\u043a\u0430\u0437\u0430",
                                                                 None))
        self.deliver_date_label.setText(QCoreApplication.translate("Form",
                                                                   u"\u0414\u0430\u0442\u0430 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438",
                                                                   None))
    # retranslateUi

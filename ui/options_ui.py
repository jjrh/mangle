# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dev/ui/options.ui'
#
# Created: Sat Sep 11 12:04:56 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DialogOptions(object):
    def setupUi(self, DialogOptions):
        DialogOptions.setObjectName("DialogOptions")
        DialogOptions.resize(350, 350)
        self.verticalLayout = QtGui.QVBoxLayout(DialogOptions)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(DialogOptions)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEditTitle = QtGui.QLineEdit(self.groupBox)
        self.lineEditTitle.setObjectName("lineEditTitle")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditTitle)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(DialogOptions)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.comboBoxDevice = QtGui.QComboBox(self.groupBox_2)
        self.comboBoxDevice.setObjectName("comboBoxDevice")
        self.comboBoxDevice.addItem("")
        self.comboBoxDevice.addItem("")
        self.comboBoxDevice.addItem("")
        self.comboBoxDevice.addItem("")
        self.comboBoxDevice.addItem("")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBoxDevice)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.checkboxOverwrite = QtGui.QCheckBox(self.groupBox_2)
        self.checkboxOverwrite.setObjectName("checkboxOverwrite")
        self.verticalLayout_2.addWidget(self.checkboxOverwrite)
        self.checkboxOrient = QtGui.QCheckBox(self.groupBox_2)
        self.checkboxOrient.setObjectName("checkboxOrient")
        self.verticalLayout_2.addWidget(self.checkboxOrient)
        self.checkboxResize = QtGui.QCheckBox(self.groupBox_2)
        self.checkboxResize.setObjectName("checkboxResize")
        self.verticalLayout_2.addWidget(self.checkboxResize)
        self.checkboxQuantize = QtGui.QCheckBox(self.groupBox_2)
        self.checkboxQuantize.setObjectName("checkboxQuantize")
        self.verticalLayout_2.addWidget(self.checkboxQuantize)
        self.checkboxFrame = QtGui.QCheckBox(self.groupBox_2)
        self.checkboxFrame.setObjectName("checkboxFrame")
        self.verticalLayout_2.addWidget(self.checkboxFrame)
        self.verticalLayout.addWidget(self.groupBox_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(DialogOptions)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogOptions)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DialogOptions.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DialogOptions.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogOptions)

    def retranslateUi(self, DialogOptions):
        DialogOptions.setWindowTitle(QtGui.QApplication.translate("DialogOptions", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("DialogOptions", "Book", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogOptions", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("DialogOptions", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DialogOptions", "Device", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDevice.setItemText(0, QtGui.QApplication.translate("DialogOptions", "Kindle 1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDevice.setItemText(1, QtGui.QApplication.translate("DialogOptions", "Kindle 2", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDevice.setItemText(2, QtGui.QApplication.translate("DialogOptions", "Kindle 3", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDevice.setItemText(3, QtGui.QApplication.translate("DialogOptions", "Kindle DX", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDevice.setItemText(4, QtGui.QApplication.translate("DialogOptions", "Kindle DXG", None, QtGui.QApplication.UnicodeUTF8))
        self.checkboxOverwrite.setText(QtGui.QApplication.translate("DialogOptions", "Overwrite existing files", None, QtGui.QApplication.UnicodeUTF8))
        self.checkboxOrient.setText(QtGui.QApplication.translate("DialogOptions", "Orient images to match aspect ratio", None, QtGui.QApplication.UnicodeUTF8))
        self.checkboxResize.setText(QtGui.QApplication.translate("DialogOptions", "Resize images to center on screen", None, QtGui.QApplication.UnicodeUTF8))
        self.checkboxQuantize.setText(QtGui.QApplication.translate("DialogOptions", "Dither images to match device palette", None, QtGui.QApplication.UnicodeUTF8))
        self.checkboxFrame.setText(QtGui.QApplication.translate("DialogOptions", "Draw frame around images", None, QtGui.QApplication.UnicodeUTF8))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prototype.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from dataclasses import dataclass
from functools import partial

from core import *
from ifc import *

@dataclass
class ValidInput:
    length: float = 10
    width: float = 10

class ProjectParams():
    def __init__(self):
        pass
    
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(770, 780)
        MainWindow.setMinimumSize(QtCore.QSize(770, 780))
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.leftLayout = QtWidgets.QVBoxLayout()
        self.leftLayout.setObjectName("leftLayout")
        self.structureGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.structureGroup.setAlignment(QtCore.Qt.AlignCenter)
        self.structureGroup.setFlat(False)
        self.structureGroup.setObjectName("structureGroup")
        self.layoutWidget = QtWidgets.QWidget(self.structureGroup)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 351, 323))
        self.layoutWidget.setObjectName("layoutWidget")
        self.structureLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.structureLayout.setContentsMargins(0, 0, 0, 0)
        self.structureLayout.setObjectName("structureLayout")
        self.image = QtWidgets.QLabel(self.layoutWidget)
        self.image.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("assets/imgs/thumbnail.png"))
        self.image.setScaledContents(True)
        self.image.setWordWrap(False)
        self.image.setObjectName("image")
        self.structureLayout.addWidget(self.image)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.widthLabel = QtWidgets.QLabel(self.layoutWidget)
        self.widthLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.widthLabel.setObjectName("widthLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.widthLabel)

        self.widthBox = QtWidgets.QLineEdit(self.layoutWidget)
        self.widthBox.setAlignment(QtCore.Qt.AlignCenter)
        self.widthBox.setObjectName("widthBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.widthBox)
        self.lengthLabel = QtWidgets.QLabel(self.layoutWidget)
        self.lengthLabel.setObjectName("lengthLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lengthLabel)
        self.lengthBox = QtWidgets.QLineEdit(self.layoutWidget)
        self.lengthBox.setAlignment(QtCore.Qt.AlignCenter)
        self.lengthBox.setObjectName("lengthBox")


        self.valid = ValidInput()
        self.validator = QtGui.QDoubleValidator()
        self.widthBox.setValidator(self.validator)
        self.lengthBox.setValidator(self.validator)
        self.widthBox.textChanged.connect(self.SetWidth)
        self.lengthBox.textChanged.connect(self.SetLength)
        

        
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lengthBox)
        self.pavementLabel = QtWidgets.QLabel(self.layoutWidget)
        self.pavementLabel.setObjectName("pavementLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.pavementLabel)
        self.pavementBox = QtWidgets.QLineEdit(self.layoutWidget)
        self.pavementBox.setAlignment(QtCore.Qt.AlignCenter)
        self.pavementBox.setObjectName("pavementBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pavementBox)
        self.beamLabel = QtWidgets.QLabel(self.layoutWidget)
        self.beamLabel.setObjectName("beamLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.beamLabel)
        self.beamBox = QtWidgets.QLineEdit(self.layoutWidget)
        self.beamBox.setAlignment(QtCore.Qt.AlignCenter)
        self.beamBox.setObjectName("beamBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.beamBox)
        self.structureLayout.addLayout(self.formLayout)
        self.leftLayout.addWidget(self.structureGroup)

        # Roof
        self.roofGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.roofGroup.setAlignment(QtCore.Qt.AlignCenter)
        self.roofGroup.setObjectName("roofGroup")
        self.layoutWidget1 = QtWidgets.QWidget(self.roofGroup)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 20, 351, 191))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.rooftileLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.rooftileLayout.setContentsMargins(0, 0, 0, 0)
        self.rooftileLayout.setObjectName("rooftileLayout")
        self.roofTileCheckLayout = QtWidgets.QHBoxLayout()
        self.roofTileCheckLayout.setObjectName("roofTileCheckLayout")
        self.rooftileCheck = QtWidgets.QCheckBox(self.layoutWidget1)
        self.rooftileCheck.setObjectName("rooftileCheck")
        self.roofTileCheckLayout.addWidget(self.rooftileCheck)
        self.rooftileLayout.addLayout(self.roofTileCheckLayout)
        self.roofLine = QtWidgets.QFrame(self.layoutWidget1)
        self.roofLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.roofLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.roofLine.setObjectName("roofLine")
        self.rooftileLayout.addWidget(self.roofLine)
        self.rooftileDataLayout = QtWidgets.QVBoxLayout()
        self.rooftileDataLayout.setObjectName("rooftileDataLayout")
        self.rooftileTypeLayout = QtWidgets.QHBoxLayout()
        self.rooftileTypeLayout.setObjectName("rooftileTypeLayout")
        self.rooftileLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.rooftileLabel.setEnabled(False)
        self.rooftileLabel.setObjectName("rooftileLabel")
        self.rooftileTypeLayout.addWidget(self.rooftileLabel)
        self.rooftileBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.rooftileBox.setEnabled(False)
        self.rooftileBox.setObjectName("rooftileBox")
        self.rooftileTypeLayout.addWidget(self.rooftileBox)
        self.rooftileDataLayout.addLayout(self.rooftileTypeLayout)
        self.angleLayout = QtWidgets.QHBoxLayout()
        self.angleLayout.setObjectName("angleLayout")
        self.angleLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.angleLabel.setEnabled(False)
        self.angleLabel.setObjectName("angleLabel")
        self.angleLayout.addWidget(self.angleLabel)
        self.angleSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.angleSpinBox.setEnabled(False)
        self.angleSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.angleSpinBox.setObjectName("angleSpinBox")
        self.angleLayout.addWidget(self.angleSpinBox)
        self.rooftileDataLayout.addLayout(self.angleLayout)
        self.weightLayout = QtWidgets.QHBoxLayout()
        self.weightLayout.setObjectName("weightLayout")
        self.weightLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.weightLabel.setEnabled(False)
        self.weightLabel.setObjectName("weightLabel")
        self.weightLayout.addWidget(self.weightLabel)
        self.weigthSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.weigthSpinBox.setEnabled(False)
        self.weigthSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.weigthSpinBox.setObjectName("weigthSpinBox")
        self.weightLayout.addWidget(self.weigthSpinBox)
        self.rooftileDataLayout.addLayout(self.weightLayout)
        self.spacingLayout = QtWidgets.QHBoxLayout()
        self.spacingLayout.setObjectName("spacingLayout")
        self.spacingLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.spacingLabel.setEnabled(False)
        self.spacingLabel.setObjectName("spacingLabel")
        self.spacingLayout.addWidget(self.spacingLabel)
        self.spacingSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.spacingSpinBox.setEnabled(False)
        self.spacingSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spacingSpinBox.setObjectName("spacingSpinBox")
        self.spacingLayout.addWidget(self.spacingSpinBox)
        self.rooftileDataLayout.addLayout(self.spacingLayout)
        self.rooftileLayout.addLayout(self.rooftileDataLayout)
        self.leftLayout.addWidget(self.roofGroup)
        self.regionGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.regionGroup.setAlignment(QtCore.Qt.AlignCenter)
        self.regionGroup.setObjectName("regionGroup")
        self.layoutWidget2 = QtWidgets.QWidget(self.regionGroup)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 20, 351, 111))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.stateLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.stateLayout.setContentsMargins(0, 0, 0, 0)
        self.stateLayout.setObjectName("stateLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stateLabel = QtWidgets.QLabel(self.layoutWidget2)
        self.stateLabel.setObjectName("stateLabel")
        self.horizontalLayout.addWidget(self.stateLabel)
        self.stateBox = QtWidgets.QComboBox(self.layoutWidget2)
        self.stateBox.setPlaceholderText("")
        self.stateBox.setObjectName("stateBox")
        self.horizontalLayout.addWidget(self.stateBox)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.stateLayout.addLayout(self.horizontalLayout)
        self.stateTable = QtWidgets.QTableView(self.layoutWidget2)
        self.stateTable.setObjectName("stateTable")
        self.stateLayout.addWidget(self.stateTable)
        self.stateLayout.setStretch(0, 6)
        self.stateLayout.setStretch(1, 4)
        self.leftLayout.addWidget(self.regionGroup)
        self.leftLayout.setStretch(0, 5)
        self.leftLayout.setStretch(1, 3)
        self.leftLayout.setStretch(2, 2)
        self.horizontalLayout_2.addLayout(self.leftLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.materialGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.materialGroup.setAlignment(QtCore.Qt.AlignCenter)
        self.materialGroup.setObjectName("materialGroup")
        self.layoutWidget3 = QtWidgets.QWidget(self.materialGroup)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 20, 351, 531))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.materialLayout = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.materialLayout.setContentsMargins(0, 0, 0, 0)
        self.materialLayout.setObjectName("materialLayout")
        self.materialTypeLayout = QtWidgets.QHBoxLayout()
        self.materialTypeLayout.setSpacing(6)
        self.materialTypeLayout.setObjectName("materialTypeLayout")
        self.materialTypeLabel = QtWidgets.QLabel(self.layoutWidget3)
        self.materialTypeLabel.setObjectName("materialTypeLabel")
        self.materialTypeLayout.addWidget(self.materialTypeLabel)
        self.materialTypeBox = QtWidgets.QComboBox(self.layoutWidget3)
        self.materialTypeBox.setCurrentText("")
        self.materialTypeBox.setPlaceholderText("")
        self.materialTypeBox.setObjectName("materialTypeBox")
        self.materialTypeLayout.addWidget(self.materialTypeBox)
        self.materialLayout.addLayout(self.materialTypeLayout)
        self.materialLine = QtWidgets.QFrame(self.layoutWidget3)
        self.materialLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.materialLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.materialLine.setObjectName("materialLine")
        self.materialLayout.addWidget(self.materialLine)
        self.woodLayout = QtWidgets.QVBoxLayout()
        self.woodLayout.setObjectName("woodLayout")
        self.classLayout = QtWidgets.QHBoxLayout()
        self.classLayout.setObjectName("classLayout")
        self.classLabel = QtWidgets.QLabel(self.layoutWidget3)
        self.classLabel.setObjectName("classLabel")
        self.classLayout.addWidget(self.classLabel)
        self.classBox = QtWidgets.QComboBox(self.layoutWidget3)
        self.classBox.setCurrentText("")
        self.classBox.setPlaceholderText("")
        self.classBox.setObjectName("classBox")
        self.classLayout.addWidget(self.classBox)
        self.toolButton = QtWidgets.QToolButton(self.layoutWidget3)
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/imgs/gear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(16, 16))
        self.toolButton.setObjectName("toolButton")
        self.classLayout.addWidget(self.toolButton)
        self.classLayout.setStretch(0, 4)
        self.classLayout.setStretch(1, 3)
        self.woodLayout.addLayout(self.classLayout)
        self.materialTableLayout = QtWidgets.QVBoxLayout()
        self.materialTableLayout.setObjectName("materialTableLayout")
        self.propertiesLabel = QtWidgets.QLabel(self.layoutWidget3)
        self.propertiesLabel.setObjectName("propertiesLabel")
        self.materialTableLayout.addWidget(self.propertiesLabel)
        self.materialTable = QtWidgets.QTableView(self.layoutWidget3)
        self.materialTable.setShowGrid(True)
        self.materialTable.setObjectName("materialTable")
        self.materialTableLayout.addWidget(self.materialTable)
        self.woodLayout.addLayout(self.materialTableLayout)
        self.materialLayout.addLayout(self.woodLayout)
        self.verticalLayout_4.addWidget(self.materialGroup)
        self.actionGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.actionGroup.setAlignment(QtCore.Qt.AlignCenter)
        self.actionGroup.setObjectName("actionGroup")

        # Test
        self.pushButton = QtWidgets.QPushButton(self.actionGroup)
        self.pushButton.setGeometry(QtCore.QRect(100, 50, 181, 51))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.Generate)

        self.verticalLayout_4.addWidget(self.actionGroup)
        self.verticalLayout_4.setStretch(0, 8)
        self.verticalLayout_4.setStretch(1, 2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 770, 21))
        self.menubar.setObjectName("menubar")
        self.menuCreditos = QtWidgets.QMenu(self.menubar)
        self.menuCreditos.setObjectName("menuCreditos")
        MainWindow.setMenuBar(self.menubar)
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.actionContato = QtWidgets.QAction(MainWindow)
        self.actionContato.setObjectName("actionContato")
        self.actionSair_2 = QtWidgets.QAction(MainWindow)
        self.actionSair_2.setObjectName("actionSair_2")
        self.menuCreditos.addAction(self.actionContato)
        self.menubar.addAction(self.menuCreditos.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def SetWidth(self):
        self.valid.width = float(self.widthBox.text())
        
    def SetLength(self):
        self.valid.length = float(self.lengthBox.text())

    def Generate(self):
        #print(self.valid.width)
        #print(self.valid.length)

        s = ifcproject.StructureSettings(length=self.valid.length, width=self.valid.width)
        project = ifcproject.Project(structureSettings=s)
        #project.structure.length = self.valid.length

        #os.chdir('..')
        project.GenerateIFCFile("test")
        #process = subprocess.run(['C:\Program Files\Data Design System\Viewer\Exe\DdsViewer.exe', 'build\\test.ifc'])
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Unnamed"))
        self.structureGroup.setTitle(_translate("MainWindow", "Estrutura"))
        self.widthLabel.setToolTip(_translate("MainWindow", "A largura do terreno medida em metros (m)"))
        self.widthLabel.setText(_translate("MainWindow", "Largura (a)"))
        self.widthBox.setPlaceholderText(_translate("MainWindow", "10m"))
        self.lengthLabel.setToolTip(_translate("MainWindow", "O comprimento do terreno medida em metros (m)"))
        self.lengthLabel.setText(_translate("MainWindow", "Comprimento (b)"))
        self.lengthBox.setPlaceholderText(_translate("MainWindow", "10m"))
        self.pavementLabel.setToolTip(_translate("MainWindow", "Assume uma altura de 3m por andar"))
        self.pavementLabel.setText(_translate("MainWindow", "No. Pavimentos"))
        self.pavementBox.setPlaceholderText(_translate("MainWindow", "1"))
        self.beamLabel.setToolTip(_translate("MainWindow", "Número de vigas por andar"))
        self.beamLabel.setText(_translate("MainWindow", "No. Vigas"))
        self.beamBox.setPlaceholderText(_translate("MainWindow", "1"))
        self.roofGroup.setTitle(_translate("MainWindow", "Cobertura"))
        self.rooftileCheck.setText(_translate("MainWindow", "Telhas"))
        self.rooftileLabel.setText(_translate("MainWindow", "Tipo"))
        self.angleLabel.setToolTip(_translate("MainWindow", "Ângulo da telha em relação ao horizonte"))
        self.angleLabel.setText(_translate("MainWindow", "Ângulo"))
        self.weightLabel.setToolTip(_translate("MainWindow", "Peso total de telhas por metro quadrado"))
        self.weightLabel.setText(_translate("MainWindow", "Peso (m²)"))
        self.spacingLabel.setToolTip(_translate("MainWindow", "Espaçamento entre as galgas medido em metros (m)"))
        self.spacingLabel.setText(_translate("MainWindow", "Espaçamento das galgas"))
        self.regionGroup.setTitle(_translate("MainWindow", "Região"))
        self.stateLabel.setText(_translate("MainWindow", "Estado"))
        self.materialGroup.setTitle(_translate("MainWindow", "Material"))
        self.materialTypeLabel.setText(_translate("MainWindow", "Tipo"))
        self.classLabel.setText(_translate("MainWindow", "Classe"))
        self.propertiesLabel.setText(_translate("MainWindow", "Propriedades"))
        self.actionGroup.setTitle(_translate("MainWindow", "Ações"))
        self.pushButton.setText(_translate("MainWindow", "Calcular"))
        self.menuCreditos.setTitle(_translate("MainWindow", "Ajuda"))
        self.actionSair.setText(_translate("MainWindow", "Novo"))
        self.actionContato.setText(_translate("MainWindow", "Contato"))
        self.actionSair_2.setText(_translate("MainWindow", "Sair"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
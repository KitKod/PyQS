# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/qtview.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MplMainWindow(object):
    def setupUi(self, MplMainWindow):
        MplMainWindow.setObjectName("MplMainWindow")
        MplMainWindow.resize(909, 549)
        self.centralwidget = QtWidgets.QWidget(MplMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox_inter_fires = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_inter_fires.sizePolicy().hasHeightForWidth())
        self.comboBox_inter_fires.setSizePolicy(sizePolicy)
        self.comboBox_inter_fires.setMinimumSize(QtCore.QSize(140, 0))
        self.comboBox_inter_fires.setObjectName("comboBox_inter_fires")
        self.verticalLayout.addWidget(self.comboBox_inter_fires)
        self.comboBox_time_of_putout = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_time_of_putout.sizePolicy().hasHeightForWidth())
        self.comboBox_time_of_putout.setSizePolicy(sizePolicy)
        self.comboBox_time_of_putout.setMinimumSize(QtCore.QSize(140, 0))
        self.comboBox_time_of_putout.setObjectName("comboBox_time_of_putout")
        self.verticalLayout.addWidget(self.comboBox_time_of_putout)
        self.lineEdit_count_fire_engine = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_count_fire_engine.sizePolicy().hasHeightForWidth())
        self.lineEdit_count_fire_engine.setSizePolicy(sizePolicy)
        self.lineEdit_count_fire_engine.setMinimumSize(QtCore.QSize(140, 0))
        self.lineEdit_count_fire_engine.setObjectName("lineEdit_count_fire_engine")
        self.verticalLayout.addWidget(self.lineEdit_count_fire_engine)
        self.lineEdit_time_of_modeling = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_time_of_modeling.sizePolicy().hasHeightForWidth())
        self.lineEdit_time_of_modeling.setSizePolicy(sizePolicy)
        self.lineEdit_time_of_modeling.setMinimumSize(QtCore.QSize(140, 0))
        self.lineEdit_time_of_modeling.setInputMask("")
        self.lineEdit_time_of_modeling.setText("")
        self.lineEdit_time_of_modeling.setObjectName("lineEdit_time_of_modeling")
        self.verticalLayout.addWidget(self.lineEdit_time_of_modeling)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_test = QtWidgets.QWidget()
        self.tab_test.setObjectName("tab_test")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_test)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.mpl = MplWidget(self.tab_test)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mpl.sizePolicy().hasHeightForWidth())
        self.mpl.setSizePolicy(sizePolicy)
        self.mpl.setObjectName("mpl")
        self.verticalLayout_3.addWidget(self.mpl)
        self.button_start_test = QtWidgets.QPushButton(self.tab_test)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_start_test.sizePolicy().hasHeightForWidth())
        self.button_start_test.setSizePolicy(sizePolicy)
        self.button_start_test.setObjectName("button_start_test")
        self.verticalLayout_3.addWidget(self.button_start_test, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_test, "")
        self.tab_stat = QtWidgets.QWidget()
        self.tab_stat.setObjectName("tab_stat")
        self.tabWidget.addTab(self.tab_stat, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        MplMainWindow.setCentralWidget(self.centralwidget)
        self.mplmenuBar = QtWidgets.QMenuBar(MplMainWindow)
        self.mplmenuBar.setGeometry(QtCore.QRect(0, 0, 909, 30))
        self.mplmenuBar.setObjectName("mplmenuBar")
        self.mplmenuFile = QtWidgets.QMenu(self.mplmenuBar)
        self.mplmenuFile.setObjectName("mplmenuFile")
        MplMainWindow.setMenuBar(self.mplmenuBar)
        self.mplactionOpen = QtWidgets.QAction(MplMainWindow)
        self.mplactionOpen.setObjectName("mplactionOpen")
        self.mplactionQuit = QtWidgets.QAction(MplMainWindow)
        self.mplactionQuit.setObjectName("mplactionQuit")
        self.mplmenuFile.addAction(self.mplactionOpen)
        self.mplmenuFile.addAction(self.mplactionQuit)
        self.mplmenuBar.addAction(self.mplmenuFile.menuAction())

        self.retranslateUi(MplMainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MplMainWindow)

    def retranslateUi(self, MplMainWindow):
        _translate = QtCore.QCoreApplication.translate
        MplMainWindow.setWindowTitle(_translate("MplMainWindow", "MainWindow"))
        self.lineEdit_count_fire_engine.setPlaceholderText(_translate("MplMainWindow", "Count of fire engine"))
        self.lineEdit_time_of_modeling.setPlaceholderText(_translate("MplMainWindow", "Time of modeling"))
        self.button_start_test.setText(_translate("MplMainWindow", "Start"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_test), _translate("MplMainWindow", "Test"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_stat), _translate("MplMainWindow", "Tab 2"))
        self.mplmenuFile.setTitle(_translate("MplMainWindow", "Fi&le"))
        self.mplactionOpen.setText(_translate("MplMainWindow", "&Open"))
        self.mplactionQuit.setText(_translate("MplMainWindow", "&Quit"))


from gui.mplwidget import MplWidget

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_Layout.ui'
#
# Created: Fri May  9 16:46:26 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(1427, 849)
        MainWindow.setAnimated(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.run = QtGui.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(0, 760, 101, 31))
        self.run.setObjectName(_fromUtf8("run"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1391, 751))
        self.tabWidget.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setItalic(False)
        font.setUnderline(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.p_label = QtGui.QLabel(self.tab)
        self.p_label.setGeometry(QtCore.QRect(20, 70, 71, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p_label.sizePolicy().hasHeightForWidth())
        self.p_label.setSizePolicy(sizePolicy)
        self.p_label.setObjectName(_fromUtf8("p_label"))
        self.execPath_label = QtGui.QLabel(self.tab)
        self.execPath_label.setGeometry(QtCore.QRect(20, 630, 111, 16))
        self.execPath_label.setObjectName(_fromUtf8("execPath_label"))
        self.cpu_label = QtGui.QLabel(self.tab)
        self.cpu_label.setGeometry(QtCore.QRect(20, 580, 111, 16))
        self.cpu_label.setObjectName(_fromUtf8("cpu_label"))
        self.nb_cpu = QtGui.QComboBox(self.tab)
        self.nb_cpu.setGeometry(QtCore.QRect(160, 580, 71, 31))
        self.nb_cpu.setObjectName(_fromUtf8("nb_cpu"))
        self.sens = QtGui.QSlider(self.tab)
        self.sens.setEnabled(True)
        self.sens.setGeometry(QtCore.QRect(630, 360, 741, 31))
        self.sens.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.sens.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sens.setAutoFillBackground(False)
        self.sens.setOrientation(QtCore.Qt.Horizontal)
        self.sens.setObjectName(_fromUtf8("sens"))
        self.label_17 = QtGui.QLabel(self.tab)
        self.label_17.setGeometry(QtCore.QRect(580, 370, 41, 16))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.line = QtGui.QFrame(self.tab)
        self.line.setEnabled(True)
        self.line.setGeometry(QtCore.QRect(560, 0, 20, 721))
        self.line.setAutoFillBackground(False)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.exec_path = QtGui.QLineEdit(self.tab)
        self.exec_path.setEnabled(False)
        self.exec_path.setGeometry(QtCore.QRect(40, 660, 481, 21))
        self.exec_path.setObjectName(_fromUtf8("exec_path"))
        self.p_values = QtGui.QLineEdit(self.tab)
        self.p_values.setGeometry(QtCore.QRect(120, 70, 401, 21))
        self.p_values.setObjectName(_fromUtf8("p_values"))
        self.title_label = QtGui.QLabel(self.tab)
        self.title_label.setGeometry(QtCore.QRect(10, 0, 241, 31))
        self.title_label.setObjectName(_fromUtf8("title_label"))
        self.particules_label = QtGui.QLabel(self.tab)
        self.particules_label.setGeometry(QtCore.QRect(20, 100, 151, 21))
        self.particules_label.setObjectName(_fromUtf8("particules_label"))
        self.x_value = QtGui.QLineEdit(self.tab)
        self.x_value.setGeometry(QtCore.QRect(120, 120, 51, 21))
        self.x_value.setObjectName(_fromUtf8("x_value"))
        self.y_value = QtGui.QLineEdit(self.tab)
        self.y_value.setGeometry(QtCore.QRect(120, 150, 51, 21))
        self.y_value.setObjectName(_fromUtf8("y_value"))
        self.x_label = QtGui.QLabel(self.tab)
        self.x_label.setGeometry(QtCore.QRect(60, 120, 21, 16))
        self.x_label.setObjectName(_fromUtf8("x_label"))
        self.y_label = QtGui.QLabel(self.tab)
        self.y_label.setGeometry(QtCore.QRect(60, 150, 21, 16))
        self.y_label.setObjectName(_fromUtf8("y_label"))
        self.organic_label = QtGui.QLabel(self.tab)
        self.organic_label.setGeometry(QtCore.QRect(20, 180, 231, 21))
        self.organic_label.setObjectName(_fromUtf8("organic_label"))
        self.s_value = QtGui.QLineEdit(self.tab)
        self.s_value.setGeometry(QtCore.QRect(120, 230, 51, 21))
        self.s_value.setObjectName(_fromUtf8("s_value"))
        self.g_value = QtGui.QLineEdit(self.tab)
        self.g_value.setGeometry(QtCore.QRect(120, 200, 51, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g_value.sizePolicy().hasHeightForWidth())
        self.g_value.setSizePolicy(sizePolicy)
        self.g_value.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.g_value.setObjectName(_fromUtf8("g_value"))
        self.g_label = QtGui.QLabel(self.tab)
        self.g_label.setGeometry(QtCore.QRect(60, 200, 21, 16))
        self.g_label.setObjectName(_fromUtf8("g_label"))
        self.s_label = QtGui.QLabel(self.tab)
        self.s_label.setGeometry(QtCore.QRect(60, 230, 21, 16))
        self.s_label.setObjectName(_fromUtf8("s_label"))
        self.z_label = QtGui.QLabel(self.tab)
        self.z_label.setGeometry(QtCore.QRect(20, 260, 71, 16))
        self.z_label.setObjectName(_fromUtf8("z_label"))
        self.z_value = QtGui.QLineEdit(self.tab)
        self.z_value.setGeometry(QtCore.QRect(120, 260, 51, 21))
        self.z_value.setObjectName(_fromUtf8("z_value"))
        self.label_10 = QtGui.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(190, 260, 21, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.exec_path_button = QtGui.QPushButton(self.tab)
        self.exec_path_button.setGeometry(QtCore.QRect(160, 620, 71, 31))
        self.exec_path_button.setObjectName(_fromUtf8("exec_path_button"))
        self.waveL_label = QtGui.QLabel(self.tab)
        self.waveL_label.setGeometry(QtCore.QRect(20, 290, 101, 16))
        self.waveL_label.setObjectName(_fromUtf8("waveL_label"))
        self.wavelength_values = QtGui.QLineEdit(self.tab)
        self.wavelength_values.setGeometry(QtCore.QRect(120, 290, 401, 21))
        self.wavelength_values.setObjectName(_fromUtf8("wavelength_values"))
        self.phyto_label = QtGui.QLabel(self.tab)
        self.phyto_label.setGeometry(QtCore.QRect(20, 420, 191, 21))
        self.phyto_label.setTextFormat(QtCore.Qt.AutoText)
        self.phyto_label.setObjectName(_fromUtf8("phyto_label"))
        self.phyto_button = QtGui.QPushButton(self.tab)
        self.phyto_button.setGeometry(QtCore.QRect(220, 410, 71, 31))
        self.phyto_button.setObjectName(_fromUtf8("phyto_button"))
        self.phyto_path = QtGui.QLineEdit(self.tab)
        self.phyto_path.setEnabled(False)
        self.phyto_path.setGeometry(QtCore.QRect(30, 450, 491, 21))
        self.phyto_path.setObjectName(_fromUtf8("phyto_path"))
        self.bottom_label = QtGui.QLabel(self.tab)
        self.bottom_label.setGeometry(QtCore.QRect(20, 350, 141, 16))
        self.bottom_label.setObjectName(_fromUtf8("bottom_label"))
        self.bottom_path = QtGui.QLineEdit(self.tab)
        self.bottom_path.setEnabled(False)
        self.bottom_path.setGeometry(QtCore.QRect(30, 380, 491, 21))
        self.bottom_path.setObjectName(_fromUtf8("bottom_path"))
        self.bottom_button = QtGui.QPushButton(self.tab)
        self.bottom_button.setGeometry(QtCore.QRect(220, 340, 71, 31))
        self.bottom_button.setObjectName(_fromUtf8("bottom_button"))
        self.verbose_label = QtGui.QLabel(self.tab)
        self.verbose_label.setGeometry(QtCore.QRect(20, 550, 66, 17))
        self.verbose_label.setObjectName(_fromUtf8("verbose_label"))
        self.verbose_value = QtGui.QLineEdit(self.tab)
        self.verbose_value.setGeometry(QtCore.QRect(160, 550, 71, 21))
        self.verbose_value.setObjectName(_fromUtf8("verbose_value"))
        self.label_14 = QtGui.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(530, 290, 31, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_31 = QtGui.QLabel(self.tab)
        self.label_31.setGeometry(QtCore.QRect(240, 550, 51, 16))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.label_32 = QtGui.QLabel(self.tab)
        self.label_32.setGeometry(QtCore.QRect(240, 590, 251, 16))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.graphicsView_3 = QtGui.QGraphicsView(self.tab)
        self.graphicsView_3.setGeometry(QtCore.QRect(580, 10, 791, 351))
        self.graphicsView_3.setObjectName(_fromUtf8("graphicsView_3"))
        self.graphic_widget = matplotlibWidget(self.tab)
        self.graphic_widget.setGeometry(QtCore.QRect(570, 0, 811, 371))
        self.graphic_widget.setObjectName(_fromUtf8("graphic_widget"))
        self.line_3 = QtGui.QFrame(self.tab)
        self.line_3.setGeometry(QtCore.QRect(830, 410, 20, 261))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(580, 410, 141, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(870, 410, 141, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.column1_label = QtGui.QLabel(self.tab)
        self.column1_label.setGeometry(QtCore.QRect(890, 440, 111, 21))
        self.column1_label.setObjectName(_fromUtf8("column1_label"))
        self.column2_label = QtGui.QLabel(self.tab)
        self.column2_label.setGeometry(QtCore.QRect(890, 470, 111, 21))
        self.column2_label.setObjectName(_fromUtf8("column2_label"))
        self.column1_result = QtGui.QLabel(self.tab)
        self.column1_result.setGeometry(QtCore.QRect(1030, 440, 21, 17))
        self.column1_result.setObjectName(_fromUtf8("column1_result"))
        self.column2_result = QtGui.QLabel(self.tab)
        self.column2_result.setGeometry(QtCore.QRect(1030, 470, 21, 17))
        self.column2_result.setObjectName(_fromUtf8("column2_result"))
        self.show_all_curves = QtGui.QCheckBox(self.tab)
        self.show_all_curves.setGeometry(QtCore.QRect(600, 440, 131, 22))
        self.show_all_curves.setObjectName(_fromUtf8("show_all_curves"))
        self.column3_label = QtGui.QLabel(self.tab)
        self.column3_label.setGeometry(QtCore.QRect(890, 500, 111, 16))
        self.column3_label.setObjectName(_fromUtf8("column3_label"))
        self.column5_label = QtGui.QLabel(self.tab)
        self.column5_label.setGeometry(QtCore.QRect(890, 560, 111, 16))
        self.column5_label.setObjectName(_fromUtf8("column5_label"))
        self.column6_label = QtGui.QLabel(self.tab)
        self.column6_label.setGeometry(QtCore.QRect(890, 590, 111, 16))
        self.column6_label.setObjectName(_fromUtf8("column6_label"))
        self.column7_label = QtGui.QLabel(self.tab)
        self.column7_label.setGeometry(QtCore.QRect(890, 620, 111, 16))
        self.column7_label.setObjectName(_fromUtf8("column7_label"))
        self.column8_label = QtGui.QLabel(self.tab)
        self.column8_label.setGeometry(QtCore.QRect(890, 650, 111, 16))
        self.column8_label.setObjectName(_fromUtf8("column8_label"))
        self.column3_result = QtGui.QLabel(self.tab)
        self.column3_result.setGeometry(QtCore.QRect(1030, 500, 21, 17))
        self.column3_result.setObjectName(_fromUtf8("column3_result"))
        self.column4_result = QtGui.QLabel(self.tab)
        self.column4_result.setGeometry(QtCore.QRect(1030, 530, 21, 17))
        self.column4_result.setObjectName(_fromUtf8("column4_result"))
        self.column5_result = QtGui.QLabel(self.tab)
        self.column5_result.setGeometry(QtCore.QRect(1030, 560, 21, 17))
        self.column5_result.setObjectName(_fromUtf8("column5_result"))
        self.column6_result = QtGui.QLabel(self.tab)
        self.column6_result.setGeometry(QtCore.QRect(1030, 590, 21, 17))
        self.column6_result.setObjectName(_fromUtf8("column6_result"))
        self.column7_result = QtGui.QLabel(self.tab)
        self.column7_result.setGeometry(QtCore.QRect(1030, 620, 21, 17))
        self.column7_result.setObjectName(_fromUtf8("column7_result"))
        self.column8_result = QtGui.QLabel(self.tab)
        self.column8_result.setGeometry(QtCore.QRect(1030, 650, 21, 17))
        self.column8_result.setObjectName(_fromUtf8("column8_result"))
        self.column4_label = QtGui.QLabel(self.tab)
        self.column4_label.setGeometry(QtCore.QRect(890, 526, 111, 20))
        self.column4_label.setObjectName(_fromUtf8("column4_label"))
        self.line_4 = QtGui.QFrame(self.tab)
        self.line_4.setGeometry(QtCore.QRect(60, 320, 371, 21))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.line_5 = QtGui.QFrame(self.tab)
        self.line_5.setGeometry(QtCore.QRect(60, 480, 371, 21))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.report_parameter_value = QtGui.QLineEdit(self.tab)
        self.report_parameter_value.setGeometry(QtCore.QRect(160, 510, 71, 21))
        self.report_parameter_value.setObjectName(_fromUtf8("report_parameter_value"))
        self.report_parameter_label = QtGui.QLabel(self.tab)
        self.report_parameter_label.setGeometry(QtCore.QRect(20, 510, 131, 16))
        self.report_parameter_label.setObjectName(_fromUtf8("report_parameter_label"))
        self.batch_name_label = QtGui.QLabel(self.tab)
        self.batch_name_label.setGeometry(QtCore.QRect(20, 40, 91, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.batch_name_label.sizePolicy().hasHeightForWidth())
        self.batch_name_label.setSizePolicy(sizePolicy)
        self.batch_name_label.setObjectName(_fromUtf8("batch_name_label"))
        self.batch_name_value = QtGui.QLineEdit(self.tab)
        self.batch_name_value.setGeometry(QtCore.QRect(120, 40, 101, 21))
        self.batch_name_value.setObjectName(_fromUtf8("batch_name_value"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.ReverseTab = QtGui.QWidget()
        self.ReverseTab.setObjectName(_fromUtf8("ReverseTab"))
        self.line_2 = QtGui.QFrame(self.ReverseTab)
        self.line_2.setGeometry(QtCore.QRect(560, 0, 20, 721))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_20 = QtGui.QLabel(self.ReverseTab)
        self.label_20.setGeometry(QtCore.QRect(580, 400, 66, 17))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.McGee_radioButton = QtGui.QRadioButton(self.ReverseTab)
        self.McGee_radioButton.setGeometry(QtCore.QRect(80, 80, 116, 22))
        self.McGee_radioButton.setObjectName(_fromUtf8("McGee_radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.ReverseTab)
        self.radioButton_2.setGeometry(QtCore.QRect(80, 110, 116, 22))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(self.ReverseTab)
        self.radioButton_3.setGeometry(QtCore.QRect(80, 140, 116, 22))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.label_19 = QtGui.QLabel(self.ReverseTab)
        self.label_19.setGeometry(QtCore.QRect(40, 50, 101, 16))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_18 = QtGui.QLabel(self.ReverseTab)
        self.label_18.setGeometry(QtCore.QRect(10, 20, 191, 16))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.x_value_reverse = QtGui.QLineEdit(self.ReverseTab)
        self.x_value_reverse.setGeometry(QtCore.QRect(710, 480, 51, 21))
        self.x_value_reverse.setObjectName(_fromUtf8("x_value_reverse"))
        self.label_27 = QtGui.QLabel(self.ReverseTab)
        self.label_27.setGeometry(QtCore.QRect(650, 600, 21, 16))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.label_22 = QtGui.QLabel(self.ReverseTab)
        self.label_22.setGeometry(QtCore.QRect(610, 460, 151, 21))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_29 = QtGui.QLabel(self.ReverseTab)
        self.label_29.setGeometry(QtCore.QRect(770, 630, 21, 16))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.label_24 = QtGui.QLabel(self.ReverseTab)
        self.label_24.setGeometry(QtCore.QRect(650, 510, 21, 16))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.label_23 = QtGui.QLabel(self.ReverseTab)
        self.label_23.setGeometry(QtCore.QRect(650, 480, 21, 16))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.y_value_reverse = QtGui.QLineEdit(self.ReverseTab)
        self.y_value_reverse.setGeometry(QtCore.QRect(710, 510, 51, 21))
        self.y_value_reverse.setObjectName(_fromUtf8("y_value_reverse"))
        self.label_21 = QtGui.QLabel(self.ReverseTab)
        self.label_21.setGeometry(QtCore.QRect(610, 430, 71, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_30 = QtGui.QLabel(self.ReverseTab)
        self.label_30.setGeometry(QtCore.QRect(610, 660, 101, 16))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.label_25 = QtGui.QLabel(self.ReverseTab)
        self.label_25.setGeometry(QtCore.QRect(610, 540, 151, 21))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.g_value_reverse = QtGui.QLineEdit(self.ReverseTab)
        self.g_value_reverse.setGeometry(QtCore.QRect(710, 560, 51, 21))
        self.g_value_reverse.setObjectName(_fromUtf8("g_value_reverse"))
        self.p_values_reverse = QtGui.QLineEdit(self.ReverseTab)
        self.p_values_reverse.setGeometry(QtCore.QRect(710, 430, 311, 21))
        self.p_values_reverse.setObjectName(_fromUtf8("p_values_reverse"))
        self.s_value_reverse = QtGui.QLineEdit(self.ReverseTab)
        self.s_value_reverse.setGeometry(QtCore.QRect(710, 600, 51, 21))
        self.s_value_reverse.setObjectName(_fromUtf8("s_value_reverse"))
        self.label_28 = QtGui.QLabel(self.ReverseTab)
        self.label_28.setGeometry(QtCore.QRect(610, 630, 71, 16))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.wavelength_values_reverse = QtGui.QLineEdit(self.ReverseTab)
        self.wavelength_values_reverse.setGeometry(QtCore.QRect(710, 660, 311, 21))
        self.wavelength_values_reverse.setObjectName(_fromUtf8("wavelength_values_reverse"))
        self.z_value_reverse = QtGui.QLineEdit(self.ReverseTab)
        self.z_value_reverse.setGeometry(QtCore.QRect(710, 630, 51, 21))
        self.z_value_reverse.setObjectName(_fromUtf8("z_value_reverse"))
        self.label_26 = QtGui.QLabel(self.ReverseTab)
        self.label_26.setGeometry(QtCore.QRect(650, 560, 21, 16))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.graphicsView_4 = QtGui.QGraphicsView(self.ReverseTab)
        self.graphicsView_4.setGeometry(QtCore.QRect(580, 10, 791, 351))
        self.graphicsView_4.setObjectName(_fromUtf8("graphicsView_4"))
        self.widget_2 = QtGui.QWidget(self.ReverseTab)
        self.widget_2.setGeometry(QtCore.QRect(570, 0, 811, 371))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.label_33 = QtGui.QLabel(self.ReverseTab)
        self.label_33.setGeometry(QtCore.QRect(580, 370, 41, 16))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.label_15 = QtGui.QLabel(self.ReverseTab)
        self.label_15.setGeometry(QtCore.QRect(1040, 660, 31, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.sens_2 = QtGui.QSlider(self.ReverseTab)
        self.sens_2.setEnabled(True)
        self.sens_2.setGeometry(QtCore.QRect(630, 360, 741, 31))
        self.sens_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.sens_2.setAutoFillBackground(False)
        self.sens_2.setOrientation(QtCore.Qt.Horizontal)
        self.sens_2.setObjectName(_fromUtf8("sens_2"))
        self.tabWidget.addTab(self.ReverseTab, _fromUtf8(""))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(110, 770, 351, 16))
        self.progressBar.setMouseTracking(False)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(True)
        self.progressBar.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.cancel = QtGui.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(470, 760, 101, 31))
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.quit = QtGui.QPushButton(self.centralwidget)
        self.quit.setGeometry(QtCore.QRect(1290, 760, 101, 31))
        self.quit.setObjectName(_fromUtf8("quit"))
        self.error_text_label = QtGui.QLabel(self.centralwidget)
        self.error_text_label.setGeometry(QtCore.QRect(850, 760, 241, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.error_text_label.sizePolicy().hasHeightForWidth())
        self.error_text_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.error_text_label.setFont(font)
        self.error_text_label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.error_text_label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.error_text_label.setAcceptDrops(False)
        self.error_text_label.setAccessibleName(_fromUtf8(""))
        self.error_text_label.setAccessibleDescription(_fromUtf8(""))
        self.error_text_label.setAutoFillBackground(False)
        self.error_text_label.setInputMethodHints(QtCore.Qt.ImhNone)
        self.error_text_label.setScaledContents(False)
        self.error_text_label.setWordWrap(False)
        self.error_text_label.setOpenExternalLinks(False)
        self.error_text_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.error_text_label.setObjectName(_fromUtf8("error_text_label"))
        self.error_label = QtGui.QLabel(self.centralwidget)
        self.error_label.setGeometry(QtCore.QRect(800, 750, 51, 51))
        self.error_label.setText(_fromUtf8(""))
        self.error_label.setPixmap(QtGui.QPixmap(_fromUtf8("Icons/beCareful.png")))
        self.error_label.setScaledContents(True)
        self.error_label.setObjectName(_fromUtf8("error_label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setEnabled(True)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1427, 25))
        self.menuBar.setDefaultUp(False)
        self.menuBar.setNativeMenuBar(True)
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuEssai = QtGui.QMenu(self.menuBar)
        self.menuEssai.setObjectName(_fromUtf8("menuEssai"))
        self.menuFigure = QtGui.QMenu(self.menuBar)
        self.menuFigure.setObjectName(_fromUtf8("menuFigure"))
        self.menuAbout = QtGui.QMenu(self.menuBar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionDd = QtGui.QAction(MainWindow)
        self.actionDd.setObjectName(_fromUtf8("actionDd"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSve_as = QtGui.QAction(MainWindow)
        self.actionSve_as.setObjectName(_fromUtf8("actionSve_as"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionRun = QtGui.QAction(MainWindow)
        self.actionRun.setObjectName(_fromUtf8("actionRun"))
        self.actionLog_file = QtGui.QAction(MainWindow)
        self.actionLog_file.setObjectName(_fromUtf8("actionLog_file"))
        self.actionDocumentation = QtGui.QAction(MainWindow)
        self.actionDocumentation.setObjectName(_fromUtf8("actionDocumentation"))
        self.menuEssai.addAction(self.actionOpen)
        self.menuEssai.addSeparator()
        self.menuEssai.addAction(self.actionRun)
        self.menuEssai.addSeparator()
        self.menuEssai.addAction(self.actionQuit)
        self.menuFigure.addAction(self.actionSave)
        self.menuFigure.addAction(self.actionSve_as)
        self.menuHelp.addAction(self.actionLog_file)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuBar.addAction(self.menuEssai.menuAction())
        self.menuBar.addAction(self.menuFigure.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Batch scripts and Reverse", None, QtGui.QApplication.UnicodeUTF8))
        self.run.setText(QtGui.QApplication.translate("MainWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.p_label.setText(QtGui.QApplication.translate("MainWindow", "P values :", None, QtGui.QApplication.UnicodeUTF8))
        self.execPath_label.setText(QtGui.QApplication.translate("MainWindow", "Executive path :", None, QtGui.QApplication.UnicodeUTF8))
        self.cpu_label.setText(QtGui.QApplication.translate("MainWindow", "Number of CPU :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("MainWindow", "Sens.", None, QtGui.QApplication.UnicodeUTF8))
        self.exec_path.setText(QtGui.QApplication.translate("MainWindow", "/home/boulefi/jude2_install/bin", None, QtGui.QApplication.UnicodeUTF8))
        self.title_label.setText(QtGui.QApplication.translate("MainWindow", "Set the Bio-optical parameters list :", None, QtGui.QApplication.UnicodeUTF8))
        self.particules_label.setText(QtGui.QApplication.translate("MainWindow", "Particules scaterring :", None, QtGui.QApplication.UnicodeUTF8))
        self.x_label.setText(QtGui.QApplication.translate("MainWindow", "x :", None, QtGui.QApplication.UnicodeUTF8))
        self.y_label.setText(QtGui.QApplication.translate("MainWindow", "y :", None, QtGui.QApplication.UnicodeUTF8))
        self.organic_label.setText(QtGui.QApplication.translate("MainWindow", "Organic absorption (CDOM Files) :", None, QtGui.QApplication.UnicodeUTF8))
        self.g_label.setText(QtGui.QApplication.translate("MainWindow", "g :", None, QtGui.QApplication.UnicodeUTF8))
        self.s_label.setText(QtGui.QApplication.translate("MainWindow", "s :", None, QtGui.QApplication.UnicodeUTF8))
        self.z_label.setText(QtGui.QApplication.translate("MainWindow", "Depth (z) :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "(m)", None, QtGui.QApplication.UnicodeUTF8))
        self.exec_path_button.setText(QtGui.QApplication.translate("MainWindow", "DIrectory", None, QtGui.QApplication.UnicodeUTF8))
        self.waveL_label.setText(QtGui.QApplication.translate("MainWindow", "Wavelengths :", None, QtGui.QApplication.UnicodeUTF8))
        self.phyto_label.setText(QtGui.QApplication.translate("MainWindow", "Phytoplankton absorption :", None, QtGui.QApplication.UnicodeUTF8))
        self.phyto_button.setText(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.phyto_path.setText(QtGui.QApplication.translate("MainWindow", "/home/boulefi/jude2_install/bin", None, QtGui.QApplication.UnicodeUTF8))
        self.bottom_label.setText(QtGui.QApplication.translate("MainWindow", "Bottom reflectance :", None, QtGui.QApplication.UnicodeUTF8))
        self.bottom_path.setText(QtGui.QApplication.translate("MainWindow", "/home/boulefi/jude2_install/bin", None, QtGui.QApplication.UnicodeUTF8))
        self.bottom_button.setText(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.verbose_label.setText(QtGui.QApplication.translate("MainWindow", "Verbose :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "(nm)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setText(QtGui.QApplication.translate("MainWindow", "(1 -> 6)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_32.setText(QtGui.QApplication.translate("MainWindow", "(-1 means query the number of CPUs)", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Plot tools (options) :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Curve\'s information :</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.column1_label.setText(QtGui.QApplication.translate("MainWindow", "column1_label :", None, QtGui.QApplication.UnicodeUTF8))
        self.column2_label.setText(QtGui.QApplication.translate("MainWindow", "column2_label :", None, QtGui.QApplication.UnicodeUTF8))
        self.column1_result.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.column2_result.setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.show_all_curves.setText(QtGui.QApplication.translate("MainWindow", "Show all curves", None, QtGui.QApplication.UnicodeUTF8))
        self.column3_label.setText(QtGui.QApplication.translate("MainWindow", "column3_label :", None, QtGui.QApplication.UnicodeUTF8))
        self.column5_label.setText(QtGui.QApplication.translate("MainWindow", "column5_label :", None, QtGui.QApplication.UnicodeUTF8))
        self.column6_label.setText(QtGui.QApplication.translate("MainWindow", "column6_label :", None, QtGui.QApplication.UnicodeUTF8))
        self.column7_label.setText(QtGui.QApplication.translate("MainWindow", "column7_label :", None, QtGui.QApplication.UnicodeUTF8))
        self.column8_label.setText(QtGui.QApplication.translate("MainWindow", "column8_label :", None, QtGui.QApplication.UnicodeUTF8))
        self.column3_result.setText(QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.column4_result.setText(QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.column5_result.setText(QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.column6_result.setText(QtGui.QApplication.translate("MainWindow", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.column7_result.setText(QtGui.QApplication.translate("MainWindow", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.column8_result.setText(QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.column4_label.setText(QtGui.QApplication.translate("MainWindow", "column4_label :", None, QtGui.QApplication.UnicodeUTF8))
        self.report_parameter_label.setText(QtGui.QApplication.translate("MainWindow", "Report parameter :", None, QtGui.QApplication.UnicodeUTF8))
        self.batch_name_label.setText(QtGui.QApplication.translate("MainWindow", "Batch name :", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("MainWindow", "Details :", None, QtGui.QApplication.UnicodeUTF8))
        self.McGee_radioButton.setText(QtGui.QApplication.translate("MainWindow", "McGEE 1999", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("MainWindow", "RadioButton", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_3.setText(QtGui.QApplication.translate("MainWindow", "RadioButton", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("MainWindow", "Tool (method) :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("MainWindow", "Deconvolution parameters :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("MainWindow", "s :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("MainWindow", "Particules scaterring :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("MainWindow", "(m)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("MainWindow", "y :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("MainWindow", "x :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("MainWindow", "P values :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setText(QtGui.QApplication.translate("MainWindow", "Wavelengths :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("MainWindow", "Organic absorption :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("MainWindow", "Depth (z) :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("MainWindow", "g :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_33.setText(QtGui.QApplication.translate("MainWindow", "Sens.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("MainWindow", "(nm)", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ReverseTab), QtGui.QApplication.translate("MainWindow", "Reverse", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel.setText(QtGui.QApplication.translate("MainWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.quit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.error_text_label.setText(QtGui.QApplication.translate("MainWindow", "You typed wrong values !", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEssai.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFigure.setTitle(QtGui.QApplication.translate("MainWindow", "Figure", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help !", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDd.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSve_as.setText(QtGui.QApplication.translate("MainWindow", "Save As ...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun.setText(QtGui.QApplication.translate("MainWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLog_file.setText(QtGui.QApplication.translate("MainWindow", "Log file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDocumentation.setText(QtGui.QApplication.translate("MainWindow", "Documentation", None, QtGui.QApplication.UnicodeUTF8))

from matplotlibwidgetFile import matplotlibWidget

from PyQt5 import QtCore, QtGui, QtWidgets


class TelaResultado(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1119, 698)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(33, 46, 46);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QtCore.QSize(700, 0))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame_7)
        self.frame_2.setStyleSheet("border: none;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setContentsMargins(20, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding-bottom: 10px;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.widget = QVideoWidget(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(640, 360))
        self.widget.setMaximumSize(QtCore.QSize(400, 230))
        self.widget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_3.setStyleSheet("border: none;\n"
"padding-top: 0px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_2.setMaximumSize(QtCore.QSize(40, 40))
        self.checkBox_2.setStyleSheet("QCheckBox{\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"    image: url(:/play/play.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover{\n"
"    image: url(:/play/play_hover.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"    image: url(:/play/pause.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover{\n"
"    image: url(:/play/pause_hover.png);\n"
"}\n"
"")
        self.checkBox_2.setText("")
        self.checkBox_2.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_2.addWidget(self.checkBox_2)
        self.horizontalSlider = QtWidgets.QSlider(self.frame_3)
        self.horizontalSlider.setMaximumSize(QtCore.QSize(640, 40))
        self.horizontalSlider.setSizeIncrement(QtCore.QSize(0, 0))
        self.horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 9px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: rgb(59, 31, 104);\n"
"height: 9px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"height: 9px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border-radius: 4px;\n"
"}")
        self.horizontalSlider.setPageStep(0)
        self.horizontalSlider.setSliderPosition(15)
        self.horizontalSlider.setTracking(True)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_2.addWidget(self.horizontalSlider)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setStyleSheet("border: none;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox = QtWidgets.QCheckBox(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("QCheckBox{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    width: 50px;\n"
"    height: 50px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"    image: url(:/checkbox/checbox_disable.png);\n"
"\n"
"    transition: 500ms;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"    image: url(:/checkbox/checbox_enable.png);\n"
"}")
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_3.addWidget(self.checkBox, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout.addWidget(self.frame_6)
        self.horizontalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.frame = QtWidgets.QFrame(self.frame_7)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 600))
        self.frame.setStyleSheet("border: none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 406, 582))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_titulo_pessoa = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_titulo_pessoa.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_titulo_pessoa.setFont(font)
        self.label_titulo_pessoa.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 38, 38);\n"
"padding: 8px;\n"
"border-radius: 10px;")
        self.label_titulo_pessoa.setObjectName("label_titulo_pessoa")
        self.verticalLayout_3.addWidget(self.label_titulo_pessoa)
        self.frame_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.formLayout = QtWidgets.QFormLayout(self.frame_5)
        self.formLayout.setContentsMargins(-1, -1, 20, -1)
        self.formLayout.setObjectName("formLayout")
        self.label_rsp_tempo = QtWidgets.QLabel(self.frame_5)
        self.label_rsp_tempo.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_rsp_tempo.setObjectName("label_rsp_tempo")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_rsp_tempo)
        self.label_tempo = QtWidgets.QLabel(self.frame_5)
        self.label_tempo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_tempo.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_tempo.setObjectName("label_tempo")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_tempo)
        self.label_rsp_velocidade = QtWidgets.QLabel(self.frame_5)
        self.label_rsp_velocidade.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_rsp_velocidade.setObjectName("label_rsp_velocidade")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_rsp_velocidade)
        self.label_velocidade = QtWidgets.QLabel(self.frame_5)
        self.label_velocidade.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_velocidade.setObjectName("label_velocidade")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_velocidade)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout_5.addWidget(self.frame_7)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "19 pessoas detectadas"))
        self.checkBox_2.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Iniciar/Pausar</span></p></body></html>"))
        self.checkBox.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Ativar analise frame a frame</span></p></body></html>"))
        self.checkBox.setText(_translate("MainWindow", "Analise frame a frame"))
        self.label_titulo_pessoa.setText(_translate("MainWindow", "Pessoa 01"))
        self.label_rsp_tempo.setText(_translate("MainWindow", "00:00:07.429"))
        self.label_tempo.setText(_translate("MainWindow", "Tempo no vídeo:"))
        self.label_rsp_velocidade.setText(_translate("MainWindow", " 2.5 pixels/frame"))
        self.label_velocidade.setText(_translate("MainWindow", "Velocidade: "))
from PyQt5.QtMultimediaWidgets import QVideoWidget
import create_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TelaResultado()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

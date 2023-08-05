# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_processando.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
import cv2

class TelaProcessamento(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1128, 698)
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
        self.centralwidget.setMinimumSize(QtCore.QSize(1000, 800))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.text_video_processando = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_video_processando.sizePolicy().hasHeightForWidth())
        self.text_video_processando.setSizePolicy(sizePolicy)
        self.text_video_processando.setMinimumSize(QtCore.QSize(0, 70))
        self.text_video_processando.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.text_video_processando.setFont(font)
        self.text_video_processando.setStyleSheet("color: rgb(239, 239, 239);")
        self.text_video_processando.setAlignment(QtCore.Qt.AlignCenter)
        self.text_video_processando.setObjectName("text_video_processando")
        self.verticalLayout.addWidget(self.text_video_processando)
        self.frame_video = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_video.sizePolicy().hasHeightForWidth())
        self.frame_video.setSizePolicy(sizePolicy)
        self.frame_video.setMaximumSize(QtCore.QSize(16777215, 380))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frame_video.setFont(font)
        self.frame_video.setStyleSheet("border: none;")
        self.frame_video.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_video.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_video.setObjectName("frame_video")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_video)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Criando o QLabel para exibir o frame de vídeo
        self.image_label = QLabel()
        self.image_label.setFixedSize(640, 330)
        self.image_label.setStyleSheet("background-color: black;")

        self.horizontalLayout.addWidget(self.image_label)
        self.verticalLayout.addWidget(self.frame_video)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 50))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setStyleSheet("border: none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(500, 30))
        self.progressBar.setMaximumSize(QtCore.QSize(500, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet("background-color: rgb(68, 88, 88);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(59, 31, 104);\n"
"\n"
"\n"
"")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_3.addWidget(self.progressBar)
        self.verticalLayout.addWidget(self.frame)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_3.setStyleSheet("border: none;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_cancelar = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_cancelar.sizePolicy().hasHeightForWidth())
        self.pushButton_cancelar.setSizePolicy(sizePolicy)
        self.pushButton_cancelar.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_cancelar.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.pushButton_cancelar.setFont(font)
        self.pushButton_cancelar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_cancelar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_cancelar.setAutoFillBackground(False)
        self.pushButton_cancelar.setStyleSheet("QPushButton{\n"
"    background: rgb(68, 88, 88);\n"
"    border-radius: 3px;\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    padding: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background: rgb(47, 61, 61);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.pushButton_cancelar.setAutoDefault(False)
        self.pushButton_cancelar.setDefault(False)
        self.pushButton_cancelar.setFlat(False)
        self.pushButton_cancelar.setObjectName("pushButton_cancelar")
        self.horizontalLayout_2.addWidget(self.pushButton_cancelar)
        self.verticalLayout.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def update_progress(self, frame, percent, people_count):
        # Converta o frame para o formato RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        height, width, _ = frame_rgb.shape
        bytes_per_line = 3 * width

        # atualizar o percentual de progresso
        self.progressBar.setValue(percent)

        q_image = QtGui.QImage(frame_rgb.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(q_image)
        self.image_label.setPixmap(pixmap)

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.text_video_processando.setText(_translate("MainWindow", "Seu vídeo está sendo processado"))
        self.pushButton_cancelar.setText(_translate("MainWindow", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TelaProcessamento()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

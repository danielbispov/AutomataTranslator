# -*- coding: utf-8 -*-
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from datetime import datetime

class Interface():
    def __init__(self):
        # Confiduração da janela principal
        self.app = QApplication(sys.argv)
        self.width = 800
        self.height = 480
        self.w = QWidget()
        self.w.setWindowTitle("AutomataTranslator")
        #self.w.setGeometry(100, 100, 800, 450)
        self.w.setFixedSize(self.width, self.height)
        self.center_widget()

        # Configuração da barra de menu
        self.menu_bar = QMenuBar(self.w)
        self.menu_opcoes = self.menu_bar.addMenu("Opcoes")
        self.sair = QAction("Sair", self.w)
        self.sair.triggered.connect(qApp.quit)
        self.abrir_arquivo = QAction("Abrir", self.w)
        self.abrir_arquivo.triggered.connect(self.open_read_file)
        self.salvar_arquivo = QAction("Salvar AFD Gerado", self.w)
        self.salvar_arquivo.triggered.connect(self.save_afd)
        self.menu_bar.adjustSize()

        self.menu_opcoes.addAction(self.abrir_arquivo)
        self.menu_opcoes.addAction(self.salvar_arquivo)
        self.menu_opcoes.addAction(self.sair)

        # Primeira caixa de texto(input)
        self.txt = QTextEdit(self.w)
        self.txt.setObjectName("text")
        self.txt.setText("Insira JSON aqui")
        self.txt.setGeometry(30, 40, 300, 360)

        # Segunda caixa de texto(output)
        self.out = QTextEdit(self.w)
        self.out.setReadOnly(True)
        self.out.setStyleSheet("background: #EBEBE4;")
        self.out.setObjectName("output")
        self.out.setGeometry(470, 40, 300, 360)

        # Botão para iniciar a conversão do input
        self.convert_button = QPushButton(self.w)
        self.convert_button.setObjectName("convert")
        self.convert_button.setText("Converter")
        self.convert_button.clicked.connect(self.button_convert)
        self.convert_button.move(686, 420)

        # Botão para limpar a caixa de texto "input"
        self.clear_button = QPushButton(self.w)
        self.clear_button.setObjectName("clear")
        self.clear_button.setText("Limpar Input")
        self.clear_button.clicked.connect(self.button_clear)
        self.clear_button.move(576, 420)

        self.w.show()
        sys.exit(self.app.exec_())

    def button_convert(self):
        texto = self.txt.toPlainText()
        return texto

    def button_clear(self):
        self.txt.setText("")

    def center_widget(self):
        resolution = QDesktopWidget().screenGeometry()
        self.w.move((resolution.width() / 2) - (self.width / 2),
                  (resolution.height() / 2) - (self.height / 2))

    def open_read_file(self):
        #fi_le = QFileDialog()
        file_path = QFileDialog().getOpenFileName(self.w, "Open File", "/home", "JSON (*.json)")
        with open(file_path, 'r') as my_file:
            data = my_file.read()

        self.txt.setText(data)

    def save_afd(self):
        afd_content = self.txt.toPlainText()
        save_path = QFileDialog().getSaveFileName(self.w, "Save File", "/home", "JSON (*.json)")
        print save_path
        with open(save_path + ".json", "w+") as afd:
            afd.write(afd_content)



interface = Interface()
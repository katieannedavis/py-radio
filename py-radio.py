import os
import sys
import xml.etree.ElementTree as ET
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
        QGroupBox, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTreeView, QVBoxLayout,
        QWidget, QButtonGroup) 
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtCore import Qt
from PyQt5.Qt import QRadioButton

file_name = 'Stations.xml'

dom = ET.parse(file_name)

stations = dom.findall('Stations')

sName = []
sGenre = []
sAddress = []

for c in stations:
    
    stationName = c.find('station_name').text
    stationGenre = c.find('station_genre').text
    stationAddress = c.find('station_address').text
    
    sName.append(stationName)
    sGenre.append(stationGenre)
    sAddress.append(stationAddress)
    
stationAddressDirectory = dict(zip(sName, sAddress))
stationGenreDirectory = dict(zip(sName, sGenre))   

class RadioButtonWidget(QWidget):
    """this class creates a group of radio buttons from a given list of labels"""
    
    #constructor
    def __init__(self, label, instruction, button_list):
        super().__init__() 
        
        self.title_label = QLabel(label)
        self.radio_group_box = QGroupBox(instruction)
        self.radio_button_group = QButtonGroup()
        
        #create the radio buttons
        self.radio_button_list = []
        for each in button_list:
            self. radio_button_list.append(QRadioButton(each))
        
        self.radio_button_list[0].setChecked(True)
        
        self.radio_button_layout = QVBoxLayout()
        
        counter = 1
        for each in self.radio_button_list:
            self.radio_button_layout.addWidget(each)
            self.radio_button_group.addButton(each)
            self.radio_button_group.setId(each, counter)
            counter += 1
        

class Radio(QWidget):
    def start_music(self, musicAddress):
        vlc_path = "C:\Program Files (x86)\VideoLAN\VLC"
        
        os.chdir(vlc_path)
        os.system("vlc -I dummy --dummy-quiet --one-instance " + musicAddress)
               
        
    def stop_music(self):
        vlc_path = "C:\Program Files (x86)\VideoLAN\VLC"
        
        os.chdir(vlc_path)
        os.system("vlc --one-instance vlc:quit")
        
    
    def playButton(self, music, location, name):
        startButton = QPushButton(name, self)
        startButton.setStyleSheet("font-size:12px;" 
                             "background-color:green;" 
                             "color:white;"
                             "border-style: outset;"
                             "border-width: 2px;"
                             "border-color: grey;"
                             "padding: 2px;")
        startButton.move(100, location)
        startButton.clicked.connect(lambda: self.start_music(music))
        
    def chooseStation(self, chosen):
        self.start_music(chosen)
                        
    def __init__(self):
        super().__init__()
        self.title = "Radio"
        self.left = 100
        self.top = 100
        self.width = 300
        self.height = 600
        self.setStyleSheet("background-color: silver;")
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        i = 10
        j = 0
        choice = " "
        NumGridRows = len(stationAddressDirectory.keys()) - 1
        NumButtons = len(stationAddressDirectory.keys())
        print(NumGridRows)
        for key in stationAddressDirectory:
            self.playButton(stationAddressDirectory[key], i, key)
            i = i + 50
            print(key, 'corresponds to', stationAddressDirectory[key], 'and', stationGenreDirectory[key])

        print(NumButtons)
        button2 = QPushButton('Stop Music', self)
        button2.setStyleSheet("font-size:19px;" 
                             "background-color:red;" 
                             "color:white;"
                             "border-style: outset;"
                             "border-width: 2px;"
                             "border-color: grey;"
                             "padding: 2px;")
        button2.move(150, 500)
        button2.clicked.connect(self.stop_music)
                  
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Radio()
    sys.exit(ex.exec_())

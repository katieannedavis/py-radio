import os
import sys
import xml.etree.ElementTree as ET
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
        QGroupBox, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTreeView, QVBoxLayout,
        QWidget) 
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtCore import Qt

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
        choice = " "
        for key in stationAddressDirectory:
            self.playButton(stationAddressDirectory[key], i, key)
            i = i + 50
            print(key, 'corresponds to', stationAddressDirectory[key], 'and', stationGenreDirectory[key])
        
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
    sys.exit(app.exec_())

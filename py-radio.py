from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
import subprocess
import sys
import xml.etree.ElementTree as ET

class Radio(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Py-Radio"
        self.left = 100
        self.top = 100
        self.width = 300
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createRadio()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        
    #Constructor function for radio
    def createRadio(self):
        file_name = 'Stations.xml'
        dom = ET.parse(file_name)
        stations = dom.findall('Stations')
        stationDict = {}
        
        for station in stations:
            stationName = station.find('station_name').text
            stationGenre = station.find('station_genre').text
            stationAddress = station.find('station_address').text
            stationDict.setdefault(stationName, []).append(stationGenre)
            stationDict.setdefault(stationName, []).append(stationAddress)

        radioStations = []
        radioGenre = []
        radioAddress = []
        
        for key in stationDict.keys():
            radioStations.append(key)
            radioGenre.append(stationDict[key][0])
            radioAddress.append(stationDict[key][1])

        self.horizontalGroupBox = QGroupBox("Radio")
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)

        i = 0
        for numberOfStations in radioStations:
            radiobutton = QRadioButton(radioStations[i])
            radiobutton.genre = radioGenre[i]
            radiobutton.address = radioAddress[i]
            radiobutton.toggled.connect(self.on_radio_button_toggled)
            layout.addWidget(radiobutton, i, 0)
            i += 1
            
        stopButton = QPushButton('Stop Music', self)
        stopButton.setStyleSheet("font-size:12px;" 
                             "background-color:red;" 
                             "color:white;"
                             "border-style: outset;"
                             "border-width: 1px;"
                             "border-color: grey;"
                             "padding: 1px;")
        
        stopButton.clicked.connect(self.stopRadio)
        layout.addWidget(stopButton, 0,2)

        self.horizontalGroupBox.setLayout(layout)

    # Stop radio on button click
    def stopRadio(self):
        vlc_path = "C:\Program Files (x86)\VideoLAN\VLC"
        os.chdir(vlc_path)
        subprocess.call("vlc --one-instance vlc:quit")

    # On radio button click, start playing radio station    
    def on_radio_button_toggled(self):
        choice = self.sender()
        
        if choice.isChecked() == True:
            
            vlc_path = "C:\Program Files (x86)\VideoLAN\VLC"

            os.chdir(vlc_path)
            subprocess.call("vlc -I dummy --dummy-quiet --one-instance " + choice.address)
            
if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = Radio()
    ex.show()
    sys.exit(app.exec_())

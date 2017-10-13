from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
import sys
import xml.etree.ElementTree as ET

class radio(QWidget):

    NumGridRows = 2
    def __init__(self):

        super(radio, self).__init__()

        '''https://github.com/Programmica/pyqt5-tutorial/blob/master/_examples/radiobutton.py'''
        layout = QGridLayout()
        self.setLayout(layout)
        self.createRadio(layout)
        
    def createRadio(self, setup):
        file_name = 'Stations.xml'
        dom = ET.parse(file_name)
        stations = dom.findall('Stations')
        stationDict = {}
        

        for c in stations:
            stationName = c.find('station_name').text
            stationGenre = c.find('station_genre').text
            stationAddress = c.find('station_address').text
            stationDict.setdefault(stationName, []).append(stationGenre)
            stationDict.setdefault(stationName, []).append(stationAddress)

        i = 0

        radioStations = []
        radioGenre = []
        radioAddress = []
        
        for key in stationDict.keys():
            radioStations.append(key)
            radioGenre.append(stationDict[key][0])
            radioAddress.append(stationDict[key][1])

        for n in radioStations:
            radiobutton = QRadioButton(radioStations[i])
            radiobutton.genre = radioGenre[i]
            radiobutton.address = radioAddress[i]
            radiobutton.toggled.connect(self.playRadio)
            setup.addWidget(radiobutton, 0, i)
            i += 1
        
    def playRadio(self):
        print("Radio played")

    def stopRadio():
        print("Radio stopped")
        
    def on_radio_button_toggled(self):
        radioSelected

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = radio()
    sys.exit(app.exec_())

#Written by Siddarth Sreeram
#Background information/data acquired from:
#https://www.kaggle.com/datasets/vinven7/comprehensive-database-of-minerals

# import necessary packages
from cProfile import label
from ctypes import Structure
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cm
from sklearn.metrics import r2_score
import scipy as spi
from tkinter import *
import tkinter as tk
from tkinter import simpledialog
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QGraphicsView, QLabel, QPlainTextEdit, QPushButton, QTextBrowser
from PyQt5 import uic
import sys
import seaborn as sn
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import os
import nest_asyncio

nest_asyncio.apply()


#use pandas to read CSV data - **Adjust to location of CSV on one's computer**
df=pd.read_csv("Minerals_Database.csv")

#main PyQt5 window
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        #Load the UI file
        uic.loadUi("Gem2GUI.ui", self)

        #define widgets
        self.label = self.findChild(QLabel, "label")
        self.backgroundTxt = self.findChild(QTextBrowser, "textBrowser")
        self.textedit = self.findChild(QPlainTextEdit, "plainTextEdit")
        self.button1 = self.findChild(QPushButton, "pushButton")
        self.button2 = self.findChild(QPushButton, "pushButton_2")
        self.button3 = self.findChild(QPushButton, "pushButton_3")
        self.graphics = self.findChild(QGraphicsView, "graphicsView")

        #button works
        self.button1.clicked.connect(self.corrMat)
        self.button2.clicked.connect(self.boxPlot)
        self.button3.clicked.connect(self.histograms)

        #show app
        self.setStyleSheet("background-color: lightGray;")
        self.show()

    #function for correlation matrix 
    def corrMat(self):
        plt.figure()
        plt.clf()
        plt.rcParams["figure.figsize"] = [7.50, 3.50]
        plt.rcParams["figure.autolayout"] = True
        plt.rcParams["font.size"] =6

        #creates data from dataframe
        data = {'Specific Gravity': df["Specific Gravity"],
        'Refractive Index': df["Refractive Index"],
        'Molar Mass': df["Molar Mass"],
        'Molar Volume': df["Molar Volume"],
        'Mohs Hardness': df["Mohs Hardness"]
        }

        df2=pd.DataFrame(data,columns=['Specific Gravity','Refractive Index','Molar Mass', 'Molar Volume', 'Mohs Hardness'])

        #creates the matrix
        corrMatrix = df2.corr()
        sn.heatmap(corrMatrix, annot=True)

        #displays the matrix
        plt.title("Correlation Matrix of Mineral Qualities", size=14)
        figManager = plt.get_current_fig_manager()
        figManager.window.showMaximized()
        plt.show(block=False)
        
    #function for making the boxplot 
    def boxPlot(self):
        plt.figure()
        plt.clf()
        plt.rcParams["figure.figsize"] = [7.50, 3.50]
        plt.rcParams["figure.autolayout"] = True
        plt.rcParams["font.size"] =6

        monoclinicArr=[]
        for i in range(0, len(df)):
            if df._get_value(i, 'Crystal Structure')==2:
                monoclinicArr.append(df._get_value(i, 'Mohs Hardness'))
        orthorombicArr=[]
        for i in range(0, len(df)):
            if df._get_value(i, 'Crystal Structure')==3:
                orthorombicArr.append(df._get_value(i, 'Mohs Hardness'))
        tetragonalArr=[]
        for i in range(0, len(df)):
            if df._get_value(i, 'Crystal Structure')==4:
                tetragonalArr.append(df._get_value(i, 'Mohs Hardness'))
        hexagonalArr=[]
        for i in range(0, len(df)):
            if df._get_value(i, 'Crystal Structure')==5:
                hexagonalArr.append(df._get_value(i, 'Mohs Hardness'))
        triclinicArr=[]
        for i in range(0, len(df)):
            if df._get_value(i, 'Crystal Structure')==1:
                triclinicArr.append(df._get_value(i, 'Mohs Hardness'))

        data = [monoclinicArr,
        triclinicArr,
        orthorombicArr,
        hexagonalArr,
        tetragonalArr
        ]

        plt.xlabel("Crystal Structure", size=14)
        plt.ylabel("Mohs Hardness", size=14)
        labels=["Monoclinic", "Triclinic", "Orthorombic", "Hexagonal", "Tetragonal"]
        plt.gca().set_xticklabels(labels)
        plt.boxplot(data)
        plt.title("Box and Whisker Plots of Mineral Structures' \nMohs Hardness Data", size=14)
        figManager = plt.get_current_fig_manager()
        figManager.window.showMaximized()
        plt.show(block=False)

    #method for making the layered histograms
    def histograms(self):
        plt.figure()
        plt.clf()
        plt.rcParams["figure.figsize"] = [7.50, 3.50]
        plt.rcParams["figure.autolayout"] = True
        plt.rcParams["font.size"] =6

        monoclinicArr=[]
        for i in range(0, len(df)):
            if df._get_value(i, 'Crystal Structure')==2:
                monoclinicArr.append(df._get_value(i, 'Mohs Hardness'))
        orthorombicArr=[]
        for i in range(0, len(df)):
            if df._get_value(i, 'Crystal Structure')==3:
                orthorombicArr.append(df._get_value(i, 'Mohs Hardness'))
        tetragonalArr=[]
        for i in range(0, len(df)):
            if df._get_value(i, 'Crystal Structure')==4:
                tetragonalArr.append(df._get_value(i, 'Mohs Hardness'))
        hexagonalArr=[]
        for i in range(0, len(df)):
            if df._get_value(i, 'Crystal Structure')==5:
                hexagonalArr.append(df._get_value(i, 'Mohs Hardness'))
        triclinicArr=[]
        for i in range(0, len(df)):
            if df._get_value(i, 'Crystal Structure')==1:
                triclinicArr.append(df._get_value(i, 'Mohs Hardness'))

        plt.hist(monoclinicArr, bins=15, alpha=0.5, label="Monoclinic")
        plt.hist(orthorombicArr, bins=15, alpha=0.5, label="Orthombic")
        plt.hist(tetragonalArr, bins=15, alpha=0.5, label="Tetragonal")
        plt.hist(hexagonalArr, bins=15, alpha=0.5, label="Hexagonal")
        plt.hist(triclinicArr, bins=15, alpha=0.5, label="Triclinic")
        plt.xlabel("Mohs Hardness", size=14) 
        plt.ylabel("Count", size=14) 
        plt.title("Histograms of Mineral Structures' Mohs Hardness Data", size=14)
        plt.legend(loc='upper right')
        result=(spi.stats.kruskal(monoclinicArr, orthorombicArr, tetragonalArr, hexagonalArr, triclinicArr))
        plt.text(0.75, 25, "Kruskal-Wallis test results:\np-value: "+str(round(result.pvalue,3))+"\n"+"statistic: "+str(round(result.statistic,3)), size=14)
        figManager = plt.get_current_fig_manager()
        figManager.window.showMaximized()
        plt.show(block=False)

#initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 16:34:17 2021

@author: vazquez
"""

import numpy as np

#csv-Datei (comma-separated values) wird eingelesen:
data = np.loadtxt('magic_matrix.csv', delimiter=',')



#1_Berechnen Sie die Summe aller Elemente:
summe = np.sum(data)



#2_Berechnen Sie die Position des größten und des kleinsten Elements in der Matrix:
    #Zuerst werden min und max Werte gesucht:
mini=data.min()
maxi=data.max()

    #Jetzt wird die Position dieser Werte untersucht:
loc_mini = np.where(data == mini) #np.where(conditional, out[ut if true, output if false])
loc_maxi = np.where(data == maxi)

print("Min: " + str(mini) + " Zeile: " + str(int(loc_mini[0])) + " Spalte: " + str(int(loc_mini[1])))
print("Max: " + str(maxi) + " Zeile: " + str(int(loc_maxi[0])) + " Spalte: " + str(int(loc_maxi[1])))

    #warum loc_max[0][0] ? Ist so, weil loc_max = [[x1_zeile,...],
    #                                              [x1_spalte,...] ]   



#3_Spaltenvektor v_1 bestehend aus 3 Spalte von Matrix A:
v_1 = data[:,2]
v_1 = v_1.reshape(v_1.shape[0], 1)
    #Um Zeilenvektor zu machen: v_1.reshape(1,9)
print("Spaltenvektor v_1 bestehend aus 3 Spalte von Matrix A: " + str(v_1))



#4_Summe aller Elemente > 40:
summe_40 = np.sum(data[np.where(data>79)])
print("Summe aller Elemente, die groesser als 40 sind, lautet: " + str(summe_40))



#5_Zeilenvektor v_2 bestehen aus A3,4 bis A7,4:
v_2 = data[3-1:7, 4-1]
v_2 = v_2.reshape(1, v_2.shape[0])
print("Zeilenvektor bestehend aus A3,4 bis A7,4: " + str(v_2))
    
    
    
    
    
    
    
    

from ROOT import *
from array import array

maxn=4 #Number of points
file     = TFile( 'data_file.root', 'recreate' )
tree     = TTree( 'data_tree', 'data_tree' )
date     = array( 'i', 6*[0]) 
speed    = array( 'f', maxn*[0.])
direction= array( 'f', maxn*[0.])
actual   = array( 'f', [0.]) 

tree.Branch('date',date,'date[6]/I')
tree.Branch('speed',speed,'speed[4]/F')
tree.Branch('direction',direction,'direction[4]/F')
tree.Branch('actual',actual,'actual[1]/F')
#####READ the file and fill the tree
with open('WindPower_PythonTest.csv') as file_res:
#with open('test_File.csv') as file_res:#just a test file
    next(file_res) #skip the first line 
    for line in file_res:  #Line is a string 
        data_string = line.split(',')  
        #print data_string[0]  #
        date_ =TDatime(data_string[0])
        date[0] =date_.GetYear()
        date[1] =date_.GetMonth()
        date[2] =date_.GetDay()
        date[3] =date_.GetHour()
        date[4] =date_.GetMinute()
        date[5] =date_.GetSecond()
        speed[0]=float(data_string[1])
        speed[1]=float(data_string[2])
        speed[2]=float(data_string[3])
        speed[3]=float(data_string[4])
        direction[0]=float(data_string[5])
        direction[1]=float(data_string[6])
        direction[2]=float(data_string[7])
        direction[3]=float(data_string[8])
        try:
            actual[0]      =float(data_string[9])
        except ValueError:
            actual[0]      =-999.
        #print actual[0]
        #Filling the tree
        if actual[0] == -999:
            continue
        tree.Fill()

file.Write()
file.Close()


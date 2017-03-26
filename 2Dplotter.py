import ROOT
import numpy as np
ROOT.gSystem.Load("rootlogon_C.so")
ROOT.rootlogon()

file=ROOT.TFile('data_file.root','READ')
tree=file.Get("data_tree")

#list_direction = []
#list_speed     = []
#list_actual    = []
#for entry in tree:
#    #if entry.actual == -999:   
#    #    continue
#    list_direction.append(entry.direction[0])
#    list_speed.append(entry.speed[0])
#    list_actual.append(entry.actual)
#
#g=ROOT.TGraph2D(len(list_actual),np.asarray(list_speed),np.asarray(list_direction),np.asarray(list_actual))
#c1=ROOT.TCanvas()
#g.Draw()
#g.SaveAs("actual_distribution.root")
#c1.SaveAs("Plots/graph_2d.png")

c2=ROOT.TCanvas()
h2D=ROOT.TH2F("h2D","h2D",60,0,30,2,0,360)
h2D=ROOT.TH2F("h2D","h2D",60,0,30,12,0,360)
h2D=ROOT.TH2F("h2D","h2D",60,0,30,24,0,360)
tree.Draw("direction[1]:speed[1]>>h2D")
h2D.GetXaxis().SetTitle("speed [m/s]")
h2D.GetYaxis().SetTitle("direction")
h2D.Draw("lego")
h2D.SaveAs("2d.root")
c2.SaveAs("Plots/2D_histo.png")




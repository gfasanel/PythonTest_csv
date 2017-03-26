import ROOT
ROOT.gSystem.Load("rootlogon_C.so")
ROOT.rootlogon()

file=ROOT.TFile('test.root','READ')
tree=file.Get("TrainTree")

bins=250
minx=0
maxx=5000
pred_=ROOT.TH1F("pred_","pred_",bins,minx,maxx)
real_=ROOT.TH1F("real_","real_",bins,minx,maxx)
diff_2=ROOT.TH1F("diff_2","diff_2",100,-0.02,0.02)
diff_3=ROOT.TH1F("diff_3","diff_3",400,-0.0004,0.0004) #Normalized difference
corr  =ROOT.TH2F("corr","corr",250,0,5000,250,0,5000)

#Closure test of the model
tree.Draw("BDT>>pred_")
tree.Draw("actual>>real_")
c1=ROOT.TCanvas()
real_.SetLineColor(ROOT.kBlack)
pred_.SetLineColor(ROOT.kRed)
pred_.GetXaxis().SetTitle("actual [kW]")
pred_.GetYaxis().SetTitle("Number of events")
leg=ROOT.TLegend(0.6,0.6,0.82,0.82)
pred_.DrawNormalized()
real_.DrawNormalized("same")
leg.AddEntry(pred_,"model","l")
leg.AddEntry(real_,"data (1st half)","l")
leg.Draw("same")
c1.SetLogy()
c1.SaveAs("Plots/model_closure.png")


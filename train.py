import ROOT
 
ROOT.TMVA.Tools.Instance()
 
fout = ROOT.TFile("test.root","RECREATE")

file_in=ROOT.TFile.Open("data_file.root")
mytree = file_in.Get("data_tree")
 
factory = ROOT.TMVA.Factory("FasanellaRegr", fout,
                            ":".join([
                                "!V",
                                "!Silent",
                                "Color",
                                "DrawProgressBar",
                                "Transformations=I;D;P;G,D"]
                                #"AnalysisType=Classification"]
                                     ))
factory.AddRegressionTree(mytree)

factory.AddVariable("date[3]","I") #date[3]==hour
factory.AddVariable("speed[0]","F")
factory.AddVariable("speed[1]","F") 
factory.AddVariable("speed[2]","F") 
factory.AddVariable("speed[3]","F") 
factory.AddVariable("direction[0]","F") 
factory.AddVariable("direction[1]","F") 
factory.AddVariable("direction[2]","F") 
factory.AddVariable("direction[3]","F") 

factory.AddTarget("actual") #you want to predict the actual

# cuts defining the signal and background sample
myCut = ROOT.TCut("")
 
factory.PrepareTrainingAndTestTree(myCut,   # signal events
                                   ":".join([
                                        "SplitMode=Block",
                                        "nTrain_Regression=9000",
                                        "nTest_Regression=9526",
                                        #"nTrain_Regression=13000",
                                        #"nTest_Regression=5526",
                                       ]))

#First attempt
#method = factory.BookMethod(ROOT.TMVA.Types.kPDERS, "PDERS", "VolumeRangeMode=MinMax" )

#Boost-Decision-Tree
method = factory.BookMethod(ROOT.TMVA.Types.kBDT, "BDT",":".join(["NTrees=800","!H","!V","BoostType=Grad", ]))
 
factory.TrainAllMethods()
factory.TestAllMethods()
factory.EvaluateAllMethods()

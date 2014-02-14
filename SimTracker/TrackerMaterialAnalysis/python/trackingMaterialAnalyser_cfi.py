import FWCore.ParameterSet.Config as cms

trackingMaterialAnalyser = cms.EDAnalyzer("TrackingMaterialAnalyser",
    MaterialAccounting      = cms.InputTag("trackingMaterialProducer"),
    SplitMode               = cms.string("NearestLayer"),
    SkipBeforeFirstDetector = cms.bool(False),
    SkipAfterLastDetector   = cms.bool(True),
    SaveSummaryPlot         = cms.bool(True),
    SaveDetailedPlots       = cms.bool(False),
    SaveParameters          = cms.bool(True),
    SaveXML                 = cms.bool(True),
    Groups = cms.vstring(
        'TrackerRecMaterialPixelBarrelLayer0_Z0', 
        'TrackerRecMaterialPixelBarrelLayer0_Z20', 
        'TrackerRecMaterialPixelBarrelLayer1_Z0', 
        'TrackerRecMaterialPixelBarrelLayer1_Z20', 
        'TrackerRecMaterialPixelBarrelLayer2_Z0', 
        'TrackerRecMaterialPixelBarrelLayer2_Z20', 
        'TrackerRecMaterialTIBLayer0', 
        'TrackerRecMaterialTIBLayer1_Z0', 
        'TrackerRecMaterialTIBLayer1_Z50', 
        'TrackerRecMaterialTIBLayer2_Z0', 
        'TrackerRecMaterialTIBLayer2_Z55', 
        'TrackerRecMaterialTIBLayer3', 
        'TrackerRecMaterialTOBLayer0_Z0', 
        'TrackerRecMaterialTOBLayer0_Z10', 
        'TrackerRecMaterialTOBLayer0_Z70', 
        'TrackerRecMaterialTOBLayer1_Z0', 
        'TrackerRecMaterialTOBLayer1_Z90', 
        'TrackerRecMaterialTOBLayer2_Z0', 
        'TrackerRecMaterialTOBLayer2_Z20', 
        'TrackerRecMaterialTOBLayer2_Z90', 
        'TrackerRecMaterialTOBLayer3_Z0', 
        'TrackerRecMaterialTOBLayer3_Z20', 
        'TrackerRecMaterialTOBLayer3_Z30', 
        'TrackerRecMaterialTOBLayer3_Z90', 
        'TrackerRecMaterialTOBLayer4_Z0', 
        'TrackerRecMaterialTOBLayer4_Z20', 
        'TrackerRecMaterialTOBLayer4_Z30', 
        'TrackerRecMaterialTOBLayer5_Z0', 
        'TrackerRecMaterialTOBLayer5_Z20', 
        'TrackerRecMaterialTOBLayer5_Z30', 
        'TrackerRecMaterialPixelEndcapDisk1_R0', 
        'TrackerRecMaterialPixelEndcapDisk1_R7', 
        'TrackerRecMaterialPixelEndcapDisk1_R11', 
        'TrackerRecMaterialPixelEndcapDisk2', 
        'TrackerRecMaterialTIDDisk1', 
        'TrackerRecMaterialTIDDisk2_R0', 
        'TrackerRecMaterialTIDDisk2_R40', 
        'TrackerRecMaterialTIDDisk3_R0', 
        'TrackerRecMaterialTIDDisk3_R30', 
        'TrackerRecMaterialTECDisk0_R0', 
        'TrackerRecMaterialTECDisk0_R30', 
        'TrackerRecMaterialTECDisk0_R60', 
        'TrackerRecMaterialTECDisk1_R0', 
        'TrackerRecMaterialTECDisk1_R30', 
        'TrackerRecMaterialTECDisk2_R0', 
        'TrackerRecMaterialTECDisk2_R30', 
        'TrackerRecMaterialTECDisk3', 
        'TrackerRecMaterialTECDisk4', 
        'TrackerRecMaterialTECDisk5_R0', 
        'TrackerRecMaterialTECDisk5_R40', 
        'TrackerRecMaterialTECDisk6', 
        'TrackerRecMaterialTECDisk7_R0', 
        'TrackerRecMaterialTECDisk7_R50', 
        'TrackerRecMaterialTECDisk8_R0', 
        'TrackerRecMaterialTECDisk8_R80', 
        'TrackerRecMaterialTECDisk8_R90'
    )
)

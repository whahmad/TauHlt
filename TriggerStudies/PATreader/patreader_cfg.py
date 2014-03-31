import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring(
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_10_1_sFh.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_11_1_ebQ.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_12_1_uks.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_13_1_LEO.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_14_1_puW.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_15_1_c90.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_16_1_FZq.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_17_1_7Lr.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_18_1_uoA.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_19_1_4VM.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_1_1_we1.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_20_1_GF7.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_2_1_ym8.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_3_1_xWa.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_4_1_TKW.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_5_1_kpG.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_6_1_bFE.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_7_1_FgY.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_8_1_YG3.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_9_1_h3h.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_10_1_GSv.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_11_1_0iH.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_12_1_HCO.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_13_1_eJd.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_14_1_TQF.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_15_1_Ry8.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_16_1_8sv.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_17_1_TRc.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_18_1_yfO.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_1_1_jgu.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_2_1_mgR.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_3_1_jnu.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_4_1_ZU5.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_5_1_fWq.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_6_1_Djv.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_7_1_jSQ.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_8_1_ZOv.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_9_1_5F8.root',
  )
)

process.low1p0high10pow2 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(1.0) ,
  upperPtThreshold = cms.double(10.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(2. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)

process.low1p0high20pow2 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(1.0) ,
  upperPtThreshold = cms.double(20.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(2. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)

process.low1p0high00pow2 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(1.0) ,
  upperPtThreshold = cms.double(-1.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(2. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)

process.low1p0high10pow4 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(1.0) ,
  upperPtThreshold = cms.double(10.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(4. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)

process.low1p0high20pow4 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(1.0) ,
  upperPtThreshold = cms.double(20.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(4. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)

process.low1p0high00pow4 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(1.0) ,
  upperPtThreshold = cms.double(-1.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(4. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)


process.low1p0high10pow6 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(1.0) ,
  upperPtThreshold = cms.double(10.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(6. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)

process.low1p0high20pow6 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(1.0) ,
  upperPtThreshold = cms.double(20.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(6. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)

process.low1p0high00pow6 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(1.0) ,
  upperPtThreshold = cms.double(-1.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(6. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)


process.low1p5high10pow2 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(1.5) ,
  upperPtThreshold = cms.double(10.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(2. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)

process.low1p5high20pow2 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(1.5) ,
  upperPtThreshold = cms.double(20.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(2. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)

process.low1p5high10pow4 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(1.5) ,
  upperPtThreshold = cms.double(10.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(4. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)

process.low1p5high20pow4 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(1.5) ,
  upperPtThreshold = cms.double(20.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(4. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)

process.low1p5high10pow6 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(1.5) ,
  upperPtThreshold = cms.double(10.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(6. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)

process.low1p5high20pow6 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(1.5) ,
  upperPtThreshold = cms.double(20.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(6. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)

process.low2p0high10pow2 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(2.0) ,
  upperPtThreshold = cms.double(10.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(2. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)

process.low2p0high20pow2 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(2.0) ,
  upperPtThreshold = cms.double(20.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(2. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)

process.low2p0high10pow4 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(2.0) ,
  upperPtThreshold = cms.double(10.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(4. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)

process.low2p0high20pow4 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(2.0) ,
  upperPtThreshold = cms.double(20.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(4. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)

process.low2p0high10pow6 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(2.0) ,
  upperPtThreshold = cms.double(10.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(6. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)

process.low2p0high20pow6 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(2.0) ,
  upperPtThreshold = cms.double(20.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(6. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)

process.low2p5high10pow2 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(2.5) ,
  upperPtThreshold = cms.double(10.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(2. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)

process.low2p5high20pow2 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(2.5) ,
  upperPtThreshold = cms.double(20.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(2. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)

process.low2p5high10pow4 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(2.5) ,
  upperPtThreshold = cms.double(10.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(4. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)

process.low2p5high20pow4 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(2.5) ,
  upperPtThreshold = cms.double(20.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(4. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)

process.low2p5high10pow6 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(2.5) ,
  upperPtThreshold = cms.double(10.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(6. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)

process.low2p5high20pow6 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(2.5) ,
  upperPtThreshold = cms.double(20.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(6. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)

process.low3p0high10pow2 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(3.0) ,
  upperPtThreshold = cms.double(10.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(2. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)

process.low3p0high20pow2 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(3.0) ,
  upperPtThreshold = cms.double(20.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(2. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)

process.low3p0high10pow4 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(3.0) ,
  upperPtThreshold = cms.double(10.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(4. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)

process.low3p0high20pow4 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(3.0) ,
  upperPtThreshold = cms.double(20.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(4. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)

process.low3p0high10pow6 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(3.0) ,
  upperPtThreshold = cms.double(10.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(6. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)

process.low3p0high20pow6 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(3.0) ,
  upperPtThreshold = cms.double(20.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(6. ) ,
  enhanceWeight    = cms.int32 (-1 ) ,
  verbose          = cms.bool(False) ,
)







process.weightMoreTheFirst2TracksLow2p5high10pow2 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(2.5) ,
  upperPtThreshold = cms.double(10.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(2. ) ,
  enhanceWeight    = cms.int32 (2  ) ,
  verbose          = cms.bool(False) ,
)

process.weightMoreTheFirst2TracksLow2p5high10pow4 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(2.5) ,
  upperPtThreshold = cms.double(10.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(4. ) ,
  enhanceWeight    = cms.int32 (2  ) ,
  verbose          = cms.bool(False) ,
)

process.weightMoreTheFirst4TracksLow2p5high10pow2 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(2.5) ,
  upperPtThreshold = cms.double(10.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(2. ) ,
  enhanceWeight    = cms.int32 (4  ) ,
  verbose          = cms.bool(False) ,
)

process.weightMoreTheFirst4TracksLow2p5high10pow4 = cms.EDAnalyzer(
  'PATreader'                        ,
  lowerPtThreshold = cms.double(2.5) ,
  upperPtThreshold = cms.double(10.) ,
  maxZDistance     = cms.double(0.2) ,
  power            = cms.double(4. ) ,
  enhanceWeight    = cms.int32 (4  ) ,
  verbose          = cms.bool(False) ,
)


process.p = cms.Path(
  process.weightMoreTheFirst2TracksLow2p5high10pow2 +
  process.weightMoreTheFirst2TracksLow2p5high10pow4 +
  process.weightMoreTheFirst4TracksLow2p5high10pow2 +
  process.weightMoreTheFirst4TracksLow2p5high10pow4 +
  process.low1p0high10pow2 +
  process.low1p0high20pow2 +
  process.low1p0high00pow2 +
  process.low1p0high10pow4 +
  process.low1p0high20pow4 +
  process.low1p0high00pow4 +
  process.low1p0high10pow6 +
  process.low1p0high20pow6 +
  process.low1p0high00pow6 +
  process.low1p5high10pow2 +
  process.low1p5high20pow2 +
  process.low1p5high10pow4 +
  process.low1p5high20pow4 +
  process.low1p5high10pow6 +
  process.low1p5high20pow6 +
  process.low2p0high10pow2 +
  process.low2p0high20pow2 +
  process.low2p0high10pow4 +
  process.low2p0high20pow4 +
  process.low2p0high10pow6 +
  process.low2p0high20pow6 +
  process.low2p5high10pow2 +
  process.low2p5high20pow2 +
  process.low2p5high10pow4 +
  process.low2p5high20pow4 +
  process.low2p5high10pow6 +
  process.low2p5high20pow6 +
  process.low3p0high10pow2 +
  process.low3p0high20pow2 +
  process.low3p0high10pow4 +
  process.low3p0high20pow4 +
  process.low3p0high10pow6 +
  process.low3p0high20pow6 
  )

process.TFileService = cms.Service(
  "TFileService"                          ,
  fileName      = cms.string("test.root") ,
  closeFileFast = cms.untracked.bool(False)
)


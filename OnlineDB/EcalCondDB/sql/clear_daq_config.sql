DROP VIEW ECAL_RUN_CONFIGURATION;
DROP VIEW ECAL_SEQUENCE;
DROP VIEW ECAL_CYCLE;
DROP view ECAL_SCAN ;


DROP TABLE ECAL_CCS_CYCLE ;
DROP TABLE ECAL_DCC_CYCLE ;
DROP TABLE ECAL_srp_CYCLE ;
DROP TABLE ECAL_LASER_CYCLE; 
DROP TABLE ECAL_TCC_CYCLE ;
DROP TABLE ECAL_TTCCI_CYCLE; 
DROP TABLE ECAL_LTC_CYCLE ;
DROP TABLE ECAL_LTS_CYCLE ;
DROP TABLE ECAL_JBH4_CYCLE ;
DROP TABLE ECAL_SCAN_CYCLE ;
DROP TABLE ECAL_ttcf_CYCLE ;
DROP TABLE ECAL_dcu_CYCLE ;

DROP TABLE ECAL_CCS_CONFIGURATION; 
DROP TABLE ECAL_DCC_CONFIGURATION ;
DROP TABLE ECAL_SRP_CONFIGURATION ;
DROP TABLE ECAL_LASER_CONFIGURATION; 
DROP TABLE ECAL_TCC_CONFIGURATION ;
DROP TABLE ECAL_TTCCI_CONFIGURATION; 
DROP TABLE ECAL_LTC_CONFIGURATION ;
DROP TABLE ECAL_LTS_CONFIGURATION ;
DROP TABLE ECAL_JBH4_CONFIGURATION ;
DROP TABLE ECAL_ttcf_CONFIGURATION ;
DROP TABLE ECAL_dcu_CONFIGURATION ;
DROP TABLE ECAL_SCAN_DAT ;

DROP TABLE ECAL_CYCLE_DAT ;
DROP TABLE ECAL_SEQUENCE_DAT ;
DROP TABLE ECAL_RUN_CONFIGURATION_DAT ;


DROP TABLE ECAL_SCAN_DEF ;
DROP TRIGGER ecal_sequence_insert;
drop  SEQUENCE run_type_def_sq ;
DROP trigger run_type_def_trg;
drop function get_run_type_def_id;
drop table RUN_TYPE_DEF;
DROP TABLE ECAL_RUN_MODE_DEF; 
DROP TABLE ECAL_SEQUENCE_TYPE_DEF; 
DROP SEQUENCE ecal_run_mode_def_sq; 
DROP trigger ecal_run_mode_def_trg;

drop function get_run_mode_def_id;
drop function get_run_conf_id;
DROP FUNCTION get_sequence_type_def_id;
drop function get_sequence_id;


DROP SEQUENCE ecal_sequence_dat_sq; 
DROP SEQUENCE ecal_cycle_dat_sq ;
DROP SEQUENCE ecal_CCS_CONFIG_sq ;
DROP SEQUENCE ecal_SRP_CONFIG_sq ;
DROP SEQUENCE ecal_DCC_CONFIG_sq ;
DROP SEQUENCE ecal_run_sq ;
DROP SEQUENCE ecal_sequence_type_def_sq; 
DROP SEQUENCE ecal_JBH4_CONFIG_sq ;
DROP SEQUENCE ecal_scan_def_sq ;
DROP SEQUENCE ecal_scan_config_sq ;
DROP SEQUENCE ecal_dcu_config_sq ;
DROP SEQUENCE ecal_LTS_CONFIG_sq; 
DROP SEQUENCE ecal_LTC_CONFIG_sq ;
DROP SEQUENCE ecal_TTCCI_CONFIG_sq; 
DROP SEQUENCE ecal_TCC_CONFIG_sq ;
DROP SEQUENCE ecal_TtCf_CONFIG_sq ;
DROP SEQUENCE ecal_LASER_CONFIG_sq; 

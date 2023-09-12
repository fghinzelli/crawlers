#!/bin/bash
PRC_PATH=''
export PRC_URL_BASE='https://www.procergs.rs.gov.br/concurso-publico-2023'
export PRC_FILE_NAME=${PRC_PATH}'/crawler-procergs.txt'
export PRC_EMAIL_ORIGIN=''
export PRC_SMTP_SERVER=''
export PRC_DESTINATION_LIST=''
python3 ${PRC_PATH}/crawler-procergs.py

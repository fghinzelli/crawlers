#!/bin/bash
PRC_PATH=''
export SERPRO_URL_BASE='https://www.cebraspe.org.br/concursos/serpro_23'
export SERPRO_URL_JSON='https://api.cebraspe.org.br/eventos/serpro_23'
export SERPRO_FILE_NAME=${PRC_PATH}'/crawler-serpro.txt'
export SERPRO_EMAIL_ORIGIN=''
export SERPRO_SMTP_SERVER=''
export SERPRO_DESTINATION_LIST=''
python3 ${PRC_PATH}/crawler-serpro.py

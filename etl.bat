@echo off
title Fluxo de Dados Axis - Excel para SQL
echo [PASSO 1] Abrindo Excel... aguardando edicao terminar...

:: Abre o Excel e o BAT fica esperando voce fechar
start /wait "" "axis.xlsx"

echo.
echo [PASSO 2] Excel fechado. Aguardando 2s para o arquivo ser liberado...
timeout /t 2 /nobreak > nul

echo.
echo [PASSO 3] Iniciando Python (Limpando e enviando para o SQL)...
python axis_etl.py

echo.
echo ==========================================
echo [SUCESSO] Banco de Dados Atualizado!
echo Agora e so clicar em 'Atualizar' no Power BI.
echo ==========================================
pause
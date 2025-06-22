# Arquivo que sera usado para somente chamar a função menu e rodar o jogo

### comando para cria o executavel do jogo
import os, sys
dirpath = os.getcwd()
sys.path.append(dirpath)
if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)
###

import TelaMenu

TelaMenu.menu()

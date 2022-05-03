from genericpath import exists
import os
import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()    
data=cursor.execute('''SELECT * FROM core_holerite''')
def criar_pasta():
    for linha in data:
        mes = linha[1]
        ano = linha[2]
        dir = r"C:/Users/Sandro Bispo/Desktop/APONTAMENTOS/core/F0001/"
        if not exists(dir + str(ano)+'_'+ mes):
            os.mkdir(dir + str(ano)+'_'+ mes)

criar_pasta()

os.chdir(r"C:/Users/Sandro Bispo/Desktop/APONTAMENTOS/media/PDF/HOLERITE")
os.listdir()
for f in os.listdir():
    ano = f[4:8]
    mes = f[9:12]
    nome = ano+'_' +mes
    if nome in f:
        os.chdir(r"C:/Users/Sandro Bispo/Desktop/APONTAMENTOS/media/PDF/HOLERITE/")
        novo = os.listdir()
        for i in novo:
            os.chdir(r"C:/Users/Sandro Bispo/Desktop/APONTAMENTOS/media/PDF/HOLERITE/"+ str(novo[0]))
            nome_func = os.listdir()
        print(nome_func)
              
# # ir até a pasta que desejo loopar
# os.chdir(r"C:\Users\Sandro Bispo\Desktop\APONTAMENTOS\media\PDF\HOLERITE\PDF_2011_Abr_230420222036")

# # para cada Arquivo na lista de arquivos do diretório "List Dir"
# # imprimo o nome do arquivo
# os.listdir()

# for f in os.listdir():
#     os.rename(f,r"C:/Users/Sandro Bispo/Desktop/APONTAMENTOS/media/PDF/F0001/ "+f)
    
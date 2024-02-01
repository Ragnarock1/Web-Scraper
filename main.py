from betano import *
from unibet.testSuperbet import *
import multiprocessing as mp
    

def ceva():
    tabelSuperbet = []
    tabelBetano = []
    tabelSuperbet = superbet('https://superbet.ro/pariuri-sportive/fotbal/argentina/argentina-supercupa')
    tabelBetano = betano('https://ro.betano.com/sport/fotbal/argentina/super-cupa/181903r/')

    
    for i in range(len(tabelSuperbet)):
        for j in range(len(tabelBetano)):
            if(tabelSuperbet[i][1] in tabelBetano[j][1] and tabelSuperbet[i][2] in tabelBetano[j][2] and tabelSuperbet[i][3] in tabelBetano[j][3]):
                if(float(float(tabelSuperbet[i][4])) >= float(float(tabelBetano[j][4]))):
                    if(float(float(tabelSuperbet[i][5])) >= float(float(tabelBetano[j][5]))):
                        if(float(float(tabelSuperbet[i][6])) >= float(float(tabelBetano[j][6]))):
                            print("Not worth the trouble")
                        else:
                            val2 = float(float(tabelBetano[j][6])) 
                            val1 = float(float(tabelSuperbet[i][5]))
                            valx = float(tabelSuperbet[i][5])
                            result = 1/val2 + 1/val1 + 1/valx
                            if(result < 1): print(result)

if __name__ == "__main__":
    
    
    tabelSuperbet = []
    tabelBetano = []
    tabelSuperbet = superbet('https://superbet.ro/pariuri-sportive/fotbal/brazilia/brazilia-cupa')
    tabelBetano = betano('https://ro.betano.com/sport/fotbal/brazilia/copa-betano-do-brasil/10008r/')

    
    for i in range(len(tabelSuperbet)):
        for j in range(len(tabelBetano)):
            ###Verificam daca exista acelasi meci in ambele site-uri(ora, echipa1, echipa2)
            if(len(tabelBetano[j][2])<= len(tabelSuperbet[i][2])):
                substringEchipa1 = tabelBetano[j][2]
                stringEchipa1 = tabelSuperbet[i][2]
                if(len(tabelBetano[j][3])<= len(tabelSuperbet[i][3])):
                    substringEchipa2 = tabelBetano[j][3]
                    stringEchipa2 = tabelSuperbet[i][3]
                else:
                    substringEchipa2 = tabelSuperbet[i][3]
                    stringEchipa2 = tabelBetano[j][3]
            else:
                substringEchipa1 = tabelSuperbet[i][2]
                stringEchipa1 = tabelBetano[j][2]
                if(len(tabelBetano[j][3])<= len(tabelSuperbet[i][3])):
                    substringEchipa2 = tabelBetano[j][3]
                    stringEchipa2 = tabelSuperbet[i][3]
                else:
                    substringEchipa2 = tabelSuperbet[i][3]
                    stringEchipa2 = tabelBetano[j][3]

            if(tabelSuperbet[i][1] in tabelBetano[j][1] and substringEchipa1 in stringEchipa1 and substringEchipa2 in stringEchipa2):
                ###Verificam pariurile de tip 1X2
                if(float(tabelSuperbet[i][4]) >= float(tabelBetano[j][4])):
                    if(float(tabelSuperbet[i][5]) >= float(tabelBetano[j][5])):
                        if(float(tabelSuperbet[i][6]) >= float(tabelBetano[j][6])):
                            print("Not worth the trouble")
                        else:
                            val2 = float(tabelBetano[j][6]) 
                            val1 = float(tabelSuperbet[i][4])
                            valx = float(tabelSuperbet[i][5])
                            result = 1/val2 + 1/val1 + 1/valx
                            if(result < 1.00): print(result)
                    else:
                        if(float(tabelSuperbet[i][6]) >= float(tabelBetano[j][6])):
                            val2 = float(tabelSuperbet[i][6])
                            val1 = float(tabelSuperbet[i][4])
                            valx = float(tabelBetano[j][5])
                            result = 1/val2 + 1/val1 + 1/valx
                            if(result < 1.00): print(result)
                        else:
                            val2 = float(tabelBetano[i][6])
                            val1 = float(tabelSuperbet[i][4])
                            valx = float(tabelBetano[j][5])
                            result = 1/val2 + 1/val1 + 1/valx
                            if(result < 1.00): print(result)
                else:
                    if(float(tabelSuperbet[i][5]) >= float(tabelBetano[j][5])):
                        if(float(tabelSuperbet[i][6]) >= float(tabelBetano[j][6])):
                            val1 = float(tabelBetano[j][4])
                            val2 = float(tabelSuperbet[i][6])
                            valx = float(tabelSuperbet[i][5])
                            result = 1/val2 + 1/val1 + 1/valx
                            if(result < 1.00): print(result)
                        else:
                            val2 = float(tabelBetano[j][6]) 
                            val1 = float(tabelBetano[i][4])
                            valx = float(tabelSuperbet[i][5])
                            result = 1/val2 + 1/val1 + 1/valx
                            if(result < 1.00): print(result)
                    else:
                        if(float(tabelSuperbet[i][6]) >= float(tabelBetano[j][6])):
                            val2 = float(tabelSuperbet[i][6])
                            val1 = float(tabelBetano[i][4])
                            valx = float(tabelBetano[j][5])
                            result = 1/val2 + 1/val1 + 1/valx
                            if(result < 1.00): print(result)
                        else:
                            print("Not worth the trouble")
                
                ###Verificam pariurile de tip Peste/Sub
                if(float(tabelSuperbet[i][7]) >= float(tabelBetano[j][7])):
                    if(float(tabelSuperbet[i][8]) >= float(tabelBetano[j][8])):
                        print("Not worth the trouble")
                    else:
                        val2 = float(tabelBetano[j][8]) 
                        val1 = float(tabelSuperbet[i][7])
                        result = 1/val2 + 1/val1
                        if(result < 1.00): print(result)
                else:
                    if(float(tabelSuperbet[i][8]) >= float(tabelBetano[j][8])):
                        val2 = float(tabelSuperbet[i][8])
                        val1 = float(tabelBetano[i][7])
                        result = 1/val2 + 1/val1
                        if(result < 1.00): print(result)
                    else:
                        print("Not worth the trouble")

                ###Verificam pariurile de tip GG/NG
                if(float(tabelSuperbet[i][9]) >= float(tabelBetano[j][9])):
                    if(float(tabelSuperbet[i][10]) >= float(tabelBetano[j][10])):
                        print("Not worth the trouble")
                    else:
                        val2 = float(tabelBetano[j][10]) 
                        val1 = float(tabelSuperbet[i][9])
                        result = 1/val2 + 1/val1
                        if(result < 1.00): print(result)
                else:
                    if(float(tabelSuperbet[i][10]) >= float(tabelBetano[j][10])):
                        val2 = float(tabelSuperbet[i][10])
                        val1 = float(tabelBetano[i][9])
                        result = 1/val2 + 1/val1
                        if(result < 1.00): print(result)
                    else:
                        print("Not worth the trouble")





        
    
    
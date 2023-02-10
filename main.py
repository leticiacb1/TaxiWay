from utils import return_position
import sys

#-------------------- DOCUMENTAÇÃO ---------------------  
#
# # ----- Para rodar -----
# > python main.py inputFile.txt
#
# # -----  Modelo do arquivo input -----
#   
#   largura
#   altura
#   tabuleiro com paredes ? -> sim : ler posicoes (x,y) da parede até encontrar "end"  
#                           -> nao
#   posicao de inicio (coluna,linha) taxi
#   posicao de inicio (coluna,linha) passageiro
#   posicao de iniio (coluna,linha) destino
#
#--------------------------------------------------------

def main():

    input_file = sys.argv[1]
    init_information = {}
    
    # Abre arquivo
    with open(input_file,'r') as f:
        
        num_line = 0
        has_wall = 0
        
        wall_positions = []
        init_information['wall'] = wall_positions

        for line in f.readlines():

            if(has_wall):
                if(line.strip() != "end"):

                    x,y = return_position(line)
                    wall_positions.append([x,y])

                else:
                    has_wall = 0
                    init_information['wall'] = wall_positions

            else:            

                if(num_line == 0):
                    init_information['width'] = int(line)
                
                elif(num_line == 1):
                    init_information['height'] = int(line)
                
                elif(num_line == 2):
                    if(line.strip() == "yes"):
                        has_wall = 1

                elif(num_line == 3):
                    x,y = return_position(line)
                    init_information['taxi'] = [x,y]
                
                elif(num_line == 4):
                    x,y = return_position(line)
                    init_information['person'] = [x,y]
                
                elif(num_line == 5):
                    x,y = return_position(line)
                    init_information['destination'] = [x,y]

                num_line+=1

        print(init_information)


if __name__ == '__main__': 
    main()
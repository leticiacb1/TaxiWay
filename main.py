from utils import return_line_grid, return_position
import sys

# -------------------- DOCUMENTAÇÃO ---------------------  
#
# # ----- Para rodar -----
# > python main.py inputFile.txt
#
# # -----  Modelo do arquivo input -----
#   
#   largura altura
#   posicao de inicio (coluna,linha) taxi
#   posicao de inicio (coluna,linha) passageiro
#   posicao de iniio (coluna,linha) destino
#
#   Mapa:
#   T,0,0
#   0,0,P 	
#   D,0,0
#
#   0 -> Caminho livre
#   X -> Parede
#   T -> Taxi
#   P -> Person
#   D -> Destino

#--------------------------------------------------------

def main():

    input_file = sys.argv[1]
    init_information = {}
    str_map_grid = ""

    with open(input_file,'r') as f:
        
        num_line = 0
        
        for line in f.readlines():

            if(num_line == 0):
                x,y = return_position(line) 
                init_information['dimensions'] = [x,y]
             
            elif(num_line == 1):
                x,y = return_position(line)
                init_information['taxi'] = [x,y]
                
            elif(num_line == 2):
                x,y = return_position(line)
                init_information['person'] = [x,y]
            
            elif(num_line == 3):
                x,y = return_position(line)
                init_information['destination'] = [x,y]
            elif(num_line > 3):
                str_map_grid+= return_line_grid(line)
                    
            num_line+=1
        
        init_information['root_map'] = str_map_grid
        print(init_information)
        print(init_information['root_map'])

if __name__ == '__main__': 
    main()

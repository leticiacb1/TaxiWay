def return_position(position_str):
    return [int(a) for a in position_str.strip().split(' ')]

def return_line_grid(line):
    list_line = line.split(',')
    return list_line

def return_str_map(matrix):
    
    str_map = ""
    for map_list in matrix:
        str_map+= '  '.join(map_list)

    return str_map

def read_informations(input_file):
    init_information = {}
    matrix_map_grid = []
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
                matrix_map_grid.append(return_line_grid(line))
                    
            num_line+=1
       
    init_information['map'] = matrix_map_grid
    return init_information

def compare_states(state1 , state2):
    equal = ((state1.board.str_map == state2.board.str_map) and (state1.taxi.get_status() == state2.taxi.get_status()) and (state1.passager.get_status() == state2.passager.get_status()))
    return equal

def generateMap(init_list_map , type_map):
    '''
    Gera mapas do estágio intermediário e final
    '''
    list_map = []
    for map_list in init_list_map:
        map_list = list(map(lambda x: x.replace('T', '0'), map_list))

        if (type_map == 'final'):
            map_list = list(map(lambda x: x.replace('P', '0'), map_list))
            map_list = list(map(lambda x: x.replace('D', 'T'), map_list))
        elif (type_map == 'intermediate'):
            map_list = list(map(lambda x: x.replace('P', 'T'), map_list))
            
        list_map.append(map_list)
    
    return list_map

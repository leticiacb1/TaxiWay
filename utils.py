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


def generateEndMap(init_list_map):

    for map_list in init_list_map:
        print(map_list)

def calculate_goal_state(init_information):
   ... 

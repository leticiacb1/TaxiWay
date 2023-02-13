def return_position(position_str):
    return [int(a) for a in position_str.strip().split(' ')]

def return_line_grid(line):
    tile_line = ''
    for number in line.split(','):
        tile_line+= ' '+number+' ';
    return tile_line+'\n'

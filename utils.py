def read_informations(input_file):
    with open(input_file,'r') as f:
        text = f.read()
    lines = text.split('\n')
    width, height = lines[0].split(' ')
    x_taxi, y_taxi = lines[1].split(' ')
    x_passenger, y_passenger = lines[2].split(' ')
    x_destiny, y_destiny = lines[3].split(' ')
    matrix = [line.split(',') for line in lines[4:] if len(line) > 0]

    return {
        'width': int(width), 'height': int(height), 'matrix': matrix,
        'x_taxi': int(x_taxi), 'y_taxi': int(y_taxi),
        'x_passenger': int(x_passenger), 'y_passenger': int(y_passenger),
        'x_destiny': int(x_destiny), 'y_destiny': int(y_destiny), 'g': 0, 'path': [format_matrix(matrix)]
    }

def format_matrix(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    return '\n'.join(table)
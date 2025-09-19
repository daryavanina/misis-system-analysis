def main(content):
    pairs = [item.split(',') for item in content.split('\n')]

    vertexes = set([item[0] for item in pairs])#.add([item[1] for item in pairs])
    vertexes.update([item[1] for item in pairs])
    vertexes = sorted(vertexes)

    n = len(vertexes)

    matrix = [[0]*n for i in range(n)]
    
    for pair in pairs:
        f_idx = vertexes.index(pair[0]) 
        s_idx = vertexes.index(pair[1]) 

        matrix[f_idx][s_idx] = 1

    return matrix

print(main("1,2\n1,3\n3,4\n3,5"))
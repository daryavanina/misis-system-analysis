def main(content):
    new_list = []
    for item in content:
         new_list.append(int(item[0]))
         new_list.append(int(item[2]))
    
    n = max(new_list)

    matrix = [[0] * n for i in range (n)]

    for i in range (0, len(new_list), 2):
        f_idx = new_list[i] - 1
        s_idx = new_list[i+1] - 1
        matrix[f_idx][s_idx] = 1
    
    return matrix

with open("C:/progs/sis-an/misis-system-analysis/task0/task2.csv", "r") as file:
        content = file.read().split()

print(main(content))

import sys
sys.stdin = open('../input.txt', 'r')


row, column = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(row))
arr_rotate = list(list(arr[row_index][column_index] for row_index in range(row)) for column_index in range(column))
answer = 0
row_max = [max(arr[row_index]) for row_index in range(row)]
column_max = [max(arr_rotate[column_index]) for column_index in range(column)]
for row_index in range(row):
    for column_index in range(column):
        temp = arr[row_index][column_index]
        if (temp < row_max[row_index]) and (temp < column_max[column_index]):
            answer += arr[row_index][column_index]
            arr[row_index][column_index] = 0
            arr_rotate[column_index][row_index] = 0
        else:
            temp_row = arr[row_index][column_index+1:]
            temp_column = arr_rotate[column_index][row_index+1:]
            if not temp_column or not temp_row:
                continue
            if (max(temp_row) == row_max[row_index]) and (max(temp_column) == max(arr_rotate[column_index])):
                answer += arr[row_index][column_index]
                arr[row_index][column_index] = 0
                arr_rotate[column_index][row_index] = 0
print(answer)

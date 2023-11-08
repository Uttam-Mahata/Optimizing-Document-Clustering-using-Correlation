import pandas as pd
import os

# Get average of whole matrix
def get_avg_full(matrix):
    matrix_dict = dict(matrix)
    s = 0
    c = 0
    for v in matrix_dict.values():
        for j in v:
            if j == 1:
                break
            s += j
            c += 1

    return s / c

# Get maximum of whole matrix
def get_max_full(matrix):
    matrix_dict = matrix.to_dict()
    m = 0
    pair = [None, None]
    for k, v in matrix_dict.items():
        for key, j in v.items():
            if k != key:
                if j > m:
                    m = j
                    pair[0] = k
                    pair[1] = key

    if m < Threshold_value:
        return [None, None], 0
    return pair, m

# Get average of one row of matrix
def get_avg_row(matrix_row):
    return (sum(matrix_row) - 1) / (len(matrix_row) - 1)

# 
def get_relatable_fields(matrix, header):
    matrix_dict = dict(matrix)
    greater_avg_dict = {}
    for k, v in matrix_dict.items():
        greater_avg_dict[k] = set()
        val = 0
        avg = get_avg_row(v)
        for j in v:
            if j >= avg and j >= Threshold_value:
                greater_avg_dict[k].add(header[val])
            val += 1

    # print(*greater_avg_dict.items(),sep='\n')
    return greater_avg_dict

# 
def relatable_val(greater_avg_dict):
    tranform_dict = {}
    for k1, v1 in greater_avg_dict.items():
        tranform_dict[k1] = []
        for v2 in greater_avg_dict.values():
            n1 = len(v1.union(v2))
            n2 = len(v1.intersection(v2))
            d = n2 / n1
            tranform_dict[k1].append(d)

    # print(*tranform_dict.items(),sep='\n')

    ans = pd.DataFrame(
        tranform_dict, columns=greater_avg_dict.keys(), index=greater_avg_dict.keys()
    )
    ans_test = ans.to_dict()
    return ans

# 
def make_folder(name):
    if name not in os.listdir():
        os.mkdir(name)
    for i in os.listdir(f"{name}"):
        os.remove(f"{name}\\{i}")


print("Started...\n\n")

if __name__ == "__main__":
    # Dataset
    data = pd.read_csv("new.csv")
    
    # Constants
    Threshold_value = 0.05

    # Make Output_folder
    make_folder("Output0.05")

    # Correlation coefficients
    correlation_matrix = data.corr()
    header = tuple(correlation_matrix.columns)
    correlation_matrix.to_csv("Output0.05/output.csv")  # Save the output.csv in the "Output" folder

    common_fields = get_relatable_fields(correlation_matrix, header)
    # print(*common_fields.items(),sep='\n')

    c = 0
    while True:
        res2 = relatable_val(common_fields)
        c += 1
        rel_pair, max1 = get_max_full(res2)
        if max1 == 0:
            break
        common_fields[rel_pair[0]] = common_fields[rel_pair[0]].union(common_fields.pop(rel_pair[1]))
        pd.Series(common_fields).to_csv(f"Output0.05/file{c}.csv")  # Save the output files in the "Output" folder

    print(*common_fields.items(),sep='\n\n')

    final_list = sorted(common_fields.items(),key=lambda x: len(x[1]), reverse=True)
    # print(*final_list, sep="\n")

    print("\nTotal final columns =", len(final_list))
    final_res = set()
    col = None
    val=0
    for k, v in final_list:
        val+=1
        final_res = final_res.union(v)
        if len(final_res) == len(header):
            col = k
            break
    if col:
        print(val)
    
    diff = []
    for i in header:
        if i not in final_res:
            diff.append(i)
    print("Different - ", diff)

print("Done")

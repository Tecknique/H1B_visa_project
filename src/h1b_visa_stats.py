import sys
import os
import csv
from collections import Counter

FILENAME = sys.argv[1]

def csv_to_dict(FILENAME):
    reader = csv.DictReader(open(FILENAME,'rb'),delimiter = ';')
    dict_list = []
    for line in reader:
        dict_list.append(line)
    return dict_list



def top_10(dic, col_name):
    top_10_list = []
    c = Counter()
    for d in dic:
        val = d[col_name]
        c[val] += 1
    result = [key for key,value in c.most_common(10)]
    return result


def separate_dics(dic, col_name, fields, sorted_by):  
    top_ten_vals = top_10(dic, col_name)
    lst = []
    for item in top_ten_vals:
        num_certified_by_var = len([entry for entry in dic if entry[col_name] == item and entry['CASE_STATUS'] == 'CERTIFIED'])
        num_certified = len([entry for entry in dic if entry['CASE_STATUS'] == 'CERTIFIED'])
        percentage = '{:.1%}'.format(float(num_certified_by_var)/float(num_certified))
        rows = [item, num_certified_by_var, percentage]
        lst.append(dict(zip(fields, rows)))
    return sorted(lst, key=lambda d: (-d['NUMBER_CERTIFIED_APPLICATIONS'], d[sorted_by]))
    
def dictionary_to_text(lst_dic, fieldnames, filename):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        for d in lst_dic:
            writer.writerow(d)


if __name__ == '__main__':
    dict_list = csv_to_dict(FILENAME)
    print dict_list
    TOP_10_OCCUPATION_COL_NAMES = ['TOP_OCCUPATIONS', 'NUMBER_CERTIFIED_APPLICATIONS','PERCENTAGE']
    TOP_10_STATES_COL_NAMES = ['TOP_STATES', 'NUMBER_CERTIFIED_APPLICATIONS', 'PERCENTAGE']
    top_10_occupation_dic = separate_dics(dict_list, 'SOC_NAME',TOP_10_OCCUPATION_COL_NAMES,'TOP_OCCUPATIONS')
    top_10_states_dic = separate_dics(dict_list, 'WORKSITE_STATE',TOP_10_STATES_COL_NAMES,'TOP_STATES') 
    top_10_occupation_txt = dictionary_to_text(top_10_occupation_dic, TOP_10_OCCUPATION_COL_NAMES, sys.argv[2])
    top_10_state_txt = dictionary_to_text(top_10_states_dic, TOP_10_STATES_COL_NAMES, sys.argv[3])
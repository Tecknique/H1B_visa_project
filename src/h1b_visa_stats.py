import sys
import os
import csv
from collections import Counter

FILENAME = sys.argv[1]

def csv_to_dict(FILENAME):
    ''' reads in csv file specifying the delimiter as ";"
    add each line of the csv into a list of dictionaries
    return the dictionary list after iterating through all entries
    '''    
    reader = csv.DictReader(open(FILENAME,'rb'),delimiter = ';')
    dict_list = []
    for line in reader:
        dict_list.append(line)
    return dict_list



def top_10(dic, col_name):
    ''' count and determine the top 10 instances of occupation and state
    using the 'SOC_NAME' and the 'WORKSITE_STATE'
    '''
    top_10_list = []
    c = Counter()
    for d in dic:
        val = d[col_name]
        c[val] += 1
    result = [key for key,value in c.most_common(10)]
    return result


def separate_dics(dic, col_name, fields, sorted_by):  
    '''Count instances of the top ten values provided as the result of top_ten
    that are also certified, and use that number as a value for the column name
    "NUMBER_CERTIFIED_APPLICACTIONS".
    Find the value of "NUMBER_CERTIFIED_APPLICATIONS" reguardless of occupation
    or state and find a percentage using this value as a denominator and
    "NUMBER_CERTIFIED_APPLICATIONS" as a numerator.
    Change the format to show a percentage instead of a decimal fraction.
    Zip the output values to their specific fieldnames.
    Order the dictionary by "NUMBER_CERTIFIED_APPLICATIONS". In case of tie,
    order the tied ones alphabetically by "TOP_OCCUPATIONS" or "TOP_STATES"
    '''
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
    '''
    Write out each dictionary as a text file
    '''
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        for d in lst_dic:
            writer.writerow(d)


if __name__ == '__main__':
    '''
    Create variables here
    '''
    dict_list = csv_to_dict(FILENAME)
    print dict_list
    TOP_10_OCCUPATION_COL_NAMES = ['TOP_OCCUPATIONS', 'NUMBER_CERTIFIED_APPLICATIONS','PERCENTAGE']
    TOP_10_STATES_COL_NAMES = ['TOP_STATES', 'NUMBER_CERTIFIED_APPLICATIONS', 'PERCENTAGE']
    top_10_occupation_dic = separate_dics(dict_list, 'SOC_NAME',TOP_10_OCCUPATION_COL_NAMES,'TOP_OCCUPATIONS')
    top_10_states_dic = separate_dics(dict_list, 'WORKSITE_STATE',TOP_10_STATES_COL_NAMES,'TOP_STATES') 
    top_10_occupation_txt = dictionary_to_text(top_10_occupation_dic, TOP_10_OCCUPATION_COL_NAMES, sys.argv[2])
    top_10_state_txt = dictionary_to_text(top_10_states_dic, TOP_10_STATES_COL_NAMES, sys.argv[3])
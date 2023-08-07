import sys
import getopt
import struct
import csv
from math import exp

DATA_PATH =''

MAX_TIME = 60.0
MAX_TIME_DELTA = 0.5

TEMP_VALUE_CNT = int(MAX_TIME // MAX_TIME_DELTA)

MAX_TEMPERATURE = 850.0
MAX_TEMPERATURE_DELTA = 10.0
HTC_VALUE_CNT = int(MAX_TEMPERATURE // MAX_TEMPERATURE_DELTA) + 1

MAX_CONTROL_POINT_CNT = 5

def load_temp(temp_file, pset=0):
    temp_file.seek(pset * TEMP_VALUE_CNT * 4)
    x = temp_file.read(TEMP_VALUE_CNT * 4)
    temp_vector = struct.unpack('f' * TEMP_VALUE_CNT, x)
    return temp_vector

def load_htc_header(htc_header_file, pset=0):
    htc_header_record_size = MAX_CONTROL_POINT_CNT * 3 + 1
    htc_header_file.seek(pset * htc_header_record_size * 4)
    y = htc_header_file.read(htc_header_record_size * 4)
    floats = struct.unpack('f' * htc_header_record_size, y)

    ''' 
    floats is array of type 
    floats[0] = no of control points. always 5. So we drop it
    floats[1:] = ith control pt temp, ith control pt htc, ith cont pt alpha for all i control pts
    basically 15 + 1 (+1 for floats[0]) no. of values
    '''

    res_arr = []
    for i in range(1, 16, 3):
        tmp_dict = {'temp': floats[i], 'htc': floats[i+1], 'alpha': floats[i+2]}
        res_arr.append(tmp_dict)

    # print('floats', floats)
    return res_arr


def load_htc(htc_data_file, pset=0):
    htc_data_file.seek(pset * HTC_VALUE_CNT * 4)
    x = htc_data_file.read(HTC_VALUE_CNT * 4)
    htc_arr = struct.unpack('f' * HTC_VALUE_CNT, x)
    return htc_arr

def create_htc_value(P_i, P_i_plus_1, T):
    '''
    P_i is control pt before T
    P_i_plus_1 is control pt after T
    C is scaling factor. usually 7
    '''
    C = 7

    alpha_i = P_i['alpha']

    if (alpha_i != 0):
        alpha_i_dash = 1 / (alpha_i * C)
    
    del_T = (T - P_i['temp']) / (P_i_plus_1['temp'] - P_i['temp'])
    
    if (alpha_i != 0):
        gamma_T = (1 - exp(-del_T / alpha_i_dash)) / (1 - exp(-1/alpha_i_dash))

    if (alpha_i != 0):
        HTC_T = P_i['htc'] + gamma_T * (P_i_plus_1['htc'] - P_i['htc'])
    else:
        HTC_T = P_i['htc'] + del_T * (P_i_plus_1['htc'] - P_i['htc'])

    return HTC_T

def create_htc_series(temp_series, htc_headers):
    ptr_htc_1 = 4 # end of htc array
    ptr_htc_2 = 5 # beyond end of htc array

    dummy_last_htc_val = {'temp': 850, 'htc': 0, 'alpha': 0}
    htc_headers.append(dummy_last_htc_val)

    res_arr = []
    for T in temp_series: 
        htc = None
        while True:
            # print(f'ptr1 = {ptr_htc_1}, ptr2 = {ptr_htc_2}', end= ' ')
            # print(f'ptr1.T = {htc_headers[ptr_htc_1]["temp"]}, ptr2.T = {htc_headers[ptr_htc_2]["temp"]}', end= '\n')
            # print(f'T = {T}\n')

            if (ptr_htc_1 < 0):
                break
            elif (T == htc_headers[ptr_htc_1]['temp']):
                htc = htc_headers[ptr_htc_1]['htc']
                break
            elif (T == htc_headers[ptr_htc_2]['temp']):
                htc_headers[ptr_htc_2]['htc']
                break
            elif (T > htc_headers[ptr_htc_1]['temp'] and T < htc_headers[ptr_htc_2]['temp']):
                break
            else:
                if (T < htc_headers[ptr_htc_1]['temp']):
                    ptr_htc_1 -= 1
                    ptr_htc_2 -= 1
                else:
                    ptr_htc_1 += 1
                    ptr_htc_2 += 1


        if (ptr_htc_1 < 0):
            htc = htc_headers[0]['htc']
        elif (ptr_htc_2 > 4):
            htc = htc_headers[4]['htc']
            
        if (not htc):
            P_i = htc_headers[ptr_htc_1]
            P_i_plus_1 = htc_headers[ptr_htc_2]

            htc = create_htc_value(P_i, P_i_plus_1, T)
        
        res_arr.append(htc)

    return res_arr

def create_temp_csv(filename, rows):
    with open(filename, mode='w') as csv_file:
        fieldnames = [f'col{x}' for x in range(120)]
        writer = csv.writer(csv_file)
        writer.writerow(fieldnames) # write the header row

        for i in range(rows):
            row = load_temp(temp_file, i) # generate a row of data
            writer.writerow(row) # write the row to the CSV file

def create_htc_120_csv(filename, rows):
    with open(filename, mode='w') as csv_file:
        fieldnames = [f'col{x}' for x in range(120)]
        writer = csv.writer(csv_file)
        writer.writerow(fieldnames) # write the header row

        for i in range(rows):
            htc_headers = load_htc_header(htc_header_file, i)
            temp = load_temp(temp_file, i)
            htc_created = create_htc_series(temp, htc_headers)
            row = htc_created # generate a row of data
            writer.writerow(row) # write the row to the CSV file
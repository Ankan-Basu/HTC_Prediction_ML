from data_creation import *

htc_header_file = open(f'{DATA_PATH}/valid_htc_header.bin', 'rb')
temp_file = open(f'{DATA_PATH}/valid_temp_data.bin', 'rb')

create_temp_csv(f'{DATA_PATH}temp_valid.csv', 100000)
create_htc_120_csv(f'{DATA_PATH}htc_valid.csv', 100000)
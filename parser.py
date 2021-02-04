import xml.etree.ElementTree as xml
import random
from random import randrange
from datetime import datetime
from datetime import timedelta
import csv

STB_ID = 'A0722CEEC888'
Pattern_1 = 'url(qam://sourceid='
Pattern_2_1 = 'url:"watchTv?locator=qam://sourceid='
Pattern_2_2 = '[DUMP][CH]'
Pattern_3 = 'SI record received'
Pattern_4 = 'Found supported ES CA descriptor for ca_system_id:'

output_csv = open('output.csv','wt')
header = "TIMESTAMP,DEVICE_ID,CHANNEL_ID,DEVICE_STATE\n"
output_csv.write(header)

f = open("log_chunk_2020_11_11_20_02_28_2020_11_11_20_04_38_log", "r")

for line in f:
    if(line.find(Pattern_1)) != -1:
        p = line.split('dcn=')[1]
        p = p.split(';')[0]
        str_w = str(line.split()[1]) + 'T' + str(line.split()[2]) + ',' + str(STB_ID) + ',dcn:' + str(p) + ',1\n'
        output_csv.write(str_w)
#        print('Pattern_1: ', p)

    if((line.find(Pattern_2_1)) != -1) and ((line.find(Pattern_2_2)) != -1):
        str_w = str(line.split()[1]) + 'T' + str(line.split()[2]) + ',' + str(STB_ID) + ',' + str(line.split()[12]) + ',2\n'
        output_csv.write(str_w)
#        print('Pattern_2: ', line.split())

    if (line.find(Pattern_3)) != -1:
        str_w = str(line.split()[1]) + 'T' + str(line.split()[2]) + ',' + str(STB_ID) + ',' + str(line.split()[15]) + str(line.split()[16]) + ',3\n'
        output_csv.write(str_w)
#        print('Pattern_3: ', line.split())

    if (line.find(Pattern_4)) != -1:
        str_w = str(line.split()[1]) + 'T' + str(line.split()[2]) + ',' + str(STB_ID) + ',qam::MediaSourceImpl' +str(line.split()[6])+',4\n'
        output_csv.write(str_w)
#        print('Pattern_4: ', line.split())
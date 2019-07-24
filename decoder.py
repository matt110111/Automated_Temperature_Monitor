import os
from tabula import convert_into
DIR = (os.listdir())
filenumber = 0
for filename in DIR:
    if filename[-3:] == "pdf":
        input_file = filename
        output_file = f"./CSV_output/NetSensor-{filenumber}.csv"
        print(f"Converting {input_file} to {output_file} ")
        convert_into(input_file,output_file, encoding='utf-8', spreadsheet=True,pages='all', output_format="csv")
        filenumber += 1
        f = open(output_file,"rb")
        linecount = 0
        for line in f.readlines():
            linecount+=1
        print(linecount)


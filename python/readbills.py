import os
import re

import tabula
import pandas as pd

'''
    A simple python program that read TM bills (PDF files) and sum up the total amount.
'''

root_path = './'  # Path to the directory that store your TM bills
pattern = '(.pdf)$'  # Default pattern to differentiate script and TM bills

total = 0

for file in os.listdir(root_path):
    if re.search(pattern, file):
        df = tabula.read_pdf(file, pages='all')
        total += df[0]["Unnamed: 0"][1]

print(f'Total amount: {total}')

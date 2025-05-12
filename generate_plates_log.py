import csv
from datetime import datetime

CSV_FILE = 'plates_log.csv'

# Header for the CSV
header = ['ID', 'Entry Time', 'Exit Time', 'Plate Number', 'Amount Due', 'Is Paid']

# Sample data
sample_data = [
    [1, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '', 'RAH972U', '0', '0'],
    [2, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '', 'XYZ1234', '0', '0'],
    [3, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '', 'ABC7890', '0', '0'],
]

# Writing to CSV
with open(CSV_FILE, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(sample_data)

print(f"[SUCCESS] '{CSV_FILE}' has been generated successfully.")

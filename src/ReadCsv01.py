import csv
csv_file = r'E:\Chicago_E_Drive\Deepak DOCs\Study\Data Analytics\Sample_Data\ManUtdPlayers.csv'
with open(csv_file, newline='') as csvfile:
    for row in csv.reader(csvfile):
        print(row)
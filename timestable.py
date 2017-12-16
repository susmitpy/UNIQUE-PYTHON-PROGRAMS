import csv
def generate_times_table(n, t):
    csvfile = open("D:/PYTHON MAIN/table.csv", "w")
    writer = csv.writer(csvfile, delimiter = ",")
    for i in range(1, t+1):
        l = [i*x for x in range(1, n+1)]
        writer.writerow(l)

a = int(input("Till what number: "))
b = int(input("Till what times: "))

generate_times_table(a, b)

import csv

def largest_num(inp1, inp2, inp3):
    return max(inp1, inp2, inp3)

with open("largest_number_testcases.csv","r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        inp1 = int(row['inp1'])
        inp2 = int(row['inp2'])
        inp3 = int(row['inp3'])
        out = int(row['out'])

        result = largest_num(inp1, inp2, inp3)

        if result == out:
            print("Test case passed:", out)
        else:
            print("Test case failed:", out)







# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import csv


# read csv file as a list of lists
def read_csv():
    courses = []
    with open('cursos-prouni2.csv', newline='') as inputfile:
        for row in csv.reader(inputfile):
            courses.append(row[0])

    return courses


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    courses_name = read_csv()
    #print(courses_name)
    print(type(courses_name))
    print(sorted(set(courses_name)))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# import csv
#
# with open('./weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)
import pandas


def get_average_temp(temp_list):
    total = 0
    index = 0
    for temp in temp_list:
        total += temp
        index += 1

    return round(total / index, 2)


data = pandas.read_csv('./weather_data.csv')
print(get_average_temp(data['temp'].tolist()))



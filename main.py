import pandas


def convert_to_f(celsius):
    return celsius * (9 / 5) + 32


data = pandas.read_csv('./weather_data.csv')
monday = data[data.day == 'Monday']
converted_monday_temp = convert_to_f(monday.temp[0])
print(converted_monday_temp)
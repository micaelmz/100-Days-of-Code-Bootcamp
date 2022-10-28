import pandas



with open('weather_data.csv', 'r') as file:
    data = file.readlines()

print(data)

import csv

with open('weather_data.csv') as file:
    data = csv.reader(file)
    temperatures = []
    for row in data:
        if row[1].isnumeric():
            temperatures.append(int(row[1]))

print(temperatures)


data = pandas.read_csv('weather_data.csv')
print(data['temp'])

data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()

print(f'the avarange temperature is {sum(temp_list) / len(temp_list)}')
print(f'the avarange temperature is {data["temp"].mean()}')

print(f'the max temperature is {data["temp"].max()}')


print(data['condition'])
print(data.condition)

# printe a temperatura maxima
print(data.temp.max())

# printe toda a linha do dia monday
print(data[data.day == 'Monday'])

# printe toda linha do dia em que a temperatura foi a maxima
print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
print(monday.condition)


data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [78, 58, 65]
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv('new_data.csv')


data = pandas.read_csv('2018_Central_Park_Squirrel_Census.csv')
grey_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_count = len(data[data['Primary Fur Color'] == 'Black'])
print(grey_count, red_count, black_count)

dict_flur_color = {
    'Fur Color': ['Gray', 'Red', 'Black'],
    'Count': [grey_count, red_count, black_count]
}

flur_color_dataframe = pandas.DataFrame(dict_flur_color)

flur_color_dataframe.to_csv('squiriel_count')

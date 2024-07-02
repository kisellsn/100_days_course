# import csv
#
# with open('weather_data.csv') as file:
#     data_list = csv.reader(file)
#
#     result_data = []
#     title = True
#     for row in data_list:
#         day_data = []
#         day_data.append(row[0])
#         if not title:
#             day_data.append(int(row[1]))
#         else:
#             day_data.append(row[1])
#             title = False
#         day_data.append(row[2])
#
#         result_data.append(day_data)
#
#     print(result_data)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"].max())


print(data[data.temp == data.temp.max()])


data_dict = {
    "students": ["Alex", "Bob", "Carol", "David",],
    "scores": [90, 80, 70, 60],
}
data = pandas.DataFrame(data_dict)
data.to_csv("students_data.csv")
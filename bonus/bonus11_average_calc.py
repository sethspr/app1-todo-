# def get_average_temp():
#     with open("files/bonus11_data.txt", "r") as file:
#         data = file.readlines()
#
#     values = data[1:]
#     values = [float(i) for i in values]
#
#     average_local = sum(values) / len(values)
#     return average_local
#
# average = get_average_temp()
# print(average)


##### Bug Fixing Exercise #####
## Original Code ##

# def get_maximum():
#     celsius = [14, 15.1, 12.3]
#     maximum = max(celsius)
#     print(maximum)
#
#
# celsius = get_maximum()
# fahrenheit = celsius * 1.8 + 32
#
# print(fahrenheit)

##### Bug Fixed #####
# def get_maximum():
#     celsius_temps = [14, 15.1, 12.3]
#     maximum = max(celsius_temps)
#     print(maximum)
#
#
#     celsius = float(maximum)
#     fahrenheit = celsius * 1.8 + 32
#
#     return fahrenheit
#
# print(get_maximum())
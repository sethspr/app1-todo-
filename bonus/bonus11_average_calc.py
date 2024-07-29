def get_average_temp():
    with open("files/bonus11_data.txt", "r") as file:
        data = file.readlines()

    values = data[1:]
    values = [float(i) for i in values]

    average_local = sum(values) / len(values)
    return average_local

average = get_average_temp()
print(average)
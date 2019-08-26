import matplotlib.pyplot as plot

pieLabels = []
values = []

try:
    x = int(input("Number of elements: "))

    for i in range(x):
        pieLabels.append(input(f"Name of {i + 1} element: "))
        values.append(input(f"Value of {pieLabels[i]} : "))
        i += 1

    figureObject, axesObject = plot.subplots()

    axesObject.pie(values, labels=pieLabels, autopct='%1.2f', startangle=90)

    axesObject.axis('equal')

    plot.show()

except Exception as ex:
    print(f"Error : {ex}")

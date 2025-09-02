#Declaring the array the store values
values = []

#For loop to insert values in the array 
for i in range(5):
    #Asks user for input for values in the array
    num = float(input(f"Enter value {i+1}: "))
    #Appends the each new nalue input to the array
    values.append(num)

#Calculates the average of the values using the sum and len function. The sum function adds the values while the len function finds the total number of values in the array.
average = sum(values) / len(values)

#Outputs the avarage of the values
print(f"The average of the entered values is {average:.2f}")
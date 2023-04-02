#Receiving value from user
int1 = int(input("Digite um número inteiro : \n"))
int2 = int(input("Digite outro número inteiro : \n"))
real = float(input("Digite um número real : \n"))

#Calculating instructions
#A
operation = (int1 * 2) * (int2 / 2)

#B
operation2 = (int1 * 3) + real

#C
operation3 = real **3

#Printing results for the user
print(f"No item A será calculado o dobro do 1° número vezes a metade do 2°. \nNo item B será calculado o triplo do 1° mais o 3°. \nNo item C será calculado o cubo do 3°.")
print(f"A. {operation}")
print(f"B. {operation2}")
print(f"C. {operation3}")
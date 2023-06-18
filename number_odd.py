#A four-digit integer is given. Find the number of odd digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
number = 8375
bir = number//1000
ikki = (number//100)%10
uch = (number//10)%10
turt = (number)%10
#Print the number of odd digits in the variable "var_int".
var_int = ((bir)%2+(ikki)%2+(uch)%2+(turt)%2)
print(var_int)
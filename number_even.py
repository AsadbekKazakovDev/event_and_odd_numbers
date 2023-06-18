#A four-digit integer is given. Find the number of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
number = 8369
bir = number//1000
ikki = (number//100)%10
uch = (number//10)%10
turt = (number)%10
#Print the number of even digits in the variable "var_int".
print((bir-1)%2+(ikki-1)%2+(uch-1)%2+(turt-1)%2)
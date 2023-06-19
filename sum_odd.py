#A four-digit integer is given. Find the sum of odd digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var_int = 1869

#Create a variable "sum_odd" and assign it 0.
sum_odd = 0
#Find the sum of the odd digits in the variable "var_int".
bir = var_int//1000
ikki = (var_int//100)%10
uch = (var_int//10)%10
turt = (var_int)%10
sum_odd = (bir*((bir)%2)+ikki*((ikki)%2)+uch*((uch)%2)+turt*((turt)%2))
print(sum_odd) 
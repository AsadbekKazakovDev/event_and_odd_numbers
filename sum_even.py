#A four-digit integer is given. Find the sum of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var_int = 1867
#Create a variable "sum_even" and assign it 0.
sum_even = 0
#Find the sum of the even digits in the variable "var_int".
bir = var_int//1000
ikki = (var_int//100)%10
uch = (var_int//10)%10
turt = (var_int)%10
sum_even = (bir*((bir-1)%2)+ikki*((ikki-1)%2)+uch*((uch-1)%2)+turt*((turt-1)%2))
print(sum_even)

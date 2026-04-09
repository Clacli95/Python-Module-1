x_str="Non vedo l'ora di imparare Python"
print(x_str[::-1])


replace_str = x_str.replace( " ", "")

print(replace_str)  

replace_str_inverse = replace_str[::-1]

frase_palindrome = replace_str == replace_str_inverse  
print(frase_palindrome)
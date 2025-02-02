uma_string_qualquer: str = 'uma string qualquer'

for s in range(len(uma_string_qualquer)):

     print(f'{uma_string_qualquer[-(s + 1)]}', end='')
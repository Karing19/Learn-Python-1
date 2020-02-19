pizzas = ['Pepperoni', 'Supreme', 'Cheese']
friend_pizzas = pizzas[:]
pizzas.append('Hawaiian')
friend_pizzas.append('Durian')
print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)

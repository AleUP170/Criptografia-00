import fileinput

# Lee entradas
lines = []
for line in fileinput.input():
    lines.append(line)

total = 0
# Suma todas las entradas
for x in lines:
	total += x

# Imprime resultado
print(total)
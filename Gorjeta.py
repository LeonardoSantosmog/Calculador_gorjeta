conta = float(input("digite o valor da conta: R$ "))
gorjeta = float(input("digite o percentual da gorjeta: "))

valor_gorjeta = conta * (gorjeta / 100)
total = conta + valor_gorjeta

print(f"Valor da conta: R$ {conta:.2f}")
print(f"Valor da gorjeta: R$ {valor_gorjeta:.2f}")
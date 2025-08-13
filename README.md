# 💰 Calculadora de Gorjeta

Este é um simples programa em Python que calcula o valor da gorjeta com base no valor da conta e na porcentagem informada pelo usuário.

## 📜 Como funciona
O programa:
1. Solicita ao usuário o valor total da conta.
2. Pede a porcentagem de gorjeta desejada.
3. Calcula o valor da gorjeta.
4. Exibe o valor da conta e o valor da gorjeta.

## 📂 Código
```python
conta = float(input("Digite o valor da conta: R$ "))
gorjeta = float(input("Digite o percentual da gorjeta: "))

valor_gorjeta = conta * (gorjeta / 100)
total = conta + valor_gorjeta

print(f"Valor da conta: R$ {conta:.2f}")
print(f"Valor da gorjeta: R$ {valor_gorjeta:.2f}")

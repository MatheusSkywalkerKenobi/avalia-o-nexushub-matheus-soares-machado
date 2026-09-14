#Etapa 1
startups = {
    "nome": "CyberPulse Tech",
    "segmento": "Segurança da Informação",
    "ano_adesao": "2026"
}
solucoes_ativas =["Firewall IA","Scan de Vulnerabilidades"]
print("STARTUP:",startups["nome"],"fase",startups["segmento"])
print("Soluçoes em Andamento:",solucoes_ativas[0],"inicio",startups["ano_adesao"])
#Etapa 2
bancada = [
    [1,0],
    [0,1]
]
print("Status da Bancada N1", bancada[0][0])
print("Status da Bancada N2", bancada[0][1])
print("Status da Bancada S1", bancada[0][0])
print("Status da bancada S2", bancada[0][1])

with open("custos_cloud.csv", "r", encoding="utf-8") as arquivo:
    cabecalho = arquivo.readline()
    linha_1 = arquivo.readline()
    linha_2 = arquivo.readline()
    linha_3 = arquivo.readline()
    linha_4 = arquivo.readline()

print(cabecalho, end="")
print(linha_1, end="")
print(linha_2, end="")
print(linha_3, end="")
print(linha_4, end="")

custo_1 = float(linha_1.split(",")[1].strip())
custo_2 = float(linha_2.split(",")[1].strip())
custo_3 = float(linha_3.split(",")[1].strip())
custo_4 = float(linha_4.split(",")[1].strip())
total = custo_1 + custo_2 + custo_3 + custo_4

print("\nPAINEL FINAL")
print("Startup:", startups["nome"])
print("Bancada alocada: Bancada N1")
print(f"Total de infraestrutura cloud: R$ {total:.2f}")
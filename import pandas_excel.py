import pandas as pd

# Dados fornecidos
valor_total = 100000  # Valor investido
aporte_mensal = 1000  # Aporte mensal
acoes = [
    {"ticker": "WEGE3", "setor": "Industrial", "peso": 0.15, "dy": 0.012, "pl": 32, "roe": 0.22, "beta": 0.95},
    {"ticker": "BBAS3", "setor": "Financeiro", "peso": 0.10, "dy": 0.085, "pl": 5, "roe": 0.19, "beta": 1.0},
    {"ticker": "PETR3", "setor": "Commodities", "peso": 0.12, "dy": 0.15, "pl": 3, "roe": 0.35, "beta": 1.4},
    {"ticker": "CSMG3", "setor": "Saneamento", "peso": 0.08, "dy": 0.06, "pl": 6, "roe": 0.14, "beta": 0.85},
    {"ticker": "SBSP3", "setor": "Saneamento", "peso": 0.08, "dy": 0.045, "pl": 7, "roe": 0.12, "beta": 0.80},
    {"ticker": "LEVE3", "setor": "Industrial", "peso": 0.05, "dy": 0.065, "pl": 9, "roe": 0.17, "beta": 1.2},
    {"ticker": "VALE3", "setor": "Commodities", "peso": 0.13, "dy": 0.10, "pl": 4, "roe": 0.28, "beta": 1.5},
    {"ticker": "BBDC3", "setor": "Financeiro", "peso": 0.05, "dy": 0.07, "pl": 6, "roe": 0.16, "beta": 1.1},
    {"ticker": "ITSA3", "setor": "Financeiro", "peso": 0.05, "dy": 0.08, "pl": 5.5, "roe": 0.18, "beta": 0.9},
    {"ticker": "EGIE3", "setor": "Energia", "peso": 0.05, "dy": 0.065, "pl": 12, "roe": 0.21, "beta": 0.7},
    {"ticker": "PSSA3", "setor": "Financeiro", "peso": 0.05, "dy": 0.06, "pl": 10, "roe": 0.15, "beta": 0.85},
    {"ticker": "EZTC3", "setor": "Construção Civil", "peso": 0.04, "dy": 0.025, "pl": 8, "roe": 0.13, "beta": 1.3},
    {"ticker": "SAPR3", "setor": "Saneamento", "peso": 0.05, "dy": 0.04, "pl": 7.5, "roe": 0.11, "beta": 0.75}
]

# Criar DataFrame
df = pd.DataFrame(acoes)

# Calcular valor investido por ação
df["Valor Investido (R$)"] = df["peso"] * valor_total

# Calcular dividendos estimados
df["Dividendos Anuais Estimados (R$)"] = df["Valor Investido (R$)"] * df["dy"]

# Calcular dividend yield médio ponderado
dividend_yield_ponderado = (df["peso"] * df["dy"]).sum()

# Calcular beta médio ponderado
beta_ponderado = (df["peso"] * df["beta"]).sum()

# Agrupamento por setor
df_setores = df.groupby("setor")["peso"].sum().reset_index().rename(columns={"peso": "Peso por Setor (%)"})
df_setores["Peso por Setor (%)"] *= 100

# Exportar para Excel
with pd.ExcelWriter("Carteira_Arrojada.xlsx") as writer:
    df.to_excel(writer, sheet_name="Carteira Detalhada", index=False)
    df_setores.to_excel(writer, sheet_name="Distribuição por Setor", index=False)
    resumo = pd.DataFrame({
        "Indicador": ["Dividend Yield Médio (%)", "Beta Médio da Carteira"],
        "Valor": [dividend_yield_ponderado * 100, beta_ponderado]
    })
resumo.to_excel(writer, sheet_name="Resumo da Carteira", index=False)

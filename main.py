# %% [markdown]

# Base de dados e arquivos: https://drive.google.com/drive/folders/1uDesZePdkhiraJmiyeZ-w5tfc8XsNYFZ?usp=drive_link

# %%
import pandas as pd

tabela = pd.read_csv("cancelamentos.csv")
tabela = tabela.drop(columns="CustomerID")
print(tabela)


# %%
print(tabela.info())
tabela = tabela.dropna()
print(tabela.info())

# %%
#analise da contagem de cancelamentos (numero de cadastrados que cancelaram. e numero dos que não cancelaram):

print(tabela["cancelou"].value_counts())

#contagem em percentual:

print(tabela["cancelou"].value_counts(normalize = True))

display(tabela["cancelou"].value_counts(normalize = True).map("{:.1%}".format))

# %%
# Analise das causas dos cancelamentos dos clientes (como as colunas impactaram)
import plotly.express as px

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x = coluna, color = "cancelou")
    grafico.show()

# %%
# Causas do cancelamento

# Todos os clientes de contrato mensal cancelaram
    # Dar desconto nos contratos anuais e trimestrais
# Todos os clientes com mais de 20 dias de atraso cancelaram o serviço
    # Criar um sistema de cobrança dps clinetes que com 10 dias de atraso entramos em contato
# Todos os clientes que ligaram mais de 4x para o call center cancelaram
    # Criar um alerta para um cliente que ligou mais de 2x para o call center

# Analisar se eu resolver esses problemas em quanto cai o cancelamento?
   
# duracao do contrato nao pode ser mensal
tabela = tabela[tabela["duracao_contrato"]!="Montly"]

# atrasos so podem ser de ate 20 dias
tabela = tabela[tabela["dias_atraso"]<= 20]

# ligacoes no call center so ate 4 ligacoes 
tabela = tabela[tabela["ligacoes_callcenter"]<= 4]

print(tabela["cancelou"].value_counts(normalize = True))


import pandas as pd

try:
    clientes = pd.read_csv('analise_com_merge/data/clientes.csv')
    produtos = pd.read_csv('analise_com_merge/data/produtos.csv')
    vendas = pd.read_csv('analise_com_merge/data/vendas.csv')

except FileNotFoundError:
    print('Erro: Um ou mais arquivos CSV não foram encontrados.')
    print('Verifique se os arquivos estão na pasta correta.')
    exit()

df1 = pd.merge(vendas, clientes, how='inner', on='id_cliente')
df = pd.merge(df1, produtos, how='inner', on='id_produto')

df['faturamento'] = df['preco'] * df['quantidade']

def todos_dados(df):
    print('\n=== TODOS OS DADOS ===')
    print(df)

def faturamento_total(df):
    print('\n=== FATURAMENTO TOTAL ===')
    print(f"R$ {(df['preco'] * df['quantidade']).sum():.2f}")

def faturamento_por_cliente(df):
    print('=== FATURAMENTO POR CLIENTE ===')
    print((df['faturamento']).groupby(df['nome']).sum())

def produtos_mais_vendidos(df):
    print('=== PRODUTOS MAIS VENDIDOS ===')
    print(df.groupby('nome_produto')['quantidade'].sum())

def compras_acima(df):
    print('=== ANALISE DE COMPRAS ===')
    
    print('\n COMPRA ATE R$ 500 ')
    print((df['faturamento']).groupby(df['nome']).sum().loc[lambda x: x <= 500])

    print('\n COMPRAS ACIMA DE R$ 1000 ')
    print((df['faturamento']).groupby(df['nome']).sum().loc[lambda x : x > 1000])

def ranking_clientes(df):
    print('\n=== RANKING DE CLIENTES ===')
    print((df['faturamento']).groupby(df['nome']).sum().sort_values(ascending=False))

def relatorio_geral(df):
    print('\n=== RELATORIO GERAL ===')
    todos_dados(df)
    print()
    faturamento_total(df)
    print()
    faturamento_por_cliente(df)
    print()
    produtos_mais_vendidos(df)
    print()
    compras_acima(df)
    print()
    ranking_clientes(df)
    

print('========================================\nSISTEMA DE ANÁLISE DE VENDAS\n========================================')
while True:
    print('\n[1] Ver todos os dados\n[2] Faturamento total\n[3] Faturamento por cliente\n[4] Produtos mais vendidos\n[5] Compras acima de um valor\n[6] Ranking de clientes\n[7] Relatorio geral\n[0] Sair\n')
    
    try:
        opcao = int(input('Escolha uma opcao: '))
    except ValueError:
        print('Digite apenas numeros!')
        continue

    if opcao == 1:
        todos_dados(df)
    
    elif opcao == 2:
        faturamento_total(df)
    
    elif opcao == 3:
        faturamento_por_cliente(df)
    
    elif opcao == 4:
        produtos_mais_vendidos(df)
    
    elif opcao == 5:
        compras_acima(df)

    elif opcao == 6:
        ranking_clientes(df)
    
    elif opcao == 7:
        relatorio_geral(df)

    elif opcao == 0:
        break

    else:
        print('OPCAO INVALIDA!')

print('Programa encerrado.')

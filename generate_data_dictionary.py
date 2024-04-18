import pandas as pd
import snakemd as snake
from datetime import date


dados = pd.read_csv("./view_columns.csv", delimiter=',')

infos = pd.read_csv("./config_doc.csv", delimiter=';')

data = dados.iloc[:,[0,1,2]] 

    
#Escrita de texto do documento md
doc = snake.new_doc("DOCUMENTACAO_TESTE")


# Filtrando o valor a partir da coluna "VARIAVEL" 
valor_filtrado = infos.loc[infos['VARIAVEL'] == 'TITULO', 'VALOR'].values[0]
print(valor_filtrado)
arq_title = valor_filtrado

valor_filtrado = infos.loc[infos['VARIAVEL'] == 'DEV_RESPONSAVEL', 'VALOR'].values[0]
print(valor_filtrado)
arq_dev = valor_filtrado


valor_filtrado = infos.loc[infos['VARIAVEL'] == 'TABELA', 'VALOR'].values[0]
print(valor_filtrado)
arq_table = valor_filtrado


doc.add_header("Dicionário de Dados - "+ arq_title)

doc.add_paragraph("Dicionário de Dados do desenvolvimento da Tabela "+ arq_table)

    #Recuperando os dados que serão inseridos no documento
header_data = data.columns
rows = data.to_numpy()

    #Inserindo os dados no arquivo md
doc.add_table(
        header_data,
        rows
    )

data_hora = date.today()

doc.add_paragraph("Última atualização"+ str(data_hora))

    #Gerando o arquivo md
doc.output_page()

    



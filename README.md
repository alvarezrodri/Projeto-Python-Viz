# Documentação do Projeto de Visualização de Dados

## Visão Geral
Este projeto tem como objetivo analisar e visualizar dados de um e-commerce, utilizando Python e bibliotecas como Pandas, NumPy, Plotly e Dash. Ele gera diferentes tipos de gráficos para explorar relações entre variáveis, auxiliando na tomada de decisão e compreensão dos dados.

## Tecnologias Utilizadas
- **Linguagem**: Python
- **Bibliotecas**: Pandas, NumPy, Plotly, Dash, SciPy
- **Framework Web**: Dash

## Funcionalidades
### 1. Leitura e Processamento de Dados
O projeto utiliza um conjunto de dados salvo no arquivo `ecommerce_estatistica.csv`, carregado com Pandas.

### 2. Criação de Visualizações
A função `criar_graficos(df)` gera os seguintes tipos de gráficos:
- **Histograma**: Exibe a distribuição de notas.
- **Gráfico de Dispersão**: Analisa a relação entre preço e nota dos produtos.
- **Mapa de Calor**: Apresenta a correlação entre variáveis numéricas.
- **Gráfico de Barras**: Representa a distribuição de gênero.
- **Gráfico de Pizza**: Mostra a distribuição das marcas mais vendidas.
- **Gráfico de Densidade**: Demonstra a distribuição de preços usando uma função de densidade kernel.
- **Regressão Linear**: Adiciona uma linha de tendência ao gráfico de dispersão entre preço e nota.

### 3. Aplicativo Web com Dash
A função `cria_app(df)` cria um aplicativo interativo utilizando Dash, exibindo os gráficos em uma interface web.

## Como Executar o Projeto
1. Instalar as dependências necessárias:
   ```sh
   pip install pandas numpy plotly dash scipy
   ```
2. Executar o script Python:
   ```sh
   python Projeto_Visualizacao_dados.py
   ```
3. Acessar o aplicativo no navegador pelo endereço:
   ```
   http://127.0.0.1:8050
   ```

## Conclusão
Este projeto demonstra habilidades em análise de dados, visualização interativa e desenvolvimento web com Dash. Ele pode ser expandido para incluir mais métricas e interatividade, sendo útil para e-commerces que desejam entender melhor seus dados.


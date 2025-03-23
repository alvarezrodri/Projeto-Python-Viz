import pandas as pd
import numpy as np
import plotly.express as px
from dash import Dash, html, dcc
from scipy.stats import gaussian_kde

def criar_graficos(df):
    # Histograma
    fig1 = px.histogram(df, x='Nota', nbins=30, title='Distribuição Notas')
    fig1.update_layout(
        title="Distribuição de Notas",
        xaxis_title='Nota',
        yaxis_title='Frequência',
        plot_bgcolor='rgba(222, 255, 253, 1)',  # Fundo Interno
        paper_bgcolor='rgba(186, 245, 241, 1)'  # Fundo Externo
    )

    # Gráfico de Dispersão
    fig2 = px.scatter(df, x='Preço', y='Nota', size='Preço', color='Nota', size_max=60)
    fig2.update_layout(title='Preço por Nota e Números de Avaliações')

    #Gráfico de calor
    corr = df[['Preço', 'Nota', 'N_Avaliações', 'Desconto', 'Qtd_Vendidos_Cod']].corr()
    fig3 = px.imshow(corr, text_auto=True, aspect="auto", color_continuous_scale='Viridis', title="Mapa de calor de Correlação")

    # Gráfico de Barras
    contagem_genero = df['Gênero'].value_counts().reset_index()
    contagem_genero.columns = ['Gênero', 'Contagem']
    fig4 = px.bar(contagem_genero, x='Gênero', y='Contagem', color_discrete_sequence=px.colors.qualitative.Bold, opacity=1)
    fig4.update_layout(
        title="Distribuição de Gênero",
        xaxis_title='Gênero',
        yaxis_title='Frequência',
        plot_bgcolor='rgba(222, 255, 253, 1)', # Fundo Interno
        paper_bgcolor='rgba(186, 245, 241, 1)' # Fundo Externo
    )
    # Gráfico de pizza

    marca_counts = df["Marca"].value_counts()
    top_n = 7

    # Separar as principais marcas e agrupar as restantes como "Outras"
    top_marcas = marca_counts.nlargest(top_n)
    outros = marca_counts.iloc[top_n:].sum()

    # Criar novo conjunto de dados com a categoria "Outras"
    marcas_reduzidas = pd.concat([top_marcas, pd.Series(outros, index=["Outras"])])

    fig5 = px.pie(values=marcas_reduzidas, names=marcas_reduzidas.index, hole=0.2, color_discrete_sequence=px.colors.sequential.RdBu)
    fig5.update_layout(title=f"Distribuição de Marcas(top {top_n} e Outras)")

    # Gráfico de densidade
    preco = df['Preço'].dropna()
    kde = gaussian_kde(preco)

    # Gera os valores para o gráfico
    x_vals = np.linspace(preco.min(), preco.max(), 100)
    y_vals = kde(x_vals)

    # Cria o gráfico de densidade
    fig6 = px.line(
        x=x_vals,
        y=y_vals,
        labels={'x': 'Preço', 'y': 'Densidade'},
        title="Densidade de Preços"
    )

    fig7 = px.scatter(df, x='Preço', y='Nota', trendline='ols', color='Nota', color_continuous_scale='Bluered')
    fig7.update_layout(title="Regressão Nota Por Preço")

    return fig1, fig2, fig3, fig4, fig5, fig6, fig7

def cria_app(df):
    app = Dash(__name__)
    fig1, fig2, fig3, fig4, fig5, fig6, fig7 = criar_graficos(df)

    app.layout = html.Div([
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
        dcc.Graph(figure=fig3),
        dcc.Graph(figure=fig4),
        dcc.Graph(figure=fig5),
        dcc.Graph(figure=fig6),
        dcc.Graph(figure=fig7),
    ])
    return app

df = pd.read_csv('ecommerce_estatistica.csv')

# Executa APP
if __name__ == '__main__':
    app = cria_app(df)
    app.run_server(debug=True, port=8050)

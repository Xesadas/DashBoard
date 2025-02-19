import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

# Inicializar o app
app = dash.Dash(__name__)

# Definir cores
colors = {
    'background': '#111111',  # Cor de fundo da página inteira
    'text': '#C0C0C0'         # Cor do texto
}

# Carregar os dados
df = pd.read_csv('mcteste.csv')

# Criar o gráfico
fig = px.line(df, x='Year', y='Revenue ($B)', title='Valores Gastos ao Longo do Tempo')

# Personalizar o layout do gráfico
fig.update_layout(
    plot_bgcolor=colors['background'],  # Fundo da área do gráfico
    paper_bgcolor=colors['background'],  # Fundo externo do gráfico
    font_color=colors['text']  # Cor do texto
)

# Definir o layout do app
app.layout = html.Div(style={'backgroundColor': colors['background'], 'height': '100vh'}, children=[  # Altura 100% da tela


    html.H1(
        children='Receita do McDonalds',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    
    html.Div(children='Receita bruta do Mcdonalds entre 2002 e 2022', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='Saldo',
        figure=fig
    )
])

# Rodar o servidor
if __name__ == '__main__':
    app.run_server(debug=True)

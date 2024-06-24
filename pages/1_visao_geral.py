# bibliotecas
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from PIL import Image
import folium
from streamlit_folium import folium_static


# importando dataset
df = pd.read_csv('zomato.csv')


# fazendo a limpeza dos dados
df1 = df.copy()

# verificando e eliminando linhas duplicadas
linhas_duplicadas = df1[df.duplicated()]
df1 = df1.drop_duplicates()

# eliminando coluna 'Switch to order menu'
df1.drop('Switch to order menu', axis=1, inplace=True)

# eliminando os dados nulos (NaN)
df1 = df1.dropna()

# 'resetando' os indices do dataframe
df1 = df1.reset_index(drop=True)

# seguindo a sugestão da descrição do projeto de categorizar os restaurantes por apenas um tipo de culinária
df1["Cuisines"] = df1.loc[:, "Cuisines"].apply(lambda x: x.split(",")[0])

#--------------------------
# Funções
#--------------------------
COLORS = {
    "3F7E00": "darkgreen",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "orange",
    "FFBA00": "red",
    "CBCBC8": "darkred",
    "FF7800": "darkred",
}
def color_name(color_code):
    return COLORS[color_code]

COUNTRIES = {
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zeland",
    162: "Philippines",
    166: "Qatar",
    184: "Singapure",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "United Arab Emirates",
    215: "England",
    216: "United States of America",
}
def country_name(country_id):
    return COUNTRIES[country_id]

def create_price_tye(price_range):
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet"

# usando as funções sugeridas no projeto para criar colunas no dataframe
df1['Country'] = df1.loc[:, 'Country Code'].apply(country_name)
df1['Price'] = df1.loc[:, 'Price range'].apply(create_price_tye)
df1['Color'] = df1.loc[:, 'Rating color'].apply(color_name)   
    
df2 = df1.copy()    
    
#=================================================================
# Barra lateral
#=================================================================
image_path = 'logo.png'
image = Image.open(image_path) 
st.sidebar.image(image, width=80)   

st.sidebar.markdown('# Fome Zero')
st.sidebar.markdown("""---""")

country_options = st.sidebar.multiselect(
    'Selecione o país:',
    ['India', 'Australia', 'Brazil', 'Canada', 'Indonesia', 'New Zeland', 'Philippines', 'Qatar', 'Singapore', 'South Africa', 'Sri Lanka', 'Turkey', 'United Arab Emirates', 'England', 'United States of America'],
    default=['India', 'Australia', 'Brazil', 'Indonesia', 'United Arab Emirates', 'England', 'United States of America'] )

st.sidebar.markdown("""---""")

cuisine_options = st.sidebar.multiselect(
    'Selecione o tipo culinário:',
    ['Italian', 'European', 'Filipino', 'American', 'Korean', 'Pizza', 'Taiwanese', 'Japanese', 'Coffee', 'Chinese', 'Seafood', 'Singaporean', 'Vietnamese', 'Latin American', 'Healthy Food', 'Cafe', 'Fast Food', 'Brazilian', 'Argentine', 'Arabian', 'Bakery', 'Tex-Mex', 'Bar Food', 'International', 'French', 'Steak', 'German', 'Sushi', 'Grill', 'Peruvian', 'North Eastern', 'Ice Cream', 'Burger', 'Mexican', 'Vegetarian', 'Contemporary', 'Desserts', 'Juices', 'Beverages', 'Spanish', 'Thai', 'Indian', 'Mineira', 'BBQ', 'Mongolian', 'Portuguese', 'Greek', 'Asian', 'Author', 'Gourmet Fast Food', 'Lebanese', 'Modern Australian', 'African', 'Coffee and Tea', 'Australian', 'Middle Eastern',     'Malaysian', 'Tapas', 'New American', 'Pub Food', 'Southern', 'Diner', 'Donuts', 'Southwestern', 'Sandwich', 'Irish', 'Mediterranean', 'Cafe Food', 'Korean BBQ', 'Fusion', 'Canadian', 'Breakfast', 'Cajun', 'New Mexican', 'Belgian', 'Cuban', 'Taco', 'Caribbean', 'Polish', 'Deli', 'British', 'California', 'Others', 'Eastern European', 'Creole', 'Ramen', 'Ukrainian', 'Hawaiian', 'Patisserie', 'Yum Cha', 'Pacific Northwest', 'Tea', 'Moroccan', 'Burmese', 'Dim Sum', 'Crepes', 'Fish and Chips', 'Russian',     'Continental', 'South Indian', 'North Indian', 'Salad', 'Finger Food', 'Mandi', 'Turkish', 'Kerala', 'Pakistani', 'Biryani', 'Street Food', 'Nepalese', 'Goan', 'Iranian', 'Mughlai', 'Rajasthani', 'Mithai', 'Maharashtrian', 'Gujarati', 'Rolls', 'Momos', 'Parsi', 'Modern Indian', 'Andhra', 'Tibetan', 'Kebab', 'Chettinad', 'Bengali', 'Assamese', 'Naga', 'Hyderabadi', 'Awadhi', 'Afghan', 'Lucknowi', 'Charcoal Chicken', 'Mangalorean', 'Egyptian', 'Malwani', 'Armenian', 'Roast Chicken', 'Indonesian', 'Western', 'Dimsum', 'Sunda', 'Kiwi', 'Asian Fusion', 'Pan Asian', 'Balti', 'Scottish', 'Cantonese', 'Sri Lankan', 'Khaleeji', 'South African', 'Drinks Only', 'Durban', 'World Cuisine', 'Izgara', 'Home-made', 'Giblets', 'Fresh Fish', 'Restaurant Cafe', 'Kumpir', 'Döner', 'Turkish Pizza', 'Ottoman', 'Old Turkish Bars', 'Kokoreç'],
    default = ['Italian', 'American', 'Japanese', 'Fast Food', 'Brazilian', 'Arabian', 'Vegetarian', 'Thai', 'Pizza', 'Burger'])

st.sidebar.markdown("""---""")

# fazendo link dos filtros com os gráficos
linhas_selecionadas = df1['Country'].isin(country_options)
df1 = df1.loc[linhas_selecionadas, :]

linhas_selecionadas = df1['Cuisines'].isin(cuisine_options)
df1 = df1.loc[linhas_selecionadas, :]

#===============================================================
# Layout no Streamlit
#===============================================================
#st.header('Marketplace - Visão Geral')

tab1, tab2, tab3, tab4 = st.tabs(['Visão Geral', 'Visão Países', 'Visão Cidades', 'Visão Restaurantes'])

#----------------------
# Visão Geral
#----------------------

with tab1:
    with st.container():
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            paises_cadastrados = df2['Country Code'].nunique()
            col1.metric('Países cadastrados', paises_cadastrados)
            
        with col2:
            cidades_cadastradas = df2['City'].nunique()
            col2.metric('Cidades cadastradas', cidades_cadastradas)
            
        with col3:
            restaurantes_cadastrados = df2['Restaurant ID'].nunique()
            col3.metric('Restaurantes cadastrados', restaurantes_cadastrados)
            
        with col4:
            tipos_culinarios = df2['Cuisines'].nunique()
            col4.metric('Tipos culinários', tipos_culinarios)
            
        with col5:
            numero_avaliacoes = df2['Votes'].sum()
            col5.metric('Número de avaliações', numero_avaliacoes)
        
    with st.container():
        df_aux = df2.loc[:, ['City', 'Restaurant Name', 'Aggregate rating', 'Latitude', 'Longitude']].reset_index()
        
        map = folium.Map()

        for index, location_info in df_aux.iterrows():
            folium.Marker([location_info['Latitude'], location_info['Longitude']],
                          popup=location_info[['Restaurant Name', 'Aggregate rating']]).add_to(map)
                                  
        folium_static(map, width=1024, height=600)                

        map
    
#----------------------
# Visão Países
#----------------------
    
with tab2:
    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            aux = df1[['Country', 'City']].groupby('Country').nunique().reset_index()
            fig = px.bar(aux, x='Country', y='City', title='Número de cidades registradas por país', labels={'City':'Número de cidades', 'Country':'País'}, text_auto=True)
            fig.update_traces(textfont_size=12, textposition="outside", cliponaxis=False)
            st.plotly_chart(fig, use_container_width=True)
            
        with col2:
            aux = df1[['Restaurant ID', 'Country']].groupby('Country').count().reset_index()
            fig = px.bar(aux, x='Country', y='Restaurant ID', title='Número de restaurantes registrados por país', labels={'Restaurant ID':'Número de restaurantes', 'Country':'País'}, text_auto=True)
            fig.update_traces(textfont_size=12, textposition="outside", cliponaxis=False)
            st.plotly_chart(fig, use_container_width=True)
            
            
    with st.container(): 
        
            aux = df1[['Country', 'Aggregate rating']].groupby('Country').agg('median', 'sort_values')
            aux1 = aux.sort_values(by='Aggregate rating', ascending=False).reset_index()
            fig = px.bar(aux1, x='Country', y='Aggregate rating', title='Nota média das avaliações por país', labels={'Aggregate rating':'Nota média', 'Country':'País'}, text_auto=True)
            fig.update_traces(textfont_size=12, textposition="outside", cliponaxis=False)
            st.plotly_chart(fig, use_container_width=True)
                        
    with st.container():  
        col1, col2 = st.columns(2)
        
        with col1:
            aux = df1[['Country', 'Average Cost for two']].groupby('Country').mean().reset_index()
            fig = px.bar(aux, x='Country', y='Average Cost for two', title='Preço médio prato duas pessoas', labels={'Average Cost for two':'Preço médio', 'Country':'País'}, text_auto=True)
            fig.update_traces(textfont_size=12, textposition="outside", cliponaxis=False)
            st.plotly_chart(fig, use_container_width=True)
            
            
        with col2:
            aux = df2[['Country', 'Cuisines']].groupby('Country').nunique()
            aux1 = aux.sort_values(by='Cuisines', ascending=False).reset_index()
            fig = px.bar(aux1, x='Country', y='Cuisines', title='Tipos culinários por país', labels={'Cuisines':'Tipos culinários', 'Country':'País'}, text_auto=True)
            fig.update_traces(textfont_size=12, textposition="outside", cliponaxis=False)
            st.plotly_chart(fig, use_container_width=True)
  

            
#--------------------
# Visão Cidades
#--------------------

with tab3:
    with st.container():
        aux = df1[['Restaurant ID', 'City', 'Country']].groupby('City').count().reset_index()
        fig = px.bar(aux, x='City', y='Restaurant ID', title='Número de restaurantes registrados por cidade', labels={'Restaurant ID':'Número de restaurantes', 'City':'Cidade'}, text_auto=True)
        fig.update_traces(textfont_size=12, textposition="outside", cliponaxis=False)
        st.plotly_chart(fig, use_container_width=True)
        
    with st.container():
            aux = df1[['City', 'Aggregate rating']].groupby('City').agg('median', 'sort_values')
            aux1 = aux.sort_values(by='Aggregate rating', ascending=False).reset_index()
            fig = px.bar(aux1, x='City', y='Aggregate rating', title='Nota média das avalições por cidade', labels={'Aggregate rating':'Nota média', 'City':'Cidade'}, text_auto=True)
            fig.update_traces(textfont_size=12, textposition="outside", cliponaxis=False)
            st.plotly_chart(fig, use_container_width=True)
            
            
    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            aux = df1[['City', 'Average Cost for two']].groupby('City').mean().reset_index()
            fig = px.bar(aux, x='City', y='Average Cost for two', title='Preço médio prato duas pessoas', labels={'Average Cost for two':'Preço médio', 'City':'Cidade'}, text_auto=True)
            fig.update_traces(textfont_size=12, textposition="outside", cliponaxis=False)
            st.plotly_chart(fig, use_container_width=True)
            
        with col2:
            aux = df2[['City', 'Cuisines']].groupby('City').nunique()
            aux1 = aux.sort_values(by='Cuisines', ascending=False).reset_index()
            aux2 = aux1.iloc[0:15,0]
            aux3 = aux1.iloc[0:15,1]
            fig = px.bar(aux1, x=aux2, y=aux3, title='Tipos culinários por cidade (Top 15)', labels={'y':'Tipos culinários', 'x':'Cidade'}, text_auto=True)
            fig.update_traces(textfont_size=12, textposition="outside", cliponaxis=False)
            st.plotly_chart(fig, use_container_width=True)

            
#----------------------
# Visão Restaurantes
#----------------------

with tab4:
    with st.container():
        aux = df1[['Cuisines', 'Average Cost for two']].groupby('Cuisines').mean().reset_index()
        fig = px.bar(aux, x='Cuisines', y='Average Cost for two', title='Valor médio prato para duas pessoas por tipo culinário', labels={'Cuisines':'Tipos culinários', 'Average Cost for two':'Valor médio'}, text_auto=True)
        fig.update_traces(textfont_size=12, textposition="outside", cliponaxis=False)
        st.plotly_chart(fig, use_container_width=True)
        
    with st.container():
        aux = df1[['Cuisines', 'Aggregate rating']].groupby('Cuisines').mean().reset_index()
        fig = px.bar(aux, x='Cuisines', y='Aggregate rating', title='Nota média das avaliações por tipo culinário', labels={'Cuisines':'Tipos culinários', 'Aggregate rating':'Avaliação média'}, text_auto=True)
        fig.update_traces(textfont_size=12, textposition="outside", cliponaxis=False)
        st.plotly_chart(fig, use_container_width=True)
        
    with st.container():
        aux = df1[['Aggregate rating', 'Has Online delivery']].groupby('Has Online delivery').mean().reset_index()
        fig = px.bar(aux, x='Has Online delivery', y='Aggregate rating', title='Relação entre restaurantes que aceitam pedido online e avaliação média', labels={'Has Online delivery':'Pedido online', 'Aggregate rating':'Avaliação média'})
        fig.update_xaxes(type='category')
        st.plotly_chart(fig, use_container_width=True)
        
        
    with st.container():
        aux = df1[['Aggregate rating', 'Has Table booking']].groupby('Has Table booking').mean().reset_index()
        fig = px.bar(aux, x='Has Table booking', y='Aggregate rating', title='Relação entre restaurantes que aceitam reserva e avaliação média', labels={'Has Table booking':'Reserva', 'Aggregate rating':'Avaliação média'})
        fig.update_xaxes(type='category')
        st.plotly_chart(fig, use_container_width=True)
        
    with st.container():
        aux = df1[['Aggregate rating', 'Price']].groupby('Price').mean().reset_index()
        fig = px.bar(aux, x='Price', y='Aggregate rating', title='Relação entre classificação de preço e avaliação média', labels={'Price':'Classificação de preço', 'Aggregate rating':'Avaliação média'})
        fig.update_xaxes(type='category')
        st.plotly_chart(fig, use_container_width=True)












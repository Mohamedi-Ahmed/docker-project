import streamlit as st
import pandas as pd
import requests

# Titre de l'application Streamlit
st.title("Analyses des ventes")

# Récupérer les données depuis l'API Flask
response = requests.get('http://flask-app:5000/')

if response.status_code == 200:
    data = pd.DataFrame(response.json())

    # Afficher les données
    st.write("### Les données : ")
    st.write(data)

    # Analyse 1 : Ventes totales par produit
    total_sales_by_product = data.groupby('product_name')['sales'].sum().reset_index()
    st.write("### Ventes totales par produit")
    st.bar_chart(total_sales_by_product.set_index('product_name'))

    # Analyse 2 : Ventes totales par région
    total_sales_by_region = data.groupby('region')['sales'].sum().reset_index()
    st.write("### Ventes totales par région")
    st.bar_chart(total_sales_by_region.set_index('region'))

    # Analyse 3 : Ventes totales au fil du temps
    data['date'] = pd.to_datetime(data['date'])
    total_sales_over_time = data.groupby('date')['sales'].sum().reset_index()
    st.write("### Ventes totales au fil du temps")
    st.line_chart(total_sales_over_time.set_index('date'))

else:
    st.error("Échec de la connexion à l'API")
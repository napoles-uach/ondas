import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Configuración de Streamlit
st.title('Mapa de Contorno del Nivel Sonoro')

# Parámetros para la simulación
potencia = st.slider('Potencia de la fuente sonora (W)', min_value=0.1, max_value=10.0, value=1.0, step=0.1)
max_distancia = st.slider('Máxima distancia de visualización (m)', min_value=10, max_value=100, value=50, step=10)

# Crear una malla de puntos alrededor de la fuente
x = np.linspace(-max_distancia, max_distancia, 400)
y = np.linspace(-max_distancia, max_distancia, 400)
x, y = np.meshgrid(x, y)
r = np.sqrt(x**2 + y**2) + 0.01  # Evitar dividir por cero en la ubicación de la fuente

# Cálculo de la Intensidad Sonora
intensidad = potencia / (4 * np.pi * r ** 2)

# Cálculo del Nivel Sonoro (en decibelios)
nivel_sonoro = 10 * np.log10(intensidad / 1e-12)

# Crear mapa de contorno con Plotly
fig = go.Figure(data=go.Contour(
    z=nivel_sonoro,
    x=np.linspace(-max_distancia, max_distancia, 400),
    y=np.linspace(-max_distancia, max_distancia, 400),
    colorscale='Jet',
    contours=dict(
        start=nivel_sonoro.min(),
        end=nivel_sonoro.max(),
        size=2,
        showlabels=True,
        labelfont=dict(size=12, color='white')
    ),
    colorbar_title='Nivel Sonoro (dB)'
))
fig.update_layout(
    title='Mapa de Contorno del Nivel Sonoro',
    xaxis_title='Distancia en X (m)',
    yaxis_title='Distancia en Y (m)'
)
st.plotly_chart(fig, use_container_width=True)


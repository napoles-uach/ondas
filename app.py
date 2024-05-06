import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Configuración de Streamlit
st.title('Simulación de Ondas Acústicas')

# Parámetros para la simulación
potencia = st.slider('Potencia de la fuente sonora (W)', min_value=0.1, max_value=10.0, value=1.0, step=0.1)
distancia = st.slider('Distancia desde la fuente sonora (m)', min_value=1.0, max_value=100.0, value=10.0, step=1.0)

# Constantes
rho = 1.21  # Densidad del aire kg/m³
c = 343  # Velocidad del sonido en aire m/s

# Cálculo de la Intensidad Sonora
intensidad = potencia / (4 * np.pi * distancia ** 2)

# Cálculo del Nivel Sonoro (en decibelios)
nivel_sonoro = 10 * np.log10(intensidad / 1e-12)

# Crear gráficos con Plotly
fig = go.Figure()
fig.add_trace(go.Scatter(x=[distancia], y=[intensidad], mode='markers', name='Intensidad'))
fig.update_layout(
    title='Intensidad Sonora en función de la Distancia',
    xaxis_title='Distancia (m)',
    yaxis_title='Intensidad (W/m²)',
    xaxis=dict(range=[0, 100]),
    yaxis=dict(type='log')
)
st.plotly_chart(fig, use_container_width=True)

st.write(f'Nivel Sonoro: {nivel_sonoro:.2f} dB')


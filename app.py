import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configuración de Streamlit
st.title('Simulación de Onda en una Cuerda')

# Parámetros para la simulación
tension = st.slider('Tensión de la cuerda (N)', min_value=10.0, max_value=1000.0, value=100.0, step=10.0)
densidad = st.slider('Densidad lineal de la cuerda (kg/m)', min_value=0.01, max_value=0.1, value=0.05, step=0.01)
frecuencia = st.slider('Frecuencia de vibración (Hz)', min_value=1.0, max_value=100.0, value=10.0, step=1.0)

# Constantes
longitud = 1.0  # longitud de la cuerda en metros

# Cálculo de la velocidad de la onda
velocidad = np.sqrt(tension / densidad)

# Tiempo
t = np.linspace(0, 2*np.pi, 400)
x = np.linspace(0, longitud, 1000)

# Función de onda
onda = np.sin(2 * np.pi * frecuencia * (t[:, None] - x[None, :] / velocidad))

# Graficar la onda en un momento dado
fig, ax = plt.subplots()
ax.plot(x, onda[200, :], label=f'Velocidad de onda: {velocidad:.2f} m/s')
ax.set_xlabel('Posición en la cuerda (m)')
ax.set_ylabel('Amplitud de la onda')
ax.legend()
st.pyplot(fig)

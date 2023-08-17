import streamlit as st

# Función para la pantalla Readme
def intro_page():
    st.title("Introduccion")
    st.write("Bienvenido a la pantalla Introduccion. Aquí encontrarás información sobre la aplicación.")

# Función para la pantalla Dashboard
def dashboard_page():
    st.title("Incrustar Dashboard de Power BI")
    
    st.write("Inserta el código de inserción del dashboard de Power BI:")
    embed_code = st.text_area("Código de inserción", height=200)
    
    st.write("Vista previa del dashboard:")
    st.write(embed_code, unsafe_allow_html=True)

# Función para la pantalla Machine Learning
def machine_learning_page():
    st.title("Machine Learning")
    st.write("Bienvenido a la pantalla Machine Learning. Aquí podrás interactuar con modelos de ML.")

# Configuración de la barra lateral de navegación
menu_options = ["Introduccion", "Dashboard", "Machine Learning"]
selected_page = st.sidebar.radio("Selecciona una opción:", menu_options)

# Mostrar la página correspondiente según la selección
if selected_page == "Readme":
    intro_page()
elif selected_page == "Dashboard":
    dashboard_page()
elif selected_page == "Machine Learning":
    machine_learning_page()
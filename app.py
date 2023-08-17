import streamlit as st
import joblib
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import nltk
nltk.download('punkt')
nltk.download('stopwords')

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
    # Cargar el modelo y el vectorizador TF-IDF
    model_filename = 'svm_model.pkl'
    loaded_model = joblib.load(model_filename)

    # Cargar el vectorizador TF-IDF utilizado durante el entrenamiento
    tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')  # Asegúrate de reemplazar 'tfidf_vectorizer.pkl' con el nombre correcto

    # Función de preprocesamiento de texto
    stemmer = PorterStemmer()
    stop_words = set(stopwords.words('english'))
    def preprocess_text(text):
        words = word_tokenize(text)
        cleaned_words = [stemmer.stem(word.lower()) for word in words if word.isalpha()]
        filtered_words = [word for word in cleaned_words if word not in stop_words]
        cleaned_text = ' '.join(filtered_words)
        return cleaned_text

    # Interfaz de Streamlit
    st.title("Análisis de Sentimiento")
    review = st.text_area("Ingresa tu reseña aquí:")
    if st.button("Predecir Sentimiento"):
        cleaned_review = preprocess_text(review)
        tfidf_review = tfidf_vectorizer.transform([cleaned_review])
        predicted_sentimiento = loaded_model.predict(tfidf_review)
        st.write("Sentimiento Predicho:", predicted_sentimiento[0])

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
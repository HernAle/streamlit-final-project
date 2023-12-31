import streamlit as st
import joblib
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import nltk
from PIL import Image
nltk.download('punkt')
nltk.download('stopwords')

# Función para la pantalla Dashboard
def intro_page():

    # Cargar una imagen usando Pillow
    image_path = 'data-solution.png'
    image = Image.open(image_path)
    st.image(image, caption='Logo Data Solution', use_column_width=True)
    # Leer el contenido del archivo Markdown
    with open("intro.md", "r") as markdown_file:
        markdown_text = markdown_file.read()

    # Mostrar el contenido del archivo Markdown
    st.markdown(markdown_text, unsafe_allow_html=True)

# Función para la pantalla Dashboard
def dashboard_page():
    st.title("Dashboard con Power BI")
    st.write("Bienvenido a la pantalla de Data Analytics. Aquí podrás interactuar con el Dashboard ")
    
    powerbi_url = "https://app.powerbi.com/reportEmbed?reportId=29ef71cf-051b-4691-a8fa-47799ebe2366&autoAuth=true&ctid=c4a66c34-2bb7-451f-8be1-b2c26a430158"
  
    # Ajustar el margen derecho del iframe para alejarlo del lado derecho
    iframe_style = "width: 1140px; margin: 0 auto; margin-right: 100px"
    iframe_code = f'<iframe title="Dashboard_Proyecto_Final" height="541.25" src="{powerbi_url}" frameborder="0" allowFullScreen="true" style="{iframe_style}"></iframe>'
    st.markdown(iframe_code, unsafe_allow_html=True)


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

    loaded_pipe = joblib.load("bert_model.joblib")

    text_to_analyze = "The food was more or less, the attention should be faster"
    #text_to_analyze = "The attention was not so good they took time to serve me"
    #text_to_analyze = "The menu was very varied and the food was very good."

    result = loaded_pipe(text_to_analyze)
    sentiment = result[0]['label']
    confidence = result[0]['score']

    print("Sentimiento:", sentiment)
    print("Confianza:", confidence)

# Configuración de la barra lateral de navegación
menu_options = ["Introduccion","Dashboard", "Machine Learning"]
selected_page = st.sidebar.radio("Selecciona una opción:", menu_options)

# Mostrar la página correspondiente según la selección
if selected_page == "Introduccion":
    intro_page()
elif selected_page == "Dashboard":
    dashboard_page()
elif selected_page == "Machine Learning":
    machine_learning_page()

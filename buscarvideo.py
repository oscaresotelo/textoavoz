from pytube import Search
import webbrowser
import streamlit as st

def buscar_videos_en_youtube(palabra_clave, max_resultados=5):
    st.write(palabra_clave)
    try:
        # Crear un objeto de búsqueda
        search_query = Search(palabra_clave)
        
        # Obtener los primeros 'max_resultados' resultados de la búsqueda
        resultados = search_query.results[:max_resultados]

        # Abrir el primer resultado en el navegador
        if resultados:
            primer_video = resultados[0]
            video_url = f"https://www.youtube.com/watch?v={primer_video.video_id}"
            webbrowser.open(video_url)
            print(palabra_clave)
            # Imprimir los títulos y enlaces de los videos encontrados
        #     for video in resultados:
        #         video_url = f"https://www.youtube.com/watch?v={video.video_id}"
        #         print(f"Título: {video.title}")
        #         print(f"URL: {video_url}\n")
        # else:
        #     print("No se encontraron resultados para la búsqueda.")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Palabra clave para la búsqueda
# palabra_clave = input("Ingrese la palabra clave para buscar en YouTube: ")

# # Número máximo de resultados a mostrar (opcional)
# # max_resultados = int(input("Ingrese el número máximo de resultados a mostrar (predeterminado es 5): ") or 5)

# # Llamar a la función para buscar videos en YouTube
# buscar_videos_en_youtube(palabra_clave, 10)

import google.generativeai as genai
from .config import GEMINI_API_KEY, GENAI_MODEL

# Configuracion del cliente de IA
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(GENAI_MODEL)

def summarize_news(raw_text):
    """
    Analiza el texto crudo utilizando IA para filtrar y resumir contenido relevante.
    
    Args:
        raw_text (str): Texto consolidado de noticias crudas.
        
    Returns:
        str: Reporte final procesado o mensaje de error.
    """
    if not raw_text:
        return "Aviso: No hubo noticias para analizar."

    print("[INFO] Enviando datos a Gemini para analisis...")
    
    # Prompt ajustado para ser texto plano y profesional
    prompt = f"""
    Actua como un Lead Data Engineer. Analiza las siguientes noticias crudas.
    
    Filtra y selecciona SOLO las 3 mas criticas para un perfil de Data Engineering, Cloud o Backend.
    Ignora noticias de relleno, ventas o marketing generico.
    
    IMPORTANTE: No uses emojis ni iconos en tu respuesta. Usa formato de texto plano y limpio.
    
    Formato de salida requerido para cada noticia:
    1. TITULO: [Titulo en Espanol]
       RESUMEN: (Maximo 20 palabras explicando la noticia)
       IMPACTO: (Por que es relevante tecnicamente)
       LINK: [Inserta el link original aqui]
    
    ---
    Noticias Crudas:
    {raw_text}
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"[ERROR] Falla en la capa de IA: {e}"
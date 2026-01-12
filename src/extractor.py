import feedparser
from .config import RSS_FEEDS

def fetch_latest_news(limit=3):
    """
    Se conecta a los RSS feeds definidos en la configuracion.
    
    Args:
        limit (int): Numero maximo de noticias a extraer por fuente.
        
    Returns:
        str: Cadena de texto con las noticias crudas formateadas.
    """
    print(f"[INFO] Iniciando extraccion de {len(RSS_FEEDS)} fuentes...")
    news_items = []

    for url in RSS_FEEDS:
        try:
            feed = feedparser.parse(url)
            source_name = feed.feed.get('title', 'Fuente desconocida')
            print(f"[INFO] Procesando fuente: {source_name}")
            
            # Extraer los N mas recientes
            for entry in feed.entries[:limit]:
                # Limpieza basica de titulo y link
                clean_item = f"Fuente: {source_name} | Titulo: {entry.title} | Link: {entry.link}"
                news_items.append(clean_item)
                
        except Exception as e:
            print(f"[ERROR] Fallo al leer {url}: {e}")

    return "\n".join(news_items)
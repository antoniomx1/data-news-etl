import requests
from .config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def send_telegram_message(message):
    """
    Envia el reporte final al chat de Telegram especificado.
    
    Args:
        message (str): El texto del mensaje a enviar.
    """
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("[WARN] Telegram no configurado. Omitiendo envio.")
        return

    print("[INFO] Enviando reporte a Telegram...")
    
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    
    # Telegram tiene un limite estricto de 4096 caracteres por mensaje.
    # La implementacion actual asume que el resumen generado por la IA 
    # se mantendra dentro de este limite.
    # TODO: Implementar logica de paginacion (chunking) para reportes extensos.
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown" 
    }
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("[INFO] Mensaje entregado exitosamente.")
        else:
            print(f"[ERROR] Respuesta no exitosa de Telegram: {response.text}")
    except Exception as e:
        print(f"[ERROR] Fallo la conexion con la API de Telegram: {e}")
"""
Tech Trends Radar - ETL Pipeline
--------------------------------
Orquestador principal.
"""
import warnings
import os

# 1. SILENCIADOR DE WARNINGS (Para que no salga basura de Google/Langchain)
# Esto le dice a Python: "Ignora las advertencias de deprecacion por ahora"
warnings.filterwarnings("ignore")
os.environ["GRPC_VERBOSITY"] = "ERROR" # Calla logs internos de conexion feos

from src.extractor import fetch_latest_news
from src.analyzer import summarize_news
from src.notifier import send_telegram_message

def run_pipeline():
    """
    Ejecuta el flujo completo: Extract -> Transform -> Load
    """
    print("INICIANDO PROCESO")
    
    # 1. EXTRACT
    raw_data = fetch_latest_news()
    if not raw_data:
        print("[WARN] Sin datos. Abortando.")
        return

    # 2. TRANSFORM (IA)
    final_report = summarize_news(raw_data)
    
    # 3. DELIVERY (Telegram)
    send_telegram_message(final_report)

    # 4. LOGGING (Respaldo en la Nube)
    # debuggear en GitHub Actions si falla Telegram
    print("\n" + "-"*20 + " LOG DE RESPALDO " + "-"*20)
    print(final_report)
    print("-" * 55)
    
    print("\n[INFO] Pipeline finalizado exitosamente.")

if __name__ == "__main__":
    run_pipeline()
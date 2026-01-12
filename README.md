# Data News Radar

### Sistema de Inteligencia Técnica Automatizado (ETL + AI)

**Pipeline "Serverless" de curación de contenidos basado en IA Generativa.**

Este proyecto implementa un pipeline ETL automatizado que monitorea fuentes de noticias técnicas, filtra el ruido mediante modelos de lenguaje (LLM) y entrega resúmenes ejecutivos de alto valor para perfiles de Data Engineering.

## Arquitectura del Sistema

El sistema opera bajo una arquitectura de flujo de datos secuencial y serverless:

1.  **Ingesta de Datos (Extraction):** Scripts automatizados consumen feeds RSS de fuentes técnicas pre-seleccionadas (Google Cloud, Real Python, Hacker News).
2.  **Motor de Inteligencia (AI Core):** Integración con **Google Gemini 2.5 Flash** para realizar análisis semántico:
    * Filtrado de contenido irrelevante o publicitario.
    * Generación de resúmenes técnicos concisos.
    * Evaluación de relevancia para roles de Ingeniería de Datos.
3.  **Orquestación (Serverless):** Ejecución programada mediante **GitHub Actions**, eliminando la necesidad de servidores dedicados (infraestructura 100% nube).
4.  **Interfaz de Usuario (Delivery):** Despliegue de notificaciones push a través de un Bot de Telegram privado.

## Stack Tecnológico

* **Lenguaje:** Python 3.10+
* **IA / NLP:** Google Generative AI SDK (Gemini 2.5 Flash)
* **Orquestación:** GitHub Actions (Cron Job / CI/CD)
* **Data Engineering:** Feedparser, Requests
* **Interfaz:** Telegram Bot API
* **Control de Versiones:** Git / GitHub

## Funcionalidades Clave

* **Curación de Contenido por Relevancia:** La IA distingue entre artículos genéricos y novedades técnicas críticas (releases, arquitecturas, vulnerabilidades).
* **Orquestación Automatizada:** El sistema se "despierta" automáticamente de Lunes a Viernes a las 09:00 AM para procesar la información.
* **Resumen Ejecutivo:** Transforma lecturas de 30 minutos en un reporte de lectura de 2 minutos.
* **Zero-Maintenance:** Arquitectura efímera que no requiere mantenimiento de servidores ni bases de datos persistentes.

## Demo

**Ejemplo de Output en Telegram:**

> **TITULO:** Python's deque: Implementación Eficiente de Colas y Pilas
>
> **RESUMEN:** Un artículo fundamental sobre `deque` de Python para implementar colas y pilas eficientes, crucial para optimización de estructuras de datos.
>
> **IMPACTO:** Es relevante para la optimización de algoritmos y la gestión de flujos de datos en pipelines.
>
> **LINK:** [https://realpython.com/python-deque/](https://realpython.com/python-deque/)

## Configuración e Instalación

**1. Clonar el repositorio:**
```bash
git clone [https://github.com/antoniomx1/data-news-etl.git](https://github.com/antoniomx1/data-news-etl.git)
cd data-news-etl
```
**2. Instalar dependencias:**
```bash
pip install -r requirements.txt
```

**3. Configurar Variables de Entorno (.env): Crea un archivo .env en la raíz con las siguientes credenciales:**
```bash
GEMINI_API_KEY="tu_api_key_de_google"
TELEGRAM_BOT_TOKEN="tu_token_de_telegram"
TELEGRAM_CHAT_ID="tu_id_de_usuario"
```
**4. Ejecutar el Pipeline (Manual):**
```bash
python src/main.py
```

**5. Configurar Automatización (GitHub):**
Agrega las mismas variables en **Settings > Secrets and variables > Actions** de tu repositorio para activar la ejecución automática diaria.

## Autor

**Antonio Velázquez**
*Data Engineer*
[LinkedIn](https://www.linkedin.com/in/antoniomx1/) | [GitHub](https://github.com/antoniomx1)







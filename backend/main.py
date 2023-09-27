from fastapi import FastAPI, HTTPException
from google.cloud import storage
import firebase_admin
from firebase_admin import firestore, credentials
import os
from fastapi.middleware.cors import CORSMiddleware


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/santi/FIFA_REVIEWS/backend/google-credentials.json'

#if not os.getenv("GOOGLE-APPLICATION-CREDENTIALS"):
     #os.environ["GOOGLE-APPLICATION-CREDENTIALS"] = 'google-credentials.json'

credentials_path = 'C:/Users/santi/FIFA_REVIEWS/backend/google-credentials.json'
cred = credentials.Certificate(credentials_path)

firebase_admin.initialize_app(cred)
#firebase_admin.initialize_app()

app = FastAPI()

# Configurar CORS para permitir el acceso desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Reemplaza con la URL de tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializa Firestore
db = firestore.Client()

@app.get("/cards")
async def get_cards():
    cards = []
    #Reemplaza "your_collection_name" con el nombre real de la colección en Firestore.
    collection_ref = db.collection("cards_information")
    for doc in collection_ref.stream():
        card_data = doc.to_dict()
        cards.append(card_data)
    print(cards)
    return cards




if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8080)
    # TODO: Refactor code


    # Or run me in the terminal with:  uvicorn main:app --reload --host 127.0.0.1 --port 8080 --env-file dev.env
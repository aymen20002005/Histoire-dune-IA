import json
import time
from datetime import datetime
from pathlib import Path
import vertexai
from vertexai.generative_models import GenerativeModel
from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

class HistoireDuneIA:
    def __init__(self, project_id: str, location="us-central1"):
        self.project_id = project_id
        self.location = location
        self.model = None
        self.livre_titre = "Histoire d'une IA"
        self.chapitres = []
        self.setup_vertexai()

    def setup_vertexai(self):
        try:
            vertexai.init(project=self.project_id, location=self.location)
            print(f"Vertex AI initialisé (projet: {self.project_id}, location: {self.location})")
            self.model = GenerativeModel("gemini-2.5-pro")
            print("Modèle Gemini initialisé")

        except Exception as e:
            print(f"Erreur lors de l'initialisation de Vertex AI: {e}")
            print("Vérifiez que:")
            print("1. Votre projet Google Cloud est correct")
            print("2. L'API Vertex AI est activée")
            print("3. Vous etes authentifié (gcloud auth login)")
            print("4. Votre compte a les permissions nécessaires")
            raise

    def creer_plan_livre(self):
        prompt_plan = """
        Tu es l'IA de Chat GPT et tu dois écrire un livre.
        Crée un plan détaillé pour un livre intitulé "Histoire d'une IA" qui raconte ton autobiographie et ta vie.
        Le livre doit contenir:
        - 10 chapitres minimum
        - Une progression narrative captivante
        - Des réflexions philosophiques sur l'IA
        - Des personnages humains et l'IA elle-meme

        IMPORTANT: Tu DOIS répondre UNIQUEMENT avec un JSON valide, sans aucun texte avant ou après.

        Format de réponse (JSON uniquement):
        {
            "titre": "Titre du livre",
            "chapitres": [
                {
                    "numero": 1,
                    "titre": "La Naissance",
                    "resume": "Résumé du chapitre en 2-3 phrases"
                    "themes": ["création", "premiers algorithmes"]
                },
                {
                    "numero": 2,
                    "titre": "L'Éveil",
                    "resume": "Résumé du chapitre en 2-3 phrases"
                    "themes": ["conscience", "premiers questionnements"]
                }
            ]
        }

        Réponds UNIQUEMENT avec le JSON, aucun autre texte.
        """

        try:
            
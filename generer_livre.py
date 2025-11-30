from histoire_dune_ia import HistoireDuneIA

def main():
    """Script Principal"""
    print("Génération du livre 'Histoire d'une IA'")
    print("=" * 50)

    PROJECT_ID = ""
    LOCATION = "europe-west4"

    try:
        generateur = HistoireDuneIA(project_id=PROJECT_ID, location=LOCATION)
        generateur.generer_livre_complet()
    except Exception as e:
        print(f"Erreur: {e}")
        print("\n Solutions possibles :")
        print("* Vérifiez votre ID de projet GCP")
        print("* Activez l'API Vertex AI dans la console GCP")
        print("* Authentifiez-vous avec 'gcloud auth application-default login'")
        print("* Vérifiez vos permissions Vertex AI")

if __name__ == "__main__":
    main()
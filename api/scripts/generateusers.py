import requests

# URL de l'API où envoyer les requêtes POST
url = 'http://localhost:8000/api/users/create-user/'

# Ouvrir le fichier contenant les utilisateurs
with open('../dataset/fake_users.txt', 'r') as file:
    lines = file.readlines()

# Parcourir chaque ligne du fichier
for line in lines:
    email, password = line.strip().split(',')
    
    # Préparer les données pour la requête POST
    data = {
        'email': email,
        'password': password
    }
    
    # Effectuer la requête POST
    response = requests.post(url, json=data)
    
    # Vérifier la réponse
    if response.status_code == 201:
        print(f"Utilisateur créé : {email}")
    else:
        print(f"Erreur lors de la création de l'utilisateur {email}: {response.text}")
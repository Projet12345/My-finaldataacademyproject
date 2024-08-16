import requests

# URL de l'API
url = 'http://localhost:8000/api/comment/'

# Lecture du fichier et envoi des commentaires
with open('../dataset/fakes_comments.txt', 'r') as file:
    for line in file:
        parts = line.strip().split(',')
        if len(parts) == 4:
            user_name = parts[0]
            user_id = int(parts[1])
            film_id = int(parts[2])
            content = parts[3]

            comment_data = {
                "user_name": user_name,
                "user": user_id,
                "film_id": film_id,
                "content": content,
            }

            response = requests.post(url, json=comment_data)

            if response.status_code == 201:
                print(f"Comment by {user_name} inserted successfully.")
            else:
                print(f"Failed to insert comment by {user_name}: {response.text}")
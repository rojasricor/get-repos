import os
import requests

# Tu nombre de usuario de GitHub
username = "rojasricor"

# Obten una lista de tus repositorios desde la API de GitHub
url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)
repos = response.json()

# Directorio donde deseas clonar los repositorios
base_directory = "~/Desktop/repos"

# Recorre la lista de repositorios y clónalos
for repo in repos:
    repo_name = repo["name"]
    repo_url = repo["clone_url"]
    repo_directory = os.path.join(base_directory, repo_name)
    
    # Clona el repositorio
    os.system(f"git clone {repo_url} {repo_directory}")

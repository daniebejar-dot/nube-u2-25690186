import os, time, requests
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("OPENWEATHER_API_KEY")

# API Key 
key = "3d23c8b375a528f82b5baffdd38626fa"

# 1. JSONPlaceholder (GET y POST)
t0 = time.perf_counter()
r = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=10)
print("GET Posts:", r.status_code, f"{(time.perf_counter()-t0)*1000:.0f} ms", len(r.content), "bytes")

t0 = time.perf_counter()
r = requests.post("https://jsonplaceholder.typicode.com/posts", json={"title": "nuevo"}, timeout=10)
print("POST Post:", r.status_code, f"{(time.perf_counter()-t0)*1000:.0f} ms", len(r.content), "bytes")

# 2. PokéAPI 
t0 = time.perf_counter()
r = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu", timeout=10)
ms = (time.perf_counter() - t0) * 1000
datos = r.json()
habilidades = [a["ability"]["name"] for a in datos["abilities"]]
print("PokéAPI:", r.status_code, f"{ms:.0f} ms", len(r.content), "bytes", habilidades)

# 3. OpenWeatherMap (Ciudad Valles con .env)
t0 = time.perf_counter()
r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Ciudad%20Valles,MX&appid={key}&units=metric", timeout=10)
print("Clima Valles:", r.status_code, f"{(time.perf_counter()-t0)*1000:.0f} ms", len(r.content), "bytes")

# 4. Errores a propósito (404 y 401)
t0 = time.perf_counter()
r = requests.get("https://jsonplaceholder.typicode.com/posts/999999", timeout=10)
print("Error 404:", r.status_code, f"{(time.perf_counter()-t0)*1000:.0f} ms", len(r.content), "bytes")

t0 = time.perf_counter()
r = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Ciudad%20Valles,MX&appid=INVALIDA", timeout=10)
print("Error 401:", r.status_code, f"{(time.perf_counter()-t0)*1000:.0f} ms", len(r.content), "bytes")
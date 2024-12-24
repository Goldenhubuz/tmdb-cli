import requests
from icecream import ic

picture_id = "cdqLnri3NEGcmfnqwk2TSIYtddg"
url = f"https://image.tmdb.org/t/p/w600_and_h900_bestv2/{picture_id}.jpg"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2MDNiOGUzYWJmYThjMWM5MmU0YTQ0NDUxZTg0ZDI3YyIsIm5iZiI6MTczNTA2MDQ5My44NzIsInN1YiI6IjY3NmFlYzBkZmNjZTM5ZDllZTY0YmRhMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.TUfjOu5Y3CjX1BILd7CDlsry6HJCOEfjfsR8DEfODMs"
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    with open(f"{picture_id}.jpg", 'wb') as f:
        f.write(response.content)
ic(response.url)
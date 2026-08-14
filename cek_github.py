import requests 
username = input("Masukan username GitHub anda: ")
response = requests.get(f"https://api.github.com/users/{username}")
if response.status_code == 200:
    hasil = response.json()
    print(f"Data : {hasil['created_at']}")
else:
    print("API gagal")    


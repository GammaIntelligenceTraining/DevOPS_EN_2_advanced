import requests
from pprint import pp

# 200s -> Success
# 300s -> Redirect (Success)
# 400s -> Client Error (Failure)
# 500s -> Server Error (Failure)

# response = requests.get("https://api.github.com/repos/torvalds/this-does-not-exists")
# print(response.status_code)

# content_type = response.headers.get("Content-Type")
# server_software = response.headers.get("Server")
# rate_limit = response.headers.get("X-RateLimit-Remaining")

# print(f'*** Content-Type\n{content_type}')
# print(f'*** Server\n{server_software}')
# print(f'*** Rate Limit\n{rate_limit}')
# # pp(content_type) 

BASE_URL = "https://fakestoreapi.com"

endpoint = "/users"
url = f"{BASE_URL}{endpoint}"

# response = requests.get(url)
# print(f"Status: {response.status_code}")
# print(f"Response:\n{response.json()}")
# pp(response.json())

# payload = {
#     "username": "Jack Smith",
#     "email": "jack.smith@example.com",
#     "password": "SuperSecret123"
# }

# # post_response = requests.post(url, json=payload)

# # print(f"Status: {post_response.status_code}")
# # pp(post_response.json())

# user_id = 1
# endpoint = f"/users/{user_id}"
# target_url = f"{BASE_URL}{endpoint}"

# updated_user_payload = {
#     "username": "john_doew_updated",
#     "email": "john.updated@example.com"
# }

# put_response = requests.put(target_url, json=updated_user_payload)

# print(f"Status: {put_response.status_code}")
# pp(put_response.json())

# response = requests.get(url+"asdasdasdsadas", headers={"Accept": "application/json"})

# raw_text = response.json()

# print(raw_text)
# print(type(raw_text))
# print(len(raw_text))

# my_car = {
#     "make": "VW",
#     "model": "Gold",
#     "info": {
#         "color": "red",
#     }
# }

# print(my_car['info'].get("mileage", "dev"))

# response = requests.get(url)
# users_list = response.json()

# print(f"{'ID':<4} {'USERNAME':<15} {'EMAIL':<25} {'CITY':<15}")
# print("*" * 60)
# for user in users_list:
#     user_id = user.get("id")
#     username = user.get("username")
#     email = user.get("email")
#     user_city = user.get("address", {}).get("city", "N/A")

#     print(f"{user_id:<4} {username:<15} {email:<25} {user_city:<15}")

# search_url = "https://api.github.com/search/repositories"

# query_params = {
#     "q": "devops",
#     "sort": "stars",
#     "order": "desc"
# }

# search_res = requests.get(search_url, params=query_params)
# top_repo = search_res.json()["items"][0]

# print(f"Top repo: {top_repo.get("name")} with {top_repo.get("stargazers_count")} stars")
# print(f"URL: {top_repo.get("html_url")}")



# secure_headers = {
#     "Authorization": "Bearer YOUR_SECRET_TOKEN",
#     "Accept": "application/json"
# }

# requests.post(url, headers=secure_headers)

# WEBHOOK_URL = "https://webhook.site/8f513663-e73c-42df-b1cf-63c68ab5a2ee"

# alert_payload = {
#     "content": "[CRITICAL ALERT]: Production CPU is at 95%"
# }

# try:
#     post_response = requests.post(WEBHOOK_URL, json=alert_payload)
#     print(f"Alert dispatched! Status: {post_response.status_code}")
# except requests.exceptions.MissingSchema:
#     print("[WARNING] Please replace url with a valid one")

# bad_res = requests.get("https://api.github.com/repos/torvalds/this-does-not-exists")

# try:
#     bad_res.raise_for_status()
# except requests.exceptions.HTTPError:
#     print("There was an error.")

# try:
#     requests.get("https://tools-httpstatus.pickup-services.com/200?sleep=5000", timeout=10)
# except requests.exceptions.Timeout:
#     print("[ERROR] Connection timed out!")

requests.exceptions.RequestException
"""
Module 6: HTTP Networking & REST APIs for Integrations
DevOps Engineering - Student Handout
"""

import requests
import json
import time

print("=" * 70)
print("SECTION 1: HTTP Fundamentals & GET Requests")
print("-" * 70)
"""
UNDERSTANDING THE HTTP REQUEST-RESPONSE CYCLE:

DevOps automation relies heavily on HTTP APIs (REST APIs) to check system health,
trigger CI/CD pipelines, query monitoring servers, and provision cloud resources.
Under the hood, HTTP (Hypertext Transfer Protocol) is a text-based, stateless
client-server protocol running over TCP/IP at Layer 7 of the OSI model.

Every HTTP interaction consists of two distinct halves:
1. The Client sends an HTTP REQUEST.
2. The Server returns an HTTP RESPONSE.

================================================================================
1. WHAT THE CLIENT SENDS IN AN HTTP REQUEST:
================================================================================
- HTTP Method (Verb): Specifies the desired action:
  * GET: Retrieve an existing resource (safe, read-only, no request body).
  * POST: Submit data to create a new resource or trigger an action (webhook).
  * PUT / PATCH: Replace or partially update an existing resource.
  * DELETE: Remove a resource from the server.
- Request URL / Path & Query Parameters: The address of the endpoint (e.g.,
  https://api.github.com/repos/torvalds/linux?sort=stars).
- Request Headers (The 'Envelope'): Metadata key-value pairs instructing the server
  how to process the request:
  * 'Content-Type': Format of data in the request body (e.g., 'application/json').
  * 'Accept': Format the client expects in the response (e.g., 'application/json').
  * 'Authorization': Security credentials (e.g., 'Bearer <token>' or API keys).
  * 'User-Agent': Identifier string for the calling tool or script.
- Request Body (Payload): The actual data being transmitted to the server. For GET
  requests, the body is empty. For POST and PUT, it usually contains JSON data.

================================================================================
2. WHAT THE SERVER RETURNS IN AN HTTP RESPONSE:
================================================================================
- Status Code: A 3-digit number indicating the result:
  * 2xx Success (e.g., 200 OK, 201 Created).
  * 3xx Redirection (e.g., 301 Moved Permanently).
  * 4xx Client Error (e.g., 400 Bad Request, 401 Unauthorized, 404 Not Found).
  * 5xx Server Error (e.g., 500 Internal Error, 502 Bad Gateway, 504 Timeout).
- Response Headers: Metadata describing the server and payload:
  * 'Content-Type': Format of returned body (e.g., 'application/json', 'text/html').
  * 'Content-Length': Size of the response payload in bytes.
  * 'Server': Software serving the request (e.g., 'nginx/1.24.0', 'cloudflare').
  * 'Date': Server timestamp when the response was generated.
  * Rate-limiting headers: 'X-RateLimit-Remaining', 'X-RateLimit-Reset'.
- Response Body: The actual resource data returned by the server, such as a JSON
  object, HTML document, or binary file.

================================================================================
3. THE ENVELOPE METAPHOR:
================================================================================
Think of an HTTP transaction like sending a letter through postal mail:
- The Request Body is the letter written inside the envelope.
- The Request Headers are the stamp, return address, and recipient address
  written on the outside of the envelope.
- The Response Headers are the postmark and delivery status on the return envelope.
- The Response Body is the reply letter sent back by the recipient.

Python's third-party 'requests' library abstracts away socket creation, byte encoding,
and raw TCP streaming, providing a clean, Pythonic interface for HTTP automation.
"""

# 1.1 The Basic GET Request
print("\n--- 1.1 Fetching Public GitHub Data ---")
response = requests.get("https://api.github.com/repos/torvalds/linux")
print(f"Status Code: {response.status_code}") 
# Output: Status Code: 200 (Which means OK!)


# 1.2 Forcing a 404 Error
print("\n--- 1.2 Handling Bad URLs ---")
bad_response = requests.get("https://api.github.com/repos/torvalds/this-does-not-exist")
print(f"Bad Repo Status: {bad_response.status_code}")
# Output: Bad Repo Status: 404


# 1.3 Inspecting Response Headers
print("\n--- 1.3 Reading Response Headers ---")
# Headers contain critical operational metadata about the payload and server state
content_type = response.headers.get("Content-Type")
server_engine = response.headers.get("Server")
rate_limit = response.headers.get("X-RateLimit-Remaining")

print(f"Content-Type: {content_type}")
print(f"Server Engine: {server_engine}")
print(f"GitHub API Calls Remaining: {rate_limit}")
# Inspecting headers prevents errors: never call response.json() if Content-Type is not JSON!


# 1.4 Dynamic URL & Endpoint Construction
print("\n--- 1.4 Base URLs & API Endpoints ---")
# Defining a base host URL and appending specific endpoint paths prevents hardcoding across scripts.
# This makes switching between staging and production clusters a clean, single-variable update.
BASE_URL = "https://fakestoreapi.com"
endpoint = "/users"
target_url = f"{BASE_URL}{endpoint}"
print(f"Target Service URL: {target_url}")

# Fetch existing users list
list_response = requests.get(target_url)
print(f"GET Users Status: {list_response.status_code}")
print(f"Total Users Found: {len(list_response.json())}")


# 1.5 Adding a New User with HTTP POST
print("\n--- 1.5 Adding a New User with POST ---")
# The POST method sends a serialized JSON payload to create a brand new resource on the server.
# The json= argument automatically converts the dictionary to JSON and sets the Content-Type header.
new_user_payload = {
    "username": "john_doe",
    "email": "john@example.com",
    "password": "pass123"
}

post_response = requests.post(target_url, json=new_user_payload)
print(f"POST Status Code: {post_response.status_code}")
print(f"Created User ID: {post_response.json().get('id')}")


# 1.6 Updating a User with HTTP PUT
print("\n--- 1.6 Updating a User with PUT ---")
# The PUT method updates an existing record identified by its unique ID on the server.
# It replaces fields on the target endpoint with the updated dictionary payload.
user_id = 1
update_url = f"{BASE_URL}{endpoint}/{user_id}"
updated_user_fields = {
    "username": "john_doe_updated",
    "email": "john.updated@example.com"
}

put_response = requests.put(update_url, json=updated_user_fields)
print(f"PUT Status Code: {put_response.status_code}")
print(f"Updated User Echo: {put_response.json()}")


# 1.7 Decommissioning a User with HTTP DELETE
print("\n--- 1.7 Deleting a User with DELETE ---")
# The DELETE method instructs the server to remove the resource matching the target URL.
# Like GET, DELETE requests typically do not carry a body payload.
delete_url = f"{BASE_URL}{endpoint}/{user_id}"
delete_response = requests.delete(delete_url)
print(f"DELETE Status Code: {delete_response.status_code}")
print(f"Deleted User Echo (ID): {delete_response.json().get('id')}")


print("\n" + "=" * 70)
print("SECTION 2: Data Serialization & JSON")
print("-" * 70)
"""
Modern cloud APIs transmit structured telemetry and configurations formatted
in JSON (JavaScript Object Notation). Python provides seamless mapping:
- JSON Objects {} map directly to Python Dictionaries.
- JSON Arrays [] map directly to Python Lists.

The .json() method decodes network response text into native Python structures.
"""

# 2.1 The Raw Text vs. The JSON Method & Schema Inspection
print("\n--- 2.1 Raw Text vs .json() Deserialization ---")
users_endpoint_url = "https://fakestoreapi.com/users"
users_response = requests.get(users_endpoint_url)

# response.text is an unindexed raw string
raw_payload = users_response.text
print(f"Type of .text: {type(raw_payload)} (Length: {len(raw_payload)} characters)")

# response.json() converts the body into a native Python list of dictionaries
users_data = users_response.json()
print(f"Type of .json(): {type(users_data)} (Records: {len(users_data)})")

# Pretty-printing with json.dumps allows clear inspection of deep API schemas
first_record = users_data[0]
print("\nFirst User Record Schema Preview:")
print(json.dumps(first_record, indent=2))


# 2.2 Deep Multi-Tier Traversals & Defensive .get()
print("\n--- 2.2 Multi-Tier Nested Keys & Defensive Lookups ---")
# Traversing nested dictionaries using chained brackets
first_name = first_record["name"]["firstname"]
last_name = first_record["name"]["lastname"]
city = first_record["address"]["city"]
lat = first_record["address"]["geolocation"]["lat"]

print(f"User: {first_name.capitalize()} {last_name.capitalize()}")
print(f"Location: {city} (Coordinates: {lat})")

# Defensive extraction: using .get() with fallback defaults prevents KeyError
# crashes when API providers omit optional keys in certain records.
department = first_record.get("department", "Unassigned")
access_tier = first_record.get("tier", "Standard-Access")
print(f"Department: {department} | Access Tier: {access_tier}")


# 2.3 Iterating Over Collections & Building Administrative Reports
print("\n--- 2.3 Iterating Over Collections & Formatting Output ---")
print(f"{'ID':<4} {'USERNAME':<15} {'EMAIL':<25} {'CITY':<15}")
print("=" * 60)

for record in users_data:
    uid = record.get("id")
    uname = record.get("username", "unknown")
    uemail = record.get("email", "unknown")
    ucity = record.get("address", {}).get("city", "N/A")
    print(f"{uid:<4} {uname:<15} {uemail:<25} {ucity:<15}")


# 2.4 Hands-On Student Micro-Task: User Directory & Regional Audit
print("\n--- 2.4 Micro-Task: User Directory & Regional Audit ---")
# Task Goal:
# Loop over users_data, extract full names (firstname + lastname capitalized),
# email, and zipcode. Count how many accounts have a phone starting with '1-'.
na_accounts = 0

print(f"{'ID':<4} {'NAME':<20} {'EMAIL':<25} {'ZIPCODE':<10}")
print("-" * 65)

for record in users_data:
    uid = record.get("id")
    name_info = record.get("name", {})
    fn = name_info.get("firstname", "").capitalize()
    ln = name_info.get("lastname", "").capitalize()
    display_name = f"{fn} {ln}".strip()
    
    email = record.get("email", "N/A")
    zipcode = record.get("address", {}).get("zipcode", "N/A")
    phone = record.get("phone", "")
    
    if phone.startswith("1-"):
        na_accounts += 1
        
    print(f"{uid:<4} {display_name:<20} {email:<25} {zipcode:<10}")

print("-" * 65)
print(f"Total Audited: {len(users_data)} users")
print(f"North American Regional Accounts (1-*): {na_accounts}")


print("\n" + "=" * 70)
print("SECTION 3: Advanced Networking (POST & Auth)")
print("-" * 70)

# 3.1 Query Parameters
print("\n--- 3.1 Safely Building Search URLs ---")
search_url = "https://api.github.com/search/repositories"
query_params = {"q": "devops", "sort": "stars", "order": "desc"}

search_res = requests.get(search_url, params=query_params)
search_data = search_res.json()
if "items" in search_data and search_data["items"]:
    top_repo = search_data['items'][0]
    print(f"Top DevOps Repo: {top_repo['name']} with {top_repo['stargazers_count']} stars")
else:
    print(f"Search API returned HTTP {search_res.status_code} (rate limit reached or query throttled).")


# 3.2 Authentication (Bearer Tokens)
print("\n--- 3.2 Injecting Security Headers ---")
secure_headers = {
    "Authorization": "Bearer YOUR_SUPER_SECRET_TOKEN",
    "Accept": "application/json"
}
# requests.get("https://api.fake.com/secure", headers=secure_headers)
print("Auth headers configured.")


# 3.3 Dispatching Webhooks (HTTP POST)
# Concept: A Webhook is an automated, event-driven HTTP callback.
# Instead of polling (repeatedly sending GET requests asking for updates),
# the source system pushes an HTTP POST with a JSON payload to a target URL
# the exact moment an event occurs (e.g., CI/CD build finished, CPU alert triggered).
print("\n--- 3.3 Firing a Webhook Alert ---")
WEBHOOK_URL = "https://webhook.site/YOUR-UNIQUE-UUID-HERE" # <-- UPDATE THIS!

alert_payload = {
    "content": "[CRITICAL ALERT]: Production Database CPU is at 95%!"
}

# We use the 'json=' parameter to automatically set the correct headers and serialize the dict
try:
    post_response = requests.post(WEBHOOK_URL, json=alert_payload)
    print(f"Alert dispatched! Server responded with: {post_response.status_code}")
except requests.exceptions.MissingSchema:
    print("[WARNING] Please replace WEBHOOK_URL with a valid URL to run this demo.")


print("\n" + "=" * 70)
print("SECTION 4: Defensive Engineering")
print("-" * 70)
"""
Networks are unreliable. Servers crash, DNS fails, and firewalls block traffic.
A professional DevOps script must NEVER crash due to an unhandled network error.
"""

# 4.1 The Silent Failure Trap (raise_for_status)
print("\n--- 4.1 Forcing HTTP Errors ---")
try:
    bad_res = requests.get("https://api.github.com/repos/torvalds/this-does-not-exist")
    bad_res.raise_for_status() 
except requests.exceptions.HTTPError:
    print("Caught an HTTP Error! The URL is invalid or unauthorized.")


# 4.2 Enforcing Timeouts
print("\n--- 4.2 Enforcing Timeouts ---")
try:
    print("Attempting to connect to a slow server...")
    requests.get("https://httpstat.us/200?sleep=5000", timeout=3)
except requests.exceptions.Timeout:
    print("[ERROR] Connection timed out! The server took too long to respond.")
except requests.exceptions.RequestException as e:
    print(f"[ERROR] Network error or timeout: {type(e).__name__}")


# 4.3 Catch-All Network Exception Handling
print("\n--- 4.3 Catching DNS & Connection Failures ---")
# 'RequestException' is the base class that catches ALL network-related errors
try:
    requests.get("https://this-website-definitely-does-not-exist-12345.com")
except requests.exceptions.RequestException as e:
    print(f"[ERROR] Network Error Intercepted: Could not reach the server.")

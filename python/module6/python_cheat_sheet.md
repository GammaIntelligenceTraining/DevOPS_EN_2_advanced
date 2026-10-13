# Python DevOps Cheat Sheet: HTTP Networking (`requests`)

## 1. HTTP Request-Response Architecture

HTTP is a stateless, text-based client-server protocol operating at Layer 7 of the OSI model. Every transaction consists of a client Request followed by a server Response.

### The Transaction Breakdown
| Component | Request (What Client Sends) | Response (What Server Returns) |
| :--- | :--- | :--- |
| **Control Line** | **HTTP Verb + Path**: e.g., `GET /api/v1/health` | **Status Code + Reason**: e.g., `200 OK` |
| **Headers** | Client metadata, accepted formats, credentials | Server metadata, payload format, rate limits |
| **Body (Payload)**| Data payload (JSON for `POST`/`PUT`; empty for `GET`)| Returned data (JSON document, HTML text, or binary) |

---

## 2. Common HTTP Headers in DevOps

Headers serve as the "envelope metadata" governing authentication, content format, and operational quotas.

| Header Name | Type | Example Value | DevOps Purpose |
| :--- | :--- | :--- | :--- |
| **`Content-Type`** | Request / Response | `application/json` | Declares the MIME format of the body payload. |
| **`Accept`** | Request | `application/json` | Tells the server what format the client is prepared to parse. |
| **`Authorization`** | Request | `Bearer eyJhbGci...` | Passes API tokens, JWTs, or basic auth credentials to access secured endpoints. |
| **`User-Agent`** | Request | `ops-monitor/2.1` | Identifies the script or service making the call (often audited in access logs). |
| **`X-RateLimit-Remaining`**| Response | `59` | Number of allowable API calls remaining before requests are throttled. |
| **`Retry-After`** | Response | `120` | Seconds to wait when encountering a `429 Too Many Requests` status code. |

---

## 3. HTTP Methods & Operations with `requests`

| Operation | Syntax Example | DevOps Use Case |
| :--- | :--- | :--- |
| **GET Request** | `res = requests.get(f"{BASE_URL}/users")` | Fetching resources (user directory, metrics, repository info). |
| **POST Request** | `res = requests.post(f"{BASE_URL}/users", json=user_dict)` | Creating new resources (adding users, provisioning runners). |
| **PUT Request** | `res = requests.put(f"{BASE_URL}/users/1", json=user_dict)` | Updating existing resources (updating user info, patching state). |
| **DELETE Request** | `res = requests.delete(f"{BASE_URL}/users/1")` | Decommissioning resources (deleting user accounts, revoking access). |
| **Base URL Pattern**| `url = f"{BASE_URL}{endpoint}"` | Dynamic URL construction allowing easy environment switching. |
| **Status Code** | `print(res.status_code)` | Validating success (200=OK, 201=Created, 404=Not Found, 500=Error). |
| **Parse JSON** | `data_dict = res.json()` | Converting a JSON API response directly into a Python dictionary. |
| **Pretty-Print JSON**| `print(json.dumps(data, indent=2))` | Formatted terminal output for inspecting deeply nested API payloads. |
| **Defensive .get()**| `val = data.get("role", "default")` | Avoiding KeyError crashes on optional or missing API fields. |
| **Read Text** | `raw_html = res.text` | Extracting raw HTML or plain text from a webpage. |
| **Read Headers** | `limit = res.headers.get("X-RateLimit-Remaining")` | Extracting metadata like rate limits or authentication tokens. |
| **Custom Headers** | `res = requests.get(url, headers={"Authorization": "Bearer token"})` | Authenticating requests and setting custom user agents. |
| **Query Params** | `res = requests.get(url, params={"sort": "desc", "q": "api"})` | Safely encoding URL query parameters without string concatenation. |
| **Webhook Event** | `requests.post(webhook_url, json={"content": "alert"})` | Event-driven push notification sending operational alerts to webhook URLs. |

---

## 4. Defensive Networking (Timeouts & Exceptions)

| Concept | Syntax Example | DevOps Use Case |
| :--- | :--- | :--- |
| **Enforce Timeout**| `requests.get("http://api.com", timeout=3)` | Preventing your automation script from hanging forever if a server freezes. |
| **Catch Everything**| `except requests.exceptions.RequestException:`| Safely catching ALL network failures (DNS down, port blocked, timeout). |
| **Catch Timeout** | `except requests.exceptions.Timeout:` | Specifically catching a timeout to trigger a retry or specific alert. |
| **Check Bad Status**| `res.raise_for_status()` | Automatically throws an exception if the status code is 4xx or 5xx. |

---

## 5. Standard HTTP Status Code Quick Reference

- **200 OK**: The request succeeded (Everything is fine).
- **201 Created**: The POST request succeeded and a new resource was created.
- **401 Unauthorized**: Missing or invalid authentication token.
- **403 Forbidden**: Token valid, but the user lacks permissions for this specific resource.
- **404 Not Found**: The target URL does not exist or was deleted.
- **429 Too Many Requests**: You hit an API rate limit. Back off and wait before retrying.
- **500 Internal Server Error**: Destination backend server crashed or encountered an unhandled exception.
- **502 Bad Gateway**: Reverse proxy / load balancer received an invalid response from upstream backend.
- **503 Service Unavailable**: Service is overloaded or undergoing maintenance.
- **504 Gateway Timeout**: Upstream microservice took too long to answer the reverse proxy.

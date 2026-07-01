

import json

# Parsing practice
api_payload = '{"username": "coder123", "email": "coder@py.org", "premium": true}'
user_profile = json.loads(api_payload)
print("Parsed profile:", user_profile)
print("Username type:", type(user_profile["username"]))  # <class 'str'>
print("Premium type:", type(user_profile["premium"]))    # <class 'bool'>

# Serializing practice
post_data = {
    "title": "Learning APIs",
    "likes": 42,
    "draft": False
}
post_json = json.dumps(post_data)
print("JSON representation:", post_json)

# =========================
# Activity
print("============Activity Section==========\n")
# =========================

# ### Activity Objectives
# 1. **Parse JSON**: Use `json.loads()` to parse the `api_payload` string and store the resulting dictionary in a variable called `user_profile`.
# 2. **Convert to JSON**: Create a dictionary called `post_data` with keys `"title"` and `"body"`. Convert it to a JSON string using `json.dumps()` and store it in a variable called `post_json`.
# 3. **Inspect Status Codes**: Complete the function `check_http_status(status_code)`. It should return:
#    - `"Success"` if the code is 200 or 201.
#    - `"Client Error"` if the code is 400, 401, or 404.
#    - `"Server Error"` if the code is 500.

# Write your activity code below

api_payload = '{"username": "coder123", "email": "coder@py.org", "premium": true}'

# 1. Parse api_payload into user_profile
# user_profile = ...

# 2. Create post_data `dict` and serialize it to post_json string
# post_data = ...
# post_json = ...

# 3. Complete check_http_status function
def check_http_status(status_code):
    # Pass your logic here
    pass

# =========================
# Mini Challenge
print("============Mini Challenge==========\n")
# =========================

# ### Challenge Objectives
# Write a request router function named `route_request(method, path, body_json)` that simulates how a server handles API routing:
# - If `method` is `"GET"` and `path` is `"/users"`, return a tuple `(200, '{"users": ["alice", "bob"]}')`.
# - If `method` is `"POST"` and `path` is `"/users"`:
#   - Parse the `body_json` string.
#   - If `body_json` is not valid JSON, or does not contain a `"name"` key, return `(400, '{"error": "Invalid payload"}')`.
#   - If valid, return `(201, '{"status": "Created"}')`.
# - For any other path or method, return `(404, '{"error": "Not Found"}')`.
# 
# > **Hint**: Wrap your JSON parsing in a `try...except json.JSONDecodeError` block to catch invalid payloads!

# Write your challenge code below

def route_request(method, path, body_json):
    # Implement routing logic
    pass

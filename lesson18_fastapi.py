

import sys
from types import ModuleType

# --- Browser WASM Sandbox Compatibility Layer ---
if 'fastapi' not in sys.modules:
    fastapi_mock = ModuleType('fastapi')
    class MockFastAPI:
        def __init__(self):
            self.routes = {}
        def get(self, path):
            def decorator(func):
                self.routes[('GET', path)] = func
                return func
            return decorator
        def post(self, path):
            def decorator(func):
                self.routes[('POST', path)] = func
                return func
            return decorator
    fastapi_mock.FastAPI = MockFastAPI
    sys.modules['fastapi'] = fastapi_mock

if 'pydantic' not in sys.modules:
    pydantic_mock = ModuleType('pydantic')
    class MockBaseModel:
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)
            if not hasattr(self, '__annotations__'):
                self.__annotations__ = {}
    pydantic_mock.BaseModel = MockBaseModel
    sys.modules['pydantic'] = pydantic_mock
# ------------------------------------------------

from fastapi import FastAPI
from pydantic import BaseModel

# Example of a working `app`
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}

print("Mock Server routes loaded:", list(app.routes.keys()))

# =========================
# Activity
print("============Activity Section==========\n")
# =========================

# ### Activity Objectives
# 1. **Instantiate App**: Create a FastAPI application instance and store it in a variable called `app`.
# 2. **Health Check Endpoint**: Add a GET route at path `"/health"` that returns a dictionary `{"status": "ok"}`.
# 3. **Pydantic Model**: Define a Pydantic model called `UserSignUp` that inherits from `BaseModel` and has two fields:
#    - `username` (annotated as a string: `str`)
#    - `email` (annotated as a string: `str`)
# 
# > **Remember**: In Python, type annotations are written as `variable_name: type_name`.

# Write your activity code below

# 1. Create `app`
# `app` = ...

# 2. Add /health endpoint
# ...

# 3. Define `UserSignUp` model
# class `UserSignUp`(...):
#     ...

# =========================
# Mini Challenge
print("============Mini Challenge==========\n")
# =========================

# ### Challenge Objectives
# Build an in-memory product inventory API using FastAPI and Pydantic:
# 1. Define a Pydantic model called `Product` that inherits from `BaseModel` and contains:
#    - `name` (string: `str`)
#    - `price` (float: `float`)
# 2. Instantiate a FastAPI application called `app`.
# 3. Create a global list called `products_db = []`.
# 4. Create a POST endpoint at `"/products"` that takes a payload of type `Product` as an argument, appends the product dictionary to `products_db`, and returns the product itself.
# 5. Create a GET endpoint at `"/products"` that returns the `products_db` `list` of products.
# 
# > **Hint**: To convert a Pydantic object `prod` to a dictionary in Python, you can access its attributes or convert it. For this sandbox simulation, appending `{"name": prod.name, "price": prod.price}` to `products_db` works perfectly!

# Write your challenge code below

# Implement class, `app`, `products_db`, and routes here

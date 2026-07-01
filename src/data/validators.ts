// Python Fundamentals Validation Engine
// This file defines Python validation scripts for each lesson's Activity and Challenge.
// If the script runs without throwing an exception, the answer is correct.

export interface SectionValidator {
  pythonCode: string;
  errorMessage: string;
}

export interface LessonValidator {
  activity: SectionValidator;
  challenge: SectionValidator;
}

export const lessonValidators: Record<number, LessonValidator> = {
  1: {
    activity: {
      pythonCode: `
# Check presence and types of variables
assert 'city' in globals(), "Variable 'city' is not defined."
assert isinstance(city, str), "Variable 'city' must be a string (text)."
assert len(city) > 0, "Variable 'city' cannot be empty."

assert 'birth_year' in globals(), "Variable 'birth_year' is not defined."
assert isinstance(birth_year, int), "Variable 'birth_year' must be an integer (whole number)."
assert 1900 < birth_year < 2030, "Variable 'birth_year' must be a valid year."

assert 'price' in globals(), "Variable 'price' is not defined."
assert isinstance(price, float), "Variable 'price' must be a float (decimal number)."

assert 'likes_python' in globals(), "Variable 'likes_python' is not defined."
assert isinstance(likes_python, bool), "Variable 'likes_python' must be a boolean (True/False)."
`,
      errorMessage: "Make sure you define 'city' (string), 'birth_year' (integer), 'price' (float), and 'likes_python' (boolean) exactly as requested."
    },
    challenge: {
      pythonCode: `
# Check for variable patterns
str_vars = [k for k, v in globals().items() if isinstance(v, str) and not k.startswith('_') and k != 'code']
int_vars = [k for k, v in globals().items() if isinstance(v, int) and not k.startswith('_') and not isinstance(v, bool)]
bool_vars = [k for k, v in globals().items() if isinstance(v, bool) and not k.startswith('_')]

assert len(str_vars) >= 2, "Ensure you have created string variables for your first name and favorite food."
assert len(int_vars) >= 1, "Ensure you have created an integer variable for your current age."
assert len(bool_vars) >= 1, "Ensure you have created a boolean variable for your coding preference."
`,
      errorMessage: "Make sure you create all 4 required variables (name, age, food, coding preference) with their correct data types."
    }
  },
  2: {
    activity: {
      pythonCode: `
# Since inputs are mocked or run, let's ensure variables are defined
assert 'city' in globals(), "Variable 'city' is missing."
assert 'favorite_color' in globals(), "Variable 'favorite_color' is missing."
assert 'birth_year' in globals(), "Variable 'birth_year' is missing."
assert isinstance(birth_year, int), "Variable 'birth_year' must be converted to an integer."
assert 'item_price' in globals(), "Variable 'item_price' is missing."
assert isinstance(item_price, float), "Variable 'item_price' must be converted to a float."
`,
      errorMessage: "Make sure you capture all inputs and convert 'birth_year' to int and 'item_price' to float."
    },
    challenge: {
      pythonCode: `
# Check variables
str_vars = [k for k, v in globals().items() if isinstance(v, str) and not k.startswith('_') and k != 'code']
int_vars = [k for k, v in globals().items() if isinstance(v, int) and not k.startswith('_') and not isinstance(v, bool)]

assert len(str_vars) >= 2, "Make sure you ask and store the name and hobby as text (strings)."
assert len(int_vars) >= 1, "Make sure you ask and store the age as an integer."
`,
      errorMessage: "Make sure you ask for a name, age, and hobby, and format the output sentence correctly."
    }
  },
  3: {
    activity: {
      pythonCode: `
assert 'num1' in globals() and 'num2' in globals(), "Variables 'num1' and 'num2' must be defined."
assert isinstance(num1, (int, float)) and isinstance(num2, (int, float)), "num1 and num2 must be numbers."

assert 'points' in globals(), "Variable 'points' must be defined."
assert points == 110, "Calculation for 'points' is incorrect. It should be (50 + 10 - 5) * 2 = 110."

assert 'age1' in globals() and 'age2' in globals(), "Variables 'age1' and 'age2' must be defined."
assert 'has_ticket' in globals() and 'has_money' in globals(), "Variables 'has_ticket' and 'has_money' must be defined."
assert isinstance(has_ticket, bool) and isinstance(has_money, bool), "Ticket and money variables must be booleans."
`,
      errorMessage: "Make sure you perform the math operations, points arithmetic, age comparisons, and define ticket/money booleans."
    },
    challenge: {
      pythonCode: `
# Check for arithmetic operations
nums = [v for k, v in globals().items() if isinstance(v, (int, float)) and not k.startswith('_') and not isinstance(v, bool)]
assert len(nums) >= 3, "Make sure you define item price, quantity, and calculate the total cost."
`,
      errorMessage: "Make sure you ask for price and quantity, calculate the total cost correctly, and print it."
    }
  },
  4: {
    activity: {
      pythonCode: `
assert 'has_username' in globals() and 'has_password' in globals(), "Variables 'has_username' and 'has_password' must be defined."
assert isinstance(has_username, bool) and isinstance(has_password, bool), "Variables must be booleans."
`,
      errorMessage: "Ensure you use if-statements for age voting, positive/negative numbers, grading logic, and username/password check."
    },
    challenge: {
      pythonCode: `
# Check logic is present in code
assert 'if' in code, "You must use an 'if' statement to solve the discount checker."
`,
      errorMessage: "Ensure your conditional checks check both the purchase amount (1000+) and member status ('yes')."
    }
  },
  5: {
    activity: {
      pythonCode: `
# Should have a loop
assert 'for' in code, "You must use at least one 'for' loop."
assert 'while' in code, "You must use at least one 'while' loop."
`,
      errorMessage: "Ensure you use a 'for' loop for printing 1-10, printing letters in name, and even numbers, and a 'while' loop for 1-5 and counting down."
    },
    challenge: {
      pythonCode: `
assert 'for' in code or 'while' in code, "You must use a loop to build the multiplication table."
`,
      errorMessage: "Ensure you loop from 1 to 10 and print each multiplication result dynamically."
    }
  },
  6: {
    activity: {
      pythonCode: `
assert 'favorite_foods' in globals(), "List 'favorite_foods' must be defined."
assert isinstance(favorite_foods, list), "favorite_foods must be a list."
assert len(favorite_foods) == 3, "favorite_foods list must contain exactly 3 items after adding and removing."
`,
      errorMessage: "Make sure you create a list, print index 0, update index 1, append, remove, and use a for loop."
    },
    challenge: {
      pythonCode: `
assert 'shopping_list' in globals(), "List 'shopping_list' must be defined."
assert isinstance(shopping_list, list), "shopping_list must be a list."
assert len(shopping_list) >= 3, "You must add three items to the list."
`,
      errorMessage: "Ensure you create an empty shopping_list, append 3 user inputs, print the list, and loop to print each item."
    }
  },
  7: {
    activity: {
      pythonCode: `
assert 'favorite_movie' in globals(), "Dictionary 'favorite_movie' must be defined."
assert isinstance(favorite_movie, dict), "favorite_movie must be a dictionary."
assert 'genre' not in favorite_movie, "The 'genre' key must be removed using pop()."
assert 'rating' in favorite_movie, "The 'rating' key must be added to the dictionary."
`,
      errorMessage: "Make sure you define movie dict keys (title, year, genre), update year, add rating, pop genre, and loop items."
    },
    challenge: {
      pythonCode: `
assert 'contact' in globals(), "Dictionary 'contact' must be defined."
assert isinstance(contact, dict), "contact must be a dictionary."
assert 'name' in contact and 'phone' in contact and 'email' in contact, "Dictionary must contain 'name', 'phone', and 'email' keys."
`,
      errorMessage: "Make sure you create the contact dictionary, fill it with user answers, and print them in a loop."
    }
  },
  8: {
    activity: {
      pythonCode: `
assert 'say_welcome' in globals() and callable(say_welcome), "Function 'say_welcome' is not defined."
assert 'print_name' in globals() and callable(print_name), "Function 'print_name' is not defined."
assert 'multiply' in globals() and callable(multiply), "Function 'multiply' is not defined."
assert multiply(3, 5) == 15, "Function 'multiply' should return the product of two numbers (e.g. multiply(3, 5) should be 15)."
assert 'check_number' in globals() and callable(check_number), "Function 'check_number' is not defined."
assert 'print_colors' in globals() and callable(print_colors), "Function 'print_colors' is not defined."
`,
      errorMessage: "Define say_welcome(), print_name(name), multiply(num1, num2) with return, check_number(number), and print_colors(colors)."
    },
    challenge: {
      pythonCode: `
assert 'add' in globals() and callable(add), "Function 'add' is missing."
assert 'subtract' in globals() and callable(subtract), "Function 'subtract' is missing."
assert 'multiply_numbers' in globals() and callable(multiply_numbers), "Function 'multiply_numbers' is missing."
assert 'divide' in globals() and callable(divide), "Function 'divide' is missing."

assert add(4, 2) == 6, "add(4, 2) is incorrect."
assert subtract(4, 2) == 2, "subtract(4, 2) is incorrect."
assert multiply_numbers(4, 2) == 8, "multiply_numbers(4, 2) is incorrect."
assert divide(4, 2) == 2.0, "divide(4, 2) is incorrect."
`,
      errorMessage: "Create add, subtract, multiply_numbers, and divide functions, ask for inputs, and output results using functions."
    }
  },
  9: {
    activity: {
      pythonCode: `
assert 'safe_multiply' in globals() and callable(safe_multiply), "Function 'safe_multiply' is not defined."
assert safe_multiply(5, 6) == 30, "safe_multiply(5, 6) should return 30."
assert safe_multiply('a', 5) == "Invalid values.", "safe_multiply must catch TypeError and return 'Invalid values.'"
`,
      errorMessage: "Ensure you write all requested try-except blocks, including ValueError, ZeroDivisionError, else/finally, and safe_multiply."
    },
    challenge: {
      pythonCode: `
assert 'divide' in globals() and callable(divide), "Function 'divide' is not defined."
# check if divide handles zero division
try:
    res = divide(10, 0)
    # If it returns a string warning instead of raising exception, it is safe
    assert isinstance(res, str) or res is None, "divide function should safely handle division by zero."
except Exception:
    # If it raised exception, it is not caught safely
    assert False, "divide function did not safely handle division by zero."
`,
      errorMessage: "Build a safe calculator that handles invalid input and division by zero using try-except blocks."
    }
  },
  10: {
    activity: {
      pythonCode: `
assert 'rgb' in globals(), "Tuple 'rgb' is not defined."
assert isinstance(rgb, tuple), "rgb must be a tuple."
assert rgb == (255, 128, 0), "rgb must contain (255, 128, 0)."

assert 'describe_pet' in globals() and callable(describe_pet), "Function 'describe_pet' is not defined."
`,
      errorMessage: "Complete the exercises for Tuple Basics, Set Operations, Removing Duplicates, Nested Data, and *args/**kwargs."
    },
    challenge: {
      pythonCode: `
# Should have a loop
assert 'for' in code or 'while' in code, "Use a loop to maintain the menu interface."
`,
      errorMessage: "Create a contact book dictionary with nested dictionaries for phone, email, and city, and support menu options."
    }
  },
  11: {
    activity: {
      pythonCode: `
assert 'strip' in code or 'lower' in code or 'replace' in code, "Ensure you are using string methods like strip(), lower(), or replace()."
`,
      errorMessage: "Use string methods to clean up the input, replace values, find substrings, and format sentences."
    },
    challenge: {
      pythonCode: `
assert 'split' in code or 'len' in code, "Ensure you use split() or len() to count words/characters."
`,
      errorMessage: "Build a text analyzer that asks for text and prints word count, character count, and checks for keyword search."
    }
  },
  12: {
    activity: {
      pythonCode: `
assert 'open' in code or 'with' in code, "Make sure you use file open() or with open() operations."
`,
      errorMessage: "Create a file called 'notes.txt', write text to it, read and print its contents, and append a new line."
    },
    challenge: {
      pythonCode: `
assert 'open' in code or 'with' in code, "Ensure you write log messages to a file."
`,
      errorMessage: "Implement a logging program that writes logs to 'activity_log.txt' with a timestamp/action and reads them back."
    }
  },
  13: {
    activity: {
      pythonCode: `
assert 'lambda' in code, "You must define at least one lambda function."
assert '[' in code and 'for' in code, "You must use list comprehensions."
`,
      errorMessage: "Complete the exercises using list/dictionary comprehensions and lambda functions."
    },
    challenge: {
      pythonCode: `
assert 'lambda' in code, "Use lambda functions for filtering or mapping values."
`,
      errorMessage: "Create a list of dictionaries for products, use list comprehensions to filter them, and sort using a lambda function."
    }
  },
  14: {
    activity: {
      pythonCode: `
assert 'Car' in globals() and isinstance(Car, type), "Class 'Car' is not defined."
c = Car("TestMake", "TestModel", 2022)
assert hasattr(c, 'make') and hasattr(c, 'model') and hasattr(c, 'year'), "Car must initialize make, model, and year."
assert hasattr(c, 'start_engine') and callable(c.start_engine), "Car must have a start_engine() method."
`,
      errorMessage: "Define the Car class, initialize properties, add methods, and create objects correctly."
    },
    challenge: {
      pythonCode: `
assert 'Book' in globals() and isinstance(Book, type), "Class 'Book' must be defined."
assert 'Library' in globals() and isinstance(Library, type), "Class 'Library' must be defined."
`,
      errorMessage: "Implement the Book and Library classes, linking books inside a library list, and support add/remove methods."
    }
  },
  15: {
    activity: {
      pythonCode: `
import sys
assert 'math' in sys.modules, "You must import the math module."
assert 'random' in sys.modules, "You must import the random module."
`,
      errorMessage: "Import the math and random modules and use them for calculations and generating random numbers."
    },
    challenge: {
      pythonCode: `
# Ensure they import math or custom operations
assert 'import' in code, "You must use import statements."
`,
      errorMessage: "Import your custom helper operations or emulate standard math/random package modules."
    }
  },
  16: {
    activity: {
      pythonCode: `
assert 'yield' in code or '@' in code, "Ensure you are using generators (yield) or decorators (@)."
`,
      errorMessage: "Complete the closure, custom decorator (@my_decorator), and generator (yield) exercises."
    },
    challenge: {
      pythonCode: `
assert '@' in code, "Use a decorator (@) to modify function behaviors."
`,
      errorMessage: "Create a timing or logging decorator and apply it to a heavy execution function."
    }
  },
  17: {
    activity: {
      pythonCode: `
import json
assert 'user_profile' in globals(), "Variable 'user_profile' is not defined."
assert isinstance(user_profile, dict), "user_profile must be a dictionary."
assert user_profile.get('username') == 'coder123', "user_profile username value is incorrect."
assert user_profile.get('email') == 'coder@py.org', "user_profile email value is incorrect."

assert 'post_json' in globals(), "Variable 'post_json' is not defined."
assert isinstance(post_json, str), "post_json must be a JSON string."
loaded_post = json.loads(post_json)
assert 'title' in loaded_post and 'body' in loaded_post, "post_data dictionary must contain 'title' and 'body' keys."

assert 'check_http_status' in globals(), "Function 'check_http_status' is not defined."
assert check_http_status(200) == "Success", "check_http_status(200) should return 'Success'"
assert check_http_status(201) == "Success", "check_http_status(201) should return 'Success'"
assert check_http_status(404) == "Client Error", "check_http_status(404) should return 'Client Error'"
assert check_http_status(500) == "Server Error", "check_http_status(500) should return 'Server Error'"
`,
      errorMessage: "Make sure you parse 'api_payload' to 'user_profile', serialize 'post_data' to 'post_json', and return correct status labels in 'check_http_status'."
    },
    challenge: {
      pythonCode: `
assert 'route_request' in globals(), "Function 'route_request' is not defined."

res_code, res_body = route_request("GET", "/users", "")
assert res_code == 200, f"Expected status code 200, got {res_code}"
assert "users" in res_body, "Expected 'users' in GET response body"

res_code, res_body = route_request("POST", "/users", '{"name": "Charlie"}')
assert res_code == 201, f"Expected status code 201, got {res_code}"
assert "Created" in res_body, "Expected 'Created' in valid POST response"

res_code, res_body = route_request("POST", "/users", 'invalid-json')
assert res_code == 400, f"Expected status code 400 for invalid JSON, got {res_code}"

res_code, res_body = route_request("POST", "/users", '{"age": 30}')
assert res_code == 400, f"Expected status code 400 for missing name, got {res_code}"

res_code, res_body = route_request("GET", "/unknown", "")
assert res_code == 404, f"Expected status code 404, got {res_code}"
`,
      errorMessage: "Ensure 'route_request' implements GET /users, POST /users (with validation), and handles 400/404 errors appropriately."
    }
  },
  18: {
    activity: {
      pythonCode: `
assert 'app' in globals(), "FastAPI app instance 'app' is not defined."
assert hasattr(app, 'routes'), "app must be a FastAPI instance."

assert ('GET', '/health') in app.routes, "GET route for '/health' is not registered."
health_func = app.routes[('GET', '/health')]
assert health_func() == {"status": "ok"}, "GET '/health' should return {'status': 'ok'}."

assert 'UserSignUp' in globals(), "Pydantic model 'UserSignUp' is not defined."
assert isinstance(UserSignUp, type), "UserSignUp must be a class."
user_test = UserSignUp(username="testuser", email="test@domain.com")
assert getattr(user_test, 'username') == 'testuser', "UserSignUp must have a 'username' attribute."
assert getattr(user_test, 'email') == 'test@domain.com', "UserSignUp must have an 'email' attribute."
`,
      errorMessage: "Make sure you instantiate 'app = FastAPI()', register GET '/health', and declare the Pydantic 'UserSignUp' class."
    },
    challenge: {
      pythonCode: `
assert 'app' in globals(), "FastAPI app instance 'app' is not defined."
assert 'Product' in globals(), "Pydantic model 'Product' is not defined."
assert 'products_db' in globals(), "List 'products_db' is not defined."
assert isinstance(products_db, list), "products_db must be a list."

assert ('POST', '/products') in app.routes, "POST route for '/products' is not registered."
assert ('GET', '/products') in app.routes, "GET route for '/products' is not registered."

post_func = app.routes[('POST', '/products')]
get_func = app.routes[('GET', '/products')]

products_db.clear()

test_prod = Product(name="Laptop", price=999.99)
post_res = post_func(test_prod)

assert len(products_db) == 1, "POST route should add the product to products_db."
assert products_db[0]['name'] == "Laptop", "Product name in database is incorrect."
assert products_db[0]['price'] == 999.99, "Product price in database is incorrect."

get_res = get_func()
assert isinstance(get_res, list), "GET route must return a list."
assert len(get_res) == 1, "GET route should return list containing the added product."
`,
      errorMessage: "Make sure you define 'Product' (Pydantic), GET/POST '/products' routes, and correctly add incoming products to the 'products_db' list."
    }
  }
};

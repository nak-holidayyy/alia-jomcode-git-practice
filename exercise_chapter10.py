# print("Example 1: Standard-library Namespaces")
# import math
# from pathlib import Path

# print(math.ceil(4.22))
# print(Path("backend")/"app"/"main.py")

print("Example 2: JSON round Trip")
import json
records = [{
            "title": "python",
            "capacity": 20
        }]
text = json.dumps(records, indent=2) 
restored = json.loads(text)
print(restored==records)
print(restored[0]["capacity"])

# print("Example 3: Explicit Configuration")
# import os

# def api_origin():
#     return os.getenv("API_ORIGIN", "http://localhost:3000")
# print(api_origin())

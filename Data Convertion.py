import yaml
import json

with open("Training SQL Data.yaml", "r", encoding = "utf-8") as file:
    data = yaml.safe_load(file)
    
print(data)

with open("sql json.json", "w", encoding = "utf-8") as f:
    json.dump(data, f, indent = 2, ensure_ascii = False)

print("YAML Converted to JSON Successfully")

import json



PATH: str = "lezione_15/config.json"
mode: str = "r"
encoding: str = "utf-8"

def connect(host: str, port: int) -> None:
    print(f"Connected to {host}:{port}")

with open(PATH, mode=mode, encoding=encoding) as file:

    config: dict = json.load(file)

config["AGGIUNTA"] = "NUOVO"
config["server"]["host"] = "google.it"

with open(PATH, mode="w") as file:

    json.dump(config, file, indent=4)

# print(f'Host: {config["server"]["host"]} Port: {config["server"]["port"]}')

# connect(host=config["server"]["host"], port=config["server"]["port"])
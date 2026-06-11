REGISTRY = {}

def tool(name):
    def wrapper(fn):
        REGISTRY[name] = fn
        return fn
    return wrapper

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "searchWeb",
            "description": "Busca informações atuais na web. Use para clima, notícias, preços.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Query de busca específica"
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "openApp",
            "description": "Abre um aplicativo no sistema.",
            "parameters": {
                "type": "object",
                "properties": {
                    "appName": {
                        "type": "string",
                        "description": "Nome do aplicativo"
                    }
                },
                "required": ["appName"]
            }
        }
    },
    {
    "type": "function",
    "function": {
        "name": "openSpotify",
        "description": "Abre o Spotify. Pode tocar uma playlist ou uma música específica.",
        "parameters": {
            "type": "object",
            "properties": {
                "target": {
                    "type": "string",
                    "description": "Nome da playlist ou música a tocar"
                },
                "targetType": {
                    "type": "string",
                    "enum": ["playlist", "song"],
                    "description": "Se o target é uma playlist ou uma música"
                },
                "shuffle": {
                    "type": "boolean",
                    "description": "Modo aleatório. Relevante apenas para playlists."
                }
            },
            "required": ["target", "targetType"]
        }
    },
    },
    {
    "type": "function",
    "function": {
        "name": "exit",
        "description": "Encerra a sua execução e o programa.",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    }
    }
]

from copy import deepcopy

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
            "description": "Busca informações na web e retorna o resultado diretamente. Use quando o usuário quer saber algo — clima, notícias, preços, fatos. NÃO use se o usuário pediu pra abrir o navegador ou ver os resultados.",
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
            "name": "saveMemory",
            "description": "Salva um fato importante sobre o usuário. Usar para informações relevantes que precisem de persistência ou quando o usuário pedir.",
            "parameters": {
                "type": "object",
                "properties": {
                    "fact": {
                        "type": "string",
                        "description": "Fato a ser salvo"
                    },
                    "category": {
                        "type": "string",
                        "enum": ["preference", "personal", "routine", "other"],
                        "description": "Categoria do fato"
                    }
                },
                "required": ["fact", "category"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "updateMemory",
            "description": "Salva um fato importante sobre o usuário no lugar de outra memória. Usar para atualizar informações relevantes que precisem de persistência ou quando o usuário pedir.",
            "parameters": {
                "type": "object",
                "properties": {
                    "factId": {
                        "type": "number",
                        "description": "ID do fato a ser sobreescrito"
                    },
                    "fact": {
                        "type": "string",
                        "description": "Conteúdo do novo fato"
                    }
                },
                "required": ["factId", "fact"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "deleteMemory",
            "description": "Deleta um fato sobre o usuário. Usar quando o usuário pedir ou quando achar que a informação não seja mais relevante.",
            "parameters": {
                "type": "object",
                "properties": {
                    "factId": {
                        "type": "number",
                        "description": "ID do fato a ser deletado"
                    }
                },
                "required": ["factId"]
            }
        }
    },
    {
        "local": True,
        "type": "function",
        "function": {
            "name": "openApp",
            "description": "Abre um aplicativo no sistema.",
            "parameters": {
                "type": "object",
                "properties": {
                    "appName": {
                        "type": "string",
                        "enum": [],
                        "description": "Nome do aplicativo"
                    }
                },
                "required": ["appName"]
            }
        }
    },
    {
        "local": True,
        "type": "function",
        "function": {
            "name": "openWeb",
            "description": "Abre o navegador do usuário com uma pesquisa ou URL. Use quando o usuário quer navegar, ver resultados por conta própria, ou usou palavras como 'abre', 'pesquisa no google', 'me mostra'.",
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
        "local": True,
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
        "local": True,
        "type": "function",
        "function": {
            "name": "setClock",
            "description": "Faz uma função baseada em relógio.",
            "parameters": {
                "type": "object",
                "properties": {
                    "feature": {
                        "type": "string",
                        "enum": ["alarm", "cronometer", "timer"],
                        "description": "Tipo de função do relógio"
                    },
                    "hours": {
                        "type": "integer",
                        "description": "Horas. Para alarme: hora do disparo. Para timer: duração."
                    },
                    "minutes": {
                        "type": "integer", 
                        "description": "Minutos. Para alarme: minuto do disparo. Para timer: duração."
                    },
                    "seconds": {
                        "type": "integer",
                        "description": "Segundos. Para timer: duração."
                    }
                },
                "required": ["feature"]
            }
        },
    },
    {
        "local": True,
        "type": "function",
        "function": {
            "name": "pressKey",
            "description": "Pressiona ou segura uma key do teclado do usuário",
            "parameters": {
                "type": "object",
                "properties": {
                    "key": {
                        "type": "string",
                        "description": "Key que deve ser pressionada. Exemplo: A, B, ENTER, SPACE, MOUSE1"
                    },
                    "holdTime": {
                        "type": "number",
                        "description": "Tempo que a key deve permanecer pressionada"
                    }
                },
                "required": ["key"]
            }
        }
    },
    {
        "local": True,
        "type": "function",
        "function": {
            "name": "windowMove",
            "description": "Move uma janela no sistema do usuário com base em posição relativa.",
            "parameters": {
                "type": "object",
                "properties": {
                    "activeWindows": {
                        "type": "string",
                        "enum": [],
                        "description": "Nome das janelas que você pode atuar."
                    },
                    "x": {
                        "type": "number",
                        "description": "Número entre 0 e 1 que representa a posição horizontal relativa da janela"
                    },
                    "y": {
                        "type": "number",
                        "description": "Número entre 0 e 1 que representa a posição vertical relativa da janela"
                    }
                },
                "required": ["activeWindows", "x", "y"]
            }
        }
    },
    {
        "local": True,
        "type": "function",
        "function": {
            "name": "windowResize",
            "description": "Muda o tamanho de uma janela no sistema do usuário com base em tamanho relativo.",
            "parameters": {
                "type": "object",
                "properties": {
                    "activeWindows": {
                        "type": "string",
                        "enum": [],
                        "description": "Nome das janelas que você pode atuar."
                    },
                    "width": {
                        "type": "number",
                        "description": "Número entre 0 e 1 que representa o tamanho horizontal relativo da janela"
                    },
                    "height": {
                        "type": "number",
                        "description": "Número entre 0 e 1 que representa o tamanho vertical relativo da janela"
                    }
                },
                "required": ["activeWindows", "width", "height"]
            }
        }
    },
    {
        "local": True,
        "type": "function",
        "function": {
            "name": "windowContext",
            "description": "Minimiza ou Maximiza uma janela.",
            "parameters": {
                "type": "object",
                "properties": {
                    "activeWindows": {
                        "type": "string",
                        "enum": [],
                        "description": "Nome das janelas que você pode atuar."
                    },
                    "feature": {
                        "type": "string",
                        "enum": ["fullscreen", "window_maximize", "window_minimize"],
                        "description": "Qual função deve ser executada"
                    }
                },
                "required": ["activeWindows", "feature"]
            }
        }
    }
]

def buildTools(capabilities: dict) -> list:
    result = []

    for tool in TOOLS:
        name = tool["function"]["name"]
        isLocal = tool.get("local", False)

        if isLocal:
            inDefault = name in capabilities.get("default", [])
            inDynamic = name in capabilities and name != "default"

            if not inDefault and not inDynamic:
                continue

        toolCopy = deepcopy(tool)
        toolCopy.pop("local", None)

        if name in capabilities and capabilities[name]:
            params = toolCopy["function"]["parameters"]["properties"]
            for fieldName, field in params.items():
                if "enum" in field:
                    field["enum"] = capabilities[name]

        result.append(toolCopy)

    return result
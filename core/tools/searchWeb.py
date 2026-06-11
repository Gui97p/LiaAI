from ddgs import DDGS
from core.tools.registry import tool

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

@tool('searchWeb')
def searchWeb(query: str, max_results: int = 3) -> str:
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=max_results))
    
    if not results:
        return "Nenhum resultado encontrado."
    
    parts = []
    for r in results:
        parts.append(f"{r['title']}: {r['body']}")
    
    return "\n".join(parts)

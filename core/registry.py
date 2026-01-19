from typing import Callable, Dict, List

class FormulaRegistry:
    def __init__(self):
        self._formulas: Dict[str, Callable] = {}
        self._aliases: Dict[str, List[str]] = {}

    def register(self, key: str, func: Callable, aliases: List[str] | None = None):
        self._formulas[key] = func
        if aliases:
            self._aliases[key] = aliases

    def get(self, key: str) -> Callable:
        if key not in self._formulas:
            raise KeyError(f"Formula '{key}' not found.")
        return self._formulas[key]

    def search(self, query: str) -> List[str]:
        query = query.lower()
        results = []

        for key, aliases in self._aliases.items():
            if query in key.lower():
                results.append(key)
                continue

            for alias in aliases:
                if query in alias.lower():
                    results.append(key)
                    break

        return sorted(set(results))

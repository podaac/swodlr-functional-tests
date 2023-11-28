
class ErrorInjector:
    
    def ValueTypeInjector(expectedType:str, value:str) -> str:
        if expectedType.lower() == 'integer':
            return f"{value}"
        elif expectedType.lower() == 'string':
            return f'"{value}"'
        elif expectedType.lower() == 'bool':
            return f"{value.lower()}"
        elif expectedType.lower() == 'null':
            return 'null'
        return None
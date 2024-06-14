from .comfy_terminal_display import TerminalNodeDisplay

# A dictionary that contains all nodes you want to export with their names
NODE_CLASS_MAPPINGS = {
    "TerminalNodeDisplay": TerminalNodeDisplay
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "TerminalNodeDisplay": "Terminal Node Display"
}

# Export symbols
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

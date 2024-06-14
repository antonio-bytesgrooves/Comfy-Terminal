from .comfy_standalone_terminal import TerminalStandAloneNode

# A dictionary that contains all nodes you want to export with their names
NODE_CLASS_MAPPINGS = {     
    "TerminalStandAloneNode": TerminalStandAloneNode,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "TerminalStandAloneNode": "Terminal Standalone Node",
}

# Export symbols
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

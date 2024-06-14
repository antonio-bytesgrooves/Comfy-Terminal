from .comfy_terminal import TerminalNode
from .comfy_terminal_display import TerminalDisplayNode

# A dictionary that contains all nodes you want to export with their names
NODE_CLASS_MAPPINGS = {     
    "TerminalNode": TerminalNode,
    "TerminalDisplayNode": TerminalDisplayNode
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "TerminalNode": "Terminal Node",
    "TerminalDisplayNode": "Terminal Display Node"
}

# Export symbols
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

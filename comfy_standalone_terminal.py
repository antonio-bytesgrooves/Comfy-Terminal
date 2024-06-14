from subprocess import getoutput
class TerminalStandAloneNode:
    """
    A custom node with no external input, only a multiline textbox for user input.
    The output will be displayed in a second multiline textbox within the same node.

    Class methods
    -------------
    INPUT_TYPES (dict): 
        Returns the input parameters configuration of the node.

    Attributes
    ----------
    RETURN_TYPES (tuple): 
        The type of each element in the output tuple.
    FUNCTION (str):
        The name of the entry-point method. For example, if `FUNCTION = "execute"` then it will run TerminalNode().execute()
    CATEGORY (str):
        The category the node should appear in the UI.
    """
    def __init__(self):
        self.text_input = ""
        self.text_output = ""

    @classmethod
    def INPUT_TYPES(cls):
        """
        Return a dictionary which contains config for all input fields.

        Returns:
            dict: Contains input fields config.
        """
        return {
            "required": {
                "text_input": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
            },
            "optional": {
                "text_output": ("STRING", {
                    "multiline": True,
                    "default": "",
                    "read_only": True
                }),
            },
        }

    RETURN_TYPES = ()
    FUNCTION = "execute"
    CATEGORY = "OS Utils"

    def execute(self, text_input):
        out = getoutput(f"{text_input}")
        self.text_output = out


    def get_text_output(self):
        """
        Get the output text to be displayed in the second textbox.

        Returns:
            str: The output text.
        """
        return self.text_output

    def UI_ELEMENTS(self):
        """
        Return a dictionary of the UI elements configuration.

        Returns:
            dict: Contains UI elements config.
        """
        return {
            "text_input": {
                "type": "multiline_textbox",
                "default": "",
                "on_enter": self.execute
            },
            "text_output": {
                "type": "multiline_textbox",
                "default": "",
                "read_only": True,
                "get_value": self.get_text_output
            },
        }

# Register the node so it can be used in the UI
# A dictionary that contains all nodes you want to export with their names
NODE_CLASS_MAPPINGS = {
    "TerminalStandAloneNode": TerminalStandAloneNode
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "TerminalStandAloneNode": "Terminal StandAlone Node"
}


from subprocess import getoutput

class TerminalNode:
    """
    A custom node with no external input, only a multiline textbox for user input.

    Class methods
    -------------
    INPUT_TYPES (dict): 
        Returns the input parameters configuration of the node.

    Attributes
    ----------
    RETURN_TYPES (tuple): 
        The type of each element in the output tuple.
    FUNCTION (str):
        The name of the entry-point method. For example, if `FUNCTION = "execute"` then it will run CustomTextNode().execute()
    CATEGORY (str):
        The category the node should appear in the UI.
    """

    def __init__(self):
        pass

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
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "get_input"
    CATEGORY = "OS Utils"
    def execute(self, text_input):
        text_output = getoutput(f"{text_input}")
        return(text_output)
    
    @classmethod
    def get_input(str):
        """
        Return a dictionary which contains config for all input fields.

        Returns:
            dict: Contains input fields config.
        """
        return {
            "optional": {
                "text_output": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
            },
        }
    def execute(self, text_output):
        return(text_output)
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "str"
    CATEGORY = "OS Utils"
 
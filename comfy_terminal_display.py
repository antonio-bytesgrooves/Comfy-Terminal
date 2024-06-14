from subprocess import getoutput

class TerminalDisplayNode:
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
                },
                {
            "optional": {
                "text_display": ("STRING", {
                    "multiline": True,
                    "default": ""
                })}
                }),
            },
        }
    
    RETURN_TYPES = ("STRING")
    FUNCTION = "execute"
    OUTPUT_NODE=True
    CATEGORY = "OS Utils"
    def execute(self,text_input):
        text_display = getoutput(f"{text_input}")
        print(text_display)
        return (text_display)
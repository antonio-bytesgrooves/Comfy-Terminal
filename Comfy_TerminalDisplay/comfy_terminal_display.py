class TerminalNodeDisplay:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "info": ("STRING", {"multiline": True, "forceInput": True}),
            },
            "hidden": {
                "unique_id": "UNIQUE_ID",
                "extra_pnginfo": "EXTRA_PNGINFO",
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ()
    FUNCTION = "notify"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True,)

    CATEGORY =  'OS Utils'

    def notify(self, info, unique_id = None, extra_pnginfo=None):
        text = info 
        if unique_id and extra_pnginfo and "workflow" in extra_pnginfo[0]:
            workflow = extra_pnginfo[0]["workflow"]
            node = next((x for x in workflow["nodes"] if str(x["id"]) == unique_id[0]), None)
            if node: 
                node["widgets_values"] = [text]

        return {"ui": {"text": text}, "result": (text,)}

NODE_CLASS_MAPPINGS = {
    "TerminalNodeDisplay": TerminalNodeDisplay
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TerminalNodeDisplay": "Terminal Node Display"
}

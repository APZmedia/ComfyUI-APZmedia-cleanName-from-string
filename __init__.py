from .nodes.APZnamefromtext import CleanFileNameNode
from .nodes.APZgeneratePathNode import GenerateFilePathNode

NODE_CLASS_MAPPINGS = {
    "CleanFileNameNode": CleanFileNameNode,
    "GenerateFilePathNode": GenerateFilePathNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CleanFileNameNode": "APZmedia Clean File Name Node",
    "GenerateFilePathNode": "Generate File Path Node"
}

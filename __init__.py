from .nodes.APZnamefromtext import CleanFileNameNode
from .nodes.APZgeneratePathNode import GenerateFilePathNode
from .nodes.APZfileNameBuilder import APZmediaStandardFilenameBuilder

NODE_CLASS_MAPPINGS = {
    "CleanFileNameNode": CleanFileNameNode,
    "GenerateFilePathNode": GenerateFilePathNode,
    "APZmediaStandardFilenameBuilder": APZmediaStandardFilenameBuilder,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CleanFileNameNode": "APZmedia Clean File Name Node",
    "GenerateFilePathNode": "Generate File Path Node",
    "APZmediaStandardFilenameBuilder": "APZmedia Standard Filename Builder",
}

from setuptools import setup, find_packages

setup(
    name="clean_file_name_node",
    version="0.2",  # Updated version since you're adding a new node
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'unidecode',
    ],
    entry_points={
        'comfyui.nodes': [
            'clean_file_name_node = nodes.APZnamefromtext:CleanFileNameNode',
            'generate_file_path_node = nodes.APZgeneratePathNode:GenerateFilePathNode',  # Corrected this line
            'standard_name_node = nodes.APZfileNameBuilder:APZmediaStandardFilenameBuilder'
        ],
    },
    author="Pablo Apiolazza",
    author_email="info@apzmedia.com",
    description="A ComfyUI node to clean and sanitize text to be used as file names, and generate file paths.",
    url="https://github.com/apzmedia/ComfyUI-APZmedia-cleanName-from-string",
    python_requires='>=3.6',
)

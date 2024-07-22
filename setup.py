from setuptools import setup, find_packages

setup(
    name="clean_file_name_node",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'unidecode',
    ],
    entry_points={
        'comfyui.nodes': [
            'clean_file_name_node = nodes.APZnamefromtext:CleanFileNameNode',
        ],
    },
    author="Pablo Apiolazza",
    author_email="info@apzmedia.com",
    description="A ComfyUI node to clean and sanitize text to be used as file names.",
    url="https://github.com/apzmedia/ComfyUI-APZmedia-cleanName-from-string",
    python_requires='>=3.6',
)

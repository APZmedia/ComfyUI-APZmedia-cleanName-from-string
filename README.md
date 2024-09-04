# APZmedia File Name Nodes

## Overview
This package provides a set of custom nodes for ComfyUI that streamline text processing for VFX file naming and file path generation. The nodes include the **Clean File Name Node**, **Generate File Path Node**, and **APZmedia Standard Filename Builder**, all designed to fit common conventions in VFX pipelines. These nodes help sanitize text, create valid filenames, and generate file paths based on typical VFX directory structures, making it easier to manage large-scale projects.

## Features

### 1. **Clean File Name Node**
- **Input Text**: Accepts a string input to be sanitized.
- **Replacement Character**: Allows specification of a character to replace invalid characters.
- **Invalid Characters**: A precompiled list of characters to be removed from the input text.
- **Character Limit**: Truncates the cleaned text to a specified maximum length.
- **Prefix**: Adds a user-defined prefix to the resulting cleaned text.

### 2. **Generate File Path Node**
- **VFX Folder Structure Customization**: Dynamically generates a file path based on the specified project components, such as the root folder, project name, episode name, shot name, and pass type.
- **Toggle Components**: Each component (e.g., project name, episode name, shot name) can be toggled to be included or excluded, providing flexibility in generating the path structure.
- **OS-Compatible Paths**: Automatically uses the correct file path separator for the operating system (e.g., `/` for Unix-based systems and `\` for Windows).
- **Flexible Path Generation**: Build paths that match your project needs, such as `/root/project/episode/shot/pass`, based on the components you choose to include.

### 3. **APZmedia Standard Filename Builder**
- **Customizable Segments**: Concatenate any combination of project name, episode name, shot name, and pass name.
- **Flexible Inclusion**: Each segment can be toggled on or off, allowing users to include only the relevant components.
- **Delimiter Control**: Specify a custom delimiter to separate segments in the filename (e.g., hyphen, underscore, etc.).
- **Standardized Naming**: Helps maintain consistent file naming across projects, shots, and passes.

## Input and Output Types

### **Clean File Name Node**
- **Input Types**:
  - `input_text` (STRING): The text to be cleaned.
  - `replacement_char` (STRING): Character to replace invalid characters (default: `-`).
  - `invalid_chars` (STRING): Characters to be removed (default: ` #%&{}\\<>*?/ $!'\":@+`|=.`, emojis, and alt codes).
  - `char_limit` (INT): Maximum length of the output string (default: 255).
  - `prefix` (STRING): Prefix to prepend to the filename.
  
- **Output Types**:
  - `cleaned_text` (STRING): The sanitized and truncated text string.

### **Generate File Path Node**
- **Input Types**:
  - `root_folder` (STRING): The root directory for the project (e.g., `/mnt/projects`).
  - `project_name` (STRING): The name of the VFX project or show (e.g., `Starwars`).
  - `episode_name` (STRING): The episode or sequence name (optional).
  - `shot_name` (STRING): The shot number or identifier (e.g., `0010`).
  - `pass_name` (STRING): The type of pass (e.g., compositing, animation).
  - `toggle_root_folder` (INCLUDE/EXCLUDE): Whether to include the root folder in the path.
  - `toggle_project_name` (INCLUDE/EXCLUDE): Whether to include the project name in the path.
  - `toggle_episode_name` (INCLUDE/EXCLUDE): Whether to include the episode name in the path.
  - `toggle_shot_name` (INCLUDE/EXCLUDE): Whether to include the shot name in the path.
  - `toggle_pass_name` (INCLUDE/EXCLUDE): Whether to include the pass type in the path.
  
- **Output Types**:
  - `generated_path` (STRING): The generated file path based on the selected components and operating system conventions.

### **APZmedia Standard Filename Builder**
- **Input Types**:
  - `project_name` (STRING): The project or show name (optional).
  - `episode_name` (STRING): The episode or sequence name (optional).
  - `shot_name` (STRING): The shot number or identifier (e.g., `0010`).
  - `pass_name` (STRING): The type of pass (e.g., compositing, animation).
  - `delimiter` (STRING): The character to separate the segments (default: `-`).
  - `toggle_project_name` (INCLUDE/EXCLUDE): Whether to include the project name in the concatenated file name.
  - `toggle_episode_name` (INCLUDE/EXCLUDE): Whether to include the episode name in the concatenated file name.
  - `toggle_shot_name` (INCLUDE/EXCLUDE): Whether to include the shot name in the concatenated file name.
  - `toggle_pass_name` (INCLUDE/EXCLUDE): Whether to include the pass name in the concatenated file name.
  
- **Output Types**:
  - `concatenated_name` (STRING): The concatenated filename based on the selected segments and delimiter.

## How They Work

### **Clean File Name Node**
1. **Replace Invalid Characters**: Replaces invalid characters in the input text with the specified replacement character.
2. **Remove Invalid Characters**: Removes characters defined in `invalid_chars`.
3. **Truncate**: Truncates the text to the maximum defined length.
4. **Prepend Prefix**: Adds the user-defined prefix to the beginning of the cleaned text.

### **Generate File Path Node**
1. **Segmented Path Construction**: The node allows for building a file path by concatenating different segments (root folder, project name, episode name, shot name, and pass type). Each segment can be included or excluded based on the user's selection.
2. **Flexible Structure**: You can toggle on or off any part of the path structure, allowing for customized path generation that suits different VFX project workflows.
3. **OS-Aware**: Automatically generates paths that conform to the path separator required by the operating system (`/` or `\`).
4. **Output**: The resulting full path is generated based on the included components.

### **APZmedia Standard Filename Builder**
1. **Segment Inclusion**: Users specify whether to include the project name, episode name, shot name, and pass name by toggling them on or off.
2. **Delimiter Selection**: A delimiter (default is a hyphen) is chosen to separate the different segments in the final filename.
3. **Concatenation**: The selected segments are concatenated in the order specified and joined using the selected delimiter.
4. **Output**: The node returns a single concatenated filename that adheres to VFX standards or custom naming conventions.

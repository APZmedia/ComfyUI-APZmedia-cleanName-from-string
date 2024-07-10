# Clean File Name Node

## Overview
The Clean File Name Node is a custom node for ComfyUI designed to process and sanitize text strings for use as valid file names. It replaces invalid characters with a user-specified character and truncates the resulting string to a defined length.

## Features
- **Input Text**: Accepts a string input to be sanitized.
- **Replacement Character**: Allows specification of a character to replace invalid characters.
- **Invalid Characters**: A precompiled list of characters to be removed from the input text.
- **Character Limit**: Truncates the cleaned text to a specified maximum length.

## Input Types
- `input_text` (STRING): The text to be cleaned.
- `replacement_char` (STRING): Character to replace invalid characters (default: `-`).
- `invalid_chars` (STRING): A string containing characters to be removed (default: ` #%&{}\\<>*?/ $!'\":@+`|=.`, emojis, and alt codes).
- `char_limit` (INT): Maximum length of the output string (default: 255).
- `Prefix` (STRING): A prefix to create filenames.

## Output Types
- `cleaned_text` (STRING): The sanitized and truncated text string.

## How It Works
1. **Replace Spaces**: All spaces in the input text are replaced with the specified replacement character.
2. **Remove Invalid Characters**: The node removes all characters defined in the `invalid_chars` string.
3. **Truncate Text**: The resulting text is truncated to the length defined by `char_limit`.

## Usage Example
```
input_text: "This is a text! With Very Invalid £ Character$."
replacement_char: "-"
char_limit: 255
```
### Output
```
cleaned_text: "This-is-a-text-With-Very-Invalid-Character"
```

This node is useful for preparing strings to be used as file names, ensuring they are valid and meet specific length requirements.

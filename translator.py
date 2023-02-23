import os
import re
from bs4 import BeautifulSoup
from googletrans import Translator

# Project directory and output directory
PROJECT_NAME = "input"
OUTPUT_DIR = "output"

# Define output language
target_lang = 'de'

# Define a regular expression pattern to match numbers and punctuation
num_punct_pattern = r'^[\d\W]+$'

# Initialize the translator
translator = Translator()

# Iterate over all files in the project directory
def translate_html_files():
    for root, dirs, files in os.walk(os.path.join(PROJECT_NAME)):
        for file in files:
            if file.endswith('.html'):
                # Read the HTML file and parse it with BeautifulSoup
                with open(os.path.join(root, file), 'r', encoding="utf-8") as f:
                    html = f.read()
                # Set the language attribute of the html tag to Hindi
                soup = BeautifulSoup(html, 'html.parser')
                if soup.html is not None:
                    soup.html['lang'] = target_lang

                # Translate all text strings in the HTML file to Hindi
                for tag in soup.find_all(string=True):
                    # Skip script and style tags
                    if tag.parent.name in ['script', 'style']:
                        continue
                    # Exclude numbers and punctuation from language detection
                    if re.match(num_punct_pattern, tag.string):
                        continue
                    try:
                        # Translate the text to English
                        translated_text = translator.translate(tag.string or tag.text, dest=target_lang).text
                        # Replace the original text with the translated text
                        tag.replace_with(translated_text)
                        print(f"Translated text: {translated_text}")
                    except Exception as e:
                        print(f"Error translating '{tag}': {str(e)}")
                        continue
                
                # Save the translated HTML file
                try:
                    # Create the output directory with complete folder names
                    output_dir = os.path.join(OUTPUT_DIR, os.path.relpath(root, PROJECT_NAME))
                    # Create the output directory if it doesn't exist
                    os.makedirs(output_dir, exist_ok=True)
                    # Save the translated HTML file to the output directory
                    output_file = os.path.join(output_dir, file)
                    with open(output_file, "w", encoding="utf-8") as f:
                        f.write(str(soup.prettify()))
                
                except Exception as e:
                            print(f"Error writing file '{tag}': {str(e)}")
                            continue

translate_html_files()
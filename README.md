# HTML and EPUB Translator
This Github repository contains two Python scripts for translating HTML and EPUB files using the Google Translate API.

## HTML Translator
The html_translator.py script iterates over all HTML files in the input directory, sets the language attribute of the html tag to the target language, and translates all text strings in the HTML file to the target language using the Google Translate API. The translated files are saved in the output directory.

### Prerequisites
- Python 3.6 or later
- BeautifulSoup
- googletrans

### Usage
1. Set the target language by changing the target_lang variable in the script.
2. Run the script in your terminal: python html_translator.py

## EPUB Translator
The epub_translator.py script iterates over all EPUB files in the input directory, sets the language attribute of the html tag to the target language, and translates all text strings in the HTML file to the target language using the Google Translate API. The translated files are saved in the output directory.

### Prerequisites
- Python 3.6 or later
- BeautifulSoup
- googletrans
- ebooklib

### Usage
1. Set the target language by changing the target_lang variable in the script.
2. Run the script in your terminal: python epub_translator.py

## Important Notes
Before running the script, make sure to place the files you want to translate in the input directory.
The scripts do not handle files with non-UTF-8 encoding. If you encounter issues with encoding, please ensure that your files are encoded in UTF-8.

# HTML Translator
The `html_translator.py` script iterates over all HTML files in the input directory, sets the language attribute of the html tag to the target language, and translates all text strings in each HTML file using the Google Translate API. The translated files are saved in the output directory.

### Prerequisites
- Python 3.7 or later
- `BeautifulSoup`
- `googletrans`

### Usage
1. Set the target language by changing the target_lang variable in the script.
2. Run the script in your terminal: `python html_translator.py`

## Important Notes
Before running the script, make sure to place the files you want to translate in the input directory.
The script does not handle files with non-UTF-8 encoding. If you encounter issues with encoding, please ensure that your files are encoded in UTF-8.

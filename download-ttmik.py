import os
from bs4 import BeautifulSoup
import urllib.request

# Get the TTMIK curriculum page and parse it into html
with urllib.request.urlopen("http://talktomeinkorean.com/curriculum/") as url:
    r = url.read()
soup = BeautifulSoup(r, 'lxml')

# Find all <a> elements
links = soup.find_all("a")

# Set the target directory for downloaded files
cwd = os.getcwd()
tgt_path = os.path.join(cwd + '/ttmik', 'example.mp3')
directory = os.path.dirname(tgt_path)

# Check if the directory exists; if false, create it
try:
    os.stat(directory)
except:
    os.mkdir(directory)

links_to_download = []

# Get all of the relevant mp3 links in <a> tags
for link in links:
    href = link.get('href')
    if href is not None and link.string == 'MP3' and href.find('.mp3') > -1:
        ttmikIndex = href.lower().find('ttmik')
        extIndex = href.find('mp3')
        filename = href[ttmikIndex:extIndex+3]
        links_to_download.append([href, filename])

# Clear console and print target directory
print(chr(27) + "[2J")
print('Target directory: ' + cwd + '/ttmik')

# Download each link
for link in links_to_download:
    href = link[0]
    filename = link[1]
    tgt_path = os.path.join(cwd + '/ttmik/', filename)

    # TODO: Parse the level/lesson numbers. Download the files to the associated directory.

    # TODO: Print out the target directory cleanly.
    # TODO: If file exists at path, skip.
    # TODO: Update file names to be consistent (ttmik-level-1-lesson-1)?

    print('Downloading ' + filename + '...', end='\r', flush=True)
    urllib.request.urlretrieve(href, tgt_path)
    # TODO: Add download status bar

    # \033[K = clear line, \r = carriage return (go back to start of line)
    print('\033[K Downloaded %s successfully!' % filename)
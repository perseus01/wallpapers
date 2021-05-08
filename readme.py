# Python script to generate README.md file for https://github.com/perseus01/wallpapers

import os
import re

head = """# Wallpapers
### Preview:
\n
"""

f = open('README.md', 'w')
f.write(head)

# Sorted (in ascending order) list of all wallpapers in the directory.
files_list = os.listdir()
wallpapers_list = sorted(list(filter(re.compile('[0-9]{4}\.(jpg|png|jpeg)').match, files_list)))

# Generate wallpaper previews in README.md
f.write('<div text-align="center">\n')
for name in wallpapers_list:
    f.write(f'<img width="50%" src="https://raw.githubusercontent.com/perseus01/wallpapers/main/{name}" alt="{name[:4]}"> <p font-size="1.5em">{name[:4]}</p>\n')
f.write('</div>')
f.close()
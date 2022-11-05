# Python script to generate README.md file for https://github.com/perseus01/wallpapers

import os
import re

head = """# Wallpapers

### Click on a preview to download the wallpaper.

### Preview:
\n
"""

f = open('README.md', 'w')
f.write(head)

# Sorted (in ascending order) list of all wallpapers in the wps directory.
cur_dir = os.getcwd()
files_list = os.listdir(f'{cur_dir}/wps')
wallpapers_list = sorted(list(filter(re.compile('[0-9]{4}\.(jpg|png|jpeg)').match, files_list)))

# Generate wallpaper previews in README.md
for name in wallpapers_list:
    f.write(f'<p font-size="1.5em" align="center"><img width="75%" src="https://raw.githubusercontent.com/perseus01/wallpapers/main/wps/{name}" alt="{name[:4]}"><br>{name[:4]}</p>\n')
f.close()
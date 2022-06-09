import in_place
from pathlib import Path
import os

for file_name in Path(os.curdir).rglob('*.ttslua'):
    with in_place.InPlace(file_name,mode='b') as file:
        for line in file:
            if line.startswith(b'#include'):
                line = line.replace(b'\\',b'/')
            file.write(line)

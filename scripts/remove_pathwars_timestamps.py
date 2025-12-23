import re
import shutil
from pathlib import Path

file_path = Path(r"c:\Users\Lewis\WritersideProjects\PathWarsWiki\Writerside\topics\C04-Guards-of-Magni-Watch\Allisee-Tea-Magni-Watch.md")
backup_path = file_path.with_suffix(file_path.suffix + '.bak2')

# make a backup
shutil.copy2(file_path, backup_path)

text = file_path.read_text(encoding='utf-8')
# remove lines that start with optional whitespace then 'Path Wars,'
clean = re.sub(r"(?m)^\s*Path Wars, \[.*\]\s*\r?\n?", "", text)

file_path.write_text(clean, encoding='utf-8')
print('DONE')


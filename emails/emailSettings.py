import ezgmail, os
from pathlib import Path

os.chdir(Path.home() / Path("OneDrive", "Escritorio", "python", "emails"))
ezgmail.init()
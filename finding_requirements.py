import os
# import sys
# from fuzzywuzzy import fuzz
import subprocess

path = r"C://some_code_dir"

files = os.listdir(path)
pyfiles = []
for root, dirs, files in os.walk(path):
      for file in files:
        if file.endswith('.py'):
              pyfiles.append(os.path.join(root, file))

stopWords = ['from', 'import',',','.']

importables = []

for file in pyfiles:
    with open(file) as f:
        content = f.readlines()

        for line in content:
            if "import" in line:
                for sw in stopWords:
                    line = ' '.join(line.split(sw))

                importables.append(line.strip().split(' ')[0])

importables = sorted(list(dict.fromkeys(importables)))
with open(f"{path}/requirements.txt", 'w') as fp:
    for item in importables:
        fp.write("%s\n" % item)


# importables = set(importables)
# subprocess.call(f"pip freeze > {path}/requirements.txt", shell=True)

#~~~From Reese <3~~~

import os
for i in os.listdir():
    print(i)
    if i.endswith(".mf"):
        os.system('cmd /c "multify -x -f' + i + '"')

import runpy
import os
param="hello world"
os.chdir("../")
r=runpy.run_path("some_script.py",init_globals=globals(),run_name="__main__")
# cannot reach native path.
print(type(r),r)
# so it is working, and can be think out of brain IF HAVE EXPERIENCE.
# not running as main. cannot reach the content.

import subprocess

# import subprocess
out = subprocess.Popen(['ls', '-l'],
           stdout=subprocess.PIPE,
           stderr=subprocess.STDOUT)
stdout,stderr = out.communicate()

print(stdout)

print(stderr)

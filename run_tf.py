import sys
from subprocess import call
from subprocess import check_output

commands = ["terraform", "apply"]

print(commands)
call(commands)

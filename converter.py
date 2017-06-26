import subprocess
import fnmatch
import glob, os
import sys

matches = []

for root, dirnames, filenames in os.walk(str(sys.argv[1])):
    for filename in fnmatch.filter(filenames, '*.wav'):
        matches.append(os.path.join(root, filename))

for match in matches:
	cmd = 'lame --preset insane %s' % match
	subprocess.call(cmd, shell=True)

	#
	## Removes the original
	#
	os.remove(match)
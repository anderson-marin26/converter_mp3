import subprocess
import fnmatch
import glob, os

matches = []
for root, dirnames, filenames in os.walk("teste/01"):
    for filename in fnmatch.filter(filenames, '*.wav'):
        matches.append(os.path.join(root, filename))

for match in matches:
	cmd = 'lame --preset insane %s' % match
	subprocess.call(cmd, shell=True)

	#
	## Removes the original
	#
	os.remove(match)

#wav = '20150917152033-4-sorriso-36091477.wav'
#cmd = 'lame --preset insane %s' % wav
#subprocess.call(cmd, shell=True)

import subprocess
import os, random
import glob

path = '/home/kush/Ad/'
print 'Play ad videos'
infiles = glob.glob(os.path.join(path, '*'))
randfile = []
while 1:
    a = subprocess.call(['cvlc', '-Z', path])
# for infile in infiles:
#     randfile.append(infile)
#     infile = random.choice(randfile)
#     a = subprocess.call(['vlc', '-f', '--slide-show', infile])
#     print infile
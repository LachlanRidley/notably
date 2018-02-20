import os
import sys
import shutil
from subprocess import call

notable_dir = os.environ['NOTABLE']

command = sys.argv[1]

old_note_file = sys.argv[2]
new_note_file = ""

if len(sys.argv) > 3:
    new_note_file = sys.argv[3]

def duplicate_note(old_note, new_note):
    shutil.copyfile(notable_dir + '/' + old_note + '.md', notable_dir + '/' + new_note + '.md')

def open_note(note_name):
    call(['subl', notable_dir + '/' + note_name + '.md'])

if command == "open":
    open_note(old_note_file)
elif command == "copy":
    duplicate_note(old_note_file, new_note_file)
    open_note(new_note_file)

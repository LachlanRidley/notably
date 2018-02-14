import os
import sys
import shutil
from subprocess import call

notable_dir = os.environ['NOTABLE']
old_note_file = sys.argv[1]
new_note_file = sys.argv[2]

def duplicate_note(old_note, new_note):
    shutil.copyfile(notable_dir + '/' + old_note + '.md', notable_dir + '/' + new_note + '.md')

def open_note(note_name):
    call(['subl', notable_dir + '/' + note_name + '.md'])

duplicate_note(old_note_file, new_note_file)
open_note(new_note_file)

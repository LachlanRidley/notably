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

def list_done(note_name):
    note = open(notable_dir + '/' + note_name + '.md')
    for line in note:
        done_start = line.find('[x]')
        if done_start > -1:
            print(line[done_start+3:])

def list_todo(note_name):
    note = open(notable_dir + '/' + note_name + '.md')
    
    section_title = "None"

    for line in note:
        section_start = line.find('##')
        if section_start > -1:
            section_title = line[section_start+2:]
            print(section_title)

        done_start = line.find('[ ]')
        if done_start > -1:
            print("\t" + line[done_start+3:])

if command == "open":
    open_note(old_note_file)
elif command == "copy":
    duplicate_note(old_note_file, new_note_file)
    open_note(new_note_file)
elif command == "done":
    list_done(old_note_file)
elif command == 'todo':
    list_todo(old_note_file)

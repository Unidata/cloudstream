#!/usr/bin/python3

import pexpect
import sys
import subprocess

child = pexpect.spawnu('rclone config')
child.logfile = sys.stdout

child.expect('n/s/q> ')
child.sendline('n')

child.expect('name> ')
child.sendline('dropbox')

child.expect('Storage> ')
child.sendline('dropbox')

child.expect('app_key> ')
child.sendline('')

child.expect('app_secret> ')
child.sendline('')

child.expect('https://.*response_type=code')

subprocess.run(["/usr/bin/midori", child.after])
#child.expect('Enter the code: ')

child.interact()

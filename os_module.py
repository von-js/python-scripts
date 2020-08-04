import os
# Get current wrkdir
os.getcwd()
# change dir
os.chdir()
# The os.environ holds the environment variables that were set when the os module was loaded.
os.environ.get()
# This is the setting and environment variable. This setting exists for subprocesses spawned from this code.
os.environ['LOGLEVEL'] = 'DEBUG'
#This is the login of the user in the terminal that spawned this process.
os.getlogin()
# List he content in the directory
os.listdir('.')
# Rename a file or directory
os.rename('_crud_handler', 'crud_handler')
# Change the permission settings of a file or directory
os.chmod('my_script.py', 0o755)
# Create a directory
os.mkdir('/tmp/holding')
# Delete a file
os.remove('my_script.py')
# Delete a single dir
os.rmdir('/tmp/holding')
# Delete a tree of directories, starting with the leaf directory and working up the tree. The operation stops with the first nonempty directory.
os.removedirs('/Users/kbehrman/tmp/scripts/devops')
#Get stats about the file or directory. These stats include st_mode, the file type and permissions, and st_atime, the time the item was last accessed.
os.stat_result(st_mode=16877,
st_ino=4359290300,
st_dev=16777220,
st_nlink=18,
st_uid=501,
st_gid=20,
st_size=576,
st_atime=1544115987,
st_mtime=1541955837,
st_ctime=1567266289)


# OS path
cur_dir = os.getcwd() # Get the current wrkdir
os.path.split(cur_dir) # os.path.split splits the leaf level of the path from the parentpath.
os.path.dirname(cur_dir) # os.path.dirname returns the parent path.
os.path.basename(cur_dir) #os.path.basename returns the leaf name.


#There are many instances when you need to run applications outside
#of Python from within your Python code. This could be built-in shell
#commands, Bash scripts, or any other command-line application. To
#do this, you spawn a new process (instance of the application). The
#subprocess module is the right choice when you want to spawn a
#process and run commands within it. With subprocess, you can
#run your favorite shell command or other command-line software and
#collect its output from within Python. For the majority of use cases,
#you should use the subprocess.run function to spawn processes: 
import subprocess

cp = subprocess.run(['ls','-l'],capture_output=True,universal_newlines=True)
cp.stdout
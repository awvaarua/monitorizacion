password = "fura4468AB\n"

def restart():
    import sys, os
    python = sys.executable
    os.execl(python, python, * sys.argv)

try:
    import requests
    print "Paquete importado"
except ImportError:
    from subprocess import Popen, PIPE
    process = Popen(['sudo', '-H', 'pip', 'install', 'requests'])
    process.communicate(password)
    process.wait()
    print "Instalando requests"
    restart()
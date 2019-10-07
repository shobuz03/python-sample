#!C:\Github\Projects\python-sample\helloclick\env\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'HelloWorld','console_scripts','hello'
__requires__ = 'HelloWorld'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('HelloWorld', 'console_scripts', 'hello')()
    )

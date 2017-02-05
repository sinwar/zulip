import sys

def check_venv(filename):
    try:
        import lister
        from typing import cast, Any, Callable, Dict, Iterator, List, Optional, Tuple
    except ImportError:
        print("You need to run the %s inside a Zulip dev environment." %(filename,))
        print("If you are using Vagrant, you can `vagrant ssh` to enter the Vagrant guest.")
        sys.exit(1)

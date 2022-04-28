"""codemy module entrypoint

You should not need to modify this file. This file's purpose
is to allow running codemy as a module, ex:

$ python -m codemy

or to quickly run from within the root directory as:

$ python codemy

"""
import sys

from codemy import main

sys.exit(main())  # type: ignore

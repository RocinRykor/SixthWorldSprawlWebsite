import os
import sys

basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(basedir)

import sixthworldsprawl

application = sixthworldsprawl.application

if __name__ == "__main__":
    application.run(host="0.0.0.0", debug=True, port=5001)

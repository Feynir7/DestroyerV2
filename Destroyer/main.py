#!/usr/bin/python3
import os
from DestroyerV2 import main
import sys
import asyncio
if __name__=='__main__':
    if os.geteuid()!=0:
        sys.exit('Run as administrator')
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        sys.exit('\nQuitting...\n')

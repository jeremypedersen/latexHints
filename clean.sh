#!/bin/bash

# A small script to clean up the mess left by TexShop when building PDFs
rm $(find * | grep .synctex)
rm $(find * | grep .aux)
rm $(find * | grep .log)

# Get rid of python junk
rm $(find * | grep .pyc)

# Get rid of Mac junk
rm $(find * | grep .DS_Store)



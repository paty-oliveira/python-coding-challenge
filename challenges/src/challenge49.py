"""
You have to extract a portion of the file name as follows:

- Assume it will start with date represented as long number
- Followed by an underscore
- You'll have then a filename with an extension
- It will always have an extra extension at the end

Inputs:
1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION
1_This_is_an_otherExample.mpg.OTHEREXTENSIONadasdassdassds34
1231231223123131_myFile.tar.gz2

Outputs:
FILE_NAME.EXTENSION
This_is_an_otherExample.mpg
myFile.tar
"""

import re


def extract_file_name(dirty_file_name):
    regex_pattern = r"^(?P<id>\d+)_+(?P<filename>[a-zA-Z0-9_-]+)\.(?P<extension1>[a-zA-Z0-9_-]+)\.(?P<extension2>[a-zA-Z0-9_-]+)$"
    match = re.search(regex_pattern, dirty_file_name)
    file_name = ""

    if match:
        occur = match.groupdict()
        file_name = occur["filename"] + "." + occur["extension1"]
        return file_name

    return file_name

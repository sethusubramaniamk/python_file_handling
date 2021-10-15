This script is used to list all the files & folders in a directory or list files of specific extension

**Format:**

_sudo python3 list_dir_elements.py -d <target_directory> -e <file_extension>_


**Example:**

_sudo python3 list_dir_elements.py -d ./newfolder -e .txt_

**Note:**

  1. For more information, type in the following command,

      _sudo python3 list_dir_elements.py --help_

  2. If the target directory argument is not provided, the current working directory is taken as default.

  3. If the extension is not provided, all the files & folders in the directory are listed.

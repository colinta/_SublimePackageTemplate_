----
target_name: README.md
----
 {{ ProJect }} for Sublime Text 2
={{ '=' * len(ProJect) }}====================
{%- if desc %}

{{ desc }}
{%- endif %}

 Installation
--------------

1. Using Package Control, install "{{ ProJect }}"

Or:

1. Open the Sublime Text 2 Packages folder

    - OS X: ~/Library/Application Support/Sublime Text 2/Packages/
    - Windows: %APPDATA%/Sublime Text 2/Packages/
    - Linux: ~/.Sublime Text 2/Packages/

2. clone this repo
3. Install keymaps for the commands (see Example.sublime-keymap for my preferred keys)

 Commands
----------

`{{ project }}`:

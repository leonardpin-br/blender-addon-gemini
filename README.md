# Python starter project to create addons for Blender.

This starter kit is preconfigured to facilitate fast development.



## Before you begin

### Git and Cygwin
Install Git (and Git Bash) for version control.

Cygwin is a good terminal and I suggest you use it. But, you can execute the BASH
scripts with just Git Bash.

### Spaces in file paths
Make sure you clone this repository to a path without spaces in it. Sphinx will throw an error if there are any spaces in the path.

### _example files
There are files that have ``_example`` in their names. Those files were created to deal with source control.

It is necessary to copy and rename them, removing the ``_example``. Those files are:

```
<project_root>/.vscode/settings_example.json
<project_root>/docs/sphinx/make_example.bat
```

### Line endings (CRLF and LF) on Windows
The ``<project_root>/docs/sphinx/make.bat`` file should have CRLF line endings.

The BASH script (``.sh``) files should have LF (Unix) line endings even if you are using Windows. They should be executed in Cygwin or Git Bash.

The provided ``.gitattributes`` file has a configuration that should work without problems (Reference: [Configuring Git to handle line endings](https://docs.github.com/en/get-started/getting-started-with-git/configuring-git-to-handle-line-endings)).

### Visual Studio Code Extension
If you use Visual Studio Code, install the **Blender Development** or
**Blender Development [Experimental Fork]**. It will automatically create
the link in the appropriate folder connecting the addon to Blender.

If you do not use VSCODE, you can try to create a link to the addon folder
(``<project_root>\Gemini``) at
``C:\Users\<USERNAME>\AppData\Roaming\Blender Foundation\Blender\4.0\scripts\addons``
with the same name of this addon (Gemini).

In my tests, it did not work though. Using the extension is the preferred way
to go.

### Python module
It is a good idea to install ``fake-bpy-module-latest`` to avoid import
warnings in the editor.



## Inspirations and reference
This kit is based on the course
[Blender 2.9 Addon Development With Python](https://www.udemy.com/course/st3-addon-course/)
taught by **ST3 (>O.o)>**.



## Why is it better than a script in a single file?
This starter kit allows the development of a more powerfull tool. Instead of creating a single script, the user of this kit will be able to create a small application (addon).



## It includes
    1. The Gemini addon created by ST3 and patched by me.
    2. The code is heavly documented (using Sphinx and Google style docstrings) and HTML generation
    is preconfigured.
    3. Line endings are preconfigured.
    4. BASH scripts to facilitate the setup.



## Dependencies

### Node.js
It depends on Node.js, but only for development (documentation).

Install Node.js and navigate to the root folder of this project. Install node
dependencies with the command:

```
npm install
```

The provided `package.json` file has many useful scripts.

### Virtual Environments

It will be advantageous to install the `virtualenv` package in order for you to
create virtual environments.

The command to install the recommended package is:

```
pip install virtualenv
```

Then, create a virtual environment (`py310env` folder)
in the root folder of this project. Run this command from the project's root folder:

```
virtualenv --python="C:/Program Files/Python310/python.exe" "./py310env"
```

Activate the virtual environment with the command:
```
source ./py310env/Scripts/activate   => Cygwin and Git Bash
py310env\Scripts\activate            => Command Prompt
py310env\Scripts\activate.ps1        => PowerShell
```

It is important to install the necessary packages using the command below from
the project's root:
```
pip install -r requirements.txt
```
It will install all the packages, including the appropriate version of Sphinx.



## Documentation
By now, you should have installed Sphinx inside the virtual environment (`py310env` folder).

### Terminals on Windows systems
On Windows systems, the terminal you are using makes a big difference. On my tests, I used
- Command Prompt
- Cygwin
- Git Bash
- Powershell

Even after activating the virtual environment in all of them, the results may differ.

### Step-by-step on Windows systems
For the documentation generation to work as expected, it is necessary to do the following:

#### 1. Edit the environment variables
Add the path to the `blender.exe` to the system variables. The default path is
```
C:\Program Files\Blender Foundation\Blender 4.0\
```
Move it tho the top (or near the top) of the list.

#### 2. Edit the make.bat file
Make a copy of `<project_root>/docs/sphinx/make_example.bat` and rename the copy to `make.bat`. This is necessary because of Git source control.

Sphinx will be configured to use the Blender's interpreter (`blender.exe`) instead of the interpreter in the virtual environment.

`sphinx-quickstart` creates two important files (they are inside the `<project_root>/docs/sphinx` folder):

```
make.bat    => Edit this one if you are on Windows.
Makefile
```

There is a script in the `package.json` file to make it easy. Just run this command
in a terminal like **Cygwin** or **Git Bash**:

```
npm run update:make_bat
```

It executes a BASH script (`<project_root>/scripts/update_make_bat.sh`). In turn, that script edits the `make.bat` file with the following:

```
set SPHINXBUILD=blender --background --python "full/path/to/resources/documentation_config/build_sphinx_blender_doc.py"
```

The `blender --background --python` command is important. Without it, all terminals fail to generate the documentation.

The above file (`build_sphinx_blender_doc.py`) is a custom config file that instructs Sphinx to work with the Blender modules.

Having said that, the `conf.py` file is configured to mock the Blender modules, because it can cause importing errors.

#### Portability

In Windows (inside `make.bat`), the path with foward slashes (`/`) works as well as with back slashes (`\`). To keep it easy to copy and paste between different systems, it is best to keep the `/`.

#### If the Makefile is edited instead of the make.bat

The result is the same on all terminals:

- The Python executable is the one inside the py310env.

- That interpreter does not know anything about any Blender modules. So, it fails to import them.



## Folder structure
```
<project_root>
|- Gemini                       (the addon)
    |- menu                     ()
    |- operator                 ()
    |- property                 ()
    |- register                 ()
    |- utility                  ()
|- docs                         (for the generated HTML documentation)
    |- sphinx                   (for the generated HTML documentation)
|- py310env                     (virtual environment folder)
|- resources                    (good to have and needed files)
    |- documentation_config     (configuration for Sphinx)
|- scripts                      (usefull bash scripts)

```



## Which file will be executed?
No Python files in this project should be executed directly.

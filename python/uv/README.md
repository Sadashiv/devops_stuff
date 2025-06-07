UV
========

pip - used to install package in current environment
pipx - used to install package in isolated virtual environment

1. Install uv also we can use the binary for W-uv.exe L-uv
    pipx install uv

2. Uninstall uv
    uv cache clean
    rm -r "$(uv python dir)"
    rm -r "$(uv tool dir)"

3. Features https://docs.astral.sh/uv/getting-started/features/ 

4. Install python
    uv python install 3.8 3.14 #Installs in user home directory {find,list, pin, dir, uninstall}
5. uv run --python 3.13 python -c "print('Hello World')" #If python not found it downloads and install
6. uv venv #if python not found it will download and install

7. Run scripts with arguments can also be passed
    uv run python hello.py or uv run hello.py
    uv run --with boto3 example.py #boto3 > < versions can be added

8. Create lock for script and project 
    uv lock --script example.py #create example.py.lock file same level as example.py
    uv lock #will create uv.lock file
    uv run --with boto3 --python 3.14  --script example.py
    uv tree   --script example.py

9. Using tools https://docs.astral.sh/uv/guides/tools/#running-tools
    "uvx django" equivalent to "uv tool run django"# to uv tool run django #package should provide executables

10. Python project metadata is defined in a pyproject.toml
    Application projects are suitable for web servers, and command line interfaces
    v init --python 3.8 or uv init <project_name> will not include build system as it considered as app
    uv init --package example-pkg (package or app is same)
    A library provides functions and objects for other projects to consume.
    uv init --lib example-lib
    uv run --directory . python -c "import my_library; print(my_library.hello())"
    Projects with extension modules
    Guv init --build-backend maturin example-ext
    maturin for projects with Rust
    scikit-build-core for projects with C, C++, FORTRAN, Cython

11. manage dependencies
    uv add git+https://github.com/psf/requests #Add as editable installation
    uv add "httpx @ git+https://github.com/encode/httpx" #can be add as --branch, --tag --rev
    uv add boto3
    uv remove boto3

The following dependency sources are supported by uv:

    Index: A package resolved from a specific package index.
    Git: A Git repository.
    URL: A remote wheel or source distribution.
    Path: A local wheel, source distribution, or project directory.
    Workspace: A member of the current workspace.

    uv add torch==2.5.1 --index pytorch=https://download.pytorch.org/whl/cpu
    set explicit = true in [[uv.tool.index]]
    uv add --editable ~/projects/bar/

    uv lock will generate with source code to avoid this run with --no-sources
    uv lock --no-sources
    Add optional dependecies
    uv add matplotlib --optional extra
    uv add --dev pytest
    uv add --group lint ruff

    The --dev, --only-dev, and --no-dev flags are equivalent to --group dev, --only-group dev, and --no-group dev respectively.
    Default groups
    [tool.uv]
    default-groups = ["dev", "foo"]

12. Generate lock file
    uv run, uv sync, uv export --format requirementstxt > requirements.txt
      525  uv lock --check
    uv lock --upgrade
    uv lock --upgrade-package boto3
    uv lock --upgrade-package boto3==1.35.98

13. Configuration:
    uv run consolescript #Run console script
**plugin entry points**
    setting tool.uv.package = true will force a project to be built and installed into the project environment.

uv build ../../my_package/
uv build --wheel or --sdist
uv build --build-constraint constraints.txt --require-hashes

Using workspaces to work on multiple projects at once

uvx ruff@0.6.0 --version
uv tool install ruff==0.5.0
default tool directory ~/.local/share/uv/tools
uv tool dir
uvx --isolated ruff --version
uv tool install black
uv tool upgrade black --reinstall

uv venv --python 3.8
uv sync refresh
uv sync --refresh-package flask


https://docs.astral.sh/uv/reference/cli/

~/.config/uv/uv.toml

echo "MY_VAR='Hello, world'" > .envs
uv run --env-file .envs -- python -c 'import os; print(os.getenv("MY_VAR"))'

#Configuring the pip interface
[tool.uv.pip]
index-url = "https://test.pypi.org/simple"

https://docs.astral.sh/uv/configuration/environment/#environment-variables
Pakcage indexes
# On the command line.
$ uv lock --index pytorch=https://download.pytorch.org/whl/cpu
# Via an environment variable.
$ UV_INDEX=pytorch=https://download.pytorch.org/whl/cpu uv lock


use => uv venv
uv pip install --system
uv pip install --python /path/to/python
uv pip sync => will look for activated virtual env, conda and then .venv

https://docs.astral.sh/uv/pip/packages/#managing-packages
uv pip install flask ruff
uv pip install -e "ruff @ ./project/ruff"
uv pip install -e .
uv pip install -r requirements.txt
uv pip install -r pyproject.toml
uv pip install -r pyproject.toml --extra foo
uv pip install -r pyproject.toml --all-extras
Lock pip==24.0
#override with txt file
uv pip compile pyproject.toml requirements-dev.in -o requirements-dev.txt
uv pip compile pyproject.toml --extra foo =>Lock optional dependencies

uv publish
uv add "numpy; python_version >= '3.11'"

uv run python -c "import uv"
uv run python -c "import uvx"
--no-install-project


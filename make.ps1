<#
.SYNOPSIS
Testing using PowerShell to replace my Makefile

.DESCRIPTION
USAGE
    .\make.ps1 <command>

COMMANDS
    init              install Python build tools
    install           install local package in production mode
    install-dev       install local package in editable mode
    lint              run `isort` and `black`
    pylint            run `pylint`
    test              run `pytest`
    build-dist        run `python -m build`
    clean             delete generated content
    help, -?          show this help message
#>
param(
    [Parameter(Position = 0)]
    [ValidateSet("up", "down", "build", "test", "ip", "help")]
# The command to run
    [string]$Command
)

function Command-Help
{
    Get-Help $PSCommandPath
}
function Command-Init
{
    python -m pip install --upgrade pip wheel setuptools build
}
function Command-Install
{
    python -m pip install --upgrade .
}
function Command-Install-Dev
{
    python -m pip install --upgrade --editable ".[dev, tests, docs]"
}
function Command-Lint
{
    python -m isort src/
    python -m black src/
}
function Command-Pylint
{
    python -m pylint src/
}
function Command-Test
{
    python -m pytest
}
function Command-Build-Dist
{
    python -m pip install --upgrade build
    python -m build
}
function Command-Clean
{
    find . -name '*.pyc' -exec rm -f { } +
    find . -name '*.pyo' -exec rm -f { } +
    find . -name '__pycache__' -exec rm -rf { } +
    find . -name '.mypy_cache' -exec rm -rf { } +
    Remove-Item -rf .tox
    Remove-Item -f coverage.xml
    Remove-Item -f coverage.json
    Remove-Item -rf htmlcov
    Remove-Item -rf .coverage
    Remove-Item -rf .coverage.*
    find . -name '.pytest_cache' -exec rm -rf { } +
    Remove-Item -rf dist
    Remove-Item -rf build
}

if (!$Command)
{
    Command-Init
    Command-Install-Dev
    exit
}

switch ($Command)
{
    "init"    {
        Command-Init
    }
    "install"  {
        Command-Install
    }
    "install-dev" {
        Command-Install-Dev
    }
    "lint"  {
        Command-Lint
    }
    "pylint"    {
        Command-Pylint
    }
    "test"    {
        Command-Test
    }
    "build-dist"    {
        Command-Build-Dist
    }
    "clean"    {
        Command-Clean
    }
    "help"  {
        Command-Help
    }
}

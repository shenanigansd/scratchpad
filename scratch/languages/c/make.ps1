<#
.SYNOPSIS
Make script for C

.DESCRIPTION
USAGE
    .\make.ps1 <command>

COMMANDS
    build      run cmake
    clean      delete generated content
    help, -?   show this help message
#>

    [cmdletbinding()]
param(
    [Parameter(Position = 0)]
    [ValidateSet("build", "clean", "help")]
    [string]$Command
)

function Invoke-Build
{
    $path = "build"
    if (!(Test-Path -PathType Container -Path $path))
    {
        New-Item -ItemType Directory -Path $path | Out-Null
        Write-Verbose "created directory at $path"
    }
    else
    {
        Write-Verbose "using existing directory at $path"
    }
    Set-Location -Path build
    cmake ..
    cmake --build .
}

function Invoke-Clean
{
    $folders = @("build")
    foreach ($folder in $folders)
    {
        if (Test-Path $folder)
        {

            Write-Verbose "Deleting $folder"
            Remove-Item $folder -Recurse -Force
        }
    }
}

function Invoke-Help
{
    Get-Help $PSCommandPath
}

switch ($Command)
{
    "build"    {
        Invoke-Build
    }
    "clean"    {
        Invoke-Clean
    }
    "help"  {
        Invoke-Help
    }
    default
    {
        Invoke-Build
    }
}

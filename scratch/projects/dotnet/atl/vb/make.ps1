<#
.SYNOPSIS
Make script for VB

.DESCRIPTION
USAGE
    .\make.ps1 <command>

COMMANDS
    build      run `dotnet build`
    run        run `dotnet run`
    clean      delete generated content
    help, -?   show this help message
#>

    [cmdletbinding()]
param(
    [Parameter(Position = 0)]
    [ValidateSet("build", "run", "clean", "help")]
    [string]$Command
)

function Invoke-Build
{
    dotnet build
}

function Invoke-Run
{
    dotnet run
}

function Invoke-Clean
{
    $folders = @("bin", "obj")
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
    "run"    {
        Invoke-Run
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

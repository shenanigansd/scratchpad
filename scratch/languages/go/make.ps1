<#
.SYNOPSIS
Make script for Go

.DESCRIPTION
USAGE
    .\make.ps1 <command>

COMMANDS
    build      run `go build`
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
    go build
}

function Invoke-Clean
{
    $folders = @("goscratch")
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

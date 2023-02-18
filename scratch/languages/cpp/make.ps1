<#
.SYNOPSIS
Run CMake

.DESCRIPTION
USAGE
    .\make.ps1
#>

    [cmdletbinding()]
Param()

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

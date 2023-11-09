try {
    New-ItemProperty -LiteralPath 'HKCU:\Control Panel\Desktop' -Name 'PaintDesktopVersion' -Value 1 -PropertyType DWord -Force -ErrorAction Stop
    Write-Host "PaintDesktopVersion registry key set"
    exit 0
}
catch {
    $errMsg = _.Exception.Message
    Write-Host $errMsg
    exit 1
}

try {        
    if ( (Get-ItemPropertyValue -LiteralPath 'HKCU:\Control Panel\Desktop' -Name 'PaintDesktopVersion' -ErrorAction Stop ) -eq 0 ) {
        Write-Host "PaintDesktopVersion registry key already exists"
        exit 0
    }
    else {
        Write-Host "PaintDesktopVersion registry key doesn't exist"
        exit 1
    }
}
catch {
    $errMsg = _.Exception.Message
    Write-Host $errMsg
    exit 1
}

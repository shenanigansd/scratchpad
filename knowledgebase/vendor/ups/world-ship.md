# UPS World Ship

UPS' shipping software

## "Import key" window spawns off-screen

If the import key window does not appear, delete the `keyedImportWindowLocation` line
from `C:\ProgramData\UPS\WSTD\wstdShipuser.ini`

## Gotchas

> **Warning**
> UPS will strip the leading zeros off of postal codes in non-quoted CSVs.

# UPS World Ship

UPS' shipping software

## "Import key" window spawns off-screen

If the import key window does not appear, delete the `keyedImportWindowLocation` line
from `C:\ProgramData\UPS\WSTD\wstdShipuser.ini`

## Gotchas

> **Warning**
> World Ship will mangle data in non-quoted CSVs. Examples include removing the leading zeros from postal codes and converting the reference `134.609506.647380.000` to `134.6095`.

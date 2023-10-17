Get-ADComputer -Filter * -Property * | Export-CSV computers.csv -Encoding UTF8

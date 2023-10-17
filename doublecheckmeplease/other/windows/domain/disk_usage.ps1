 foreach ($computer in (Get-ADComputer -filter *).Name) {
	Invoke-Command -ComputerName $computer {Get-PSDrive | Where {$_.Free -gt 0}}
}

#!/usr/bin/env pwsh
<#
So, this script -
- Connects to MS Graph
- Finds the specified user ($FilterUser) by display name
- Finds the specified folder ($FilterFolder) in the users mailbox
- Starts a loop that runs forever that...
    - Gets the current time and subtracts 16 minutes.
    - Gets all messages received after the above time that have attachments and have a subject that starts with $FilterSubject
    - Loops through each message and saves the attachment as ${OutputPath}${timestamp} ${phone} - ${account}.wav"
        - $OutputPath is defined by you
        - $timestamp is the time the email was received formatted as "yyyy-mm-dd HHmm"
        - $phone is the subject with $FilterSubject removed
        - $account is the from email address with $FilterDomain removed
    - Sleeps for 900 seconds (15 minutes)
#>

# The User.Read scope is required to query the list of users to find the current user's ID.
# TODO: Is there a way to query the logged in user's ID directly?
Connect-MgGraph -Scopes "User.Read", "Mail.Read"

$FilterUser = "Mina Sanchez"
$FilterFolder = "Inbox"
$FilterSubject = "New voicemail from +"
$FilterDomain = "@SanchezConsulting.com"
$OutputPath = "C:\Users\MinaSanchez\Downloads\"

$user = Get-MgUser -Filter "displayName eq '${FilterUser}'"
Write-Host "Fetched user:" $user.DisplayName

$folder = Get-MgUserMailFolder -UserId $user.Id -Filter "DisplayName eq '${FilterFolder}'"
Write-Host "Fetched folder:" $folder.DisplayName

while ($true) {
    $FilterTime = (Get-Date).AddMinutes(-16).ToString("yyyy-MM-ddTHH:mm:ss.fffK")
    Write-Host "Using FilterTime:" $FilterTime

    $messages = @(Get-MgUserMailFolderMessage -UserId $user.Id -MailFolderId $folder.Id -Filter "ReceivedDateTime ge ${FilterTime} and HasAttachments eq true and startswith(Subject, '${FilterSubject}')")
    foreach ($message in $messages) {
        Write-Host "Processing message with subject:" $message.Subject
        $attachments = @(Get-MgUserMailFolderMessageAttachment -UserId $user.Id -MailFolderId $folder.Id -MessageId $message.Id)
        foreach ($attachment in $attachments) {
            $timestamp = $message.CreatedDateTime.ToString("yyyy-mm-dd HHmm")
            $phone = $message.Subject -replace $FilterSubject
            $account = $message.From.EmailAddress.Address -replace $FilterDomain
            $filepath = "${OutputPath}${timestamp} ${phone} - ${account}.wav"
            Write-Host "Writing file:" $filepath
            Set-Content -Path $filepath -Value ([Convert]::FromBase64String($attachment.AdditionalProperties.contentBytes)) -AsByteStream
        }
    }
    Write-Host "Sleeping..."
    Start-Sleep -Seconds 900 # 15 Minutes
}

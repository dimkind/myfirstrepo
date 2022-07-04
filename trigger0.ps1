$Trigger= New-ScheduledTaskTrigger -At 10:00am -Daily
$User= "NT AUTHORITY\SYSTEM"
$Action= New-ScheduledTaskAction -Execute "C:\Users\ddimkin\AppData\Local\Programs\Python\Python38\python.exe" -Argument "timetest0.py" -WorkingDirectory "C:\Users\ddimkin\Documents\GitHub\myfirstrepo\"
Register-ScheduledTask -TaskName "AppLog" -Trigger $Trigger -User $User -Action $Action -RunLevel Highest

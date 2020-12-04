# Please Use Windows powershell ,Not cmd
# Usage: Replace some dir's .txt file name and context 
# TODO: pay attention to the file extension

$CurrentDate = "20201128"
$ExpectedDate = "20201129"
$FolderLocation = "C:\Users\ruqin\Desktop\test-workspace"


echo "Show current localtion ....."

echo ">>>> Step1. Change file name..." ; sleep 3
cd $FolderLocation ; ls 

ls *.txt | Rename-Item -NewName {$_.name -replace $CurrentDate, $ExpectedDate}

echo ">>>>> Step2. Replace context in file..." ; sleep 3
$files = Get-ChildItem -Path $FolderLocation  -Recurse 

foreach ($file in $files){
$content = Get-Content $($file.FullName) -Raw
#write replaced content back to the file
$content -replace $CurrentDate,$ExpectedDate | Out-File $($file.FullName) 
}

echo ">>>>>> Congratulations ! <<<<<<"

sleep 5

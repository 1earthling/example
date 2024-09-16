osascript -e '
tell application "Notes"
    set theFolder to (POSIX path of (path to desktop folder)) & "ExportedNotes/"
    set theAccounts to every account
    repeat with theAccount in theAccounts
        set theFolders to folders of theAccount
        repeat with theFolderItem in theFolders
            set theNotes to notes of theFolderItem
            repeat with theNote in theNotes
                set noteTitle to the name of theNote
                set noteContent to the body of theNote
                set filePath to theFolder & (noteTitle as string) & ".txt"
                do shell script "echo " & quoted form of noteContent & " > " & quoted form of filePath
            end repeat
        end repeat
    end repeat
end tell'

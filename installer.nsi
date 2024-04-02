Outfile "PasswordGeneratorInstaller.exe"
Caption "Password Generator Installer"
BrandingText "Developed by Sathsara Karunarathne"
XPStyle on
SetCompressor /SOLID lzma  ; Compression settings
RequestExecutionLevel admin  ; Request administrative privileges

InstallDir $PROGRAMFILES\PasswordGenerator

Page directory
Page instfiles

Section "Install"
    SetOutPath $INSTDIR
    File /r "E:\My Software Projects\Password_Generation_Python\pythonProject\build\exe.win-amd64-3.11\*.*"
    CreateDirectory $SMPROGRAMS\PasswordGenerator
    CreateShortCut "$SMPROGRAMS\PasswordGenerator\Password Generator.lnk" "$INSTDIR\main.exe"
    CreateShortCut "$DESKTOP\Password Generator.lnk" "$INSTDIR\main.exe"
    WriteUninstaller "$INSTDIR\Uninstall.exe"
SectionEnd

Section "Uninstall"
    Delete "$INSTDIR\main.exe"
    RMDir /r $INSTDIR
    Delete "$SMPROGRAMS\PasswordGenerator\Password Generator.lnk"
    RMDir $SMPROGRAMS\PasswordGenerator
    Delete "$DESKTOP\Password Generator.lnk"
SectionEnd

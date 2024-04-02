Outfile "PGI.exe"
Caption "Password Generator Installer"
BrandingText "Developed by Sathsara Karunarathne"
XPStyle on
RequestExecutionLevel admin
InstallDir $PROGRAMFILES\PasswordGenerator

; Load the Modern UI
!include MUI2.nsh

; Set the title and subtitle
!define MUI_HEADERIMAGE
!define MUI_HEADERIMAGE_BITMAP "header.bmp" ; specify path to bitmap
!define MUI_HEADERIMAGE_RIGHT
!define MUI_HEADERIMAGE_TEXT "Password Generator Installer"
!define MUI_HEADER_SUBTEXT "Developed by Sathsara Karunarathne"

; Set the logo
!define MUI_ICON "app_icon.ico" ; Set the path to  .ico file

; Start the installer pages
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

; Start the uninstaller pages
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES

; Set the language
!insertmacro MUI_LANGUAGE "English"

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

; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Registration application"
#define MyAppVersion "0.1b"
#define MyAppPublisher "denbingon"
#define MyAppURL "https://denbingon.com/"
#define MyAppExeName "MyProg.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{32F78088-A00F-4F6E-AF93-2B757D2C303D}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName=C:\Users\denbingon\AppData\Roaming\reg_app
DefaultGroupName={#MyAppName}
OutputDir=C:\Users\denbingon\Desktop\����� ����� (2)
OutputBaseFilename=setup
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "russian"; MessagesFile: "compiler:Languages\Russian.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Program Files (x86)\Inno Setup 5\Examples\MyProg.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\denbingon\Desktop\python\dist\pass\_bz2.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\denbingon\Desktop\python\dist\pass\_hashlib.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\denbingon\Desktop\python\dist\pass\_lzma.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\denbingon\Desktop\python\dist\pass\_socket.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\denbingon\Desktop\python\dist\pass\_ssl.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\denbingon\Desktop\python\dist\pass\base_library.zip"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\denbingon\Desktop\python\dist\pass\pass.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\denbingon\Desktop\python\dist\pass\pass.exe.manifest"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\denbingon\Desktop\python\dist\pass\pyexpat.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\denbingon\Desktop\python\dist\pass\python36.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\denbingon\Desktop\python\dist\pass\select.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\denbingon\Desktop\python\dist\pass\unicodedata.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\denbingon\Desktop\python\dist\pass\VCRUNTIME140.dll"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent


@echo off
setlocal EnableExtensions EnableDelayedExpansion

set "REPO_ROOT=%~dp0"
if "%REPO_ROOT:~-1%"=="\" set "REPO_ROOT=%REPO_ROOT:~0,-1%"

if defined AGENTS_SKILLS_DIR (
  set "TARGET_ROOT=%AGENTS_SKILLS_DIR%"
) else (
  set "TARGET_ROOT=%USERPROFILE%\.agents\skills"
)

if not exist "%TARGET_ROOT%" mkdir "%TARGET_ROOT%"
set "BACKUP_ROOT=%TARGET_ROOT%\.backup"

set "RAW_DATE=%date:/=-%"
set "RAW_DATE=%RAW_DATE: =0%"
set "RAW_TIME=%time: =0%"
set "RAW_TIME=%RAW_TIME::=-%"
set "RAW_TIME=%RAW_TIME:.=-%"
set "TIMESTAMP=%RAW_DATE%_%RAW_TIME%"

set /a CREATED=0
set /a UPDATED=0
set /a SKIPPED=0

echo Syncing skills to: %TARGET_ROOT%

for /d %%D in ("%REPO_ROOT%\*") do (
  set "SKILL_DIR=%%~fD"
  set "SKILL_NAME=%%~nxD"

  if /i not "!SKILL_NAME!"==".git" if /i not "!SKILL_NAME!"==".agents" if /i not "!SKILL_NAME!"==".codex" if /i not "!SKILL_NAME!"==".codegraph" if /i not "!SKILL_NAME!"=="scripts" if exist "!SKILL_DIR!\SKILL.md" (
    set "TARGET_DIR=%TARGET_ROOT%\!SKILL_NAME!"

    if not exist "!TARGET_DIR!\" (
      call :copy_skill "!SKILL_DIR!" "!TARGET_DIR!"
      if errorlevel 8 exit /b !errorlevel!
      echo [create] !SKILL_NAME!
      set /a CREATED+=1
    ) else (
      robocopy "!SKILL_DIR!" "!TARGET_DIR!" /MIR /L /NJH /NJS /NFL /NDL >nul
      set "RC=!errorlevel!"

      if !RC! GEQ 8 exit /b !RC!

      if !RC! EQU 0 (
        echo [skip]   !SKILL_NAME! ^(already up to date^)
        set /a SKIPPED+=1
      ) else (
        set "BACKUP_DIR=%BACKUP_ROOT%\%TIMESTAMP%\!SKILL_NAME!"
        if not exist "%BACKUP_ROOT%\%TIMESTAMP%" mkdir "%BACKUP_ROOT%\%TIMESTAMP%"
        move "!TARGET_DIR!" "!BACKUP_DIR!" >nul
        if errorlevel 1 exit /b 1

        call :copy_skill "!SKILL_DIR!" "!TARGET_DIR!"
        if errorlevel 8 exit /b !errorlevel!

        echo [update] !SKILL_NAME! ^(backup: !BACKUP_DIR!^)
        set /a UPDATED+=1
      )
    )
  )
)

echo.
echo Done. created=%CREATED% updated=%UPDATED% skipped=%SKIPPED%
exit /b 0

:copy_skill
set "SOURCE_DIR=%~1"
set "DEST_DIR=%~2"

if not exist "%DEST_DIR%" mkdir "%DEST_DIR%"
robocopy "%SOURCE_DIR%" "%DEST_DIR%" /E /COPY:DAT /R:1 /W:1 /NFL /NDL /NJH /NJS >nul
exit /b %errorlevel%

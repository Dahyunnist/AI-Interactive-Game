@echo off
setlocal enabledelayedexpansion

for %%f in (*.mp3) do (
    echo 处理 %%f...
    ffmpeg -i "%%f" -filter:a "volume=3dB" -c:a libmp3lame -b:a 128k "%%~nf_temp.mp3"
    move /Y "%%~nf_temp.mp3" "%%f"
)

echo 所有文件处理完成！
pause
1. 播放视频
   1. 安装`ffmpeg`：下载FFmpeg Windows版（在[官网](https://ffmpeg.org/download.html#build-windows)选择“Windows builds by BtbN，或直接点击[此处](https://github.com/BtbN/FFmpeg-Builds/releases)”）下的最新版，如`ffmpeg-master-latest-win64-gpl.zip`，解压后将bin文件地址添加到系统Path环境变量中，并通过`ffmpeg -version`命令加以验证
   2. 在视频所在位置打开powershell，运行以下命令，将视频转换为RenPy可支持播放的webm格式(VP8视频+Vorbis音频)：
    ```
    ffmpeg -i irene.mp4 -c:v libvpx -b:v 1M -c:a libvorbis irene.webm
    ```
2. 将MP4文件转换为CosyVoice可用于训练的16khz采样音频：
   ```
   ffmpeg -i zhy2.mp4 -ar 16000 -ac 1 zhy2.wav
   ```
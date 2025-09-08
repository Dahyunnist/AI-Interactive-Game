# 已审讯过的嫌疑人
$ interrogated_suspects = []

# 功能：播放动画时渐次展示旁白
default narration_queue = []
default current_narration = ""

# 使用label的形式定义动画旁白播放函数，通过call调用
label play_animated_narration(video_path, character):
    # 显示视频
    show expression Movie(
        play = video_path,
        size = (config.screen_width, config.screen_height),
    ) as video_player
    # 使用角色对话系统显示旁白
    python:
        for text in narration_queue:
            character(text, interact=False)
            renpy.pause(len(text)/20.0 + 5)  # 句间间隔5秒
    # 清理
    hide video_player
    return
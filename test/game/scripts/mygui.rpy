# 对话框设置

init python:
    a, b = Image("images/dialog_background.jpg").load().get_size()

image dialog_background:
    "images/dialog_background.jpg"
    xsize 1920
    ysize int(1920.0 * b / a)
    alpha 1.0

style window:
    background Frame("dialog_background")

    xalign 0.5
    yalign 1.0

## 对话和菜单选择文本使用的颜色。
define gui.text_color = '#000000'
define gui.interface_text_color = '#ffffff'

# 选项文本设置
define gui.choice_button_text_size = 36
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#666666'
define gui.choice_button_text_hover_color = "#000000"
define gui.choice_button_text_insensitive_color = '#999999'

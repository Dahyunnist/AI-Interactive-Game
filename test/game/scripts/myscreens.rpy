# 主页面
# myscreens.rpy
image mm_button1:
    "gui/button/main_menu_buttons1.png"
    zoom(0.7)

image mm_button2:
    "gui/button/main_menu_buttons2.png"
    zoom(0.7)

image mm_button3:
    "gui/button/main_menu_buttons3.png"
    zoom(0.7)

image mm_button4:
    "gui/button/main_menu_buttons4.png"
    zoom(0.7)

image mm_button5:
    "gui/button/main_menu_buttons5.png"
    zoom(0.7)

image mm_button6:
    "gui/button/main_menu_buttons6.png"
    zoom(0.7)

image Calgary_Ham_complete:
    "images/Calgary_Ham_complete.png"
    size(650,700)

screen main_menu():
    # 确保替换掉任何其他菜单屏幕
    tag menu
    
    # 添加背景（可以使用原版背景或自定义背景）
    add gui.main_menu_background

    # 创建网格容器，两行三列
    grid 2 3:  # 3列2行
        # 将网格放置在屏幕中下方
        xalign 0.8
        ypos 0.15  # 从屏幕顶部60%的位置开始
        spacing 120  # 按钮间距
        
        # 第一行
        # 开始游戏
        imagebutton:
            idle Transform("mm_button1", matrixcolor=BrightnessMatrix(0.0))
            hover Transform("mm_button1", matrixcolor=BrightnessMatrix(-0.1))
            action Start()
        
        # 读取游戏
        imagebutton:
            idle Transform("mm_button2", matrixcolor=BrightnessMatrix(0.0))
            hover Transform("mm_button2", matrixcolor=BrightnessMatrix(-0.1))
            action ShowMenu("load")
        
        # 设置
        imagebutton:
            idle Transform("mm_button3", matrixcolor=BrightnessMatrix(0.0))
            hover Transform("mm_button3", matrixcolor=BrightnessMatrix(-0.1))
            action ShowMenu("preferences")
        
        # 第二行
        # 关于
        imagebutton:
            idle Transform("mm_button4", matrixcolor=BrightnessMatrix(0.0))
            hover Transform("mm_button4", matrixcolor=BrightnessMatrix(-0.1))
            action ShowMenu("about")
        
        # 帮助
        imagebutton:
            idle Transform("mm_button5", matrixcolor=BrightnessMatrix(0.0))
            hover Transform("mm_button5", matrixcolor=BrightnessMatrix(-0.1))
            action ShowMenu("help")
        
        # 退出
        imagebutton:
            idle Transform("mm_button6", matrixcolor=BrightnessMatrix(0.0))
            hover Transform("mm_button6", matrixcolor=BrightnessMatrix(-0.1))
            action Quit(confirm=False)
    
    fixed:
        add "Calgary_Ham_complete" align (0, 1.01)

# 选项页面效果设置
image choice_background:
    "choice_background.png"
    size(1185, 80)
style choice_button:
    properties gui.button_properties("choice_button")
    background "choice_background"

# 审讯过程中右上角的"返回主菜单"按钮
image button1:
    "button1.png"
    zoom(0.2)

screen interrogation_controls():
    frame:
        xalign 0.99
        yalign 0
        background None
        vbox:
            imagebutton:
                idle Transform("button1", zoom=1/1.01, matrixcolor=BrightnessMatrix(0.0))
                # 悬停时放大并变亮
                hover Transform("button1", zoom=1.01, matrixcolor=BrightnessMatrix(0.1))
                action Jump("main_menu_1")
                xalign 0.5
                yalign 0.5

# 侦探的旧照片
screen clickable_calgary_image:
    add Solid("#00000080")

    imagebutton:
        idle Transform("Calgary_Ham_old.jpeg", zoom=1/1.01, matrixcolor=BrightnessMatrix(0.0))
        hover Transform("Calgary_Ham_old.jpeg", zoom=1.01, matrixcolor=BrightnessMatrix(0.1))
        xalign 0.5
        yalign 0.5
        action Jump("detective_background")
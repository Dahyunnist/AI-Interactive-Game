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

screen clickable_calgary_image:
    add Solid("#00000080")

    imagebutton:
        idle Transform("Calgary_Ham_old.jpeg", zoom=1/1.01, matrixcolor=BrightnessMatrix(0.0))
        hover Transform("Calgary_Ham_old.jpeg", zoom=1.01, matrixcolor=BrightnessMatrix(0.1))
        xalign 0.5
        yalign 0.5
        action Jump("detective_background")
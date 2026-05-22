# Local polish layer. Keep this separate from generated chapter flow.

label splashscreen:
    scene bg_main_menu at bg_cinematic
    show cinematic_vignette
    pause 0.4
    return

label show_chapter_card(title, subtitle):
    window hide
    scene black
    show screen chapter_card(title, subtitle)
    if persistent.access_reduced_motion:
        pause 2.35
    else:
        pause 3.35
    hide screen chapter_card
    window auto
    return

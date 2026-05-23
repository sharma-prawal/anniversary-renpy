# Custom premium screens for the anniversary VN.

default history_audit_entries = None
default history_page = 0
default audit_force_mobile_layout = False

screen cold_open_caption(line, prompt=None):
    $ mobile = audit_force_mobile_layout or renpy.variant("small") or renpy.variant("touch")
    zorder 120
    add "cinematic_vignette"
    frame:
        xalign 0.5
        yalign 0.84
        xysize ((1420, 150) if mobile else (1180, 130))
        background Frame("images/ui/prompt_panel.png", 28, 28)
        padding ((44, 26) if mobile else (38, 22))
        vbox:
            spacing (8 if mobile else 6)
            xalign 0.5
            yalign 0.5
            text line:
                size (36 if mobile else 32)
                color "#FFF8F2"
                text_align 0.5
                xalign 0.5
                xmaximum (1300 if mobile else 1060)
                outlines [ (1, "#12070CB8", 0, 2) ]
            if prompt:
                text prompt:
                    size (24 if mobile else 21)
                    color "#FFD8BB"
                    text_align 0.5
                    xalign 0.5
                    xmaximum (1100 if mobile else 920)

screen cold_open_title(eyebrow, title, subtitle):
    $ mobile = audit_force_mobile_layout or renpy.variant("small") or renpy.variant("touch")
    zorder 121
    add Solid("#050007")
    add "cinematic_vignette"
    frame:
        xalign 0.5
        yalign 0.5
        xysize ((1500, 440) if mobile else (1180, 360))
        background Frame("images/ui/chapter_panel.png", 34, 34)
        padding ((72, 54) if mobile else (62, 46))
        vbox:
            xalign 0.5
            yalign 0.5
            spacing (24 if mobile else 20)
            text eyebrow:
                size (30 if mobile else 24)
                color "#FFD8BB"
                bold True
                xalign 0.5
                text_align 0.5
                xmaximum (1320 if mobile else 1020)
            text title:
                size (68 if mobile else 58)
                color "#FFF8F2"
                xalign 0.5
                text_align 0.5
                xmaximum (1320 if mobile else 1020)
            add Solid("#FFD8BB") xysize ((760, 2) if mobile else (560, 2)) xalign 0.5
            text subtitle:
                size (32 if mobile else 27)
                color "#FFE9D8"
                xalign 0.5
                text_align 0.5
                xmaximum (1260 if mobile else 920)

screen signature_peak_caption(kicker, line):
    $ mobile = audit_force_mobile_layout or renpy.variant("small") or renpy.variant("touch")
    zorder 123
    add "cinematic_vignette"
    frame at signature_peak_reveal:
        xalign 0.5
        yalign (0.20 if mobile else 0.18)
        xysize ((1460, 220) if mobile else (1120, 184))
        background Frame("images/ui/chapter_panel.png", 34, 34)
        padding ((52, 34) if mobile else (48, 30))
        vbox:
            spacing (14 if mobile else 12)
            xalign 0.5
            yalign 0.5
            text kicker:
                size (28 if mobile else 24)
                color "#FFD8BB"
                bold True
                xalign 0.5
                text_align 0.5
            add Solid("#FFD7A666"):
                xalign 0.5
                xysize ((540, 2) if mobile else (420, 2))
            text line:
                size (38 if mobile else 32)
                color "#FFF8F2"
                xalign 0.5
                text_align 0.5
                xmaximum (1280 if mobile else 980)
                line_spacing 4

screen say(who, what):
    $ mobile = audit_force_mobile_layout or renpy.variant("small") or renpy.variant("touch")
    $ access_large = bool(persistent.access_large_text)
    $ access_high = bool(persistent.access_high_contrast)
    $ is_cinematic = bool(cinematic_mode)
    $ say_window_height = (360 if access_large else 310) if mobile else (310 if access_large else 260)
    $ say_box_size = ((1760, 320) if access_large else (1760, 266)) if mobile else ((1620, 258) if access_large else (1620, 210))
    $ say_panel_size = ((1760, 314) if access_large else (1760, 260)) if mobile else ((1620, 252) if access_large else (1620, 204))
    $ who_text_size = (40 if access_large else 34) if mobile else (35 if access_large else 28)
    $ what_text_size = (40 if access_large else 34) if mobile else (35 if access_large else 29)
    $ what_y = ((118 if who else 78) if access_large else (108 if who else 72)) if mobile else ((102 if who else 74) if access_large else (88 if who else 68))

    if is_cinematic:
        $ cine_height = (190 if access_large else 164) if mobile else (158 if access_large else 136)
        $ cine_text_size = (38 if access_large else 33) if mobile else (32 if access_large else 27)
        $ cine_name_size = (27 if access_large else 23) if mobile else (22 if access_large else 19)

        add Solid("#050007CA"):
            xalign 0.5
            yalign 1.0
            xysize (1920, cine_height)

        text "▷":
            xalign 0.965
            yalign 0.984
            size (26 if mobile else 22)
            color "#FFD8BB"
            at cinematic_continue_pulse

        window:
            id "window"
            xalign 0.5
            yalign 1.0
            xsize config.screen_width
            ysize cine_height
            background None

            fixed:
                xalign 0.5
                yalign 0.5
                xysize (config.screen_width, cine_height)

                vbox:
                    xalign 0.5
                    yalign 0.5
                    spacing (5 if mobile else 4)
                    xsize (1760 if mobile else 1640)

                    if who:
                        text who id "who":
                            xalign 0.5
                            text_align 0.5
                            size cine_name_size
                            color ("#FFE9B8" if access_high else "#FFD8BBA8")
                            bold True

                    text what id "what":
                        xalign 0.5
                        text_align 0.5
                        size cine_text_size
                        color "#FFF8F2"
                        line_spacing ((8 if mobile else 6) if access_large else 4)
                        outlines ([(1, "#000000E8", 0, 1)] if access_high else [(1, "#05000780", 0, 1)])

    else:
        add "cinematic_vignette"
        if access_high:
            add Solid("#00000044")
        use quick_menu

        window:
            id "window"
            xalign 0.5
            yalign 1.0
            xsize config.screen_width
            ysize say_window_height
            background None

            fixed:
                xalign 0.5
                yalign 0.5
                xysize say_box_size

                add Frame("images/ui/dialogue_panel.png", 34, 34):
                    xalign 0.5
                    yalign 0.5
                    xysize say_panel_size

                if access_high:
                    add Solid("#050007CC"):
                        xalign 0.5
                        yalign 0.5
                        xysize say_panel_size

                if who:
                    text who id "who":
                        xpos (76 if mobile else 82)
                        ypos (24 if access_large else (28 if mobile else 30))
                        size who_text_size
                        color ("#FFE9B8" if access_high else "#FFD8BB")
                        bold True
                        outlines [ (2 if access_high else 1, "#000000E8" if access_high else "#2A141DD0", 0, 1) ]

                    add Solid("#FFD7A666"):
                        xpos (76 if mobile else 82)
                        ypos ((84 if access_large else 78) if mobile else (82 if access_large else 70))
                        xysize ((360, 2) if mobile else (280, 2))

                text what id "what":
                    xpos (76 if mobile else 82)
                    ypos what_y
                    xmaximum (1610 if mobile else 1450)
                    size what_text_size
                    color "#FFF8F2"
                    line_spacing ((8 if mobile else 7) if access_large else (5 if mobile else 3))
                    outlines ([ (1, "#000000E8", 0, 1) ] if access_high else [])

screen premium_button(label, action, sensitive=True):
    $ mobile = audit_force_mobile_layout or renpy.variant("small") or renpy.variant("touch")
    $ access_large = bool(persistent.access_large_text)
    textbutton label:
        action action
        sensitive sensitive
        xalign 0.5
        xysize ((690, 84) if access_large and mobile else (650, 78) if mobile else (548, 72) if access_large else (520, 66))
        background Frame("images/ui/button_idle.png", 22, 22)
        hover_background Frame("images/ui/button_hover.png", 22, 22)
        insensitive_background Frame("images/ui/button_idle.png", 22, 22)
        text_size ((34 if mobile else 29) if access_large else (31 if mobile else 27))
        text_color "#FFF8F2"
        text_hover_color "#FFF8F2"
        text_insensitive_color "#9C8B8F"
        text_xalign 0.5
        text_yalign 0.5

screen compact_button(label, action):
    $ mobile = audit_force_mobile_layout or renpy.variant("small") or renpy.variant("touch")
    $ access_large = bool(persistent.access_large_text)
    textbutton label:
        action action
        xysize ((360, 72) if access_large and mobile else (360, 68) if mobile else (316, 58) if access_large else (300, 54))
        background Frame("images/ui/button_idle.png", 22, 22)
        hover_background Frame("images/ui/button_hover.png", 22, 22)
        text_size ((28 if mobile else 24) if access_large else (26 if mobile else 22))
        text_color "#FFF8F2"
        text_hover_color "#FFF8F2"
        text_xalign 0.5
        text_yalign 0.5

screen voice_action_button(label, action):
    $ mobile = audit_force_mobile_layout or renpy.variant("small") or renpy.variant("touch")
    textbutton label:
        action action
        xysize ((200, 52) if mobile else (190, 44))
        background Frame("images/ui/button_idle.png", 18, 18)
        hover_background Frame("images/ui/button_hover.png", 18, 18)
        text_size (20 if mobile else 17)
        text_color "#FFF8F2"
        text_hover_color "#FFF8F2"
        text_xalign 0.5
        text_yalign 0.5

screen accessibility_toggle_button(label, field_name):
    $ mobile = audit_force_mobile_layout or renpy.variant("small") or renpy.variant("touch")
    $ access_large = bool(persistent.access_large_text)
    $ selected = bool(getattr(persistent, field_name))
    textbutton label:
        action ToggleField(persistent, field_name)
        xysize ((360, 72) if access_large and mobile else (360, 68) if mobile else (316, 58) if access_large else (300, 54))
        background Frame("images/ui/chapter_panel.png" if selected else "images/ui/button_idle.png", 22, 22)
        hover_background Frame("images/ui/button_hover.png", 22, 22)
        text_size ((28 if mobile else 24) if access_large else (26 if mobile else 22))
        text_color ("#FFE9B8" if selected else "#FFF8F2")
        text_hover_color "#FFF8F2"
        text_xalign 0.5
        text_yalign 0.5

screen voice_character_control(label, tag, sample, control_width=190):
    $ mobile = audit_force_mobile_layout or renpy.variant("small") or renpy.variant("touch")
    $ access_large = bool(persistent.access_large_text)
    $ button_size = (88, 42) if mobile else (82, 36)
    vbox:
        spacing 6
        xsize control_width
        text label size ((23 if mobile else 20) if access_large else (21 if mobile else 18)) color "#FFF8F2"
        bar value SetCharacterVolume(tag):
            xysize (control_width, 18 if mobile else 14)
            left_bar Solid("#FFD7A6")
            right_bar Solid("#2A141D")
            thumb Solid("#FFF8F2")
        hbox:
            spacing 6
            textbutton "Test":
                action PlayCharacterVoice(tag, sample)
                xysize button_size
                background Frame("images/ui/button_idle.png", 18, 18)
                hover_background Frame("images/ui/button_hover.png", 18, 18)
                text_size (19 if mobile else 16)
                text_color "#FFF8F2"
                text_hover_color "#FFF8F2"
                text_xalign 0.5
                text_yalign 0.5
            textbutton "Mute":
                action ToggleVoiceMute(tag)
                xysize button_size
                background Frame("images/ui/button_idle.png", 18, 18)
                hover_background Frame("images/ui/button_hover.png", 18, 18)
                text_size (19 if mobile else 16)
                text_color "#FFF8F2"
                text_hover_color "#FFF8F2"
                text_xalign 0.5
                text_yalign 0.5

screen quick_menu_button(label, action):
    $ mobile = audit_force_mobile_layout or renpy.variant("small") or renpy.variant("touch")
    $ access_large = bool(persistent.access_large_text)
    textbutton label:
        action action
        xysize ((224, 62) if access_large and mobile else (210, 58) if mobile else (144, 48) if access_large else (132, 44))
        background Frame("images/ui/button_idle.png", 22, 22)
        hover_background Frame("images/ui/button_hover.png", 22, 22)
        text_size ((23 if mobile else 19) if access_large else (22 if mobile else 18))
        text_color "#FFF8F2"
        text_hover_color "#FFF8F2"
        text_xalign 0.5
        text_yalign 0.5

screen quick_menu():
    $ mobile = audit_force_mobile_layout or renpy.variant("small") or renpy.variant("touch")
    zorder 80

    if mobile:
        grid 4 2:
            xalign 0.5
            yalign 0.045
            spacing 10
            use quick_menu_button("Back", Rollback())
            use quick_menu_button("Save", ShowMenu("save"))
            use quick_menu_button("Load", ShowMenu("load"))
            use quick_menu_button("History", [SetVariable("history_page", 0), ShowMenu("history")])
            use quick_menu_button("Auto", Preference("auto-forward", "toggle"))
            use quick_menu_button("Skip", Skip())
            use quick_menu_button("Settings", ShowMenu("preferences"))
            use quick_menu_button("Menu", MainMenu())
    else:
        hbox:
            xalign 0.5
            yalign 0.025
            spacing 10

            use quick_menu_button("Back", Rollback())
            use quick_menu_button("Save", ShowMenu("save"))
            use quick_menu_button("Load", ShowMenu("load"))
            use quick_menu_button("History", [SetVariable("history_page", 0), ShowMenu("history")])
            use quick_menu_button("Auto", Preference("auto-forward", "toggle"))
            use quick_menu_button("Skip", Skip())
            use quick_menu_button("Settings", ShowMenu("preferences"))
            use quick_menu_button("Menu", MainMenu())

screen brand_title_lockup(compact=False, align=0.0):
    $ mobile = audit_force_mobile_layout or renpy.variant("small") or renpy.variant("touch")
    $ title_size = (66 if mobile else 112) if compact else (84 if mobile else 126)
    $ subtitle_size = (22 if mobile else 24) if compact else (26 if mobile else 28)
    vbox:
        spacing (10 if mobile else 12)
        xalign align

        frame:
            xalign align
            background "#5A1226AA"
            padding ((20, 8) if mobile else (18, 7))
            text "ANNIVERSARY VISUAL NOVEL":
                size (17 if mobile and compact else 20 if mobile else 17)
                color "#FFE9B8"
                bold True
                xalign 0.5
                text_align 0.5

        hbox:
            spacing (18 if mobile else 20)
            xalign align
            yalign 0.5
            text "OUR":
                size (44 if mobile and compact else 52 if mobile else 72)
                color "#FFD8BB"
                bold True
                yalign 0.58
                outlines [ (2, "#140810D0", 0, 3) ]
            text "STORY":
                size title_size
                color "#FFF8F2"
                bold True
                yalign 0.5
                outlines [ (3, "#140810D8", 0, 4), (1, "#FFD7A688", 0, 0) ]

        hbox:
            spacing 16
            yalign 0.5
            xalign align
            add Solid("#FFD7A699") xysize ((160, 2) if mobile else (170, 2)) yalign 0.5
            frame:
                background "#140810B8"
                padding ((24, 8) if mobile else (22, 7))
                text "A LOVE QUEST":
                    size subtitle_size
                    color "#FFD8BB"
                    bold True
                    yalign 0.5
            add Solid("#FFD7A699") xysize ((150, 2) if mobile and compact else (160, 2) if mobile else (170, 2)) yalign 0.5

        if not compact:
            text "A cinematic anniversary VN about the click, the hoodie, and the promise.":
                size (23 if mobile else 21)
                color "#FFEDE1"
                xalign align
                text_align (0.5 if align == 0.5 else 0.0)
                xmaximum (1120 if mobile else 760)
                outlines [ (1, "#140810B8", 0, 2) ]

screen main_menu():
    $ mobile = audit_force_mobile_layout or renpy.variant("small") or renpy.variant("touch")
    $ reduce_motion = bool(persistent.access_reduced_motion)
    tag menu
    add "bg_main_menu" at menu_background_crop
    if not reduce_motion:
        add "menu_petal_layer" at menu_petal_drift_far
    add "cinematic_vignette"
    add Solid("#08020A58")
    if not reduce_motion:
        add "menu_petal_layer" at menu_petal_drift
    add "menu_foreground_depth" at menu_foreground_hold

    $ unlocked_chapters = unlocked_chapter_limit()
    $ can_continue = persistent.current_chapter > 1
    $ menu_title_transform = chapter_card_static if reduce_motion else menu_title_reveal
    $ menu_nav_transform = chapter_card_static if reduce_motion else menu_nav_reveal

    fixed:
        xysize (1920, 1080)

        vbox at menu_title_transform:
            xpos (400 if mobile else 150)
            ypos (34 if mobile else 136)
            xsize (1120 if mobile else 850)
            spacing (10 if mobile else 20)

            use brand_title_lockup(compact=mobile, align=(0.5 if mobile else 0.0))

            text ("Tap in. Turn up the sound. Let the memories play." if mobile else "An intimate anniversary visual novel told through memory, choice, and forever."):
                size (23 if mobile else 29)
                color "#FFEDE1"
                xmaximum (1120 if mobile else 700)
                line_spacing 3
                xalign (0.5 if mobile else 0.0)
                text_align (0.5 if mobile else 0.0)
                outlines [ (1, "#140810B8", 0, 2) ]

    frame:
        at menu_nav_transform
        xalign (0.5 if mobile else 0.785)
        yalign (0.64 if mobile else 0.51)
        xysize ((720, 620) if mobile else (620, 720))
        background Frame("images/ui/menu_panel.png", 34, 34)
        padding ((46, 30) if mobile else (50, 38))
        vbox:
            spacing (10 if mobile else 16)
            xalign 0.5
            yalign 0.5

            if not mobile:
                text "MAIN MENU" size 27 color "#FFD8BB" xalign 0.5
                add Solid("#FFD7A666") xysize (420, 2) xalign 0.5
                null height 6
            use premium_button("Begin Our Story", Start())
            use premium_button("Continue", Start("continue_game"), sensitive=can_continue)
            use premium_button("Chapter Select", ShowMenu("chapter_select"), sensitive=unlocked_chapters > 1)
            use premium_button("Memory Gallery", ShowMenu("memory_gallery"))
            use premium_button("Preferences", ShowMenu("preferences"))
            use premium_button("Quit", Quit(confirm=True))

            null height (2 if mobile else 6)
            text "Premium Anniversary Edition" size (21 if mobile else 21) color "#BFAAA5" xalign 0.5

screen chapter_select():
    $ mobile = audit_force_mobile_layout or renpy.variant("small") or renpy.variant("touch")
    $ unlocked_chapters = unlocked_chapter_limit()
    tag menu
    add "bg_main_menu" at menu_background_crop
    add "cinematic_vignette"
    add Solid("#050007E8")

    frame:
        xalign 0.5
        yalign (0.07 if mobile else 0.065)
        xysize ((1500, 128) if mobile else (1180, 126))
        background Frame("images/ui/chapter_panel.png", 34, 34)
        padding (40, 18)
        vbox:
            spacing 2
            xalign 0.5
            yalign 0.5
            text "Chapter Select" size (50 if mobile else 50) color "#FFF8F2" xalign 0.5
            text "Unlocked through Chapter [unlocked_chapters] of 15" size (26 if mobile else 23) color "#FFD8BB" xalign 0.5

    vpgrid:
        cols (2 if mobile else 3)
        xpos (180 if mobile else 110)
        ypos (198 if mobile else 190)
        xysize ((1560, 720) if mobile else (1700, 735))
        spacing (24 if mobile else 20)
        mousewheel True
        draggable True

        for entry in chapter_select_entries:
            $ unlocked = entry["number"] <= unlocked_chapters
            $ choice_note = choice_annotation_for_chapter(entry["number"])
            button:
                action Start(entry["target"])
                sensitive unlocked
                xysize ((760, 228) if mobile else (548, 206))
                background Frame("images/ui/menu_panel.png", 28, 28)
                hover_background Frame("images/ui/chapter_panel.png", 28, 28)
                insensitive_background Frame("images/ui/button_idle.png", 28, 28)
                padding ((16, 16) if mobile else (14, 14))

                fixed:
                    frame:
                        xysize ((728, 196) if mobile else (520, 178))
                        background "#08040AE8"
                        padding (0, 0)
                        add entry["art"]:
                            xysize ((728, 196) if mobile else (520, 178))
                            fit "cover"
                            alpha (1.0 if unlocked else 0.34)

                    add Solid("#05000799" if unlocked else "#050007D0"):
                        xysize ((728, 196) if mobile else (520, 178))

                    vbox:
                        xpos (24 if mobile else 22)
                        ypos (22 if mobile else 20)
                        xsize (660 if mobile else 460)
                        spacing (6 if mobile else 5)
                        text entry["label"].upper():
                            size (26 if mobile else 22)
                            color (entry["accent"] if unlocked else "#9C8B8F")
                            bold True
                        text entry["title"]:
                            size (34 if mobile else 29)
                            color ("#FFF8F2" if unlocked else "#B3A2A6")
                            xmaximum (660 if mobile else 460)
                        text (entry["mood"] if unlocked else "Locked until the story reaches this memory."):
                            size (23 if mobile else 20)
                            color ("#FFD8BB" if unlocked else "#8D7E82")
                            xmaximum (660 if mobile else 460)
                            line_spacing 2
                        if unlocked and choice_note:
                            text choice_note:
                                size (20 if mobile else 17)
                                color "#FFE9B8"
                                xmaximum (660 if mobile else 460)
                                line_spacing 1

                    frame:
                        xalign 0.965
                        yalign 0.12
                        xysize ((58, 48) if mobile else (50, 42))
                        background Frame("images/ui/prompt_panel.png", 18, 18)
                        padding (6, 6)
                        if unlocked:
                            text "%02d" % entry["number"]:
                                size (22 if mobile else 18)
                                color "#FFE9B8"
                                bold True
                                xalign 0.5
                                yalign 0.5
                        else:
                            add "images/ui/keepsakes/icon_lock.png":
                                xysize ((34, 34) if mobile else (28, 28))
                                xalign 0.5
                                yalign 0.5
                                alpha 0.72

    textbutton "Back":
        action Return()
        xalign 0.5
        yalign 0.972
        xysize ((430, 72) if mobile else (360, 64))
        background Frame("images/ui/button_idle.png", 22, 22)
        hover_background Frame("images/ui/button_hover.png", 22, 22)
        text_size (30 if mobile else 26)
        text_color "#FFF8F2"
        text_hover_color "#FFF8F2"
        text_xalign 0.5
        text_yalign 0.5

screen memory_gallery():
    $ mobile = audit_force_mobile_layout or renpy.variant("small") or renpy.variant("touch")
    $ unlocked_chapters = unlocked_chapter_limit()
    tag menu
    add "bg_main_menu" at menu_background_crop
    add "cinematic_vignette"
    add Solid("#050007E6")

    frame:
        xalign 0.5
        yalign (0.07 if mobile else 0.065)
        xysize ((1500, 128) if mobile else (1180, 126))
        background Frame("images/ui/chapter_panel.png", 34, 34)
        padding (40, 18)
        vbox:
            spacing 2
            xalign 0.5
            yalign 0.5
            text "Memory Gallery" size (50 if mobile else 50) color "#FFF8F2" xalign 0.5
            text "Nineteen moments with captions and chapter replay links" size (26 if mobile else 23) color "#FFD8BB" xalign 0.5

    vpgrid:
        cols (2 if mobile else 4)
        xpos (180 if mobile else 94)
        ypos (198 if mobile else 190)
        xysize ((1560, 720) if mobile else (1732, 755))
        spacing (24 if mobile else 20)
        mousewheel True
        draggable True

        for index, photo in enumerate(memory_gallery_photos):
            button:
                action Show("memory_photo_viewer", photo=photo, index=index)
                xysize ((760, 380) if mobile else (415, 328))
                background Frame("images/ui/menu_panel.png", 28, 28)
                hover_background Frame("images/ui/chapter_panel.png", 28, 28)
                padding ((18, 18) if mobile else (14, 14))

                vbox:
                    spacing (10 if mobile else 8)
                    xalign 0.5
                    frame:
                        xysize ((724, 218) if mobile else (387, 196))
                        background "#08040AE8"
                        padding (8, 8)
                        add photo:
                            xysize ((708, 202) if mobile else (371, 180))
                            fit "contain"
                            xalign 0.5
                            yalign 0.5
                    add Solid("#FFD7A64D") xysize ((708, 1) if mobile else (371, 1)) xalign 0.5
                    hbox:
                        xfill True
                        ysize (42 if mobile else 34)
                        text memory_gallery_label(index) size (29 if mobile else 25) color "#FFF8F2" yalign 0.5
                        text ("Ch. %02d" % memory_gallery_chapter(index)) size (25 if mobile else 22) color "#FFD8BB" xalign 1.0 yalign 0.5
                    text memory_gallery_caption(index):
                        size (23 if mobile else 19)
                        color "#CDBAC0"
                        xmaximum (708 if mobile else 371)
                        line_spacing 1

    add Solid("#FFD7A633"):
        xpos (180 if mobile else 94)
        ypos (940 if mobile else 950)
        xysize ((1560, 1) if mobile else (1732, 1))

    textbutton "Back":
        action Return()
        xalign 0.5
        yalign 0.972
        xysize ((430, 72) if mobile else (360, 64))
        background Frame("images/ui/button_idle.png", 22, 22)
        hover_background Frame("images/ui/button_hover.png", 22, 22)
        text_size (30 if mobile else 26)
        text_color "#FFF8F2"
        text_hover_color "#FFF8F2"
        text_xalign 0.5
        text_yalign 0.5

screen memory_photo_viewer(photo, index=0):
    $ mobile = audit_force_mobile_layout or renpy.variant("small") or renpy.variant("touch")
    $ replay_chapter = memory_gallery_chapter(index)
    $ replay_unlocked = replay_chapter <= unlocked_chapter_limit()
    $ choice_note = memory_gallery_choice_note(index)
    zorder 210
    modal True
    key "K_ESCAPE" action Hide("memory_photo_viewer")
    key "mouseup_3" action Hide("memory_photo_viewer")
    key "K_LEFT" action Show("memory_photo_viewer", photo=memory_gallery_photos[(index - 1) % len(memory_gallery_photos)], index=(index - 1) % len(memory_gallery_photos))
    key "K_RIGHT" action Show("memory_photo_viewer", photo=memory_gallery_photos[(index + 1) % len(memory_gallery_photos)], index=(index + 1) % len(memory_gallery_photos))

    add Solid("#050007F2")
    add "cinematic_vignette"

    frame:
        xalign 0.5
        yalign (0.46 if mobile else 0.47)
        xysize ((1640, 780) if mobile else (1510, 820))
        background Frame("images/ui/menu_panel.png", 34, 34)
        padding ((30, 30) if mobile else (34, 32))
        add photo:
            xysize ((1580, 720) if mobile else (1442, 756))
            fit "contain"
            xalign 0.5
            yalign 0.5

    frame:
        xalign 0.5
        yalign (0.90 if mobile else 0.91)
        xysize ((1260, 140) if mobile else (1040, 126))
        background Frame("images/ui/prompt_panel.png", 28, 28)
        padding (30, 14)
        vbox:
            spacing 2
            xalign 0.5
            yalign 0.5
            text "[memory_gallery_label(index)] / [len(memory_gallery_photos)]" size (31 if mobile else 27) color "#FFF8F2" xalign 0.5
            text memory_gallery_caption(index) size (24 if mobile else 21) color "#FFD8BB" xalign 0.5 text_align 0.5 xmaximum (1020 if mobile else 820)
            if choice_note:
                text choice_note size (21 if mobile else 18) color "#FFE9B8" xalign 0.5 text_align 0.5 xmaximum (1140 if mobile else 920)

    textbutton "Prev":
        action Show("memory_photo_viewer", photo=memory_gallery_photos[(index - 1) % len(memory_gallery_photos)], index=(index - 1) % len(memory_gallery_photos))
        xalign (0.12 if mobile else 0.07)
        yalign (0.91 if mobile else 0.47)
        xysize ((210, 76) if mobile else (178, 70))
        background Frame("images/ui/button_idle.png", 22, 22)
        hover_background Frame("images/ui/button_hover.png", 22, 22)
        text_size (30 if mobile else 27)
        text_color "#FFF8F2"
        text_hover_color "#FFF8F2"
        text_xalign 0.5
        text_yalign 0.5

    textbutton "Next":
        action Show("memory_photo_viewer", photo=memory_gallery_photos[(index + 1) % len(memory_gallery_photos)], index=(index + 1) % len(memory_gallery_photos))
        xalign (0.88 if mobile else 0.93)
        yalign (0.91 if mobile else 0.47)
        xysize ((210, 76) if mobile else (178, 70))
        background Frame("images/ui/button_idle.png", 22, 22)
        hover_background Frame("images/ui/button_hover.png", 22, 22)
        text_size (30 if mobile else 27)
        text_color "#FFF8F2"
        text_hover_color "#FFF8F2"
        text_xalign 0.5
        text_yalign 0.5

    textbutton "Close":
        action Hide("memory_photo_viewer")
        xalign (0.91 if mobile else 0.94)
        yalign (0.06 if mobile else 0.055)
        xysize ((260, 72) if mobile else (230, 62))
        background Frame("images/ui/button_idle.png", 22, 22)
        hover_background Frame("images/ui/button_hover.png", 22, 22)
        text_size (29 if mobile else 25)
        text_color "#FFF8F2"
        text_hover_color "#FFF8F2"
        text_xalign 0.5
        text_yalign 0.5

    textbutton ("Replay Ch. %02d" % replay_chapter):
        action [Hide("memory_photo_viewer"), Start(chapter_label_for_number(replay_chapter))]
        sensitive replay_unlocked
        xalign (0.09 if mobile else 0.06)
        yalign (0.06 if mobile else 0.055)
        xysize ((300, 72) if mobile else (260, 62))
        background Frame("images/ui/button_idle.png", 22, 22)
        hover_background Frame("images/ui/button_hover.png", 22, 22)
        insensitive_background Frame("images/ui/button_idle.png", 22, 22)
        text_size (27 if mobile else 23)
        text_color "#FFF8F2"
        text_hover_color "#FFF8F2"
        text_insensitive_color "#9C8B8F"
        text_xalign 0.5
        text_yalign 0.5

screen chapter_card(title, subtitle, settled=False):
    $ mobile = audit_force_mobile_layout or renpy.variant("small") or renpy.variant("touch")
    $ reduce_motion = bool(persistent.access_reduced_motion)
    $ access_high = bool(persistent.access_high_contrast)
    zorder 90
    modal False
    $ card = chapter_card_data(title)
    $ chapter_label = ("CHAPTER " + card["index"]) if card["index"] != "00" else "ANNIVERSARY"
    $ chapter_badge = card["index"] if card["index"] != "00" else "00"
    $ card_backdrop_transform = chapter_card_static if (settled or reduce_motion) else chapter_card_backdrop
    $ card_panel_transform = chapter_card_static if (settled or reduce_motion) else chapter_card_panel
    $ card_copy_transform = chapter_card_static if (settled or reduce_motion) else chapter_card_copy

    add Solid("#050007")
    add card["art"] at card_backdrop_transform
    add Solid(card["wash"])
    add "cinematic_vignette"
    add Solid("#05000788" if access_high else "#05000755")

    frame:
        xalign 0.5
        yalign 0.48
        xysize ((1500, 420) if mobile else (1030, 360))
        background Frame("images/ui/chapter_panel.png", 34, 34)
        padding ((70, 42) if mobile else (56, 34))
        at card_panel_transform

        fixed:
            frame:
                xalign 0.5
                ypos 0
                xysize ((260, 66) if mobile else (210, 58))
                background Frame("images/ui/prompt_panel.png", 22, 22)
                padding (18, 10)

                text chapter_badge:
                    size (32 if mobile else 28)
                    color card["accent"]
                    bold True
                    xalign 0.5
                    yalign 0.5

            vbox:
                ypos (84 if mobile else 72)
                xalign 0.5
                xsize (1320 if mobile else 910)
                spacing 13
                at card_copy_transform

                text chapter_label:
                    size (29 if mobile else 24)
                    color ("#FFE9B8" if access_high else card["accent"])
                    bold True
                    xalign 0.5
                    text_align 0.5
                    xmaximum (1320 if mobile else 910)

                text subtitle:
                    size (62 if mobile else 58)
                    color "#FFF8F2"
                    line_spacing 0
                    xalign 0.5
                    text_align 0.5
                    xmaximum (1320 if mobile else 910)

                add Solid(card["accent"]) xysize ((820, 2) if mobile else (620, 2)) xalign 0.5

                text card["mood"]:
                    size (32 if mobile else 28)
                    color ("#FFE9B8" if access_high else "#FFD8BB")
                    line_spacing 4
                    xalign 0.5
                    text_align 0.5
                    xmaximum (1180 if mobile else 820)

                text "OUR STORY  |  A LOVE QUEST":
                    size (20 if mobile else 17)
                    color "#BFAAA5"
                    bold True
                    xalign 0.5
                    text_align 0.5

screen hotspot_prompt(label, hx=0.5, hy=0.54, tone="gold"):
    $ mobile = audit_force_mobile_layout or renpy.variant("small") or renpy.variant("touch")
    $ reduce_motion = bool(persistent.access_reduced_motion)
    $ access_high = bool(persistent.access_high_contrast)
    $ access_large = bool(persistent.access_large_text)
    zorder 100
    modal True
    key "K_RETURN" action Return()
    key "K_SPACE" action Return()

    $ tone_tints = {
        "inspect": "#D7ECFF",
        "social": "#BEE6FF",
        "walk": "#F8D7FF",
        "gift": "#FFD6A8",
        "read": "#FFF1B8",
        "open": "#FFD0D8",
        "storm": "#C6D8FF",
        "final": "#FFF6D8",
    }
    $ marker_tint = tone_tints.get(tone, "#FFE4B8")

    if reduce_motion:
        imagebutton:
            idle Transform("images/ui/hotspot_marker.png", matrixcolor=TintMatrix(marker_tint))
            hover Transform("images/ui/hotspot_marker_hover.png", matrixcolor=TintMatrix("#FFFFFF"))
            action Return()
            xalign hx
            yalign hy
            focus_mask True
    else:
        imagebutton:
            idle Transform("images/ui/hotspot_marker.png", matrixcolor=TintMatrix(marker_tint))
            hover Transform("images/ui/hotspot_marker_hover.png", matrixcolor=TintMatrix("#FFFFFF"))
            action Return()
            xalign hx
            yalign hy
            at hotspot_pulse
            focus_mask True

    frame:
        xalign 0.5
        yalign (0.70 if mobile else 0.72)
        xysize ((1120, 118) if mobile else (820, 96))
        background Frame("images/ui/prompt_panel.png", 28, 28)
        padding ((42, 24) if mobile else (34, 18))
        at hotspot_prompt_settle
        if access_high:
            add Solid("#050007BB")
        text label size ((40 if mobile else 34) if access_large else (36 if mobile else 30)) color "#FFF8F2" xalign 0.5 yalign 0.5 text_align 0.5 outlines ([ (1, "#000000E8", 0, 1) ] if access_high else [])

screen memory_interaction_map(title, instruction, items, seen, min_required=1):
    $ mobile = audit_force_mobile_layout or renpy.variant("small") or renpy.variant("touch")
    $ reduce_motion = bool(persistent.access_reduced_motion)
    $ access_high = bool(persistent.access_high_contrast)
    $ access_large = bool(persistent.access_large_text)
    zorder 100
    modal True

    $ tone_tints = {
        "inspect": "#D7ECFF",
        "social": "#BEE6FF",
        "walk": "#F8D7FF",
        "gift": "#FFD6A8",
        "read": "#FFF1B8",
        "open": "#FFD0D8",
        "storm": "#C6D8FF",
        "final": "#FFF6D8",
    }
    $ seen_count = len(seen)
    $ can_continue = seen_count >= min_required

    $ memory_label_line = "  /  ".join([("✓ " if item["key"] in seen else str(index + 1) + ". ") + item["label"] for index, item in enumerate(items)])

    for index, item in enumerate(items):
        $ item_tint = tone_tints.get(item.get("tone", "gold"), "#FFE4B8")
        $ item_seen = item["key"] in seen

        if reduce_motion:
            imagebutton:
                idle Transform("images/ui/hotspot_marker.png", matrixcolor=TintMatrix("#A78F74" if item_seen else item_tint))
                hover Transform("images/ui/hotspot_marker_hover.png", matrixcolor=TintMatrix("#FFFFFF"))
                action Return(("item", item["key"]))
                xalign item["hx"]
                yalign item["hy"]
                focus_mask True
        else:
            imagebutton:
                idle Transform("images/ui/hotspot_marker.png", matrixcolor=TintMatrix("#A78F74" if item_seen else item_tint))
                hover Transform("images/ui/hotspot_marker_hover.png", matrixcolor=TintMatrix("#FFFFFF"))
                action Return(("item", item["key"]))
                xalign item["hx"]
                yalign item["hy"]
                at hotspot_pulse
                focus_mask True

        text str(index + 1):
            xalign item["hx"]
            yalign item["hy"]
            size 22
            bold True
            color "#FFF8F2"
            outlines [ (2, "#140810D0", 0, 1) ]

    frame:
        xalign 0.5
        yalign (0.75 if mobile else 0.78)
        xysize ((1540, 230) if mobile else (1120, 172))
        background Frame("images/ui/prompt_panel.png", 28, 28)
        padding ((46, 28) if mobile else (38, 24))
        at hotspot_prompt_settle
        if access_high:
            add Solid("#050007BB")

        hbox:
            spacing (34 if mobile else 28)
            xfill True
            yalign 0.5

            vbox:
                spacing 8
                xsize (1060 if mobile else 700)
                text title:
                    size ((40 if mobile else 34) if access_large else (36 if mobile else 30))
                    color "#FFF8F2"
                    bold True
                text instruction:
                    size ((31 if mobile else 26) if access_large else (28 if mobile else 23))
                    color ("#FFE9B8" if access_high else "#FFD8BB")
                    line_spacing 3
                    xmaximum (1020 if mobile else 680)
                text "Memories found: [seen_count] / [len(items)]":
                    size ((25 if mobile else 21) if access_large else (23 if mobile else 19))
                    color "#BFAAA5"
                text memory_label_line:
                    size ((23 if mobile else 19) if access_large else (21 if mobile else 17))
                    color "#D9C9C2"
                    line_spacing 2
                    xmaximum (1020 if mobile else 680)

            textbutton "Continue":
                action Return(("continue", None))
                sensitive can_continue
                xysize ((360, 76) if mobile else (300, 64))
                yalign 0.5
                background Frame("images/ui/button_idle.png", 22, 22)
                hover_background Frame("images/ui/button_hover.png", 22, 22)
                insensitive_background Frame("images/ui/button_idle.png", 22, 22)
                text_size (29 if mobile else 24)
                text_color "#FFF8F2"
                text_hover_color "#FFF8F2"
                text_insensitive_color "#9C8B8F"
                text_xalign 0.5
                text_yalign 0.5

# Pass 6: keepsake box — distinct centered UI for Ch11 gift chapter
screen keepsake_box(title, items, seen, min_required=1):
    $ mobile = audit_force_mobile_layout or renpy.variant("small") or renpy.variant("touch")
    $ reduce_motion = bool(persistent.access_reduced_motion)
    $ access_high = bool(persistent.access_high_contrast)
    $ access_large = bool(persistent.access_large_text)
    zorder 100
    modal True

    $ seen_count = len(seen)
    $ can_continue = seen_count >= min_required

    # Per-item icon glyphs (Geometric Shapes — guaranteed in-font)
    $ _kb_glyphs = {
        "food":   "\u25C8",
        "book":   "\u25CE",
        "sorry":  "\u25C9",
        "photos": "\u25C6",
        "mug":    "\u25C7",
    }
    # Warm accent colours for text/glyph
    $ _kb_tints = {
        "food":   "#FFCB8A",
        "book":   "#FFE080",
        "sorry":  "#FFB8C8",
        "photos": "#B0D0FF",
        "mug":    "#FFD080",
    }
    # Saturated card face colours — these show through the flat button directly
    $ _kb_bgs = {
        "food":   "#8B3A0C",
        "book":   "#6B4414",
        "sorry":  "#7A1238",
        "photos": "#103A8B",
        "mug":    "#7A4810",
    }
    $ _kb_images = {
        "food":   "images/ui/keepsakes/icon_food.png",
        "book":   "images/ui/keepsakes/prop_book.png",
        "sorry":  "images/ui/keepsakes/prop_letters.png",
        "photos": "images/ui/keepsakes/prop_framed_photos.png",
        "mug":    "images/ui/keepsakes/prop_mug.png",
    }
    $ _kb_transforms = {
        "food":   keepsake_float,
        "book":   keepsake_float,
        "sorry":  keepsake_float,
        "photos": keepsake_float,
        "mug":    keepsake_float,
    }

    # Lighter, warmer overlay — game scene shows through for intimacy
    add Solid("#120508BB")

    frame:
        xalign 0.5
        yalign 0.5
        xysize ((1480, 830) if mobile else (1020, 640))
        background Frame("images/ui/prompt_panel.png", 40, 40)
        padding ((44, 36) if mobile else (50, 40))
        if access_high:
            add Solid("#050007BB")

        vbox:
            spacing (14 if mobile else 12)
            xfill True

            # Title block
            vbox:
                spacing 6
                xalign 0.5
                text title:
                    xalign 0.5
                    size ((42 if mobile else 36) if access_large else (38 if mobile else 32))
                    color "#FFF8F2"
                    bold True
                text "Open each gift. Choose your own order.":
                    xalign 0.5
                    size ((30 if mobile else 24) if access_large else (27 if mobile else 21))
                    color "#FFD8BB"

            # Decorative separator
            add Solid("#FFD8BB66"):
                xalign 0.5
                xsize (760 if mobile else 520)
                ysize 1

            # Row 1: first 3 items — flat coloured cards, no frame overlay
            hbox:
                xalign 0.5
                spacing (18 if mobile else 14)
                for item in items[:3]:
                    $ _k = item["key"]
                    $ _kseen = _k in seen
                    $ _ktint  = _kb_tints.get(_k,  "#FFD8A8")
                    $ _kglyph = _kb_glyphs.get(_k, "\u25C6")
                    $ _kbg    = _kb_bgs.get(_k,    "#3A1A10")
                    $ _kimage = _kb_images.get(_k, None)
                    $ _ktransform = _kb_transforms.get(_k, keepsake_float)
                    if reduce_motion or _kseen:
                        button:
                            xysize ((420, 168) if mobile else (284, 156))
                            background Frame("images/ui/menu_panel.png", 28, 28)
                            hover_background Frame("images/ui/chapter_panel.png", 28, 28)
                            insensitive_background Frame("images/ui/menu_panel.png", 28, 28)
                            action Return(("item", _k))
                            sensitive not _kseen
                            fixed:
                                add Solid((_kbg + "66") if not _kseen else "#2A202788"):
                                    xysize ((420, 168) if mobile else (284, 156))
                                add Solid(_ktint if not _kseen else "#7A6A70"):
                                    xalign 0.5
                                    ypos (18 if mobile else 14)
                                    xysize ((220, 2) if mobile else (150, 2))
                                    alpha (0.95 if not _kseen else 0.48)
                                vbox:
                                    spacing (8 if mobile else 6)
                                    xalign 0.5
                                    yalign 0.5
                                    xsize ((370) if mobile else 240)
                                    if _kimage:
                                        add _kimage:
                                            xalign 0.5
                                            xysize ((170, 82) if mobile else (124, 74))
                                            fit "contain"
                                            alpha (0.32 if _kseen else 0.94)
                                    else:
                                        text _kglyph:
                                            xalign 0.5
                                            size ((54 if mobile else 50) if access_large else (50 if mobile else 44))
                                            color ("#7A6A70" if _kseen else _ktint)
                                    text ("\u2713 " + item["label"] if _kseen else item["label"]):
                                        xalign 0.5
                                        text_align 0.5
                                        layout "subtitle"
                                        size ((28 if mobile else 23) if access_large else (24 if mobile else 19))
                                        color ("#8A7A80" if _kseen else "#FFF8F2")
                    else:
                        button:
                            xysize ((420, 168) if mobile else (284, 156))
                            background Frame("images/ui/menu_panel.png", 28, 28)
                            hover_background Frame("images/ui/chapter_panel.png", 28, 28)
                            insensitive_background Frame("images/ui/menu_panel.png", 28, 28)
                            action Return(("item", _k))
                            sensitive not _kseen
                            at _ktransform
                            fixed:
                                add Solid(_kbg + "66"):
                                    xysize ((420, 168) if mobile else (284, 156))
                                add Solid(_ktint):
                                    xalign 0.5
                                    ypos (18 if mobile else 14)
                                    xysize ((220, 2) if mobile else (150, 2))
                                    alpha 0.95
                                vbox:
                                    spacing (8 if mobile else 6)
                                    xalign 0.5
                                    yalign 0.5
                                    xsize ((370) if mobile else 240)
                                    if _kimage:
                                        add _kimage:
                                            xalign 0.5
                                            xysize ((170, 82) if mobile else (124, 74))
                                            fit "contain"
                                            alpha 0.94
                                    else:
                                        text _kglyph:
                                            xalign 0.5
                                            size ((54 if mobile else 50) if access_large else (50 if mobile else 44))
                                            color _ktint
                                    text item["label"]:
                                        xalign 0.5
                                        text_align 0.5
                                        layout "subtitle"
                                        size ((28 if mobile else 23) if access_large else (24 if mobile else 19))
                                        color "#FFF8F2"

            # Row 2: last 2 items — wider cards, same total width as row 1
            hbox:
                xalign 0.5
                spacing (18 if mobile else 14)
                for item in items[3:]:
                    $ _k = item["key"]
                    $ _kseen = _k in seen
                    $ _ktint  = _kb_tints.get(_k,  "#FFD8A8")
                    $ _kglyph = _kb_glyphs.get(_k, "\u25C6")
                    $ _kbg    = _kb_bgs.get(_k,    "#3A1A10")
                    $ _kimage = _kb_images.get(_k, None)
                    $ _ktransform = _kb_transforms.get(_k, keepsake_float)
                    if reduce_motion or _kseen:
                        button:
                            xysize ((630, 168) if mobile else (431, 156))
                            background Frame("images/ui/menu_panel.png", 28, 28)
                            hover_background Frame("images/ui/chapter_panel.png", 28, 28)
                            insensitive_background Frame("images/ui/menu_panel.png", 28, 28)
                            action Return(("item", _k))
                            sensitive not _kseen
                            fixed:
                                add Solid((_kbg + "66") if not _kseen else "#2A202788"):
                                    xysize ((630, 168) if mobile else (431, 156))
                                add Solid(_ktint if not _kseen else "#7A6A70"):
                                    xalign 0.5
                                    ypos (18 if mobile else 14)
                                    xysize ((330, 2) if mobile else (230, 2))
                                    alpha (0.95 if not _kseen else 0.48)
                                vbox:
                                    spacing (8 if mobile else 6)
                                    xalign 0.5
                                    yalign 0.5
                                    xsize ((560) if mobile else 360)
                                    if _kimage:
                                        add _kimage:
                                            xalign 0.5
                                            xysize ((240, 82) if mobile else (172, 74))
                                            fit "contain"
                                            alpha (0.34 if _kseen else 0.92)
                                    else:
                                        text _kglyph:
                                            xalign 0.5
                                            size ((54 if mobile else 50) if access_large else (50 if mobile else 44))
                                            color ("#7A6A70" if _kseen else _ktint)
                                    text ("\u2713 " + item["label"] if _kseen else item["label"]):
                                        xalign 0.5
                                        text_align 0.5
                                        layout "subtitle"
                                        size ((28 if mobile else 23) if access_large else (24 if mobile else 19))
                                        color ("#8A7A80" if _kseen else "#FFF8F2")
                    else:
                        button:
                            xysize ((630, 168) if mobile else (431, 156))
                            background Frame("images/ui/menu_panel.png", 28, 28)
                            hover_background Frame("images/ui/chapter_panel.png", 28, 28)
                            insensitive_background Frame("images/ui/menu_panel.png", 28, 28)
                            action Return(("item", _k))
                            sensitive not _kseen
                            at _ktransform
                            fixed:
                                add Solid(_kbg + "66"):
                                    xysize ((630, 168) if mobile else (431, 156))
                                add Solid(_ktint):
                                    xalign 0.5
                                    ypos (18 if mobile else 14)
                                    xysize ((330, 2) if mobile else (230, 2))
                                    alpha 0.95
                                vbox:
                                    spacing (8 if mobile else 6)
                                    xalign 0.5
                                    yalign 0.5
                                    xsize ((560) if mobile else 360)
                                    if _kimage:
                                        add _kimage:
                                            xalign 0.5
                                            xysize ((240, 82) if mobile else (172, 74))
                                            fit "contain"
                                            alpha 0.94
                                    else:
                                        text _kglyph:
                                            xalign 0.5
                                            size ((54 if mobile else 50) if access_large else (50 if mobile else 44))
                                            color _ktint
                                    text item["label"]:
                                        xalign 0.5
                                        text_align 0.5
                                        layout "subtitle"
                                        size ((28 if mobile else 23) if access_large else (24 if mobile else 19))
                                        color "#FFF8F2"

            # Footer: counter + continue
            hbox:
                xfill True
                text "Opened: [seen_count] / [len(items)]":
                    yalign 0.5
                    size ((28 if mobile else 22) if access_large else (25 if mobile else 19))
                    color "#BFAAA5"
                null:
                    xfill True
                textbutton "Continue \u2192":
                    action Return(("continue", None))
                    sensitive can_continue
                    xysize ((340, 68) if mobile else (280, 58))
                    yalign 0.5
                    background Frame("images/ui/button_idle.png", 22, 22)
                    hover_background Frame("images/ui/button_hover.png", 22, 22)
                    insensitive_background Frame("images/ui/button_idle.png", 22, 22)
                    text_size ((29 if mobile else 24) if access_large else (26 if mobile else 21))
                    text_color "#FFF8F2"
                    text_hover_color "#FFF8F2"
                    text_insensitive_color "#9C8B8F"
                    text_xalign 0.5
                    text_yalign 0.5

screen choice(items):
    $ mobile = audit_force_mobile_layout or renpy.variant("small") or renpy.variant("touch")
    $ access_high = bool(persistent.access_high_contrast)
    $ access_large = bool(persistent.access_large_text)
    zorder 95
    modal True

    frame:
        xalign 0.5
        yalign (0.40 if mobile else 0.43)
        xysize ((1540, 480) if mobile else (1120, 390))
        background Frame("images/ui/chapter_panel.png", 28, 28)
        padding ((58, 38) if mobile else (46, 32))
        if access_high:
            add Solid("#050007BB")

        vbox:
            spacing (18 if mobile else 16)
            xalign 0.5
            yalign 0.5

            text "Choose what this memory holds":
                size ((38 if mobile else 32) if access_large else (34 if mobile else 28))
                color ("#FFE9B8" if access_high else "#FFD8BB")
                bold True
                xalign 0.5
                text_align 0.5

            for item in items:
                textbutton item.caption:
                    action item.action
                    xysize ((1320, 84) if mobile else (940, 66))
                    background Frame("images/ui/button_idle.png", 22, 22)
                    hover_background Frame("images/ui/button_hover.png", 22, 22)
                    text_size ((32 if mobile else 26) if access_large else (29 if mobile else 23))
                    text_color "#FFF8F2"
                    text_hover_color "#FFF8F2"
                    text_xalign 0.5
                    text_yalign 0.5

screen choice_preview(question, options):
    $ mobile = audit_force_mobile_layout or renpy.variant("small") or renpy.variant("touch")
    $ access_high = bool(persistent.access_high_contrast)
    $ access_large = bool(persistent.access_large_text)
    zorder 95
    modal True

    frame:
        xalign 0.5
        yalign (0.40 if mobile else 0.43)
        xysize ((1540, 480) if mobile else (1120, 390))
        background Frame("images/ui/chapter_panel.png", 28, 28)
        padding ((58, 38) if mobile else (46, 32))
        if access_high:
            add Solid("#050007BB")

        vbox:
            spacing (18 if mobile else 16)
            xalign 0.5
            yalign 0.5

            text question:
                size ((38 if mobile else 32) if access_large else (34 if mobile else 28))
                color ("#FFE9B8" if access_high else "#FFD8BB")
                bold True
                xalign 0.5
                text_align 0.5
                xmaximum (1320 if mobile else 960)

            for option in options:
                frame:
                    xysize ((1320, 84) if mobile else (940, 66))
                    background Frame("images/ui/button_idle.png", 22, 22)
                    padding (24, 12)
                    text option:
                        size ((32 if mobile else 26) if access_large else (29 if mobile else 23))
                        color "#FFF8F2"
                        xalign 0.5
                        yalign 0.5
                        text_align 0.5

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):
    tag menu

    add "bg_main_menu" at menu_background_crop
    add "cinematic_vignette"
    add Solid("#050007D8")

    frame:
        xalign 0.5
        yalign 0.52
        xysize (1510, 860)
        background Frame("images/ui/menu_panel.png", 34, 34)
        padding (52, 42)

        vbox:
            spacing 24
            hbox:
                xfill True
                text title size 52 color "#FFF8F2" yalign 0.5
                null width 40
                textbutton "Return":
                    action Return()
                    xalign 1.0
                    yalign 0.5
                    xysize (220, 54)
                    background Frame("images/ui/button_idle.png", 22, 22)
                    hover_background Frame("images/ui/button_hover.png", 22, 22)
                    text_size 22
                    text_color "#FFF8F2"
                    text_hover_color "#FFF8F2"
                    text_xalign 0.5
                    text_yalign 0.5

            add Solid("#FFD7A655") xysize (760, 2) xalign 0.0

            if scroll == "viewport":
                viewport:
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    xfill True
                    ysize 685
                    vbox:
                        spacing spacing
                        transclude
            else:
                frame:
                    background None
                    xfill True
                    ysize 685
                    padding (0, 0)
                    transclude

screen history(sample_entries=None):
    $ mobile = audit_force_mobile_layout or renpy.variant("small") or renpy.variant("touch")
    tag menu
    $ history_entries = [(h.who, h.what) for h in _history_list if h.what]
    if history_audit_entries is not None:
        $ history_entries = history_audit_entries
    elif sample_entries is not None:
        $ history_entries = sample_entries
    $ history_lines_per_page = 4 if mobile else 5
    $ history_ordered_entries = list(reversed(history_entries))
    $ history_total_pages = max(1, (len(history_ordered_entries) + history_lines_per_page - 1) // history_lines_per_page)
    $ history_current_page = min(history_page, history_total_pages - 1)
    $ history_page_start = history_current_page * history_lines_per_page
    $ visible_history_entries = history_ordered_entries[history_page_start:history_page_start + history_lines_per_page]

    add "bg_main_menu" at menu_background_crop
    add "cinematic_vignette"
    add Solid("#050007E8")

    frame:
        xalign 0.5
        yalign 0.52
        xysize ((1660, 900) if mobile else (1510, 850))
        background Frame("images/ui/menu_panel.png", 34, 34)
        padding ((60, 44) if mobile else (52, 40))

        fixed:
            xysize ((1540, 812) if mobile else (1406, 770))

            text "History":
                xpos 0
                ypos 0
                size (58 if mobile else 54)
                color "#FFF8F2"

            text "Recent lines from this memory.":
                xpos 0
                ypos (78 if mobile else 74)
                size (27 if mobile else 23)
                color "#FFD8BB"

            textbutton "Return":
                action Return()
                xpos (1270 if mobile else 1186)
                ypos (24 if mobile else 30)
                xysize ((270, 68) if mobile else (220, 54))
                background Frame("images/ui/button_idle.png", 22, 22)
                hover_background Frame("images/ui/button_hover.png", 22, 22)
                text_size (27 if mobile else 22)
                text_color "#FFF8F2"
                text_hover_color "#FFF8F2"
                text_xalign 0.5
                text_yalign 0.5

            add Solid("#FFD7A655"):
                xpos 0
                ypos (138 if mobile else 128)
                xysize ((1120, 2) if mobile else (860, 2))

            if visible_history_entries:
                vbox:
                    xpos 0
                    ypos (180 if mobile else 170)
                    spacing (20 if mobile else 18)
                    xsize (1480 if mobile else 1360)

                    for who, what in visible_history_entries:
                        frame:
                            xsize (1460 if mobile else 1320)
                            background Frame("images/ui/chapter_panel.png", 28, 28)
                            padding ((30, 22) if mobile else (26, 20))

                            vbox:
                                spacing 8
                                if who:
                                    text who:
                                        size (28 if mobile else 24)
                                        color "#FFD8BB"
                                        bold True
                                text what:
                                    size (31 if mobile else 27)
                                    color "#FFF8F2"
                                    line_spacing 4
                                    xmaximum (1390 if mobile else 1268)

                if len(history_ordered_entries) > history_lines_per_page:
                    hbox:
                        xpos 0
                        ypos (744 if mobile else 706)
                        spacing 18

                        textbutton "Newer":
                            action SetVariable("history_page", max(history_current_page - 1, 0))
                            sensitive history_current_page > 0
                            xysize ((270, 68) if mobile else (220, 54))
                            background Frame("images/ui/button_idle.png", 22, 22)
                            hover_background Frame("images/ui/button_hover.png", 22, 22)
                            insensitive_background Frame("images/ui/button_idle.png", 22, 22)
                            text_size (27 if mobile else 22)
                            text_color "#FFF8F2"
                            text_hover_color "#FFF8F2"
                            text_insensitive_color "#9C8B8F"
                            text_xalign 0.5
                            text_yalign 0.5

                        text "Page [history_current_page + 1] / [history_total_pages]":
                            yalign 0.5
                            size (27 if mobile else 23)
                            color "#FFD8BB"

                        textbutton "Older":
                            action SetVariable("history_page", min(history_current_page + 1, history_total_pages - 1))
                            sensitive history_current_page < history_total_pages - 1
                            xysize ((270, 68) if mobile else (220, 54))
                            background Frame("images/ui/button_idle.png", 22, 22)
                            hover_background Frame("images/ui/button_hover.png", 22, 22)
                            insensitive_background Frame("images/ui/button_idle.png", 22, 22)
                            text_size (27 if mobile else 22)
                            text_color "#FFF8F2"
                            text_hover_color "#FFF8F2"
                            text_insensitive_color "#9C8B8F"
                            text_xalign 0.5
                            text_yalign 0.5
            else:
                frame:
                    xpos 0
                    ypos (180 if mobile else 170)
                    xsize (1460 if mobile else 1320)
                    ysize (270 if mobile else 240)
                    background Frame("images/ui/chapter_panel.png", 28, 28)
                    padding (36, 30)
                    text "Dialogue will appear here as the story unfolds.":
                        size (34 if mobile else 30)
                        color "#FFD8BB"
                        xalign 0.5
                        yalign 0.5
                        text_align 0.5

screen preferences():
    $ mobile = audit_force_mobile_layout or renpy.variant("small") or renpy.variant("touch")
    $ access_large = bool(persistent.access_large_text)
    $ access_high = bool(persistent.access_high_contrast)
    tag menu

    add "bg_main_menu" at menu_background_crop
    add "cinematic_vignette"
    add Solid("#000000F0" if access_high else "#050007E6")

    if mobile:
        frame:
            xalign 0.5
            yalign 0.52
            xysize (1660, 900)
            background Frame("images/ui/menu_panel.png", 34, 34)
            padding (66, 46)

            vbox:
                spacing 18

                hbox:
                    xfill True
                    vbox:
                        spacing 2
                        text "Preferences" size (60 if access_large else 56) color "#FFF8F2"
                        text "Tune readability, motion, pacing, sound, and controls." size (29 if access_large else 27) color ("#FFE9B8" if access_high else "#FFD8BB")
                    textbutton "Return":
                        action Return()
                        xalign 1.0
                        yalign 0.5
                        xysize (270, 68)
                        background Frame("images/ui/button_idle.png", 22, 22)
                        hover_background Frame("images/ui/button_hover.png", 22, 22)
                        text_size 27
                        text_color "#FFF8F2"
                        text_hover_color "#FFF8F2"
                        text_xalign 0.5
                        text_yalign 0.5

                add Solid("#FFD7A655") xysize (1180, 2)

                hbox:
                    spacing 60

                    vbox:
                        spacing 18
                        xsize 760
                        text "Accessibility" size (40 if access_large else 38) color ("#FFE9B8" if access_high else "#FFD8BB")
                        hbox:
                            spacing 18
                            use accessibility_toggle_button("Large Text", "access_large_text")
                            use accessibility_toggle_button("High Contrast", "access_high_contrast")
                        hbox:
                            spacing 18
                            use accessibility_toggle_button("Reduced Motion", "access_reduced_motion")
                            use compact_button("Self-Voicing", Preference("self voicing", "toggle"))
                        text "Touch controls remain active; Back/History/Save are always available from the top bar.":
                            size (23 if access_large else 21)
                            color "#D9C9C2"
                            line_spacing 3
                            xmaximum 710

                        null height 4
                        text "Experience" size (40 if access_large else 38) color ("#FFE9B8" if access_high else "#FFD8BB")
                        hbox:
                            spacing 18
                            use compact_button("Window", Preference("display", "window"))
                            use compact_button("Fullscreen", Preference("display", "fullscreen"))
                        hbox:
                            spacing 18
                            use compact_button("All Text", Preference("skip", "all"))
                            use compact_button("Seen Text", Preference("skip", "seen"))
                        hbox:
                            spacing 18
                            use compact_button("Transitions", Preference("transitions", "all"))
                            use compact_button("Instant", Preference("transitions", "none"))

                        null height 4
                        text "Controls" size (40 if access_large else 38) color ("#FFE9B8" if access_high else "#FFD8BB")
                        hbox:
                            spacing 18
                            use compact_button("Start Skip", Skip())
                            use compact_button("Auto", Preference("auto-forward", "toggle"))
                        hbox:
                            spacing 18
                            use compact_button("Main Menu", MainMenu())
                            use compact_button("Quit", Quit(confirm=True))

                    vbox:
                        spacing 18
                        xsize 650
                        text "Pacing" size (40 if access_large else 38) color ("#FFE9B8" if access_high else "#FFD8BB")
                        text "Text Speed" size (31 if access_large else 29) color "#FFF8F2"
                        bar value Preference("text speed"):
                            xysize (640, 34)
                            left_bar Solid("#FFD7A6")
                            right_bar Solid("#2A141D")
                            thumb Solid("#FFF8F2")
                        text "Auto-Forward Time" size (31 if access_large else 29) color "#FFF8F2"
                        bar value Preference("auto-forward time"):
                            xysize (640, 34)
                            left_bar Solid("#FFD7A6")
                            right_bar Solid("#2A141D")
                            thumb Solid("#FFF8F2")

                        null height 12
                        text "Audio" size (40 if access_large else 38) color ("#FFE9B8" if access_high else "#FFD8BB")
                        text "Music Volume" size (31 if access_large else 29) color "#FFF8F2"
                        bar value Preference("music volume"):
                            xysize (640, 34)
                            left_bar Solid("#FFD7A6")
                            right_bar Solid("#2A141D")
                            thumb Solid("#FFF8F2")
                        text "Sound Volume" size (31 if access_large else 29) color "#FFF8F2"
                        bar value Preference("sound volume"):
                            xysize (640, 34)
                            left_bar Solid("#FFD7A6")
                            right_bar Solid("#2A141D")
                            thumb Solid("#FFF8F2")
                        text "Voice Volume" size (31 if access_large else 29) color "#FFF8F2"
                        bar value Preference("voice volume"):
                            xysize (640, 34)
                            left_bar Solid("#FFD7A6")
                            right_bar Solid("#2A141D")
                            thumb Solid("#FFF8F2")
                        hbox:
                            spacing 12
                            use voice_character_control("Prawal", "prawal", voice_character_samples["prawal"], 200)
                            use voice_character_control("Aashna", "aashna", voice_character_samples["aashna"], 200)
                            use voice_character_control("Narrator", "narrator", voice_character_samples["narrator"], 200)
                        hbox:
                            spacing 12
                            use voice_action_button("Wait Voice", ToggleField(preferences, "wait_voice"))
                            use voice_action_button("Voice Pace", Function(enable_voice_synced_pacing))
                            use voice_action_button("Replay", VoiceReplay())
    else:
        frame:
            xalign 0.5
            yalign 0.52
            xysize (1460, 790)
            background Frame("images/ui/menu_panel.png", 34, 34)
            padding (64, 46)

            vbox:
                spacing 20
                hbox:
                    xfill True
                    vbox:
                        spacing 2
                        text "Preferences" size (58 if access_large else 54) color "#FFF8F2"
                        text "Tune readability, motion, pacing, sound, and controls." size (25 if access_large else 23) color ("#FFE9B8" if access_high else "#FFD8BB")
                    textbutton "Return":
                        action Return()
                        xalign 1.0
                        yalign 0.5
                        xysize (220, 54)
                        background Frame("images/ui/button_idle.png", 22, 22)
                        hover_background Frame("images/ui/button_hover.png", 22, 22)
                        text_size 22
                        text_color "#FFF8F2"
                        text_hover_color "#FFF8F2"
                        text_xalign 0.5
                        text_yalign 0.5

                add Solid("#FFD7A655") xysize (840, 2)

                hbox:
                    spacing 70

                    vbox:
                        spacing 14
                        xsize 635
                        text "Accessibility" size (38 if access_large else 36) color ("#FFE9B8" if access_high else "#FFD8BB")
                        hbox:
                            spacing 16
                            use accessibility_toggle_button("Large Text", "access_large_text")
                            use accessibility_toggle_button("High Contrast", "access_high_contrast")
                        hbox:
                            spacing 16
                            use accessibility_toggle_button("Reduced Motion", "access_reduced_motion")
                            use compact_button("Self-Voicing", Preference("self voicing", "toggle"))
                        text "Use these first for readability, contrast, and calmer motion.":
                            size (20 if access_large else 18)
                            color "#D9C9C2"
                            xmaximum 620

                        null height 2
                        text "Experience" size (38 if access_large else 36) color ("#FFE9B8" if access_high else "#FFD8BB")
                        hbox:
                            spacing 16
                            use compact_button("Window", Preference("display", "window"))
                            use compact_button("Fullscreen", Preference("display", "fullscreen"))
                        hbox:
                            spacing 16
                            use compact_button("All Text", Preference("skip", "all"))
                            use compact_button("Seen Text", Preference("skip", "seen"))
                        hbox:
                            spacing 16
                            use compact_button("Transitions", Preference("transitions", "all"))
                            use compact_button("Instant", Preference("transitions", "none"))

                        null height 2
                        text "Controls" size (38 if access_large else 36) color ("#FFE9B8" if access_high else "#FFD8BB")
                        hbox:
                            spacing 16
                            use compact_button("Start Skip", Skip())
                            use compact_button("Auto", Preference("auto-forward", "toggle"))
                        hbox:
                            spacing 16
                            use compact_button("Main Menu", MainMenu())
                            use compact_button("Quit", Quit(confirm=True))

                    vbox:
                        spacing 14
                        xsize 635
                        text "Pacing" size (38 if access_large else 36) color ("#FFE9B8" if access_high else "#FFD8BB")
                        vbox:
                            spacing 8
                            text "Text Speed" size (27 if access_large else 25) color "#FFF8F2"
                            bar value Preference("text speed"):
                                xysize (620, 24)
                                left_bar Solid("#FFD7A6")
                                right_bar Solid("#2A141D")
                                thumb Solid("#FFF8F2")
                        vbox:
                            spacing 8
                            text "Auto-Forward Time" size (27 if access_large else 25) color "#FFF8F2"
                            bar value Preference("auto-forward time"):
                                xysize (620, 24)
                                left_bar Solid("#FFD7A6")
                                right_bar Solid("#2A141D")
                                thumb Solid("#FFF8F2")

                        null height 2
                        text "Audio" size (38 if access_large else 36) color ("#FFE9B8" if access_high else "#FFD8BB")
                        vbox:
                            spacing 8
                            text "Music Volume" size (27 if access_large else 25) color "#FFF8F2"
                            bar value Preference("music volume"):
                                xysize (620, 24)
                                left_bar Solid("#FFD7A6")
                                right_bar Solid("#2A141D")
                                thumb Solid("#FFF8F2")
                        vbox:
                            spacing 8
                            text "Sound Volume" size (27 if access_large else 25) color "#FFF8F2"
                            bar value Preference("sound volume"):
                                xysize (620, 24)
                                left_bar Solid("#FFD7A6")
                                right_bar Solid("#2A141D")
                                thumb Solid("#FFF8F2")
                        vbox:
                            spacing 8
                            text "Voice Volume" size (27 if access_large else 25) color "#FFF8F2"
                            bar value Preference("voice volume"):
                                xysize (620, 24)
                                left_bar Solid("#FFD7A6")
                                right_bar Solid("#2A141D")
                                thumb Solid("#FFF8F2")
                        hbox:
                            spacing 12
                            use voice_character_control("Prawal", "prawal", voice_character_samples["prawal"], 195)
                            use voice_character_control("Aashna", "aashna", voice_character_samples["aashna"], 195)
                            use voice_character_control("Narrator", "narrator", voice_character_samples["narrator"], 195)
                        hbox:
                            spacing 12
                            use voice_action_button("Wait Voice", ToggleField(preferences, "wait_voice"))
                            use voice_action_button("Voice Pace", Function(enable_voice_synced_pacing))
                            use voice_action_button("Replay", VoiceReplay())

screen navigation():
    vbox:
        spacing 14
        use compact_button("Save", ShowMenu("save"))
        use compact_button("Load", ShowMenu("load"))
        use compact_button("History", [SetVariable("history_page", 0), ShowMenu("history")])
        use compact_button("Chapters", ShowMenu("chapter_select"))
        use compact_button("Preferences", ShowMenu("preferences"))
        use compact_button("Main Menu", MainMenu())
        use compact_button("Return", Return())

screen save():
    tag menu
    $ save_name = current_save_name()
    use file_slots("Save Memory", "Preserve this moment")

screen load():
    tag menu
    use file_slots("Load Memory", "Return to a saved moment")

screen file_page_button(label, action, selected=False, wide=False):
    $ mobile = audit_force_mobile_layout or renpy.variant("small") or renpy.variant("touch")
    textbutton label:
        action action
        xysize (((156, 66) if mobile else (132, 54)) if wide else ((92, 66) if mobile else (72, 54)))
        background Frame("images/ui/chapter_panel.png" if selected else "images/ui/button_idle.png", 22, 22)
        hover_background Frame("images/ui/button_hover.png", 22, 22)
        text_size ((25 if mobile else 22) if wide else (28 if mobile else 24))
        text_color ("#FFD8BB" if selected else "#FFF8F2")
        text_hover_color "#FFF8F2"
        text_xalign 0.5
        text_yalign 0.5

screen file_slots(title, subtitle):
    $ mobile = audit_force_mobile_layout or renpy.variant("small") or renpy.variant("touch")
    $ is_load_screen = title.startswith("Load")
    $ current_page = FileCurrentPage()
    add "bg_main_menu" at menu_background_crop
    add "cinematic_vignette"
    add Solid("#050007E8")

    frame:
        xalign 0.5
        yalign 0.52
        xysize ((1660, 900) if mobile else (1540, 850))
        background Frame("images/ui/menu_panel.png", 34, 34)
        padding ((58, 42) if mobile else (52, 40))

        vbox:
            spacing (20 if mobile else 22)
            hbox:
                xfill True
                vbox:
                    spacing 2
                    text title size (56 if mobile else 54) color "#FFF8F2"
                    text subtitle size (27 if mobile else 23) color "#FFD8BB"
                textbutton "Return":
                    action Return()
                    xalign 1.0
                    yalign 0.5
                    xysize ((270, 68) if mobile else (220, 54))
                    background Frame("images/ui/button_idle.png", 22, 22)
                    hover_background Frame("images/ui/button_hover.png", 22, 22)
                    text_size (27 if mobile else 22)
                    text_color "#FFF8F2"
                    text_hover_color "#FFF8F2"
                    text_xalign 0.5
                    text_yalign 0.5

            add Solid("#FFD7A655") xysize ((1180, 2) if mobile else (860, 2))

            $ file_slot_cols = 2 if mobile else 3
            $ file_slot_rows = 3 if mobile else 2

            grid file_slot_cols file_slot_rows:
                spacing (20 if mobile else 22)
                xalign 0.5

                for slot in range(1, 7):
                    $ slot_loadable = FileLoadable(slot)
                    $ slot_newest = FileNewest(slot) if slot_loadable else False
                    $ slot_chapter = FileJson(slot, "chapter_title", empty="", missing="")
                    $ slot_runtime = format_save_runtime(FileJson(slot, "_game_runtime", empty=None, missing=None))
                    if not slot_chapter:
                        $ slot_chapter = FileSaveName(slot, empty="")

                    button:
                        action FileAction(slot)
                        sensitive (slot_loadable or not is_load_screen)
                        xysize ((760, 200) if mobile else (456, 270))
                        background Frame("images/ui/chapter_panel.png" if slot_newest else "images/ui/menu_panel.png", 28, 28)
                        hover_background Frame("images/ui/chapter_panel.png", 28, 28)
                        insensitive_background Frame("images/ui/menu_panel.png", 28, 28)
                        padding ((18, 14) if mobile else (16, 14))

                        if mobile:
                            hbox:
                                spacing 18
                                frame:
                                    xysize (250, 150)
                                    background ("#070309E8" if slot_loadable else "#100811E8")
                                    padding (6, 6)
                                    if slot_loadable:
                                        viewport:
                                            xysize (238, 138)
                                            add FileScreenshot(slot):
                                                xysize (238, 138)
                                                fit "cover"
                                    else:
                                        fixed:
                                            xysize (238, 138)
                                            add Solid("#0B050DE8")
                                            text "NO SAVE":
                                                size 22
                                                color "#FFD8BB"
                                                bold True
                                                xalign 0.5
                                                yalign 0.42
                                            text "Ready for a new memory":
                                                size 17
                                                color "#BFAAA5"
                                                xalign 0.5
                                                yalign 0.64
                                vbox:
                                    spacing 8
                                    yalign 0.5
                                    xsize 440
                                    hbox:
                                        xfill True
                                        text ("Slot %02d" % slot) size 29 color "#FFD8BB" bold True yalign 0.5
                                        if slot_newest:
                                            text "Latest" size 20 color "#FFD8BB" xalign 1.0 yalign 0.5
                                    if slot_loadable:
                                        text slot_chapter size 23 color "#FFF8F2" xmaximum 430
                                        text FileTime(slot, format="%b %d, %Y  %H:%M", empty="") size 21 color "#FFD8BB"
                                        if slot_runtime:
                                            text slot_runtime size 19 color "#BFAAA5"
                                    else:
                                        text ("Tap to save here" if not is_load_screen else "No memory saved here yet") size 23 color "#FFF8F2" xmaximum 430
                                        text ("This slot is empty" if not is_load_screen else "Choose a filled slot to return") size 20 color "#BFAAA5" xmaximum 430
                        else:
                            vbox:
                                spacing 10
                                frame:
                                    xysize (424, 132)
                                    background ("#070309E8" if slot_loadable else "#100811E8")
                                    padding (6, 6)
                                    if slot_loadable:
                                        viewport:
                                            xysize (412, 120)
                                            add FileScreenshot(slot):
                                                xysize (412, 120)
                                                fit "cover"
                                    else:
                                        fixed:
                                            xysize (412, 120)
                                            add Solid("#0B050DE8")
                                            add Solid("#FFD7A622"):
                                                xalign 0.5
                                                yalign 0.5
                                                xysize (280, 1)
                                            text "NO SAVE":
                                                size 25
                                                color "#FFD8BB"
                                                bold True
                                                xalign 0.5
                                                yalign 0.40
                                            text "Ready for a new memory":
                                                size 18
                                                color "#BFAAA5"
                                                xalign 0.5
                                                yalign 0.65
                                hbox:
                                    xfill True
                                    text ("Slot %02d" % slot) size 23 color "#FFD8BB" bold True yalign 0.5
                                    if slot_newest:
                                        text "Latest" size 16 color "#FFD8BB" xalign 1.0 yalign 0.5
                                    elif slot_loadable:
                                        text FileTime(slot, format="%b %d, %Y  %H:%M", empty="") size 18 color "#FFD8BB" xalign 1.0 yalign 0.5
                                if slot_loadable:
                                    text slot_chapter size 18 color "#FFF8F2" xmaximum 410
                                    if slot_runtime:
                                        text slot_runtime size 17 color "#BFAAA5" xmaximum 410
                                else:
                                    text ("Tap to save here" if not is_load_screen else "No memory saved here yet") size 19 color "#FFF8F2" xmaximum 410

            hbox:
                spacing (16 if mobile else 14)
                xalign 0.5

                use file_page_button("<", FilePagePrevious())
                use file_page_button("Auto", FilePage("auto"), selected=(current_page == "auto"), wide=True)
                use file_page_button("Quick", FilePage("quick"), selected=(current_page == "quick"), wide=True)

                for page in range(1, 6):
                    use file_page_button(str(page), FilePage(page), selected=(current_page == str(page)))

                use file_page_button(">", FilePageNext())

screen confirm(message, yes_action, no_action):
    $ mobile = audit_force_mobile_layout or renpy.variant("small") or renpy.variant("touch")
    modal True
    zorder 200

    add Solid("#050007CC")
    add "cinematic_vignette"
    add Solid("#05000766")

    frame:
        xalign 0.5
        yalign 0.5
        xysize ((1180, 500) if mobile else (900, 430))
        background Frame("images/ui/chapter_panel.png", 34, 34)
        padding ((76, 60) if mobile else (66, 52))
        vbox:
            spacing (28 if mobile else 24)
            xalign 0.5
            yalign 0.5
            text "Pause the Story?" size (54 if mobile else 48) color "#FFF8F2" xalign 0.5 text_align 0.5
            text message size (31 if mobile else 26) color "#FFD8BB" xalign 0.5 text_align 0.5
            add Solid("#FFD7A655") xysize ((720, 2) if mobile else (560, 2)) xalign 0.5
            hbox:
                spacing (34 if mobile else 26)
                xalign 0.5
                use compact_button("Yes", yes_action)
                use compact_button("No", no_action)

    key "game_menu" action no_action

screen final_message(message, button):
    $ mobile = audit_force_mobile_layout or renpy.variant("small") or renpy.variant("touch")
    $ recap_lines = final_choice_recap_lines()
    modal True
    add Solid("#050007E8")
    add "cinematic_vignette"
    frame:
        xalign 0.5
        yalign 0.48
        xysize ((1540, 760) if mobile else (1280, 620))
        background Frame("images/ui/chapter_panel.png", 34, 34)
        padding ((88, 62) if mobile else (84, 56))
        vbox:
            spacing (22 if mobile else 18)
            xalign 0.5
            yalign 0.5
            text "Forever, Again" size (62 if mobile else 56) color "#FFF8F2" xalign 0.5 text_align 0.5
            add Solid("#FFD7A666") xysize ((720, 2) if mobile else (520, 2)) xalign 0.5
            text message size (48 if mobile else 44) color "#FFEDE1" xalign 0.5 text_align 0.5 xmaximum (1280 if mobile else 1000) line_spacing 5
            if recap_lines:
                frame:
                    xalign 0.5
                    xysize ((1230, 250) if mobile else (1020, 188))
                    background "#05000777"
                    padding ((34, 22) if mobile else (30, 18))
                    vbox:
                        spacing (7 if mobile else 5)
                        xalign 0.5
                        yalign 0.5
                        text "This version remembered:":
                            size (27 if mobile else 23)
                            color "#FFD8BB"
                            bold True
                            xalign 0.5
                            text_align 0.5
                        for line in recap_lines:
                            text line:
                                size (23 if mobile else 19)
                                color "#FFF8F2"
                                xalign 0.5
                                text_align 0.5
                                xmaximum (1120 if mobile else 900)
            else:
                null height 10
            use premium_button(button, MainMenu())

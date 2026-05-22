label visual_audit_gallery:
    $ preferences.text_cps = 0

    scene bg_ch1_room_night at chapter_card_static
    show prawal neutral at left_character, sprite_night
    n "Chapter 1: room night, Prawal intro composition."

    scene bg_ch1_laptop_closeup at chapter_card_static
    n "Chapter 1: laptop closeup focus shot."

    scene bg_ch2_social_profile at chapter_card_static
    show prawal thinking at left_character, sprite_cool
    n "Chapter 2: social profile with Prawal."

    scene bg_ch3_chat_room at chapter_card_static
    show prawal thinking at left_character, sprite_night
    n "Chapter 3: chat room."

    scene bg_ch4_office_full at chapter_card_static
    show aashna office_maroon_hoodie at right_character, sprite_warm
    show prawal office_neutral at left_character, sprite_warm
    p "It was the way she stood there like an ordinary morning had no idea it had become important."

    scene bg_ch4_aashna_closeup at chapter_card_static
    n "Chapter 4: Aashna closeup."

    scene cg_ch4_first_meeting at chapter_card_static
    n "Chapter 4: first meeting key CG."

    scene bg_ch5_office_day at chapter_card_static
    show prawal office_happy at left_character, sprite_golden
    show aashna office_neutral at right_character, sprite_golden
    n "Chapter 5: office day."

    scene bg_ch5_office_corridor at chapter_card_static
    show prawal office_happy at left_character, sprite_warm
    show aashna office_happy at right_character, sprite_warm
    n "Chapter 5: corridor help moment."

    scene bg_ch6_office_gift at chapter_card_static
    show prawal office_happy at left_character, sprite_golden
    show aashna office_surprised at right_character, sprite_golden
    show prop_earphones at prop_earphones_focus
    a "You noticed I needed them?"

    scene bg_ch7_restaurant at chapter_card_static
    show friend date_happy at date_friend_character, sprite_warm
    show prawal date_happy at date_left_character, sprite_warm
    show aashna date_happy at date_right_character, sprite_warm
    n "Chapter 7: restaurant with friend staged."

    scene bg_ch7_restaurant at chapter_card_static
    show prawal date_happy at date_left_character, sprite_warm
    show aashna date_happy at date_right_character, sprite_warm
    show friend date_happy at friend_peripheral_pos, sprite_warm
    n "Chapter 7: friend peripheral beat — tactful exit while Prawal and Aashna find their moment."

    scene bg_ch7_restaurant_window at chapter_card_static
    n "Chapter 7: restaurant window focus shot."

    scene bg_ch8_clearing at chapter_card_static
    show prawal date_neutral at left_character, sprite_golden
    show aashna date_shy at right_character, sprite_golden
    n "Chapter 8: clearing."

    scene bg_ch8_clearing_stars at chapter_card_static
    show prawal date_loving at left_character, sprite_night
    show aashna date_loving at right_character, sprite_night
    p "Something was quietly, beautifully growing between us."

    scene bg_ch9_garden_dawn at chapter_card_static
    show prawal date_loving at left_character, sprite_golden
    n "Chapter 9: garden dawn."

    scene bg_ch9_study_morning at chapter_card_static
    n "Chapter 9: study morning letters."

    scene bg_ch10_storm_outside at chapter_card_static
    show overlay_rain
    n "Chapter 10: storm outside."

    scene bg_ch10_storm_inside at chapter_card_static
    show prawal storm_neutral at storm_far_left_pos, sprite_storm
    show aashna storm_emotional at storm_far_right_pos, sprite_storm
    a "And sometimes I needed you to hear the feeling, not just the words."

    scene cg_ch10_reconciliation at chapter_card_static
    n "Chapter 10: reconciliation key CG."

    scene bg_ch11_apartment at chapter_card_static
    show prawal happy at left_character, sprite_warm
    n "Chapter 11: apartment."

    scene bg_ch11_gifts at chapter_card_static
    n "Chapter 11: keepsake box interface — gift items laid out in centered box UI."

    scene bg_ch11_gifts at chapter_card_static
    show prop_book at prop_book_focus
    n "Chapter 11: book prop."

    scene bg_ch11_gifts at chapter_card_static
    show prop_framed_photos at prop_photos_focus
    n "Chapter 11: framed photos prop."

    scene bg_ch11_gifts at chapter_card_static
    show prop_mug at prop_mug_focus
    n "Chapter 11: mug prop."

    scene bg_ch12_family at chapter_card_static
    show prawal family_happy at left_character, sprite_warm
    show aashna family_happy at right_character, sprite_warm
    n "Chapter 12: family."

    scene bg_ch12_letters at chapter_card_static
    n "Chapter 12: letters."

    scene bg_ch13_paths at chapter_card_static
    show prawal date_neutral at left_character, sprite_golden
    show aashna date_neutral at right_character, sprite_golden
    n "Chapter 13: paths."

    scene bg_ch13_dawn_ethereal at chapter_card_static
    show prawal date_loving at left_character, sprite_ethereal
    show aashna date_loving at right_character, sprite_ethereal
    n "Chapter 13: dawn ethereal."

    scene bg_ch14_engagement at chapter_card_static
    show prop_rings at prop_rings_focus
    n "First came the engagement."

    scene bg_ch14_wedding at chapter_card_static
    show prawal formal_loving at wedding_still_left_pos, sprite_golden
    show aashna formal_loving at wedding_still_right_pos, sprite_golden
    n "The aisle stretched ahead, bright with flowers and people trying not to cry too early."

    scene cg_ch14_vows at chapter_card_static
    n "Chapter 14: wedding vows key CG."

    scene bg_ch14_wedding_party at chapter_card_static
    n "Chapter 14: wedding party."

    scene bg_ch15_light at chapter_card_static
    show prawal formal_loving at wedding_still_left_pos, sprite_ethereal
    show aashna formal_loving at wedding_still_right_pos, sprite_ethereal
    n "Chapter 15: light."

    scene bg_ch15_floating at chapter_card_static
    show prawal formal_loving at wedding_still_left_pos, sprite_ethereal
    show aashna formal_loving at wedding_still_right_pos, sprite_ethereal
    p "Four years of choosing each other in ways too small for anyone else to notice."

    # Pass 2: cinematic say mode audit
    $ cinematic_mode = True
    scene cg_ch4_first_meeting at chapter_card_static
    p "She was brighter in person, but not in the way photos try to be."
    scene cg_ch10_reconciliation at chapter_card_static
    a "We are okay?"
    scene cg_ch14_vows at chapter_card_static
    n "There was laughter. There were tears. There were a hundred small things."
    scene bg_ch15_floating at chapter_card_static
    show prawal formal_loving at wedding_still_left_pos, sprite_ethereal
    show aashna formal_loving at wedding_still_right_pos, sprite_ethereal
    p "Happy 4th anniversary, Aashna. ❤"
    $ cinematic_mode = False

    # Pass 3: character blocking audit
    scene bg_ch10_storm_inside at chapter_card_static
    show prawal storm_neutral at storm_far_left_pos, sprite_storm
    show aashna storm_emotional at storm_far_right_pos, sprite_storm
    a "The space between them told the story before the words."

    scene bg_ch10_storm_inside at chapter_card_static
    show prawal storm_neutral at left_character, sprite_storm
    show aashna storm_emotional at right_character, sprite_storm
    p "But every single time, we came back to each other."

    scene bg_ch14_wedding at chapter_card_static
    show prawal formal_loving at wedding_still_left_pos, sprite_golden
    show aashna formal_loving at wedding_still_right_pos, sprite_golden
    n "And then they were still. Everything else moved around them."

    return

label _visual_audit_lint_anchor:
    pass

testcase visual_audit:
    $ _test.timeout = 120.0
    $ _test.transition_timeout = 0.1
    $ preferences.text_cps = 0
    $ renpy.unlink_save("_visual_audit_tmp-1")
    $ renpy.unlink_save("999-1")
    $ persistent._file_page = "1"
    $ persistent.current_chapter = 8
    $ persistent.max_unlocked_chapter = 8
    $ persistent.access_large_text = False
    $ persistent.access_high_contrast = False
    $ persistent.access_reduced_motion = False
    $ story_choice_leap = "courage"
    $ story_choice_gift = "daily"
    $ story_choice_closeness = "honesty"
    $ story_choice_repair = "patience"
    $ story_choice_promise = "everyday"
    $ audit_force_mobile_layout = False
    $ renpy.restart_interaction()

    advance until screen "main_menu"
    screenshot "visual_audit/00_main_menu.png"
    run Hide("main_menu")
    $ renpy.scene()
    run Show("cold_open_title", eyebrow="A MEMORY FROM THE END", title="Before the Beginning", subtitle="A few fragments of forever, then the day it started.")
    advance until screen "cold_open_title"
    screenshot "visual_audit/00u_cold_open_title.png"
    run Hide("cold_open_title")
    $ renpy.scene()
    $ renpy.show("cg_ch14_vows", at_list=[chapter_card_static])
    run Show("cold_open_caption", line="Before the first message, there was a promise waiting years ahead.")
    advance until screen "cold_open_caption"
    screenshot "visual_audit/00v_cold_open_wedding.png"
    run Hide("cold_open_caption")
    $ renpy.scene()
    $ renpy.show("bg_ch4_office_full", at_list=[chapter_card_static])
    $ renpy.show("aashna office_maroon_hoodie", at_list=[right_character, sprite_warm])
    run Show("cold_open_caption", line="A maroon hoodie. An ordinary morning. The moment memory became real.")
    advance until screen "cold_open_caption"
    screenshot "visual_audit/00w_cold_open_hoodie.png"
    run Hide("cold_open_caption")
    run ShowMenu("main_menu")
    advance until screen "main_menu"
    run ShowMenu("chapter_select")
    advance until screen "chapter_select"
    screenshot "visual_audit/00t_chapter_select.png"
    run ShowMenu("main_menu")
    advance until screen "main_menu"
    run Show("chapter_card", title="Chapter 8", subtitle="Something Real", settled=True)
    screenshot "visual_audit/00a_chapter_card.png"
    run Hide("chapter_card")
    run Show("chapter_card", title="Chapter 1", subtitle="A Face in the Feed", settled=True)
    screenshot "visual_audit/00aa_chapter_card_ch1.png"
    run Hide("chapter_card")
    run Show("chapter_card", title="Chapter 5", subtitle="Starting Over", settled=True)
    screenshot "visual_audit/00ab_chapter_card_ch5.png"
    run Hide("chapter_card")
    run Show("chapter_card", title="Chapter 14", subtitle="From Engagement to Forever", settled=True)
    screenshot "visual_audit/00ac_chapter_card_ch14.png"
    run Hide("chapter_card")
    run Hide("main_menu")
    $ renpy.scene()
    $ renpy.show("bg_ch2_social_profile", at_list=[chapter_card_static])
    run Show("choice_preview", question="What gave Prawal the courage to reach out?", options=["Her smile felt familiar.", "Not knowing her felt worse than being nervous."])
    advance until screen "choice_preview"
    screenshot "visual_audit/00j_emotional_choice.png"
    run Hide("choice_preview")
    run ShowMenu("main_menu")
    advance until screen "main_menu"
    run ShowMenu("memory_gallery")
    advance until screen "memory_gallery"
    screenshot "visual_audit/00b_memory_gallery.png"
    run Show("memory_photo_viewer", photo=memory_gallery_photos[1], index=1)
    advance until screen "memory_photo_viewer"
    screenshot "visual_audit/00bb_memory_viewer.png"
    run Hide("memory_photo_viewer")
    run Show("final_message", message="Four years… and I still fall in love with you every single day.", button="Play Again")
    advance until screen "final_message"
    screenshot "visual_audit/00g_final_message.png"
    run Hide("final_message")
    run ShowMenu("preferences")
    advance until screen "preferences"
    screenshot "visual_audit/00c_preferences.png"
    $ persistent.access_large_text = True
    $ persistent.access_high_contrast = True
    $ persistent.access_reduced_motion = True
    $ renpy.restart_interaction()
    screenshot "visual_audit/00r_accessibility_preferences.png"
    run Hide("preferences")
    $ renpy.scene()
    $ renpy.show("bg_ch2_social_profile", at_list=[chapter_card_static])
    run Show("choice_preview", question="What should this memory preserve?", options=["The courage to reach out.", "The quiet feeling that this mattered."])
    advance until screen "choice_preview"
    screenshot "visual_audit/00s_accessibility_choice.png"
    run Hide("choice_preview")
    $ persistent.access_large_text = False
    $ persistent.access_high_contrast = False
    $ persistent.access_reduced_motion = False
    run ShowMenu("preferences")
    advance until screen "preferences"
    run Show("file_slots", title="Save Memory", subtitle="Preserve this moment")
    advance until screen "file_slots"
    screenshot "visual_audit/00e_save.png"
    run Hide("file_slots")
    run Show("file_slots", title="Load Memory", subtitle="Return to a saved moment")
    advance until screen "file_slots"
    screenshot "visual_audit/00f_load.png"
    run Hide("file_slots")
    run ShowMenu("main_menu")
    advance until screen "main_menu"
    run Show("confirm", message="Are you sure you want to quit?", yes_action=NullAction(), no_action=Hide("confirm"))
    advance until screen "confirm"
    screenshot "visual_audit/00d_quit_confirm.png"
    run Hide("confirm")
    run ShowMenu("main_menu")
    advance until screen "main_menu"

    $ audit_force_mobile_layout = True
    $ persistent.access_reduced_motion = True
    $ renpy.restart_interaction()
    run ShowMenu("main_menu")
    advance until screen "main_menu"
    screenshot "visual_audit/00k_mobile_main_menu.png"
    run ShowMenu("chapter_select")
    advance until screen "chapter_select"
    screenshot "visual_audit/00u_mobile_chapter_select.png"
    run ShowMenu("main_menu")
    advance until screen "main_menu"
    run ShowMenu("memory_gallery")
    advance until screen "memory_gallery"
    screenshot "visual_audit/00l_mobile_memory_gallery.png"
    run Hide("memory_gallery")
    $ renpy.scene()
    $ renpy.show("bg_ch2_social_profile", at_list=[chapter_card_static])
    run Show("choice_preview", question="What gave Prawal the courage to reach out?", options=["Her smile felt familiar.", "Not knowing her felt worse than being nervous."])
    advance until screen "choice_preview"
    screenshot "visual_audit/00m_mobile_choice.png"
    run Hide("choice_preview")
    run ShowMenu("preferences")
    advance until screen "preferences"
    screenshot "visual_audit/00n_mobile_preferences.png"
    run Show("file_slots", title="Save Memory", subtitle="Preserve this moment")
    advance until screen "file_slots"
    screenshot "visual_audit/00o_mobile_save.png"
    run Hide("file_slots")
    run Hide("preferences")
    $ renpy.scene()
    $ renpy.show("bg_ch15_light", at_list=[chapter_card_static])
    run Show("final_message", message="Four years… and I choose you again in every ordinary day.", button="Play Again")
    advance until screen "final_message"
    screenshot "visual_audit/00p_mobile_final_message.png"
    run Hide("final_message")
    $ audit_force_mobile_layout = False
    $ persistent.access_reduced_motion = False
    $ renpy.restart_interaction()
    run ShowMenu("main_menu")
    advance until screen "main_menu"
    $ preferences.text_cps = 0
    $ renpy.scene()
    $ renpy.show("bg_ch1_room_night", at_list=[chapter_card_static])
    $ renpy.show("prawal neutral", at_list=[left_character, sprite_night])
    run Hide("say")
    run Show("say", who=None, what="Chapter 1: room night, Prawal intro composition.")
    advance until screen "say"
    run Show("quick_menu")
    advance until screen "quick_menu"
    screenshot "visual_audit/00h_quick_menu_story.png"
    run Hide("quick_menu")
    run Hide("say")
    run Start("visual_audit_gallery")

    screenshot "visual_audit/01_ch1_room_night.png"
    run Hide("quick_menu")
    run Hide("say")
    $ history_audit_entries = [("Prawal", "I kept coming back to that photo."), (None, "Chapter 1: room night, Prawal intro composition.")]
    run Show("history")
    advance until screen "history"
    screenshot "visual_audit/00i_history.png"
    run Hide("history")
    $ history_audit_entries = None
    run Hide("say")
    $ persistent.access_reduced_motion = True
    $ renpy.restart_interaction()
    run Show("hotspot_prompt", label="Find her in the glow", hx=0.61, hy=0.49, tone="inspect")
    advance until screen "hotspot_prompt"
    screenshot "visual_audit/01b_hotspot_laptop.png"
    run Hide("hotspot_prompt")
    $ persistent.access_reduced_motion = False
    $ renpy.restart_interaction()
    advance
    screenshot "visual_audit/02_ch1_laptop_closeup.png"
    advance
    screenshot "visual_audit/03_ch2_social_profile.png"
    run Hide("say")
    $ audit_ch2_items = [{"key": "photo", "label": "Find her in the photo", "hx": 0.63, "hy": 0.43, "tone": "inspect"}, {"key": "post", "label": "Follow the breadcrumb", "hx": 0.53, "hy": 0.60, "tone": "read"}, {"key": "add", "label": "Hover over Add Friend", "hx": 0.79, "hy": 0.62, "tone": "social"}]
    run Show("memory_interaction_map", title="One Click. One Leap.", instruction="Look closer. One memory is enough to begin.", items=audit_ch2_items, seen=["photo"], min_required=1)
    advance until screen "memory_interaction_map"
    screenshot "visual_audit/03c_memory_map_ch2.png"
    run Hide("memory_interaction_map")
    run Hide("say")
    run Show("hotspot_prompt", label="Hover over Add Friend", hx=0.79, hy=0.62, tone="social")
    advance until screen "hotspot_prompt"
    screenshot "visual_audit/03b_hotspot_add_friend.png"
    run Hide("hotspot_prompt")
    advance
    screenshot "visual_audit/04_ch3_chat_room.png"
    advance
    screenshot "visual_audit/05_ch4_office_full.png"
    run Hide("say")
    run Show("hotspot_prompt", label="See her for the first time", hx=0.72, hy=0.43, tone="inspect")
    advance until screen "hotspot_prompt"
    screenshot "visual_audit/05b_hotspot_maroon_hoodie.png"
    run Hide("hotspot_prompt")
    advance
    screenshot "visual_audit/06_ch4_aashna_closeup.png"
    advance
    screenshot "visual_audit/06b_ch4_first_meeting_cg.png"
    run Hide("say")
    run Show("signature_peak_caption", kicker="FIRST MEETING", line="Every later version of home walked into the room.")
    advance until screen "signature_peak_caption"
    screenshot "visual_audit/39_peak_first_meeting.png"
    run Hide("signature_peak_caption")
    advance
    screenshot "visual_audit/07_ch5_office_day.png"
    advance
    screenshot "visual_audit/08_ch5_office_corridor.png"
    advance
    screenshot "visual_audit/09_ch6_office_gift.png"
    run Hide("say")
    $ audit_ch6_items = [{"key": "wrap", "label": "Touch the wrapped box", "hx": 0.45, "hy": 0.58, "tone": "gift"}, {"key": "earphones", "label": "Untangle the earphones", "hx": 0.53, "hy": 0.57, "tone": "gift"}, {"key": "reaction", "label": "Watch her realise", "hx": 0.72, "hy": 0.42, "tone": "inspect"}]
    run Show("memory_interaction_map", title="Wireless & Heartstrings", instruction="Something here matters. Find it.", items=audit_ch6_items, seen=["earphones"], min_required=1)
    advance until screen "memory_interaction_map"
    screenshot "visual_audit/09b_memory_map_ch6.png"
    run Hide("memory_interaction_map")
    advance
    screenshot "visual_audit/10_ch7_restaurant.png"
    advance
    screenshot "visual_audit/38_ch7_friend_peripheral.png"
    advance
    screenshot "visual_audit/11_ch7_restaurant_window.png"
    advance
    screenshot "visual_audit/12_ch8_clearing.png"
    advance
    screenshot "visual_audit/13_ch8_clearing_stars.png"
    advance
    screenshot "visual_audit/14_ch9_garden_dawn.png"
    advance
    screenshot "visual_audit/15_ch9_study_morning.png"
    run Hide("say")
    $ audit_ch9_items = [{"key": "first", "label": "Read the first thought", "hx": 0.40, "hy": 0.54, "tone": "read"}, {"key": "saturday", "label": "Open a Saturday morning", "hx": 0.50, "hy": 0.48, "tone": "read"}, {"key": "hope", "label": "Find the fading hope", "hx": 0.58, "hy": 0.55, "tone": "read"}, {"key": "day200", "label": "Count day two hundred", "hx": 0.66, "hy": 0.47, "tone": "read"}, {"key": "last", "label": "Read the last letter", "hx": 0.75, "hy": 0.54, "tone": "read"}]
    run Show("memory_interaction_map", title="Letters, Every Morning", instruction="Read one. That's all you need.", items=audit_ch9_items, seen=["first", "hope"], min_required=1)
    advance until screen "memory_interaction_map"
    screenshot "visual_audit/15b_memory_map_ch9.png"
    run Hide("memory_interaction_map")
    advance
    screenshot "visual_audit/16_ch10_storm_outside.png"
    run Hide("say")
    run Show("hotspot_prompt", label="Step out of the rain", hx=0.81, hy=0.51, tone="storm")
    advance until screen "hotspot_prompt"
    screenshot "visual_audit/16b_hotspot_storm_entry.png"
    run Hide("hotspot_prompt")
    advance
    screenshot "visual_audit/17_ch10_storm_inside.png"
    advance
    screenshot "visual_audit/17b_ch10_reconciliation_cg.png"
    run Hide("say")
    run Show("signature_peak_caption", kicker="AFTER THE STORM", line="Love is the hand you choose when the rain gets loud.")
    advance until screen "signature_peak_caption"
    screenshot "visual_audit/40_peak_storm_reconciliation.png"
    run Hide("signature_peak_caption")
    advance
    screenshot "visual_audit/18_ch11_apartment.png"
    advance
    screenshot "visual_audit/19_ch11_book_prop.png"
    run Hide("say")
    $ audit_ch11_items = [{"key": "food", "label": "Order her favourite food", "hx": 0.35, "hy": 0.62, "tone": "open"}, {"key": "book", "label": "Hold the printed story", "hx": 0.51, "hy": 0.51, "tone": "open"}, {"key": "sorry", "label": "Send the late apology", "hx": 0.45, "hy": 0.61, "tone": "social"}, {"key": "photos", "label": "Hang the real moments", "hx": 0.56, "hy": 0.50, "tone": "inspect"}, {"key": "mug", "label": "Fill the morning mug", "hx": 0.50, "hy": 0.56, "tone": "gift"}]
    run Show("keepsake_box", title="Love in a Box", items=audit_ch11_items, seen=["book", "photos"], min_required=1)
    advance until screen "keepsake_box"
    screenshot "visual_audit/19c_keepsake_box_ch11.png"
    run Hide("keepsake_box")
    run Hide("say")
    run Show("hotspot_prompt", label="Hold the printed story", hx=0.51, hy=0.51, tone="open")
    advance until screen "hotspot_prompt"
    screenshot "visual_audit/19b_hotspot_book.png"
    run Hide("hotspot_prompt")
    advance
    screenshot "visual_audit/20_ch11_framed_photos_prop.png"
    advance
    screenshot "visual_audit/21_ch11_mug_prop.png"
    advance
    screenshot "visual_audit/22_ch12_family.png"
    advance
    screenshot "visual_audit/23_ch12_letters.png"
    run Hide("say")
    $ audit_ch12_items = [{"key": "mom", "label": "Open his mother's letter", "hx": 0.34, "hy": 0.48, "tone": "read"}, {"key": "dad", "label": "Read his father's words", "hx": 0.48, "hy": 0.43, "tone": "read"}, {"key": "sister", "label": "Unfold his sister's note", "hx": 0.61, "hy": 0.53, "tone": "read"}, {"key": "together", "label": "Hold it all together", "hx": 0.74, "hy": 0.45, "tone": "read"}]
    run Show("memory_interaction_map", title="Two Families, One Story", instruction="Read one. Let it land.", items=audit_ch12_items, seen=["mom"], min_required=1)
    advance until screen "memory_interaction_map"
    screenshot "visual_audit/23b_memory_map_ch12.png"
    run Hide("memory_interaction_map")
    advance
    screenshot "visual_audit/24_ch13_paths.png"
    advance
    screenshot "visual_audit/25_ch13_dawn_ethereal.png"
    advance
    screenshot "visual_audit/26_ch14_engagement_rings.png"
    advance
    screenshot "visual_audit/27_ch14_wedding.png"
    advance
    screenshot "visual_audit/27b_ch14_vows_cg.png"
    run Hide("say")
    run Show("signature_peak_caption", kicker="THE VOW", line="Forever begins when ordinary days become sacred.")
    advance until screen "signature_peak_caption"
    screenshot "visual_audit/41_peak_wedding_vow.png"
    run Hide("signature_peak_caption")
    advance
    screenshot "visual_audit/28_ch14_wedding_party.png"
    advance
    screenshot "visual_audit/29_ch15_light.png"
    advance
    screenshot "visual_audit/30_ch15_floating.png"
    advance
    screenshot "visual_audit/31_cinematic_say_cg_ch4.png"
    advance
    screenshot "visual_audit/32_cinematic_say_cg_ch10.png"
    advance
    screenshot "visual_audit/33_cinematic_say_cg_ch14.png"
    advance
    screenshot "visual_audit/34_cinematic_say_ch15_finale.png"
    advance
    screenshot "visual_audit/35_blocking_storm_distance.png"
    advance
    screenshot "visual_audit/36_blocking_storm_close.png"
    advance
    screenshot "visual_audit/37_blocking_wedding_still.png"

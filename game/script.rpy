# Auto-generated from ../anniversary-game/src/data/story.json.
# Regenerate with: node tools/build_from_story.js

label start:
    $ persistent.current_chapter = 1
    if not persistent.max_unlocked_chapter:
        $ persistent.max_unlocked_chapter = 1
    $ story_choice_leap = None
    $ story_choice_gift = None
    $ story_choice_closeness = None
    $ story_choice_repair = None
    $ story_choice_promise = None
    call opening_montage
    jump chapter_1

label continue_game:
    $ persistent.current_chapter = valid_chapter_number(getattr(persistent, "current_chapter", 1), 1)
    jump expression chapter_label_for_number(persistent.current_chapter)

label opening_montage:
    window hide
    stop ambience fadeout 0.8
    play music audio.music_forever_theme fadein 1.0
    play ambience audio.ambience_ethereal_light fadein 1.0
    $ set_audio_scene("finale")

    scene black with premium_fade
    show screen cold_open_title("A MEMORY FROM THE END", "Before the Beginning", "A few fragments of forever, then the day it started.")
    pause 2.4
    hide screen cold_open_title

    scene cg_ch14_vows at cg_cinematic with directed_transition("vow")
    show screen cold_open_caption("Before the first message, there was a promise waiting years ahead.")
    pause 1.9
    hide screen cold_open_caption

    scene bg_ch2_social_profile at bg_cinematic with directed_transition("digital")
    show screen cold_open_caption("Before forever, there was one impossible button.")
    pause 1.8
    hide screen cold_open_caption

    scene bg_ch1_laptop_closeup at bg_focus with directed_transition("lonely")
    show screen cold_open_caption("A screen in lockdown. A face he could not stop returning to.")
    pause 2.0
    hide screen cold_open_caption

    scene bg_ch4_office_full at bg_cinematic with directed_transition("office")
    show aashna office_maroon_hoodie at right_character, sprite_warm with premium_dissolve
    show screen cold_open_caption("A maroon hoodie. An ordinary morning. The moment memory became real.")
    pause 2.1
    hide screen cold_open_caption
    hide aashna

    scene bg_ch14_engagement at bg_focus with directed_transition("promise")
    show prop_rings at prop_rings_focus with premium_dissolve
    $ play_audio_cue(audio.sfx_ring_shimmer, "ring")
    show screen cold_open_caption("This is where the story is going.", "Tap or click to return to where it began.")
    pause

    hide screen cold_open_caption
    hide prop_rings
    scene black with premium_fade
    show screen cold_open_title("NOW", "2020", "Chapter 1: where the promise first became possible.")
    pause 2.0
    hide screen cold_open_title
    stop ambience fadeout 0.8
    return

label show_hotspot(prompt, hx=0.5, hy=0.54, tone="gold"):
    window hide
    call screen hotspot_prompt(prompt, hx, hy, tone)
    window auto
    return

label chapter_1:
    $ mark_chapter_unlocked(1)
    stop ambience fadeout 1.0
    play music audio.music_lonely_signal fadein 1.5
    play ambience audio.ambience_city_night fadein 1.2
    $ set_audio_scene("lonely_room")
    $ play_audio_cue(audio.sfx_chapter_reveal, "chapter")
    call show_chapter_card("Chapter 1", "A Face in the Feed")
    scene bg_ch1_room_night at bg_cinematic with directed_transition("lonely")
    show prawal neutral at left_character, sprite_night with premium_dissolve
    # ch1_intro
    voice "audio/voice/narrator/chapter_1_001_narrator_c584d5a66f.ogg" # auto-generated voice
    n "It was 2020. The world had paused."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_1_002_narrator_6c3cbb4bc6.ogg" # auto-generated voice
    n "Everyone was home. Screens were our only windows to the world outside."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_1_003_narrator_d3cae5e687.ogg" # auto-generated voice
    n "And somewhere in that digital silence… Prawal found her."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    call show_hotspot("Find her in the glow", 0.61, 0.49, "inspect")
    $ play_audio_cue(audio.sfx_ui_chime, "ui")
    scene bg_ch1_laptop_closeup at bg_focus with directed_transition("digital")
    # ch1_found
    voice "audio/voice/prawal/chapter_1_004_prawal_4f5a0f49fc.ogg" # auto-generated voice
    p "Our company had organised an online event during the lockdown."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_1_005_prawal_7d61430e2d.ogg" # auto-generated voice
    p "Aashna was in one of the photos from the post."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_1_006_prawal_5a2666db6e.ogg" # auto-generated voice
    p "Something stopped me. I kept coming back to that photo."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_1_007_prawal_d52894a429.ogg" # auto-generated voice
    p "There was something about her smile… I couldn't explain it."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_1_008_prawal_3b481565ef.ogg" # auto-generated voice
    p "I didn't even know Aashna's name yet."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_1_009_prawal_bb8e6a48b6.ogg" # auto-generated voice
    p "But I already wanted to."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    jump chapter_2

label chapter_2:
    $ mark_chapter_unlocked(2)
    stop ambience fadeout 1.0
    play music audio.music_digital_spark fadeout 1.0 fadein 1.2
    play ambience audio.ambience_digital_room fadein 1.0
    $ set_audio_scene("digital")
    $ play_audio_cue(audio.sfx_chapter_reveal, "chapter")
    call show_chapter_card("Chapter 2", "One Click. One Leap.")
    scene bg_ch2_social_profile at bg_cinematic with directed_transition("digital")
    show prawal thinking at enter_left, sprite_cool
    # ch2_intro
    voice "audio/voice/prawal/chapter_2_001_prawal_8d3f0020e3.ogg" # auto-generated voice
    p "I searched. LinkedIn first. Then Facebook."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_2_002_prawal_e5f7371a05.ogg" # auto-generated voice
    p "And there she was. Same face. Same smile."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    menu:
        "What gave Prawal the courage to reach out?"
        "Her smile felt familiar.":
            $ story_choice_leap = "smile"
            voice "audio/voice/prawal/chapter_2_003_prawal_def726055e.ogg" # auto-generated voice
            p "Maybe it was that smile. Familiar before it had any right to be."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
        "Not knowing her felt worse than being nervous.":
            $ story_choice_leap = "courage"
            voice "audio/voice/prawal/chapter_2_004_prawal_060ace528c.ogg" # auto-generated voice
            p "The nervousness was real. But the thought of never knowing her felt worse."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
    $ ch2_seen = []
    $ ch2_done = False
    $ ch2_items = [
        {"key": "photo", "label": "Find her in the photo", "hx": 0.63, "hy": 0.43, "tone": "inspect"},
        {"key": "post", "label": "Follow the breadcrumb", "hx": 0.53, "hy": 0.60, "tone": "read"},
        {"key": "add", "label": "Hover over Add Friend", "hx": 0.79, "hy": 0.62, "tone": "social"},
    ]
    while not ch2_done:
        window hide
        call screen memory_interaction_map("One Click. One Leap.", "Look closer. One memory is enough to begin.", ch2_items, ch2_seen, 1)
        window auto
        $ ch2_result = _return
        if ch2_result[0] == "continue":
            $ ch2_done = True
        elif ch2_result[1] == "photo":
            $ ch2_seen.append("photo") if "photo" not in ch2_seen else None
            voice "audio/voice/prawal/chapter_2_005_prawal_598757f7f6.ogg" # auto-generated voice
            p "It was the same smile from the office event photo."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_2_006_prawal_d9b527ee4b.ogg" # auto-generated voice
            p "Only now, it felt closer. Like the screen had quietly opened a door."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
        elif ch2_result[1] == "post":
            $ ch2_seen.append("post") if "post" not in ch2_seen else None
            voice "audio/voice/prawal/chapter_2_007_prawal_3bfae10bd1.ogg" # auto-generated voice
            p "The company post was ordinary to everyone else."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_2_008_prawal_49d78a1d5e.ogg" # auto-generated voice
            p "To me, it became a breadcrumb I couldn't ignore."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
        elif ch2_result[1] == "add":
            $ ch2_seen.append("add") if "add" not in ch2_seen else None
            $ play_audio_cue(audio.sfx_add_friend, "message")
            voice "audio/voice/prawal/chapter_2_009_prawal_1d84ec6c5c.ogg" # auto-generated voice
            p "My cursor hovered over Add Friend like it was the biggest decision of lockdown."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause

    # ch2_request
    if "add" not in ch2_seen:
        $ play_audio_cue(audio.sfx_add_friend, "message")
        voice "audio/voice/prawal/chapter_2_010_prawal_1fa232ee7f.ogg" # auto-generated voice
        p "Eventually, I clicked Add Friend."
        voice sustain # auto-generated voice sustain
        $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_2_011_prawal_4a3642e681.ogg" # auto-generated voice
    p "I stared at that Add Friend button for longer than I'd like to admit."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_2_012_prawal_cd3ed244bc.ogg" # auto-generated voice
    p "What if Aashna doesn't accept? What if she thinks it's weird?"
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_2_013_prawal_ccb5a9802c.ogg" # auto-generated voice
    p "One breath. One click."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    $ play_audio_cue(audio.sfx_message_ping, "message")
    voice "audio/voice/aashna/chapter_2_014_aashna_62aa643125.ogg" # auto-generated voice
    a "✓ Friend request accepted."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_2_015_prawal_c310c2d184.ogg" # auto-generated voice
    p "That one small notification changed the course of everything."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    jump chapter_3

label chapter_3:
    $ mark_chapter_unlocked(3)
    stop ambience fadeout 1.0
    play music audio.music_digital_spark fadeout 1.0 fadein 1.2
    play ambience audio.ambience_digital_room fadein 1.0
    $ set_audio_scene("digital")
    $ play_audio_cue(audio.sfx_chapter_reveal, "chapter")
    call show_chapter_card("Chapter 3", "Hello… and Goodbye")
    scene bg_ch3_chat_room at bg_cinematic with directed_transition("digital")
    show prawal thinking at enter_left, sprite_night
    # ch3_intro
    voice "audio/voice/narrator/chapter_3_001_narrator_e8dde467d1.ogg" # auto-generated voice
    n "Connected. Friends on a screen."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_3_002_narrator_439de60a07.ogg" # auto-generated voice
    n "The messages began — hesitant, then warm."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_3_003_narrator_59d4a11685.ogg" # auto-generated voice
    n "Read the messages, one by one."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    call show_hotspot("Read the messages, one by one", 0.78, 0.49, "social")
    $ play_audio_cue(audio.sfx_message_ping, "message")

    # ch3_chat
    voice "audio/voice/prawal/chapter_3_004_prawal_d9922c2737.ogg" # auto-generated voice
    p "We started talking. Small things at first."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/aashna/chapter_3_005_aashna_aceef3f20f.ogg" # auto-generated voice
    a "How's work? How's the lockdown treating you?"
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_3_006_prawal_3a61f7bbeb.ogg" # auto-generated voice
    p "Slowly… we found a rhythm."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_3_007_prawal_c548cc2c05.ogg" # auto-generated voice
    p "And then life happened. The conversations faded."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_3_008_prawal_3c469a6d1c.ogg" # auto-generated voice
    p "Weeks went by. Then months."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_3_009_narrator_62298e0c61.ogg" # auto-generated voice
    n "Silence."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_3_010_prawal_67ab4e3ce9.ogg" # auto-generated voice
    p "But I thought about Aashna more than I should have."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_3_011_prawal_35116499a9.ogg" # auto-generated voice
    p "Some stories aren't done yet. They just… pause."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    jump chapter_4

label chapter_4:
    $ mark_chapter_unlocked(4)
    stop ambience fadeout 1.0
    play music audio.music_office_warmth fadeout 1.0 fadein 1.2
    play ambience audio.ambience_office_air fadein 1.2
    $ set_audio_scene("office")
    $ play_audio_cue(audio.sfx_chapter_reveal, "chapter")
    call show_chapter_card("Chapter 4", "The Girl in the Hoodie")
    scene bg_ch4_office_full at bg_cinematic with directed_transition("office")
    show aashna office_maroon_hoodie at already_right, sprite_warm
    show prawal office_neutral at enter_left, sprite_warm
    # ch5_intro
    voice "audio/voice/narrator/chapter_4_001_narrator_54db2e8af3.ogg" # auto-generated voice
    n "Months passed. Lockdown loosened in careful inches."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_4_002_narrator_9772c2a675.ogg" # auto-generated voice
    n "The office reopened in shifts: half-lit floors, spaced-out desks, sanitizer at every door."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_4_003_narrator_068a4fb19d.ogg" # auto-generated voice
    n "Prawal walked in expecting another quiet roster day."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    call show_hotspot("See her for the first time", 0.72, 0.43, "inspect")
    $ play_audio_cue(audio.sfx_ui_chime, "ui")
    scene bg_ch4_aashna_closeup at bg_focus with directed_transition("focus")
    # ch5_meet
    voice "audio/voice/prawal/chapter_4_004_prawal_7f1a822ad0.ogg" # auto-generated voice
    p "And then the room changed."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    $ play_audio_cue(audio.sfx_ui_chime, "ui")
    pause 0.35
    scene cg_ch4_first_meeting at cg_signature_peak with directed_transition("promise")
    show screen signature_peak_caption("FIRST MEETING", "Every later version of home walked into the room.")
    pause 1.2
    hide screen signature_peak_caption with premium_dissolve
    $ cinematic_mode = True
    voice "audio/voice/prawal/chapter_4_005_prawal_d58d5aa99a.ogg" # auto-generated voice
    p "Not a photo. Not a screen. Not a name I had searched at midnight."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_4_006_prawal_3928d97004.ogg" # auto-generated voice
    p "Aashna."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_4_007_prawal_006a164b96.ogg" # auto-generated voice
    p "Standing there in that maroon hoodie."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/aashna/chapter_4_008_aashna_dfe655b94c.ogg" # auto-generated voice
    a "Hi."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_4_009_prawal_24ada22cf5.ogg" # auto-generated voice
    p "That was all she said. One small word."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_4_010_prawal_ecb4fcc14e.ogg" # auto-generated voice
    p "And somehow I forgot every normal way to answer."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_4_011_prawal_195f728b27.ogg" # auto-generated voice
    p "Every later version of home had just walked into the room."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_4_012_prawal_026cf0c285.ogg" # auto-generated voice
    p "She was brighter in person, but not in the way photos try to be."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_4_013_prawal_3f3f048ceb.ogg" # auto-generated voice
    p "It was the way she stood there like an ordinary morning had no idea it had become important."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_4_014_prawal_20f9a24192.ogg" # auto-generated voice
    p "I didn't say much that day."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_4_015_prawal_55c4a3838a.ogg" # auto-generated voice
    p "But I remembered the hoodie. The smile. The exact second my story started moving again."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    $ cinematic_mode = False
    jump chapter_5

label chapter_5:
    $ mark_chapter_unlocked(5)
    stop ambience fadeout 1.0
    play music audio.music_office_warmth fadeout 1.0 fadein 1.2
    play ambience audio.ambience_office_air fadein 1.2
    $ set_audio_scene("office")
    $ play_audio_cue(audio.sfx_chapter_reveal, "chapter")
    call show_chapter_card("Chapter 5", "Starting Over")
    scene bg_ch5_office_day at bg_cinematic with directed_transition("office")
    show prawal office_happy at enter_left, sprite_golden
    show aashna office_neutral at enter_right, sprite_golden
    # ch6_intro
    voice "audio/voice/narrator/chapter_5_001_narrator_4228303ace.ogg" # auto-generated voice
    n "Back at the office. The same desks, the same screens."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_5_002_narrator_97be88d8db.ogg" # auto-generated voice
    n "But something had changed. Prawal found reasons to be near her."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_5_003_narrator_2be0124b85.ogg" # auto-generated voice
    n "Walk over. She could use some help."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    call show_hotspot("Find a reason to walk over", 0.70, 0.55, "walk")
    $ play_audio_cue(audio.sfx_ui_chime, "ui")
    scene bg_ch5_office_corridor at bg_cinematic with directed_transition("office")
    show prawal office_happy at left_character, sprite_warm with premium_dissolve
    show aashna office_happy at right_character, sprite_warm with premium_dissolve
    # ch6_help
    voice "audio/voice/prawal/chapter_5_004_prawal_4fb97e2ba9.ogg" # auto-generated voice
    p "After that office day, something shifted."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_5_005_prawal_30023226c2.ogg" # auto-generated voice
    p "We started talking again. Properly this time."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_5_006_prawal_685338b616.ogg" # auto-generated voice
    p "Little chats. A question here. A favour there."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/aashna/chapter_5_007_aashna_5d50431149.ogg" # auto-generated voice
    a "Hey, can you help me with something at work?"
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_5_008_prawal_e5649e0a2c.ogg" # auto-generated voice
    p "I jumped at every chance — not just to help…"
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_5_009_prawal_44342beef3.ogg" # auto-generated voice
    p "But just to have a reason to talk to Aashna."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_5_010_prawal_7e035aa5a7.ogg" # auto-generated voice
    p "Every small moment with her felt like something worth holding onto."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    jump chapter_6

label chapter_6:
    $ mark_chapter_unlocked(6)
    stop ambience fadeout 1.0
    play music audio.music_office_warmth fadeout 1.0 fadein 1.2
    play ambience audio.ambience_office_air fadein 1.2
    $ set_audio_scene("office")
    $ play_audio_cue(audio.sfx_chapter_reveal, "chapter")
    call show_chapter_card("Chapter 6", "Wireless & Heartstrings")
    scene bg_ch6_office_gift at bg_cinematic with directed_transition("gift")
    show prawal office_happy at enter_left, sprite_golden
    show aashna office_surprised at enter_right, sprite_golden
    # ch7_intro
    voice "audio/voice/narrator/chapter_6_001_narrator_1973e8a760.ogg" # auto-generated voice
    n "The office evening settled into a soft hum of keyboards, paper cups, and tired ceiling lights."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_6_002_narrator_1a3c42bb25.ogg" # auto-generated voice
    n "Prawal had hidden a small wrapped box near her desk."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_6_003_narrator_ed01771a4f.ogg" # auto-generated voice
    n "It was practical. It was nervous. It was louder than he meant it to be."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_6_004_narrator_ea5dc06cbb.ogg" # auto-generated voice
    n "Open the surprise on her desk."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    menu:
        "What made this gift matter?"
        "It was something she could use every day.":
            $ story_choice_gift = "daily"
            voice "audio/voice/prawal/chapter_6_005_prawal_bfd8543a4d.ogg" # auto-generated voice
            p "I wanted the gift to live in her routine, not disappear after the wrapping came off."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
        "It said what I was too shy to say.":
            $ story_choice_gift = "unsaid"
            voice "audio/voice/prawal/chapter_6_006_prawal_fb3e43b226.ogg" # auto-generated voice
            p "The wrapping was doing the talking for me, because I still couldn't."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
    $ ch6_seen = []
    $ ch6_done = False
    $ ch6_items = [
        {"key": "wrap", "label": "Touch the wrapped box", "hx": 0.45, "hy": 0.58, "tone": "gift"},
        {"key": "earphones", "label": "Untangle the earphones", "hx": 0.53, "hy": 0.57, "tone": "gift"},
        {"key": "reaction", "label": "Watch her realise", "hx": 0.72, "hy": 0.42, "tone": "inspect"},
    ]
    while not ch6_done:
        window hide
        call screen memory_interaction_map("Wireless & Heartstrings", "Something here matters. Find it.", ch6_items, ch6_seen, 1)
        window auto
        $ ch6_result = _return
        if ch6_result[0] == "continue":
            $ ch6_done = True
        elif ch6_result[1] == "wrap":
            $ ch6_seen.append("wrap") if "wrap" not in ch6_seen else None
            $ play_audio_cue(audio.sfx_gift_open, "gift")
            voice "audio/voice/prawal/chapter_6_007_prawal_2101cd5935.ogg" # auto-generated voice
            p "I folded the paper too carefully for a pair of earphones."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_6_008_prawal_083374c69a.ogg" # auto-generated voice
            p "Maybe because my hands knew what my mouth still didn't."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
        elif ch6_result[1] == "earphones":
            $ ch6_seen.append("earphones") if "earphones" not in ch6_seen else None
            $ play_audio_cue(audio.sfx_gift_open, "gift")
            show prop_earphones at prop_earphones_focus with premium_dissolve
            voice "audio/voice/prawal/chapter_6_009_prawal_c442ba6102.ogg" # auto-generated voice
            p "Earphones. Small, useful, almost too simple."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_6_010_prawal_e3f9bbedf0.ogg" # auto-generated voice
            p "But I could picture them in her bag, beside her laptop, becoming part of her day."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
        elif ch6_result[1] == "reaction":
            $ ch6_seen.append("reaction") if "reaction" not in ch6_seen else None
            voice "audio/voice/aashna/chapter_6_011_aashna_1bd06bfe55.ogg" # auto-generated voice
            a "Wait... this is for me?"
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_6_012_prawal_a96af4c553.ogg" # auto-generated voice
            p "The second she understood, the whole room felt warmer."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
    if "earphones" not in ch6_seen:
        show prop_earphones at prop_earphones_focus with premium_dissolve

    # ch6_gift
    voice "audio/voice/prawal/chapter_6_013_prawal_16eccbb5e9.ogg" # auto-generated voice
    p "I tried to act casual when she opened it."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_6_014_prawal_b03668dca1.ogg" # auto-generated voice
    p "Like I hadn't checked the box three times before giving it to her."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/aashna/chapter_6_015_aashna_d4bef5f444.ogg" # auto-generated voice
    a "Prawal... these are really nice."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/aashna/chapter_6_016_aashna_36ee330fb2.ogg" # auto-generated voice
    a "You noticed I needed them?"
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_6_017_prawal_f1b89ce9f5.ogg" # auto-generated voice
    p "Of course I noticed."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_6_018_prawal_b478467719.ogg" # auto-generated voice
    p "And then, that same evening, the earphones stayed behind at the office."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/aashna/chapter_6_019_aashna_3bd9954aff.ogg" # auto-generated voice
    a "I remembered when I reached home. I called. I checked. They were just... gone."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_6_020_prawal_d2fe85c370.ogg" # auto-generated voice
    p "She was really sad. Almost crying, even while she tried to stay composed."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_6_021_prawal_c05ccf26b3.ogg" # auto-generated voice
    p "I made up my mind instantly."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_6_022_prawal_5a82b5ed22.ogg" # auto-generated voice
    p "So I bought the exact same pair again."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/aashna/chapter_6_023_aashna_b6503dae51.ogg" # auto-generated voice
    a "You did not."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_6_024_prawal_69c3697221.ogg" # auto-generated voice
    p "I did."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_6_025_prawal_5b7bf2cfb6.ogg" # auto-generated voice
    p "Because the gift was never really the earphones."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_6_026_prawal_b146e209d8.ogg" # auto-generated voice
    p "It was that smile coming back."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    jump chapter_7

label chapter_7:
    $ mark_chapter_unlocked(7)
    stop ambience fadeout 1.0
    play music audio.music_date_night fadeout 1.0 fadein 1.4
    play ambience audio.ambience_restaurant_warm fadein 1.3
    $ set_audio_scene("date")
    $ play_audio_cue(audio.sfx_chapter_reveal, "chapter")
    call show_chapter_card("Chapter 7", "Pizza & New Beginnings")
    scene bg_ch7_restaurant at bg_cinematic with directed_transition("date")
    show friend date_happy at date_friend_character, sprite_warm with premium_dissolve
    show prawal date_happy at date_left_character, sprite_warm with premium_dissolve
    show aashna date_happy at date_right_character, sprite_warm with premium_dissolve
    # ch8_intro
    voice "audio/voice/narrator/chapter_7_001_narrator_8f39007d2b.ogg" # auto-generated voice
    n "A pizza place near the metro, just outside the office."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_7_002_narrator_a1a3ab480b.ogg" # auto-generated voice
    n "They'd decided that afternoon — just the two of them and a friend."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_7_003_narrator_34da5c8fda.ogg" # auto-generated voice
    n "Nothing planned. Nothing fancy."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_7_004_narrator_8c7f332ab5.ogg" # auto-generated voice
    n "The table is set. She's already waiting."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    call show_hotspot("Take the first step outside", 0.51, 0.60, "walk")
    $ play_audio_cue(audio.sfx_ui_chime, "ui")

    # ch7_pizza
    voice "audio/voice/prawal/chapter_7_005_prawal_5144028642.ogg" # auto-generated voice
    p "The day I gave Aashna the second pair of earphones…"
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_7_006_prawal_b3d687e574.ogg" # auto-generated voice
    p "We decided to go out after office. Just like that."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_7_007_prawal_ae60f83b23.ogg" # auto-generated voice
    p "Aashna, me, and a friend."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_7_008_prawal_138833b89a.ogg" # auto-generated voice
    p "A small pizza place. Nothing fancy."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_7_009_prawal_5bb063719e.ogg" # auto-generated voice
    p "But it was our first time outside together."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_7_010_prawal_f304f4610d.ogg" # auto-generated voice
    p "Our first real evening."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/aashna/chapter_7_011_aashna_662c152ce1.ogg" # auto-generated voice
    a "This is really nice… we should do this more often."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_7_012_narrator_bd354f7fbe.ogg" # auto-generated voice
    n "Their friend glanced between them once."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_7_013_narrator_20827a2c75.ogg" # auto-generated voice
    n "The kind of glance that means everything and says nothing out loud."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    show friend date_happy at friend_peripheral, sprite_warm with premium_dissolve
    voice "audio/voice/narrator/chapter_7_014_narrator_221da4574d.ogg" # auto-generated voice
    n "'I should go check on that dessert situation. Entirely alone.'"
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    hide friend with premium_dissolve
    voice "audio/voice/prawal/chapter_7_015_prawal_6092c3e2fe.ogg" # auto-generated voice
    p "Something about that evening just… felt right."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_7_016_prawal_88183648ec.ogg" # auto-generated voice
    p "Like we'd always been doing this."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    scene bg_ch7_restaurant_window at bg_focus with directed_transition("focus")
    voice "audio/voice/narrator/chapter_7_017_narrator_1a54abe8fe.ogg" # auto-generated voice
    n "Outside, the world was just beginning to glow."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_7_018_narrator_386c777748.ogg" # auto-generated voice
    n "Inside, two hearts were finding each other."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    jump chapter_8

label chapter_8:
    $ mark_chapter_unlocked(8)
    stop ambience fadeout 1.0
    play music audio.music_starlit_confession fadeout 1.0 fadein 1.5
    play ambience audio.ambience_garden_night fadein 1.4
    $ set_audio_scene("starlit")
    $ play_audio_cue(audio.sfx_chapter_reveal, "chapter")
    call show_chapter_card("Chapter 8", "Something Real")
    scene bg_ch8_clearing at bg_cinematic with directed_transition("date")
    show prawal date_neutral at left_character, sprite_golden with premium_dissolve
    show aashna date_shy at right_character, sprite_golden with premium_dissolve
    # ch9_intro
    voice "audio/voice/narrator/chapter_8_001_narrator_2e8eafb674.ogg" # auto-generated voice
    n "Somewhere between late replies, long calls, and quiet good mornings, the shape of them changed."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_8_002_narrator_6e3c39f614.ogg" # auto-generated voice
    n "Not suddenly. Not like a movie."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_8_003_narrator_9bfc69ec65.ogg" # auto-generated voice
    n "More like a room slowly filling with sunlight."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_8_004_narrator_eec7a2b98a.ogg" # auto-generated voice
    n "Walk through it. Something real is waiting."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    call show_hotspot("Let it be something real", 0.50, 0.63, "walk")
    $ play_audio_cue(audio.sfx_ui_chime, "ui")

    # ch8_growth
    voice "audio/voice/prawal/chapter_8_005_prawal_4cebc5c571.ogg" # auto-generated voice
    p "After that evening, I stopped checking the time before messaging her."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_8_006_prawal_8660c65eec.ogg" # auto-generated voice
    p "She stopped needing a reason to call."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/aashna/chapter_8_007_aashna_4d2c3c250f.ogg" # auto-generated voice
    a "Sometimes I would type something, delete it, then send it anyway."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_8_008_prawal_fadf71b74e.ogg" # auto-generated voice
    p "Messages came easier. Silences stopped feeling like endings."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_8_009_prawal_d68219984f.ogg" # auto-generated voice
    p "We both knew friendship was still there."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_8_010_prawal_c0cb9b94d4.ogg" # auto-generated voice
    p "It had just made room for something deeper."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    menu:
        "What made it feel real?"
        "The comfort between messages.":
            $ story_choice_closeness = "comfort"
            voice "audio/voice/prawal/chapter_8_011_prawal_51eed6a2fe.ogg" # auto-generated voice
            p "It wasn't only what we said. It was the peace between messages, when nothing had to be performed."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
        "The courage to be honest.":
            $ story_choice_closeness = "honesty"
            voice "audio/voice/prawal/chapter_8_012_prawal_d7b498a251.ogg" # auto-generated voice
            p "It became real when honesty stopped feeling like a risk and started feeling like relief."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/aashna/chapter_8_013_aashna_22a96b0850.ogg" # auto-generated voice
    a "I don't know what we're calling this."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_8_014_prawal_3e686d5973.ogg" # auto-generated voice
    p "Neither did I."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_8_015_prawal_8520dbe82d.ogg" # auto-generated voice
    p "But I knew I wanted to keep choosing it."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_8_016_prawal_1f42bdb033.ogg" # auto-generated voice
    p "Something quiet and beautiful was growing between us."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_8_017_prawal_9cc17b7783.ogg" # auto-generated voice
    p "And for the first time, I wasn't afraid of it."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    scene bg_ch8_clearing_stars at bg_cinematic with directed_transition("starlit")
    $ play_audio_cue(audio.sfx_final_swell, "swell")
    show prawal date_loving at left_character, sprite_night with premium_dissolve
    show aashna date_loving at right_character, sprite_night with premium_dissolve
    pause 0.8
    jump chapter_9

label chapter_9:
    $ mark_chapter_unlocked(9)
    stop ambience fadeout 1.0
    play music audio.music_family_blessing fadeout 1.0 fadein 1.4
    play ambience audio.ambience_home_warm fadein 1.2
    $ set_audio_scene("letters")
    $ play_audio_cue(audio.sfx_chapter_reveal, "chapter")
    call show_chapter_card("Chapter 9", "Letters, Every Morning")
    scene bg_ch9_garden_dawn at bg_cinematic with directed_transition("page")
    show prawal date_loving at left_character, sprite_golden with premium_dissolve
    # letters_intro
    voice "audio/voice/narrator/chapter_9_001_narrator_ef34ffbbe2.ogg" # auto-generated voice
    n "2021. The world was still finding its balance."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_9_002_narrator_e10ca65ee5.ogg" # auto-generated voice
    n "Every morning, before meetings, before noise, before the day could ask for anything, Prawal sent Aashna a message."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_9_003_narrator_00d4ba5a72.ogg" # auto-generated voice
    n "Not because anyone asked."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_9_004_narrator_b1e7bf5916.ogg" # auto-generated voice
    n "Because love had become a ritual before either of them named it."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_9_005_narrator_e21ff0d4fb.ogg" # auto-generated voice
    n "365 mornings. Then more."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_9_006_narrator_947e3e4216.ogg" # auto-generated voice
    n "The letters are here. One morning at a time."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    scene bg_ch9_study_morning at bg_focus with directed_transition("page")
    $ ch9_seen = []
    $ ch9_done = False
    $ ch9_items = [
        {"key": "first", "label": "Read the first thought", "hx": 0.40, "hy": 0.54, "tone": "read"},
        {"key": "saturday", "label": "Open a Saturday morning", "hx": 0.50, "hy": 0.48, "tone": "read"},
        {"key": "hope", "label": "Find the fading hope", "hx": 0.58, "hy": 0.55, "tone": "read"},
        {"key": "day200", "label": "Count day two hundred", "hx": 0.66, "hy": 0.47, "tone": "read"},
        {"key": "last", "label": "Read the last letter", "hx": 0.75, "hy": 0.54, "tone": "read"},
    ]
    while not ch9_done:
        window hide
        call screen memory_interaction_map("Letters, Every Morning", "Read one. That's all you need.", ch9_items, ch9_seen, 1)
        window auto
        $ ch9_result = _return
        if ch9_result[0] == "continue":
            $ ch9_done = True
        elif ch9_result[1] == "first":
            $ ch9_seen.append("first") if "first" not in ch9_seen else None
            $ play_audio_cue(audio.sfx_page_turn, "page")
            voice "audio/voice/prawal/chapter_9_007_prawal_94c99c7399.ogg" # auto-generated voice
            p "Good morning, Aashna."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_9_008_prawal_6df5fa44d4.ogg" # auto-generated voice
            p "I woke up and reached for my phone before the room had fully brightened."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_9_009_prawal_112d893603.ogg" # auto-generated voice
            p "I don't know what this feeling is yet."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_9_010_prawal_f9ab5e8149.ogg" # auto-generated voice
            p "But keeping it to myself already feels impossible."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
        elif ch9_result[1] == "saturday":
            $ ch9_seen.append("saturday") if "saturday" not in ch9_seen else None
            $ play_audio_cue(audio.sfx_page_turn, "page")
            voice "audio/voice/prawal/chapter_9_011_prawal_dd67fea4d9.ogg" # auto-generated voice
            p "Good morning again, Aashna."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_9_012_prawal_930dfec0fb.ogg" # auto-generated voice
            p "I saw something ridiculous today and saved it because I knew exactly how you'd laugh."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_9_013_prawal_0f02a5c0d5.ogg" # auto-generated voice
            p "A normal Saturday became better the second I imagined telling you about it."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
        elif ch9_result[1] == "hope":
            $ ch9_seen.append("hope") if "hope" not in ch9_seen else None
            $ play_audio_cue(audio.sfx_page_turn, "page")
            voice "audio/voice/prawal/chapter_9_014_prawal_5c3e9f7ad0.ogg" # auto-generated voice
            p "Good morning."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_9_015_prawal_0cf1b0ca0c.ogg" # auto-generated voice
            p "Today I feel hopeful in a way that doesn't feel dramatic."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_9_016_prawal_dcf6618e32.ogg" # auto-generated voice
            p "Just steady."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_9_017_prawal_c61d3e97d4.ogg" # auto-generated voice
            p "Like something in me has started making space for you."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
        elif ch9_result[1] == "day200":
            $ ch9_seen.append("day200") if "day200" not in ch9_seen else None
            $ play_audio_cue(audio.sfx_page_turn, "page")
            voice "audio/voice/prawal/chapter_9_018_prawal_94c99c7399.ogg" # auto-generated voice
            p "Good morning, Aashna."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_9_019_prawal_dd159520d4.ogg" # auto-generated voice
            p "Day two hundred and something. I have stopped pretending I know the count."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_9_020_prawal_b3f67c1e31.ogg" # auto-generated voice
            p "But I haven't missed a morning."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_9_021_prawal_a56a6104db.ogg" # auto-generated voice
            p "By now, I think we both know why."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
        elif ch9_result[1] == "last":
            $ ch9_seen.append("last") if "last" not in ch9_seen else None
            $ play_audio_cue(audio.sfx_page_turn, "page")
            voice "audio/voice/prawal/chapter_9_022_prawal_5c3e9f7ad0.ogg" # auto-generated voice
            p "Good morning."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_9_023_prawal_52eb398d76.ogg" # auto-generated voice
            p "Every morning, before the world woke up, my first words went to you."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/aashna/chapter_9_024_aashna_b37dcf603c.ogg" # auto-generated voice
            a "I started waiting for them, you know."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_9_025_prawal_d4c3a2c7a3.ogg" # auto-generated voice
            p "By the time this one reached you, Aashna..."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_9_026_prawal_7b1761a9ad.ogg" # auto-generated voice
            p "You already had my heart. Completely."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
    jump chapter_10

label chapter_10:
    $ mark_chapter_unlocked(10)
    play music audio.music_storm_pulse fadeout 1.0 fadein 1.0
    play ambience audio.ambience_rain_loop fadeout 1.0 fadein 1.0
    $ set_audio_scene("storm")
    $ play_audio_cue(audio.sfx_chapter_reveal, "chapter")
    call show_chapter_card("Chapter 10", "Little Storms")
    scene bg_ch10_storm_outside at bg_cinematic with directed_transition("storm")
    show overlay_rain with premium_dissolve
    # ch10_intro
    voice "audio/voice/narrator/chapter_10_001_narrator_ab778f018a.ogg" # auto-generated voice
    n "Not every day was golden."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_10_002_narrator_fec6111dfa.ogg" # auto-generated voice
    n "Some days had sharp edges: delayed replies, tired voices, words sent too quickly."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_10_003_narrator_e6683c55cb.ogg" # auto-generated voice
    n "The storm was not outside them."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_10_004_narrator_aca4d2f687.ogg" # auto-generated voice
    n "It was the space between two people who still wanted to understand each other."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_10_005_narrator_dcbde272d3.ogg" # auto-generated voice
    n "Walk forward. The way back is still there."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    call show_hotspot("Step out of the rain", 0.81, 0.51, "storm")
    $ play_audio_cue(audio.sfx_ui_chime, "ui")
    scene bg_ch10_storm_inside at bg_cinematic with directed_transition("storm")
    show prawal storm_neutral at storm_far_left, sprite_storm
    show aashna storm_emotional at storm_far_right, sprite_storm
    # ch9_fight
    voice "audio/voice/narrator/chapter_10_006_narrator_043f059051.ogg" # auto-generated voice
    n "Not everything was smooth. Love never is."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_10_007_prawal_4d3ace6731.ogg" # auto-generated voice
    p "We had arguments that started small and somehow grew teeth."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_10_008_prawal_fdfa2262b3.ogg" # auto-generated voice
    p "We had silences where both of us waited for the other to soften first."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/aashna/chapter_10_009_aashna_b38efdc514.ogg" # auto-generated voice
    a "Sometimes I didn't know how to say what I was feeling without sounding angry."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_10_010_prawal_0565a2eb1c.ogg" # auto-generated voice
    p "Sometimes I listened to reply, not to understand."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/aashna/chapter_10_011_aashna_e62899dc96.ogg" # auto-generated voice
    a "And sometimes I needed you to hear the feeling, not just the words."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    menu:
        "What helped them come back?"
        "Patience before pride.":
            $ story_choice_repair = "patience"
            voice "audio/voice/prawal/chapter_10_012_prawal_cb4eb21687.ogg" # auto-generated voice
            p "I learned that being right could still leave both of us lonely."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_10_013_prawal_4ecef66762.ogg" # auto-generated voice
            p "Being gentle brought us back faster."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
        "Saying sorry without defending it.":
            $ story_choice_repair = "sorry"
            voice "audio/voice/prawal/chapter_10_014_prawal_1d6ab282b4.ogg" # auto-generated voice
            p "The apology had to arrive without a defense attached to it."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_10_015_prawal_afe6e11783.ogg" # auto-generated voice
            p "That was the part that mattered."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
    show prawal storm_neutral at left_character, sprite_storm with premium_dissolve
    show aashna storm_emotional at right_character, sprite_storm with premium_dissolve
    voice "audio/voice/prawal/chapter_10_016_prawal_cc19fef769.ogg" # auto-generated voice
    p "But every single time, we came back to each other."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    $ play_audio_cue(audio.sfx_final_swell, "swell")
    pause 0.35
    scene cg_ch10_reconciliation at cg_signature_peak with directed_transition("vow")
    show screen signature_peak_caption("AFTER THE STORM", "Love is the hand you choose when the rain gets loud.")
    pause 1.2
    hide screen signature_peak_caption with premium_dissolve
    $ cinematic_mode = True
    voice "audio/voice/aashna/chapter_10_017_aashna_4be9741fb4.ogg" # auto-generated voice
    a "We are okay?"
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_10_018_prawal_dead90eb49.ogg" # auto-generated voice
    p "We are learning."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_10_019_prawal_79d9042a7a.ogg" # auto-generated voice
    p "A little more patient. A little more honest."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_10_020_prawal_87c386444d.ogg" # auto-generated voice
    p "Love wasn't the absence of storms. It was choosing the same hand when the rain got loud."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_10_021_prawal_3e1237d589.ogg" # auto-generated voice
    p "Every storm taught us how to hold on without holding too tightly."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_10_022_prawal_25c848bfc5.ogg" # auto-generated voice
    p "That's how we knew it was real."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    $ cinematic_mode = False
    stop ambience fadeout 1.2
    jump chapter_11

label chapter_11:
    $ mark_chapter_unlocked(11)
    stop ambience fadeout 1.0
    play music audio.music_office_warmth fadeout 1.0 fadein 1.3
    play ambience audio.ambience_home_warm fadein 1.2
    $ set_audio_scene("home")
    $ play_audio_cue(audio.sfx_chapter_reveal, "chapter")
    call show_chapter_card("Chapter 11", "Love in a Box")
    scene bg_ch11_apartment at bg_cinematic with directed_transition("home")
    show prawal happy at left_character, sprite_warm with premium_dissolve
    # gifts_intro
    voice "audio/voice/narrator/chapter_11_001_narrator_05e415ce6d.ogg" # auto-generated voice
    n "They say love is in the big moments."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_11_002_narrator_521262384c.ogg" # auto-generated voice
    n "But Prawal knows it's in the small ones."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_11_003_narrator_ecf3c76cf5.ogg" # auto-generated voice
    n "The ordinary evening when you order her favourite food — from your home, to hers."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_11_004_narrator_1f9c1930ba.ogg" # auto-generated voice
    n "The little things, sent with intention."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_11_005_narrator_5100806589.ogg" # auto-generated voice
    n "Look around. Something here carries her name."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    scene bg_ch11_gifts at bg_focus with directed_transition("gift")
    $ ch11_seen = []
    $ ch11_done = False
    $ ch11_items = [
        {"key": "food", "label": "Order her favourite food", "hx": 0.35, "hy": 0.62, "tone": "open"},
        {"key": "book", "label": "Hold the printed story", "hx": 0.51, "hy": 0.51, "tone": "open"},
        {"key": "sorry", "label": "Send the late apology", "hx": 0.45, "hy": 0.61, "tone": "social"},
        {"key": "photos", "label": "Hang the real moments", "hx": 0.56, "hy": 0.50, "tone": "inspect"},
        {"key": "mug", "label": "Fill the morning mug", "hx": 0.50, "hy": 0.56, "tone": "gift"},
    ]
    while not ch11_done:
        window hide
        call screen keepsake_box("Love in a Box", ch11_items, ch11_seen, 1)
        window auto
        $ ch11_result = _return
        if ch11_result[0] == "continue":
            $ ch11_done = True
        elif ch11_result[1] == "food":
            $ ch11_seen.append("food") if "food" not in ch11_seen else None
            $ play_audio_cue(audio.sfx_gift_open, "gift")
            voice "audio/voice/prawal/chapter_11_006_prawal_8f1069805e.ogg" # auto-generated voice
            p "Sometimes, after a fight — or even without reason —"
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_11_007_prawal_9719ab9d03.ogg" # auto-generated voice
            p "I'd order Aashna's favourite food. Delivered to her door."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_11_008_prawal_f9e3f27a6a.ogg" # auto-generated voice
            p "Just: here. Eat. I'm thinking of you."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_11_009_prawal_1038813499.ogg" # auto-generated voice
            p "Food says 'I love you' in every language."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
        elif ch11_result[1] == "book":
            $ ch11_seen.append("book") if "book" not in ch11_seen else None
            $ play_audio_cue(audio.sfx_page_turn, "page")
            show prop_book at prop_book_focus with premium_dissolve
            voice "audio/voice/prawal/chapter_11_010_prawal_a10ae70985.ogg" # auto-generated voice
            p "I had a book made. Our story — illustrated, printed, bound."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_11_011_prawal_81b129e42c.ogg" # auto-generated voice
            p "Photos, notes, little captions. Every chapter of Prawal & Aashna, held in your hands."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/aashna/chapter_11_012_aashna_df316e17de.ogg" # auto-generated voice
            a "…"
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_11_013_prawal_5895ffeb66.ogg" # auto-generated voice
            p "That silence was the best review I ever got."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            hide prop_book with premium_dissolve
        elif ch11_result[1] == "sorry":
            $ ch11_seen.append("sorry") if "sorry" not in ch11_seen else None
            $ play_audio_cue(audio.sfx_message_ping, "message")
            voice "audio/voice/narrator/chapter_11_014_narrator_101e0fd2ff.ogg" # auto-generated voice
            n "One time, after a disagreement between Prawal and Aashna…"
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_11_015_prawal_4a30f27241.ogg" # auto-generated voice
            p "I messaged the delivery partner before the drop."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_11_016_prawal_b39d2547d7.ogg" # auto-generated voice
            p "'Can you please tell her I'm sorry from my side?'"
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/aashna/chapter_11_017_aashna_8eaba9dc46.ogg" # auto-generated voice
            a "…the delivery guy said you're sorry. 😂"
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_11_018_prawal_3d9f005d35.ogg" # auto-generated voice
            p "That delivery guy will never know what he helped fix that evening."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
        elif ch11_result[1] == "photos":
            $ ch11_seen.append("photos") if "photos" not in ch11_seen else None
            $ play_audio_cue(audio.sfx_ui_chime, "ui")
            show prop_framed_photos at prop_photos_focus with premium_dissolve
            voice "audio/voice/prawal/chapter_11_019_prawal_b6e04c7865.ogg" # auto-generated voice
            p "We had so many photos. Scattered across phones and drives."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_11_020_prawal_afb0dd1e7a.ogg" # auto-generated voice
            p "So I had them printed. Framed. Displayed."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/aashna/chapter_11_021_aashna_343854f237.ogg" # auto-generated voice
            a "Why did you print the blurry ones too?"
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_11_022_prawal_f1fda69004.ogg" # auto-generated voice
            p "Especially the blurry ones. Those are the real ones."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            hide prop_framed_photos with premium_dissolve
        elif ch11_result[1] == "mug":
            $ ch11_seen.append("mug") if "mug" not in ch11_seen else None
            $ play_audio_cue(audio.sfx_gift_open, "gift")
            show prop_mug at prop_mug_focus with premium_dissolve
            voice "audio/voice/prawal/chapter_11_023_prawal_8da38d06f5.ogg" # auto-generated voice
            p "A simple mug. Made just for Aashna."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_11_024_prawal_cfa5f0ee86.ogg" # auto-generated voice
            p "Her name. Her photo. That's all it needed."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/aashna/chapter_11_025_aashna_e0901524ee.ogg" # auto-generated voice
            a "I use it every single day, you know."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/prawal/chapter_11_026_prawal_a1405e8527.ogg" # auto-generated voice
            p "That's the whole point. That small, daily smile."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            hide prop_mug with premium_dissolve
    jump chapter_12

label chapter_12:
    $ mark_chapter_unlocked(12)
    stop ambience fadeout 1.0
    play music audio.music_family_blessing fadeout 1.0 fadein 1.5
    play ambience audio.ambience_home_warm fadein 1.2
    $ set_audio_scene("family")
    $ play_audio_cue(audio.sfx_chapter_reveal, "chapter")
    call show_chapter_card("Chapter 12", "Two Families, One Story")
    scene bg_ch12_family at bg_cinematic with directed_transition("family")
    show prawal family_happy at left_character, sprite_warm with premium_dissolve
    show aashna family_happy at right_character, sprite_warm with premium_dissolve
    # ch12_intro
    voice "audio/voice/narrator/chapter_12_001_narrator_bded9bdced.ogg" # auto-generated voice
    n "A home. Warm and full of voices."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_12_002_narrator_72e32b12d8.ogg" # auto-generated voice
    n "Letters from those who love Prawal and Aashna most."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_12_003_narrator_5b4ae305c9.ogg" # auto-generated voice
    n "They left something here. Find the one that stays."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    scene bg_ch12_letters at bg_focus with directed_transition("page")
    $ ch12_seen = []
    $ ch12_done = False
    $ ch12_items = [
        {"key": "mom", "label": "Open his mother's letter", "hx": 0.34, "hy": 0.48, "tone": "read"},
        {"key": "dad", "label": "Read his father's words", "hx": 0.48, "hy": 0.43, "tone": "read"},
        {"key": "sister", "label": "Unfold his sister's note", "hx": 0.61, "hy": 0.53, "tone": "read"},
        {"key": "together", "label": "Hold it all together", "hx": 0.74, "hy": 0.45, "tone": "read"},
    ]
    while not ch12_done:
        window hide
        call screen memory_interaction_map("Two Families, One Story", "Read one. Let it land.", ch12_items, ch12_seen, 1)
        window auto
        $ ch12_result = _return
        if ch12_result[0] == "continue":
            $ ch12_done = True
        elif ch12_result[1] == "mom":
            $ ch12_seen.append("mom") if "mom" not in ch12_seen else None
            $ play_audio_cue(audio.sfx_page_turn, "page")
            voice "audio/voice/narrator/chapter_12_004_narrator_0bacc73620.ogg" # auto-generated voice
            n "A letter from Mom."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/narrator/chapter_12_005_narrator_e379c92f88.ogg" # auto-generated voice
            n "'I always knew you'd find someone who sees you the way I do.'"
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/narrator/chapter_12_006_narrator_11f5566ffd.ogg" # auto-generated voice
            n "'Take care of each other. That's all I ask.'"
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
        elif ch12_result[1] == "dad":
            $ ch12_seen.append("dad") if "dad" not in ch12_seen else None
            $ play_audio_cue(audio.sfx_page_turn, "page")
            voice "audio/voice/narrator/chapter_12_007_narrator_5a2e543518.ogg" # auto-generated voice
            n "A few words from Dad."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/narrator/chapter_12_008_narrator_1cf4bff2dc.ogg" # auto-generated voice
            n "'I'm proud of the person you've become.'"
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/narrator/chapter_12_009_narrator_8395a56cc0.ogg" # auto-generated voice
            n "'And I'm proud of who you chose to walk beside.'"
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
        elif ch12_result[1] == "sister":
            $ ch12_seen.append("sister") if "sister" not in ch12_seen else None
            $ play_audio_cue(audio.sfx_page_turn, "page")
            voice "audio/voice/narrator/chapter_12_010_narrator_98bca663d3.ogg" # auto-generated voice
            n "A scribbled note from a sister."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/narrator/chapter_12_011_narrator_5a73701b7a.ogg" # auto-generated voice
            n "'You two are disgustingly cute. Don't ever change. 😂'"
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/narrator/chapter_12_012_narrator_9f59d7e287.ogg" # auto-generated voice
            n "'But seriously… I've never seen you happier.'"
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
        elif ch12_result[1] == "together":
            $ ch12_seen.append("together") if "together" not in ch12_seen else None
            $ play_audio_cue(audio.sfx_page_turn, "page")
            voice "audio/voice/narrator/chapter_12_013_narrator_906dc94280.ogg" # auto-generated voice
            n "A letter written together. By both families."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/narrator/chapter_12_014_narrator_2691032eee.ogg" # auto-generated voice
            n "'We didn't lose a child. We gained one.'"
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/narrator/chapter_12_015_narrator_7d2754f66e.ogg" # auto-generated voice
            n "'This family just got bigger. And better.'"
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
            voice "audio/voice/narrator/chapter_12_016_narrator_f706cedd3d.ogg" # auto-generated voice
            n "'Welcome home.'"
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
    scene bg_ch12_family at bg_cinematic with directed_transition("family")
    show prawal family_happy at left_character, sprite_warm with premium_dissolve
    show aashna family_happy at right_character, sprite_warm with premium_dissolve
    # ch12_family
    voice "audio/voice/narrator/chapter_12_017_narrator_ef22c10c6e.ogg" # auto-generated voice
    n "Four voices. One story."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_12_018_narrator_4e46381a33.ogg" # auto-generated voice
    n "Every letter said the same thing in a different way."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_12_019_narrator_875df96ad9.ogg" # auto-generated voice
    n "'You are loved. You are seen. You belong here.'"
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_12_020_prawal_bea0de21ed.ogg" # auto-generated voice
    p "I didn't know what to expect that day."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_12_021_prawal_99bce027ba.ogg" # auto-generated voice
    p "But when both families sat down together…"
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_12_022_narrator_70f7314863.ogg" # auto-generated voice
    n "There was no divide."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_12_023_narrator_9a9f49d266.ogg" # auto-generated voice
    n "Just warmth. Just laughter. Just home."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/aashna/chapter_12_024_aashna_01a1db4a3d.ogg" # auto-generated voice
    a "My family already loved you."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_12_025_prawal_3d401cf1f1.ogg" # auto-generated voice
    p "And mine already loved you too."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_12_026_narrator_8005c30143.ogg" # auto-generated voice
    n "Two families. One story. And it was just beginning."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    jump chapter_13

label chapter_13:
    $ mark_chapter_unlocked(13)
    stop ambience fadeout 1.0
    play music audio.music_starlit_confession fadeout 1.0 fadein 1.5
    play ambience audio.ambience_garden_night fadein 1.4
    $ set_audio_scene("starlit")
    $ play_audio_cue(audio.sfx_chapter_reveal, "chapter")
    call show_chapter_card("Chapter 13", "Paths That Merge")
    scene bg_ch13_paths at bg_cinematic with directed_transition("promise")
    show prawal date_neutral at left_character, sprite_golden with premium_dissolve
    show aashna date_neutral at right_character, sprite_golden with premium_dissolve
    # ch13_intro
    voice "audio/voice/narrator/chapter_13_001_narrator_6d23154557.ogg" # auto-generated voice
    n "Two lives. Two journeys. Two different stories."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_13_002_narrator_d23a693d4a.ogg" # auto-generated voice
    n "But somewhere along the way… the paths began to bend."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_13_003_narrator_8bd846925a.ogg" # auto-generated voice
    n "She's waiting where the roads meet."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    call show_hotspot("Take the step where paths meet", 0.50, 0.64, "walk")
    $ play_audio_cue(audio.sfx_ui_chime, "ui")
    scene bg_ch13_dawn_ethereal at bg_cinematic with directed_transition("finale")
    show prawal date_loving at left_character, sprite_ethereal with premium_dissolve
    show aashna date_loving at right_character, sprite_ethereal with premium_dissolve
    # ch13_reunion
    $ cinematic_mode = True
    voice "audio/voice/narrator/chapter_13_004_narrator_a9466e8d7f.ogg" # auto-generated voice
    n "Two paths. One destination."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_13_005_prawal_f0d0a0e896.ogg" # auto-generated voice
    p "Every step I took… led me closer to her."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_13_006_prawal_c49866eae7.ogg" # auto-generated voice
    p "Through distance, through doubt, through time."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_13_007_prawal_fa077cff5f.ogg" # auto-generated voice
    p "And now… here. Together."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/aashna/chapter_13_008_aashna_6aeda72be2.ogg" # auto-generated voice
    a "It was always going to be you."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_13_009_narrator_c431562b45.ogg" # auto-generated voice
    n "Some paths are meant to merge."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    $ cinematic_mode = False
    jump chapter_14

label chapter_14:
    $ mark_chapter_unlocked(14)
    stop ambience fadeout 1.0
    play music audio.music_forever_theme fadeout 1.0 fadein 1.7
    play ambience audio.ambience_wedding_hall fadein 1.6
    $ set_audio_scene("wedding")
    $ play_audio_cue(audio.sfx_chapter_reveal, "chapter")
    call show_chapter_card("Chapter 14", "From Engagement to Forever")
    scene bg_ch14_engagement at bg_focus with directed_transition("promise")
    show prop_rings at prop_rings_focus with premium_dissolve
    # ch14_intro
    voice "audio/voice/narrator/chapter_14_001_narrator_01cc19cbb4.ogg" # auto-generated voice
    n "First came the engagement."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_14_002_narrator_b9fb6d43cf.ogg" # auto-generated voice
    n "A circle of gold resting in a small box."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_14_003_narrator_b826904f8d.ogg" # auto-generated voice
    n "Hands slightly shaking. Families watching too closely. A yes that somehow made the room exhale."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    menu:
        "What promise should echo into forever?"
        "Choose each other every day.":
            $ story_choice_promise = "everyday"
            voice "audio/voice/prawal/chapter_14_004_prawal_c3ae80a4bf.ogg" # auto-generated voice
            p "Forever sounded enormous. I trusted the smaller promise more: choose her again tomorrow."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
        "Protect the small daily smiles.":
            $ story_choice_promise = "smiles"
            voice "audio/voice/prawal/chapter_14_005_prawal_5fbb4d0513.ogg" # auto-generated voice
            p "The grand promise became simple: protect the small smiles that brought us here."
            voice sustain # auto-generated voice sustain
            $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_14_006_narrator_194bc20725.ogg" # auto-generated voice
    n "Hold the promise in your hands."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    call show_hotspot("Hold the promise in your hands", 0.50, 0.51, "final")
    $ play_audio_cue(audio.sfx_ring_shimmer, "ring")
    hide prop_rings with premium_dissolve
    scene bg_ch14_wedding at bg_cinematic with directed_transition("vow")
    show prawal formal_loving at wedding_still_left, sprite_golden
    show aashna formal_loving at wedding_still_right, sprite_golden
    # ch14_wedding
    voice "audio/voice/narrator/chapter_14_007_narrator_4c8e719b06.ogg" # auto-generated voice
    n "And then came the wedding."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_14_008_narrator_64687a7791.ogg" # auto-generated voice
    n "The aisle stretched ahead, bright with flowers and people trying not to cry too early."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_14_009_narrator_1d65d3a7fa.ogg" # auto-generated voice
    n "Lights softened everything."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_14_010_narrator_0537c17432.ogg" # auto-generated voice
    n "At the end of it all, she was waiting."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    $ play_audio_cue(audio.sfx_ring_shimmer, "ring")
    pause 0.35
    scene cg_ch14_vows at cg_signature_peak with directed_transition("vow")
    show screen signature_peak_caption("THE VOW", "Forever begins when ordinary days become sacred.")
    pause 1.2
    hide screen signature_peak_caption with premium_dissolve
    $ cinematic_mode = True
    voice "audio/voice/narrator/chapter_14_011_narrator_05ac6ace71.ogg" # auto-generated voice
    n "There was laughter. There were tears. There were a hundred small things they would only remember later."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_14_012_prawal_263560cf38.ogg" # auto-generated voice
    p "I looked at Aashna in that moment."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/aashna/chapter_14_013_aashna_383bb52bae.ogg" # auto-generated voice
    a "Don't cry before the vows."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_14_014_prawal_e7125033bb.ogg" # auto-generated voice
    p "Too late."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_14_015_prawal_9cfef0b8ad.ogg" # auto-generated voice
    p "I thought this is the best day of my life."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_14_016_prawal_57038814c9.ogg" # auto-generated voice
    p "Forever wasn't only the vow. It was every ordinary day suddenly becoming sacred."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_14_017_prawal_d1444c90cd.ogg" # auto-generated voice
    p "And then I realized it was also the beginning of all the ordinary days I wanted most."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    $ cinematic_mode = False
    scene bg_ch14_wedding_party at bg_focus with directed_transition("promise")
    $ play_audio_cue(audio.sfx_final_swell, "swell")
    pause 1.0
    jump chapter_15

label chapter_15:
    $ mark_chapter_unlocked(15)
    stop ambience fadeout 1.0
    play music audio.music_forever_theme fadeout 1.0 fadein 1.8
    play ambience audio.ambience_ethereal_light fadein 1.6
    $ set_audio_scene("finale")
    $ play_audio_cue(audio.sfx_chapter_reveal, "chapter")
    call show_chapter_card("Chapter 15", "4 Years & Counting")
    scene bg_ch15_light at bg_cinematic with directed_transition("finale")
    show prawal formal_loving at wedding_still_left, sprite_ethereal
    show aashna formal_loving at wedding_still_right, sprite_ethereal
    # ch15_intro
    voice "audio/voice/narrator/chapter_15_001_narrator_fba597e4b5.ogg" # auto-generated voice
    n "No rooms. No objects. No noise."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_15_002_narrator_0513dddc9b.ogg" # auto-generated voice
    n "Just light."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_15_003_narrator_89540ed16e.ogg" # auto-generated voice
    n "Just two people standing inside every morning, every apology, every small gift, every family blessing that brought them here."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/narrator/chapter_15_004_narrator_bedc633be3.ogg" # auto-generated voice
    n "Walk to her."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    call show_hotspot("Step into the rest of your life", 0.50, 0.49, "final")
    $ play_audio_cue(audio.sfx_final_swell, "swell")
    scene bg_ch15_floating at bg_cinematic with directed_transition("finale")
    show prawal formal_loving at wedding_still_left, sprite_ethereal
    show aashna formal_loving at wedding_still_right, sprite_ethereal
    # ch15_finale
    $ cinematic_mode = True
    voice "audio/voice/prawal/chapter_15_005_prawal_a289fa4f69.ogg" # auto-generated voice
    p "Four years."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_15_006_prawal_f3d1fdd11d.ogg" # auto-generated voice
    p "Four years of good mornings before the day could become busy."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_15_007_prawal_310653e5b2.ogg" # auto-generated voice
    p "Four years of missed calls, shared food, second chances, and laughing at things nobody else would understand."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_15_008_prawal_9f381847de.ogg" # auto-generated voice
    p "Four years of fights that taught us how to come back softer."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_15_009_prawal_a2f67c346a.ogg" # auto-generated voice
    p "Four years of families becoming home."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_15_010_prawal_fad02333c5.ogg" # auto-generated voice
    p "Four years of choosing each other in ways too small for anyone else to notice."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/aashna/chapter_15_011_aashna_2cb7c4ced5.ogg" # auto-generated voice
    a "And I noticed them."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    if story_choice_repair == "patience":
        voice "audio/voice/prawal/chapter_15_012_prawal_1457bd9990.ogg" # auto-generated voice
        p "We learned patience before pride."
        voice sustain # auto-generated voice sustain
        $ voice_line_pause() # auto-generated voice pause
    elif story_choice_repair == "sorry":
        voice "audio/voice/prawal/chapter_15_013_prawal_c1cf961333.ogg" # auto-generated voice
        p "We learned how powerful a real sorry can be."
        voice sustain # auto-generated voice sustain
        $ voice_line_pause() # auto-generated voice pause
    if story_choice_gift == "daily":
        voice "audio/voice/prawal/chapter_15_014_prawal_71f2449f18.ogg" # auto-generated voice
        p "And love kept showing up in the things we used every day."
        voice sustain # auto-generated voice sustain
        $ voice_line_pause() # auto-generated voice pause
    elif story_choice_gift == "unsaid":
        voice "audio/voice/prawal/chapter_15_015_prawal_f5fd293664.ogg" # auto-generated voice
        p "And love kept saying the words we were once too shy to say."
        voice sustain # auto-generated voice sustain
        $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_15_016_prawal_fcec838021.ogg" # auto-generated voice
    p "And I fall in love with you a little more every single day."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/aashna/chapter_15_017_aashna_2ace967a7c.ogg" # auto-generated voice
    a "Good. Because I still choose you too."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_15_018_prawal_a2aa4c3eb7.ogg" # auto-generated voice
    p "Happy 4th anniversary, Aashna. ❤"
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    voice "audio/voice/prawal/chapter_15_019_prawal_f7d2068085.ogg" # auto-generated voice
    p "Here's to forever."
    voice sustain # auto-generated voice sustain
    $ voice_line_pause() # auto-generated voice pause
    $ cinematic_mode = False
    $ play_audio_cue(audio.sfx_final_swell, "swell")
    $ final_anniversary_message = "Four years… and I still fall in love with you every single day. ❤"
    if story_choice_promise == "everyday":
        $ final_anniversary_message = "Four years… and I choose you again in every ordinary day. ❤"
    elif story_choice_promise == "smiles":
        $ final_anniversary_message = "Four years… and I still want to protect every smile. ❤"
    elif story_choice_leap == "courage":
        $ final_anniversary_message = "Four years… and I am still grateful I found the courage to click. ❤"
    call screen final_message(final_anniversary_message, "Play Again")
    stop ambience fadeout 2.0
    stop music fadeout 2.0
    return

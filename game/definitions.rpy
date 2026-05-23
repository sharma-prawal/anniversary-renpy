# Character, image, and transform definitions.

define p = Character("Prawal", color="#FFD0B8", what_color="#FFFFFF", voice_tag="prawal", callback=dialogue_advance_callback)
define a = Character("Aashna", color="#FFC0D8", what_color="#FFFFFF", voice_tag="aashna", callback=dialogue_advance_callback)
define n = Character(None, what_color="#FFEAF2", what_italic=True, voice_tag="narrator", callback=dialogue_advance_callback)

default persistent.current_chapter = 1
default persistent.max_unlocked_chapter = 1
default story_choice_leap = None
default story_choice_gift = None
default story_choice_closeness = None
default story_choice_repair = None
default story_choice_promise = None
default save_name = ""
default persistent.access_large_text = False
default persistent.access_high_contrast = False
default persistent.access_reduced_motion = False
default cinematic_mode = False

define config.check_conflicting_properties = True

define premium_fade = Fade(0.28, 0.12, 0.48, color="#050007")
define premium_dissolve = Dissolve(0.72)
define premium_focus = Dissolve(0.9)
define cg_reveal = Fade(0.18, 0.08, 0.72, color="#050007")

transform cinematic_continue_pulse:
    alpha 0.45
    linear 0.9 alpha 0.9
    linear 0.9 alpha 0.45
    repeat

init python:
    transition_reduced_motion = Dissolve(0.18)
    directed_scene_transitions = {
        "lonely": Fade(0.24, 0.08, 0.46, color="#03040A"),
        "digital": Fade(0.16, 0.04, 0.32, color="#03111C"),
        "office": Fade(0.20, 0.08, 0.44, color="#120804"),
        "gift": Fade(0.22, 0.10, 0.50, color="#1A0B08"),
        "date": Fade(0.20, 0.08, 0.42, color="#170706"),
        "starlit": Fade(0.24, 0.10, 0.56, color="#030614"),
        "page": Fade(0.18, 0.08, 0.44, color="#160D08"),
        "storm": Fade(0.06, 0.04, 0.38, color="#DCEBFF"),
        "home": Fade(0.22, 0.10, 0.48, color="#100706"),
        "family": Fade(0.22, 0.10, 0.50, color="#1C0D06"),
        "promise": Fade(0.18, 0.10, 0.58, color="#2A1408"),
        "vow": Fade(0.18, 0.08, 0.68, color="#FFF0C8"),
        "finale": Fade(0.24, 0.14, 0.72, color="#FFF4D5"),
        "soft": Dissolve(0.72),
        "focus": Dissolve(0.9),
    }

    def directed_transition(style="soft"):
        if getattr(persistent, "access_reduced_motion", False):
            return transition_reduced_motion
        return directed_scene_transitions.get(style, directed_scene_transitions["soft"])

    memory_gallery_photos = [
        "photos/WhatsApp Image 2026-04-06 at 8.42.12 PM.jpeg",
        "photos/WhatsApp Image 2026-04-06 at 8.42.13 PM.jpeg",
        "photos/WhatsApp Image 2026-04-06 at 8.42.14 PM.jpeg",
        "photos/WhatsApp Image 2026-04-06 at 8.42.14 PM (1).jpeg",
        "photos/WhatsApp Image 2026-04-06 at 8.42.15 PM.jpeg",
        "photos/WhatsApp Image 2026-04-06 at 8.42.18 PM.jpeg",
        "photos/WhatsApp Image 2026-04-06 at 8.42.18 PM (1).jpeg",
        "photos/WhatsApp Image 2026-04-06 at 8.42.19 PM.jpeg",
        "photos/WhatsApp Image 2026-04-06 at 8.42.19 PM (1).jpeg",
        "photos/WhatsApp Image 2026-04-06 at 8.42.19 PM (2).jpeg",
        "photos/WhatsApp Image 2026-04-06 at 8.42.20 PM.jpeg",
        "photos/WhatsApp Image 2026-04-06 at 8.42.20 PM (1).jpeg",
        "photos/WhatsApp Image 2026-04-06 at 8.42.21 PM.jpeg",
        "photos/WhatsApp Image 2026-04-06 at 8.42.21 PM (1).jpeg",
        "photos/WhatsApp Image 2026-04-06 at 8.42.21 PM (2).jpeg",
        "photos/WhatsApp Image 2026-04-06 at 8.42.21 PM (3).jpeg",
        "photos/WhatsApp Image 2026-04-06 at 8.42.22 PM.jpeg",
        "photos/WhatsApp Image 2026-04-06 at 8.42.23 PM.jpeg",
        "photos/WhatsApp Image 2026-04-06 at 8.42.23 PM (1).jpeg",
    ]

    memory_gallery_chapters = [1, 2, 4, 4, 6, 7, 8, 9, 10, 10, 11, 12, 12, 13, 14, 14, 15, 15, 15]
    memory_gallery_captions = [
        "The quiet before one profile changed the room.",
        "A small click that asked for courage.",
        "The first time the story stepped out of a screen.",
        "A maroon hoodie, a glance, and a memory that stayed.",
        "A gift made ordinary office light feel warmer.",
        "A table, a friend nearby, and a beginning neither of them rushed.",
        "The night friendship started sounding like love.",
        "Morning words becoming a ritual.",
        "Rain outside, patience inside.",
        "The kind of repair that makes love steadier.",
        "A box of proof that she had been listening.",
        "Family becoming part of the promise.",
        "Two homes learning the same language of care.",
        "Different paths, one direction.",
        "The day forever stopped being abstract.",
        "A celebration bright enough to hold everyone.",
        "Four years, still choosing the same person.",
        "The memory of yes after yes.",
        "A future kept open, luminous, and close.",
    ]

    def memory_gallery_label(index):
        return "Memory %02d" % (index + 1)

    def memory_gallery_caption(index):
        try:
            return memory_gallery_captions[index]
        except Exception:
            return "A preserved frame from their story."

    def memory_gallery_chapter(index):
        try:
            return int(memory_gallery_chapters[index])
        except Exception:
            return 1

    choice_lens_notes = {
        "leap": {
            "smile": {
                "chapter": "Remembered through the smile that felt familiar.",
                "gallery": "Remembered: a smile that made courage feel familiar.",
                "recap": "The first leap began with her smile.",
            },
            "courage": {
                "chapter": "Remembered as courage before certainty.",
                "gallery": "Remembered: the brave click he could not ignore.",
                "recap": "The first leap was courage before certainty.",
            },
        },
        "gift": {
            "daily": {
                "chapter": "Love, made practical in the everyday.",
                "gallery": "Remembered: care made useful, warm, and ordinary.",
                "recap": "Love lived in the ordinary things.",
            },
            "unsaid": {
                "chapter": "The gift said what words could not yet.",
                "gallery": "Remembered: the gift that spoke for him.",
                "recap": "Love lived in what was almost unsaid.",
            },
        },
        "closeness": {
            "comfort": {
                "chapter": "Comfort made the quiet feel safe.",
                "gallery": "Remembered: peace in the spaces between messages.",
                "recap": "Comfort made the quiet feel safe.",
            },
            "honesty": {
                "chapter": "Honesty started feeling like relief.",
                "gallery": "Remembered: truth becoming safe.",
                "recap": "Honesty made love feel real.",
            },
        },
        "repair": {
            "patience": {
                "chapter": "Patience mattered more than pride.",
                "gallery": "Remembered: patience before pride.",
                "recap": "Patience brought them back.",
            },
            "sorry": {
                "chapter": "A real sorry arrived without defense.",
                "gallery": "Remembered: an apology without armor.",
                "recap": "A real sorry brought them back.",
            },
        },
        "promise": {
            "everyday": {
                "chapter": "Forever became choosing each other daily.",
                "gallery": "Remembered: choosing again tomorrow.",
                "recap": "Forever meant choosing each other daily.",
            },
            "smiles": {
                "chapter": "The promise protected the small smiles.",
                "gallery": "Remembered: the smiles worth protecting.",
                "recap": "Forever meant protecting the small smiles.",
            },
        },
    }

    chapter_choice_lenses = {
        2: ["leap"],
        6: ["gift"],
        8: ["closeness"],
        10: ["repair"],
        14: ["promise"],
        15: ["repair", "gift", "promise"],
    }

    gallery_choice_lenses = {
        1: "leap",
        4: "gift",
        6: "closeness",
        8: "repair",
        9: "repair",
        14: "promise",
        15: "promise",
        16: "promise",
    }

    def choice_lens_data(lens):
        value = getattr(store, "story_choice_%s" % lens, None)
        return choice_lens_notes.get(lens, {}).get(value)

    def choice_annotation_for_chapter(number):
        notes = []
        for lens in chapter_choice_lenses.get(valid_chapter_number(number), []):
            data = choice_lens_data(lens)
            if data:
                notes.append(data["chapter"])
        return " ".join(notes[:1])

    def memory_gallery_choice_note(index):
        lens = gallery_choice_lenses.get(index)
        if not lens:
            return ""
        data = choice_lens_data(lens)
        if not data:
            return ""
        return data["gallery"]

    def final_choice_recap_lines():
        lines = []
        for lens in ["leap", "gift", "closeness", "repair", "promise"]:
            data = choice_lens_data(lens)
            if data:
                lines.append(data["recap"])
        return lines

    save_chapter_titles = {
        1: "Chapter 1: A Face in the Feed",
        2: "Chapter 2: One Click. One Leap.",
        3: "Chapter 3: Hello... and Goodbye",
        4: "Chapter 4: The Girl in the Hoodie",
        5: "Chapter 5: Starting Over",
        6: "Chapter 6: Wireless & Heartstrings",
        7: "Chapter 7: Pizza & New Beginnings",
        8: "Chapter 8: Something Real",
        9: "Chapter 9: Letters, Every Morning",
        10: "Chapter 10: Little Storms",
        11: "Chapter 11: Love in a Box",
        12: "Chapter 12: Two Families, One Story",
        13: "Chapter 13: Paths That Merge",
        14: "Chapter 14: From Engagement to Forever",
        15: "Chapter 15: 4 Years & Counting",
    }

    def current_save_name():
        chapter = getattr(persistent, "current_chapter", 1) or 1
        try:
            chapter = int(chapter)
        except Exception:
            chapter = 1
        return save_chapter_titles.get(chapter, "Our Story: A Love Quest")

    def format_save_runtime(seconds):
        if seconds is None:
            return ""
        try:
            seconds = int(seconds)
        except Exception:
            return ""
        minutes = max(0, seconds // 60)
        hours = minutes // 60
        minutes = minutes % 60
        if hours:
            return "%dh %02dm played" % (hours, minutes)
        return "%dm played" % minutes

    def anniversary_save_json(data):
        chapter = getattr(persistent, "current_chapter", 1) or 1
        try:
            chapter = int(chapter)
        except Exception:
            chapter = 1
        data["current_chapter"] = chapter
        data["chapter_title"] = save_chapter_titles.get(chapter, "Our Story: A Love Quest")

    config.save_json_callbacks.append(anniversary_save_json)

    chapter_card_entries = {
        "Our Story": {
            "index": "00",
            "art": "bg_main_menu",
            "mood": "A premium anniversary visual novel",
            "accent": "#FFD7A6",
            "wash": "#050007C8",
        },
        "Chapter 1": {
            "index": "01",
            "art": "bg_ch1_room_night",
            "mood": "Lockdown quiet, laptop glow, first curiosity",
            "accent": "#8FC8FF",
            "wash": "#050711D8",
        },
        "Chapter 2": {
            "index": "02",
            "art": "bg_ch2_social_profile",
            "mood": "The courage behind one small click",
            "accent": "#7FE2FF",
            "wash": "#050914D8",
        },
        "Chapter 3": {
            "index": "03",
            "art": "bg_ch3_chat_room",
            "mood": "Messages, pauses, and the story waiting",
            "accent": "#8EB6FF",
            "wash": "#050713D8",
        },
        "Chapter 4": {
            "index": "04",
            "art": "bg_ch4_office_full",
            "mood": "The moment a photo became a person",
            "accent": "#FFC983",
            "wash": "#100804D8",
        },
        "Chapter 5": {
            "index": "05",
            "art": "bg_ch5_office_day",
            "mood": "Small reasons to stand a little closer",
            "accent": "#FFD08D",
            "wash": "#120904D8",
        },
        "Chapter 6": {
            "index": "06",
            "art": "bg_ch6_office_gift",
            "mood": "A gift, a smile, and a promise repeated",
            "accent": "#FFD9A8",
            "wash": "#110806D8",
        },
        "Chapter 7": {
            "index": "07",
            "art": "bg_ch7_restaurant",
            "mood": "A simple evening that felt like a beginning",
            "accent": "#FFB980",
            "wash": "#130706D8",
        },
        "Chapter 8": {
            "index": "08",
            "art": "bg_ch8_clearing_stars",
            "mood": "Under the stars, friendship became something real",
            "accent": "#C8B7FF",
            "wash": "#070814D8",
        },
        "Chapter 9": {
            "index": "09",
            "art": "bg_ch9_study_morning",
            "mood": "Every morning, one more reason to hope",
            "accent": "#FFD39E",
            "wash": "#100A06D8",
        },
        "Chapter 10": {
            "index": "10",
            "art": "bg_ch10_storm_inside",
            "mood": "Rain outside, warmth inside, love choosing patience",
            "accent": "#AFC8FF",
            "wash": "#050A13D8",
        },
        "Chapter 11": {
            "index": "11",
            "art": "bg_ch11_gifts",
            "mood": "Love made visible in the smallest details",
            "accent": "#FFD4A8",
            "wash": "#100706D8",
        },
        "Chapter 12": {
            "index": "12",
            "art": "bg_ch12_family",
            "mood": "Two homes opening into one story",
            "accent": "#FFC88F",
            "wash": "#110706D8",
        },
        "Chapter 13": {
            "index": "13",
            "art": "bg_ch13_paths",
            "mood": "Two journeys bending toward the same dawn",
            "accent": "#FFE1A3",
            "wash": "#0D0805D8",
        },
        "Chapter 14": {
            "index": "14",
            "art": "bg_ch14_wedding",
            "mood": "A promise given shape, light, and forever",
            "accent": "#FFE2AE",
            "wash": "#110705D8",
        },
        "Chapter 15": {
            "index": "15",
            "art": "bg_ch15_floating",
            "mood": "Four years, still choosing each other",
            "accent": "#FFF0C8",
            "wash": "#0B0710D8",
        },
    }

    def chapter_card_data(title):
        key = title.split(":", 1)[0]
        return chapter_card_entries.get(key, chapter_card_entries["Our Story"])

    def valid_chapter_number(value, fallback=1):
        try:
            chapter = int(value)
        except Exception:
            chapter = fallback
        return max(1, min(15, chapter))

    def unlocked_chapter_limit():
        current = valid_chapter_number(getattr(persistent, "current_chapter", 1), 1)
        unlocked = valid_chapter_number(getattr(persistent, "max_unlocked_chapter", current), current)
        if unlocked < current:
            unlocked = current
        persistent.max_unlocked_chapter = unlocked
        return unlocked

    def mark_chapter_unlocked(number):
        chapter = valid_chapter_number(number)
        persistent.current_chapter = chapter
        persistent.max_unlocked_chapter = max(unlocked_chapter_limit(), chapter)

    def chapter_label_for_number(number):
        return "chapter_%d" % valid_chapter_number(number)

    chapter_select_entries = []
    for chapter_number in range(1, 16):
        key = "Chapter %d" % chapter_number
        chapter_title = save_chapter_titles[chapter_number].split(": ", 1)[1]
        card = chapter_card_entries[key]
        chapter_select_entries.append({
            "number": chapter_number,
            "label": key,
            "title": chapter_title,
            "art": card["art"],
            "mood": card["mood"],
            "accent": card["accent"],
            "target": "chapter_%d" % chapter_number,
        })

image bg_ch10_storm_inside = "backgrounds_ai/bg_ch10_storm_inside.png"
image bg_ch10_storm_outside = "backgrounds_ai/bg_ch10_storm_outside.png"
image bg_ch11_apartment = "backgrounds_ai/bg_ch11_apartment.png"
image bg_ch11_gifts = "backgrounds_ai/bg_ch11_gifts.png"
image bg_ch12_family = "backgrounds_ai/bg_ch12_family.png"
image bg_ch12_letters = "backgrounds_ai/bg_ch12_letters.png"
image bg_ch13_dawn_ethereal = "backgrounds_ai/bg_ch13_dawn_ethereal.png"
image bg_ch13_paths = "backgrounds_ai/bg_ch13_paths.png"
image bg_ch14_engagement = "backgrounds_ai/bg_ch14_engagement.png"
image bg_ch14_wedding = "backgrounds_ai/bg_ch14_wedding.png"
image bg_ch14_wedding_party = "backgrounds_ai/bg_ch14_wedding_party.png"
image bg_ch15_floating = "backgrounds_ai/bg_ch15_floating.png"
image bg_ch15_light = "backgrounds_ai/bg_ch15_light.png"
image bg_ch1_laptop_closeup = "backgrounds_ai/bg_ch1_laptop_closeup.png"
image bg_ch1_room_night = "backgrounds_ai/bg_ch1_room_night.png"
image bg_ch2_social_profile = "backgrounds_ai/bg_ch2_social_profile.png"
image bg_ch3_chat_room = "backgrounds_ai/bg_ch3_chat_room.png"
image bg_ch4_aashna_closeup = "backgrounds_ai/bg_ch4_aashna_closeup.png"
image bg_ch4_office_full = "backgrounds_ai/bg_ch4_office_full.png"
image bg_ch5_office_corridor = "backgrounds_ai/bg_ch5_office_corridor.png"
image bg_ch5_office_day = "backgrounds_ai/bg_ch5_office_day.png"
image bg_ch6_office_gift = "backgrounds_ai/bg_ch6_office_gift.png"
image bg_ch7_restaurant = "backgrounds_ai/bg_ch7_restaurant.png"
image bg_ch7_restaurant_window = "backgrounds_ai/bg_ch7_restaurant_window.png"
image bg_ch8_clearing = "backgrounds_ai/bg_ch8_clearing.png"
image bg_ch8_clearing_stars = "backgrounds_ai/bg_ch8_clearing_stars.png"
image bg_ch9_garden_dawn = "backgrounds_ai/bg_ch9_garden_dawn.png"
image bg_ch9_study_morning = "backgrounds_ai/bg_ch9_study_morning.png"
image bg_main_menu = "backgrounds_ai/bg_main_menu.png"

image prawal happy = "sprites_ai/prawal/happy.png"
image prawal neutral = "sprites_ai/prawal/neutral.png"
image prawal surprised = "sprites_ai/prawal/surprised.png"
image prawal thinking = "sprites_ai/prawal/thinking.png"
image prawal loving = "sprites_ai/prawal/loving.png"
image prawal date_happy = "sprites_ai/prawal/date_happy.png"
image prawal date_loving = "sprites_ai/prawal/date_loving.png"
image prawal date_neutral = "sprites_ai/prawal/date_neutral.png"
image prawal family_happy = "sprites_ai/prawal/family_happy.png"
image prawal office_happy = "sprites_ai/prawal/office_happy.png"
image prawal office_neutral = "sprites_ai/prawal/office_neutral.png"
image prawal storm_neutral = "sprites_ai/prawal/storm_neutral.png"
image prawal formal_loving = "sprites_ai/prawal/formal_loving.png"

image aashna happy = "sprites_ai/aashna/happy.png"
image aashna shy = "sprites_ai/aashna/shy.png"
image aashna neutral = "sprites_ai/aashna/neutral.png"
image aashna laughing = "sprites_ai/aashna/laughing.png"
image aashna surprised = "sprites_ai/aashna/surprised.png"
image aashna emotional = "sprites_ai/aashna/emotional.png"
image aashna loving = "sprites_ai/aashna/loving.png"
image aashna date_happy = "sprites_ai/aashna/date_happy.png"
image aashna date_loving = "sprites_ai/aashna/date_loving.png"
image aashna date_neutral = "sprites_ai/aashna/date_neutral.png"
image aashna date_shy = "sprites_ai/aashna/date_shy.png"
image aashna family_happy = "sprites_ai/aashna/family_happy.png"
image aashna office_happy = "sprites_ai/aashna/office_happy.png"
image aashna office_neutral = "sprites_ai/aashna/office_neutral.png"
image aashna office_maroon_hoodie = "sprites_ai/aashna/office_maroon_hoodie.png"
image aashna office_surprised = "sprites_ai/aashna/office_surprised.png"
image aashna storm_emotional = "sprites_ai/aashna/storm_emotional.png"
image aashna formal_loving = "sprites_ai/aashna/formal_loving.png"

image friend date_happy = "sprites_ai/friend/date_happy.png"

image overlay_rain = "images/effects/overlay_rain.png"
image cinematic_vignette = "images/ui/cinematic_vignette.png"
image menu_foreground_depth = "images/ui/menu_foreground_depth.png"
image menu_petal_layer = "images/ui/menu_petal_layer.png"
image prop_book = "images_ai/props/prop_book.png"
image prop_earphones = "images_ai/props/prop_earphones.png"
image prop_framed_photos = "images_ai/props/prop_framed_photos.png"
image prop_letters = "images_ai/props/prop_letters.png"
image prop_mug = "images_ai/props/prop_mug.png"
image prop_rings = "images_ai/props/prop_rings.png"
image cg_ch4_first_meeting = "images_ai/cg/cg_ch4_first_meeting.png"
image cg_ch10_reconciliation = "images_ai/cg/cg_ch10_reconciliation.png"
image cg_ch14_vows = "images_ai/cg/cg_ch14_vows.png"

transform chapter_card_backdrop:
    xalign 0.5
    yalign 0.5
    zoom 1.035
    alpha 0.0
    ease 0.35 alpha 1.0 zoom 1.0
    linear 2.1 zoom 1.04

transform chapter_card_static:
    xalign 0.5
    yalign 0.5
    zoom 1.0
    alpha 1.0

transform chapter_card_panel:
    alpha 0.0
    yoffset 34
    easeout 0.42 alpha 1.0 yoffset 0

transform chapter_card_preview:
    alpha 0.0
    xoffset -28
    easeout 0.48 alpha 1.0 xoffset 0

transform chapter_card_copy:
    alpha 0.0
    xoffset 32
    pause 0.08
    easeout 0.48 alpha 1.0 xoffset 0

transform signature_peak_reveal:
    alpha 0.0
    yoffset 24
    easeout 0.42 alpha 1.0 yoffset 0

transform cg_cinematic:
    xalign 0.5
    yalign 0.5
    zoom 1.0
    linear 11.0 zoom 1.045

transform cg_signature_peak:
    xalign 0.5
    yalign 0.5
    zoom 1.018
    linear 8.0 zoom 1.07

transform bg_cinematic:
    xalign 0.5
    yalign 0.5
    zoom 1.0
    linear 14.0 zoom 1.055

transform bg_focus:
    xalign 0.5
    yalign 0.5
    zoom 1.04
    linear 10.0 zoom 1.09

transform menu_background_crop:
    xalign 0.5
    yalign 0.5
    zoom 1.0

transform menu_title_reveal:
    alpha 1.0
    yoffset 0

transform menu_nav_reveal:
    alpha 1.0
    xoffset 0

transform menu_petal_drift:
    alpha 0.42
    xoffset -36
    yoffset -18
    linear 18.0 xoffset 34 yoffset 22
    repeat

transform menu_petal_drift_far:
    alpha 0.24
    zoom 1.04
    xoffset 32
    yoffset 18
    linear 24.0 xoffset -38 yoffset -18
    repeat

transform menu_foreground_hold:
    alpha 0.88
    xalign 0.5
    yalign 0.5

transform left_character:
    xalign 0.22
    yalign 1.01
    zoom 0.64

transform right_character:
    xalign 0.76
    yalign 1.01
    zoom 0.64

transform center_character:
    xalign 0.5
    yalign 1.01
    zoom 0.66

transform friend_character:
    xalign 0.5
    yalign 1.01
    zoom 0.56

transform date_left_character:
    xalign 0.24
    yalign 1.01
    zoom 0.58

transform date_friend_character:
    xalign 0.50
    yalign 1.01
    zoom 0.48
    alpha 0.92

transform friend_peripheral:
    xalign 0.86
    yalign 1.01
    zoom 0.46
    alpha 0.0
    easeout 0.45 alpha 0.70

transform friend_peripheral_pos:
    xalign 0.86
    yalign 1.01
    zoom 0.46
    alpha 0.70

transform date_right_character:
    xalign 0.75
    yalign 1.01
    zoom 0.58

# Pass 3: Character blocking transforms
# Animated — used in game/script.rpy for actual entrances
transform enter_left:
    xalign 0.22
    yalign 1.01
    zoom 0.64
    xoffset -200
    alpha 0.0
    easeout 0.58 xoffset 0 alpha 1.0

transform enter_right:
    xalign 0.76
    yalign 1.01
    zoom 0.64
    xoffset 200
    alpha 0.0
    easeout 0.58 xoffset 0 alpha 1.0

transform already_right:
    xalign 0.76
    yalign 1.01
    zoom 0.64
    alpha 0.0
    easeout 0.42 alpha 1.0

transform storm_far_left:
    xalign 0.10
    yalign 1.01
    zoom 0.62
    alpha 0.0
    easeout 0.55 alpha 1.0

transform storm_far_right:
    xalign 0.90
    yalign 1.01
    zoom 0.62
    alpha 0.0
    easeout 0.55 alpha 1.0

transform wedding_still_left:
    xalign 0.28
    yalign 1.01
    zoom 0.65
    alpha 0.0
    easeout 1.0 alpha 1.0

transform wedding_still_right:
    xalign 0.72
    yalign 1.01
    zoom 0.65
    alpha 0.0
    easeout 1.0 alpha 1.0

# Static positions — used in testcases/gallery (no entrance animation)
transform storm_far_left_pos:
    xalign 0.10
    yalign 1.01
    zoom 0.62

transform storm_far_right_pos:
    xalign 0.90
    yalign 1.01
    zoom 0.62

transform wedding_still_left_pos:
    xalign 0.28
    yalign 1.01
    zoom 0.65

transform wedding_still_right_pos:
    xalign 0.72
    yalign 1.01
    zoom 0.65

transform sprite_warm:
    matrixcolor TintMatrix("#FFF0DE") * SaturationMatrix(1.03)

transform sprite_golden:
    matrixcolor TintMatrix("#FFE7C2") * SaturationMatrix(1.06) * BrightnessMatrix(0.02)

transform sprite_cool:
    matrixcolor TintMatrix("#DEE9FF") * SaturationMatrix(0.96) * BrightnessMatrix(-0.01)

transform sprite_night:
    matrixcolor TintMatrix("#CBD8FF") * SaturationMatrix(0.92) * BrightnessMatrix(-0.04)

transform sprite_storm:
    matrixcolor TintMatrix("#B9C9E6") * SaturationMatrix(0.84) * BrightnessMatrix(-0.08)

transform sprite_ethereal:
    matrixcolor TintMatrix("#FFF1D6") * SaturationMatrix(1.08) * BrightnessMatrix(0.04)

transform prop_center:
    xalign 0.5
    yalign 0.5
    zoom 1.0

transform prop_book_focus:
    xalign 0.5
    yalign 0.52
    zoom 0.94

transform prop_photos_focus:
    xalign 0.5
    yalign 0.53
    zoom 0.92

transform prop_mug_focus:
    xalign 0.5
    yalign 0.55
    zoom 0.82

transform prop_earphones_focus:
    xalign 0.55
    yalign 0.55
    zoom 0.27

transform prop_rings_focus:
    xalign 0.5
    yalign 0.5
    zoom 0.96

transform hotspot_pulse:
    anchor (0.5, 0.5)
    zoom 0.82
    alpha 0.78
    linear 0.75 zoom 0.96 alpha 1.0
    linear 0.75 zoom 0.82 alpha 0.78
    repeat

transform hotspot_prompt_settle:
    alpha 1.0
    yoffset 0

# Pass 6: keepsake box per-item micro-animation transforms
transform keepsake_float:
    yoffset 0.0
    linear 1.4 yoffset -8.0
    linear 1.4 yoffset 0.0
    repeat

transform keepsake_sway:
    subpixel True
    rotate_pad False
    rotate 0.0
    linear 1.3 rotate 2.2
    linear 1.3 rotate -2.2
    linear 1.3 rotate 0.0
    repeat

transform keepsake_pulse:
    alpha 0.72
    linear 0.85 alpha 1.0
    linear 0.85 alpha 0.72
    repeat

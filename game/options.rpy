define config.name = _("Our Story: A Love Quest")
define config.version = "1.0"
define config.window_title = _("Our Story: A Love Quest")
define config.screen_width = 1920
define config.screen_height = 1080
define config.physical_width = 1280
define config.physical_height = 720
define config.gl_clear_color = "#050007"
define config.window = "auto"
define config.window_show_transition = Dissolve(0.12)
define config.window_hide_transition = Dissolve(0.10)
define config.transition_screens = False
define config.save_directory = "our-story-love-quest-renpy"
define config.has_sound = True
define config.has_music = True
define config.has_voice = True
define config.default_text_cps = 34
define config.default_afm_time = 16
define config.afm_voice_delay = 0.45
define config.default_fullscreen = False
define config.history_length = 250

define build.name = "our_story_love_quest"
define build.version = "1.0"

init python:
    build.classify("game/backgrounds_web/**", None)
    build.classify("game/images_web/**", None)
    build.classify("game/web-presplash.jpg", None)
    build.classify("game/testcases.*", None)
    build.classify("tests/**", None)
    build.classify("archive/**", None)
    build.classify("images-output/**", None)
    build.classify("docs/**", None)
    build.classify("tools/**", None)
    build.classify("node_modules/**", None)
    build.classify("package.json", None)
    build.classify("package-lock.json", None)
    build.classify("game/audio/voice/manifest.json", None)
    build.classify("game/audio/voice/**/*.mp3", None)
    build.classify("game/audio/**/*.wav", None)
    build.classify("game/audio/.DS_Store", None)

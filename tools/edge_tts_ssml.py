#!/usr/bin/env python3
import argparse
import asyncio
import html
import re

import edge_tts
import edge_tts.communicate as communicate


def make_mkssml():
    def mkssml(tts_config, escaped_text):
        if isinstance(escaped_text, bytes):
            escaped_text = escaped_text.decode("utf-8")
        return (
            "<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-US'>"
            f"<voice name='{tts_config.voice}'>"
            f"<prosody pitch='{tts_config.pitch}' rate='{tts_config.rate}' volume='{tts_config.volume}'>"
            f"{escaped_text}"
            "</prosody>"
            "</voice>"
            "</speak>"
        )

    return mkssml


async def synthesize(args):
    communicate.mkssml = make_mkssml()
    voice = edge_tts.Communicate(
        args.text,
        args.voice,
        rate=args.rate,
        volume=args.volume,
        pitch=args.pitch,
    )
    await voice.save(args.write_media)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", required=True)
    parser.add_argument("--voice", required=True)
    parser.add_argument("--rate", default="+0%")
    parser.add_argument("--volume", default="+0%")
    parser.add_argument("--pitch", default="+0Hz")
    parser.add_argument("--write-media", required=True)
    args = parser.parse_args()
    asyncio.run(synthesize(args))


if __name__ == "__main__":
    main()

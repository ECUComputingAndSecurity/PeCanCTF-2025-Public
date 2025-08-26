import subprocess
import os

# download video from https://archive.org/details/rick-roll
INPUT_VIDEO = "Rick Roll.mp4"
OUTPUT_AUDIO = "my_original_music.mp3"

FLAG = "pecan{MO0S1C_4U_LoL!}"

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.',    'D': '-..',  'E': '.',    'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',     'J': '.---', 'K': '-.-',  'L': '.-..',
    'M': '--',  'N': '-.',   'O': '---',    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-',    'U': '..-',    'V': '...-', 'W': '.--',  'X': '-..-',
    'Y': '-.--','Z': '--..', '1': '.----',  '2': '..---','3': '...--','4': '....-',
    '5': '.....','6': '-....','7': '--...', '8': '---..', '9': '----.','0': '-----',
    '{': '-.--.', '}': '-.--.-', '=': '.-.-.', '/': "   "
}


DOT_DUR = 0.15     # Duration of a dot in seconds
DASH_DUR = 0.35    # Duration of a dash in seconds
SYMBOL_GAP = 0.09  # Gap between symbols in seconds
CHAR_GAP = 0.35    # Gap between chars in seconds
START_AT = 3.0     # Seconds into the video to begin Morse signals

MESSAGE = '  ' + ' '.join(str(ord(c)) for c in FLAG) + ' '


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)


def text_to_morse(text):
    out = []
    for c in text:
        if c == ' ':
            out.append(' ')
        else:
            out.append(MORSE_CODE_DICT.get(c.upper(), ''))
    return out

def make_beep(filename, duration):
    subprocess.run([
        "ffmpeg", "-y",
        "-f", "lavfi",
        "-i", f"sine=frequency=880:duration={duration}",
        "-filter:a", "volume=3.0",
        filename
    ], check=True)

def main():
    print(f"Flag: {FLAG}")
    print("Generating Morse code overlays with FFmpeg...")

    morse_chars = text_to_morse(MESSAGE)

    make_beep("dot.wav", DOT_DUR)
    make_beep("dash.wav", DASH_DUR)

    events = []
    timeline = START_AT
    for idx, morse in enumerate(morse_chars):
        if morse == ' ':
            timeline += CHAR_GAP
            continue
        for symbol in morse:
            events.append({
                'type': 'beep',
                'file': "dot.wav" if symbol == '.' else "dash.wav",
                'start': timeline,
                'duration': DOT_DUR if symbol == '.' else DASH_DUR,
                'char': MESSAGE[idx] if False else ''
            })
            timeline += DOT_DUR if symbol == '.' else DASH_DUR
            timeline += SYMBOL_GAP
        timeline += CHAR_GAP

    beep_inputs = []
    adelay_filters = []
    amix_inputs = ["[0:a]"]
    idx = 1
    for event in events:
        beep_inputs += ["-i", event['file']]
        delay_ms = int(event['start'] * 1000)
        adelay_filters.append(f"[{idx}:a]adelay={delay_ms}|{delay_ms}[b{idx}]")
        amix_inputs.append(f"[b{idx}]")
        idx += 1

    audio_base = INPUT_VIDEO
    if len(adelay_filters) > 0:
        filter_complex = ";".join(adelay_filters) + f";{''.join(amix_inputs)}amix=inputs={len(amix_inputs)}:duration=longest[aout]"
        audio_cmd = ["ffmpeg", "-y", "-i", INPUT_VIDEO] + beep_inputs + [
            "-filter_complex", filter_complex,
            "-map", "0:v", "-map", "[aout]", "-c:v", "copy", "withbeeps.mp4"
        ]
        print("\n[+] Adding beeps to video audio...")
        subprocess.run(audio_cmd, check=True)
        audio_base = "withbeeps.mp4"

    subprocess.run([
        "ffmpeg", "-y", "-i", audio_base, "-vn", "-acodec", "libmp3lame",
        OUTPUT_AUDIO
    ], check=True)

    print("\n--- Final step: Your flag is ---")
    print(f"Actual flag: {FLAG}")
    print(f"Ascii numbers: {MESSAGE.strip()}")
    print(f"As such morse code: {' '.join(morse_chars).strip()}")
    print(f"\n[+] Output mp3: {OUTPUT_AUDIO}")

    table_lines = [
        '| Morse Code          | ASCII | Char |',
        '|---------------------| :---: | :--: |'
    ]
    char_list = list(FLAG)
    ascii_list = [str(ord(c)) for c in FLAG]
    for c, a in zip(char_list, ascii_list):
        table_lines.append(f'| `{' '.join(text_to_morse(a))+'`':<18} | `{a+'`':<4} | `{c}`  |')
    table = '\n'.join(table_lines)
    readme = f"""# Stuck in your head!

## Flag

- `{FLAG}`

## Writeup

1. The actual Morse code you hear (or see in a spectrogram) is:
```
{' '.join(morse_chars).strip()}.
```

2. Convert morse code to its string and then convert its number to its ASCII character. 
The table below shows the full mapping from Morse code to flag character for reference:

{table}

3. Join the characters to get the flag:
```
{FLAG}
```

## Resources
- [Morse code reference](https://upload.wikimedia.org/wikipedia/commons/b/b5/International_Morse_Code.svg)
- [ASCII table](https://www.asciitable.com/)

### Notes

- The Morse code only appears once per song (no looping).
- The beeps are at 880Hz and should be clearly audible over the music after a short intro.
- You can use a spectrogram viewer to see the beeps visually if listening is difficult.
- If you get stuck, try both listening and looking at the spectrogram!
- If you transcribe the Morse code correctly, you can probably just give the numbers or dots/dashes sequence to an AI, and it can do the rest (Morse code → ASCII → flag) for you.
- The process is a bit tedious, but all steps are standard and solvable with online tools or a simple script.
"""

    with open("README.md", "w") as f:
        f.write(readme)
    print("[+] Output md:  README.md")

if __name__ == "__main__":
    main()
    # write_readme()
# Stuck in your head!

## Flag

- `pecan{MO0S1C_4U_L0L!}`

## Writeup

1. The actual Morse code you hear (or see in a spectrogram) is:
```
---.. -----   -.... ----.   -.... --...   -.... .....   --... ---..   .---- ..--- ...--   --... --...   --... ----.   ....- ---..   ---.. ...--   ....- ----.   -.... --...   ----. .....   ..... ..---   ---.. .....   ----. .....   --... -....   ....- ---..   --... -....   ...-- ...--   .---- ..--- ......
```

2. Convert morse code to its string and then convert its number to its ASCII character.
The table below shows the full mapping from Morse code to flag character for reference:

| Morse Code          | ASCII | Char |
|---------------------| :---: | :--: |
| `---.. -----`       | `80`  | `P`  |
| `-.... ----.`       | `69`  | `E`  |
| `-.... --...`       | `67`  | `C`  |
| `-.... .....`       | `65`  | `A`  |
| `--... ---..`       | `78`  | `N`  |
| `.---- ..--- ...--` | `123` | `{`  |
| `--... --...`       | `77`  | `M`  |
| `--... ----.`       | `79`  | `O`  |
| `....- ---..`       | `48`  | `0`  |
| `---.. ...--`       | `83`  | `S`  |
| `....- ----.`       | `49`  | `1`  |
| `-.... --...`       | `67`  | `C`  |
| `----. .....`       | `95`  | `_`  |
| `..... ..---`       | `52`  | `4`  |
| `---.. .....`       | `85`  | `U`  |
| `----. .....`       | `95`  | `_`  |
| `--... -....`       | `76`  | `L`  |
| `....- ---..`       | `48`  | `0`  |
| `--... -....`       | `76`  | `L`  |
| `...-- ...--`       | `33`  | `!`  |
| `.---- ..--- .....` | `125` | `}`  |

3. Join the characters to get the flag:
```
pecan{MO0S1C_4U_L0L!}
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

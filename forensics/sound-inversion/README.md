#Sound Inversion

##Writeup

As always, when you download a stegonography file, try checking the exif/meta data. For this I used `exiftool`. You can do this using a command like:

Once you run this you get an output along the lines of:

This reveals not much, except the comment which says `Is it just me or is the right channel different?` With how the description says that there is a hidden audio message within the file, the right channel being different would suggest that the message might be entirely hidden within the right channel of the sound.

Time to play the file.

The audio sounds like whitenoise, with the occasional noise on the right channel, that with the prior hint, is probably the audio file we are looking for.

When opening up `Sound_Inversion.wav` in an audio file editor it looks like this:

![image](https://github.com/user-attachments/assets/386a95f7-f254-494b-b4e2-7fd97759cabb)

As can be seen, in the right channel yet again, there appear to be occasional coloumns that are different.

So, from what we have gotten so far, it seems to be that we need to isolate the solitary sound on the right channel.

Time to research!

First up, the title 'Sound Inversion'. Sound Inversion appears to be a way to do noise cancellation, by inverting the sound waves, the troughs become crests, and the crests become troughs. This results in that when the inverted sound, and the normal sound play at the same time and amplitude, they cancel each other out. This is an effect called 'destructive interference'.

By looking at the two channels of the .wav file, it appears that the left and right channels are the same, except the seperate right channel sound we want to isolate. So if we invert the left channel and play that over the right channel, they should deconstructively interfere, thereby isolating the hidden message.

Doing this allows the hidden message to be quietly heard, and by increasing the volume the spoken words can be heard. The voice sounds to be saying:

Replacing the charcter names with the characters gets:

This appears to be the NATO phonetic language, which aligns with the military esque theme of the description. Converting from the NATO phonetic alphabet is easy, as it is just the first letter of all of these words.

This conversion then gets you the flag!

`pecan{hidden_audio_only_ononeear}`

-Added second flag as the audio sounds like the first like alpha
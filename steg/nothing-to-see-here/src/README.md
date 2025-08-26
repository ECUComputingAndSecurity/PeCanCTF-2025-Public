# Excalidraw image tampering

This simple python script takes two png images, and combines the visual data from one with the text metadata of another. It is indended for use with files generated from excalidraw.

You can use the tool by running:

```sh
python3 main.py decoy.png secret.png output.png
```

where `decoy.png` and `secret.png` are the two images you want to combine, and `output.png` is the name of the output file. The script will then create a new image that contains the visual data from `decoy.png` and the metadata from `secret.png`.

The output image will be saved as `output.png`.
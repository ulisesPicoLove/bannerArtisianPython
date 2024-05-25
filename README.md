# Banner Artisian with python

## Instalation

### Windows

```cmd
:: Create virtual environment
python -m venv venv

:: Activate virtual environment
venv\Scripts\activate

:: Install dependencies
pip install -r requirements.txt
```

### Mac and Linux

```bash
# Create virtual enverioment
python3 -m venv venv

# Activate virtual enverioment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

You must have a folder with a specific date inside the stack folder. This folder will contain all the subfolders for the banners you need to convert, formatted as widthxheight (e.g., 320x100). Inside these subfolders, you should have the corresponding images for the banners formatted as widthxheight_[animation_frame_number].png, for example, 320x480_1.png.

Let's see a complete example of what the stack structure would look like.

```bash
20240430
    ├── 240x400
    │   ├── 240x400-1.jpg
    │   ├── 240x400-2.jpg
    │   └── 240x400-3.jpg
    ├── 300x250
    │   ├── 300x250-1.jpg
    │   ├── 300x250-2.jpg
    │   └── 300x250-3.jpg
    ├── 300x600
    │   ├── 300x600-1.jpg
    │   ├── 300x600-2.jpg
    │   └── 300x600-3.jpg
    ├── 320x100
    │   ├── 320x100-1.jpg
    │   ├── 320x100-2.jpg
    │   └── 320x100-3.jpg
    ├── 336x280
    │   ├── 336x280-1.jpg
    │   ├── 336x280-2.jpg
    │   └── 336x280-3.jpg
    └── 970x250
        ├── 970x250-1.jpg
        ├── 970x250-2.jpg
        └── 970x250-3.jpg
```

> **Important:** Both the folder names and the file names must use x. Sometimes they come with X or ×, and that format will not work.

Once we have that structured, we only need to execute the following command:

python3 main.py [name_dir]

```bash
python3 main.py 20240430 # The name of the folder containing the banners we want to animate.
```

This will create a folder inside the output directory with the same name as the selected folder. To verify that everything is correct, the folder should contain an index.html file along with the images used in the animation.

```bash
├── 20240430
│   ├── 240x400
│   │   ├── 240X400_01.jpg
│   │   ├── 240X400_02.jpg
│   │   ├── 240X400_03.jpg
│   │   └── index.html
│   ├── 240x400.zip
│   ├── 300x250
│   │   ├── 300X250_01.jpg
│   │   ├── 300X250_02.jpg
│   │   ├── 300X250_03.jpg
│   │   └── index.html
│   ├── 300x250.zip
│   ├── 300x600
│   │   ├── 300X600_01.jpg
│   │   ├── 300X600_02.jpg
│   │   ├── 300X600_03.jpg
│   │   └── index.html
│   ├── 300x600.zip
│   ├── 320x100
│   │   ├── 320X100_01.jpg
│   │   ├── 320X100_02.jpg
│   │   ├── 320X100_03.jpg
│   │   └── index.html
│   ├── 320x100.zip
│   ├── 336x280
│   │   ├── 336X280_01.jpg
│   │   ├── 336X280_02.jpg
│   │   ├── 336X280_03.jpg
│   │   └── index.html
│   ├── 336x280.zip
│   ├── 970x250
│   │   ├── 970X250_01.jpg
│   │   ├── 970X250_02.jpg
│   │   ├── 970X250_03.jpg
│   │   └── index.html
│   └── 970x250.zip

```

Finally, compress the created folder in the output directory and pass it to the person who requested the banners.
#!/usr/bin/env python3
"""Download the public GitHub avatar and prepare it for ASCII rendering."""
from io import BytesIO

import requests
from PIL import Image, ImageOps

AVATAR_URL = "https://avatars.githubusercontent.com/u/204649822?v=4&size=512"


def main() -> None:
    response = requests.get(
        AVATAR_URL,
        headers={"User-Agent": "Aisyahnov-profile-art"},
        timeout=30,
    )
    response.raise_for_status()
    image = Image.open(BytesIO(response.content)).convert("RGBA")
    side = min(image.size)
    left = (image.width - side) // 2
    top = (image.height - side) // 2
    image = image.crop((left, top, left + side, top + side))
    background = Image.new("RGBA", image.size, (255, 255, 255, 255))
    image = Image.alpha_composite(background, image).convert("L")
    image = ImageOps.autocontrast(image, cutoff=1)
    image = ImageOps.fit(image, (512, 512), method=Image.Resampling.LANCZOS)
    image.save("source-prepped.png")
    print("wrote source-prepped.png from the GitHub avatar")


if __name__ == "__main__":
    main()

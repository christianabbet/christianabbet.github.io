"""Resize every image in assets/images into fixed-size thumbnails in assets/images_thumbnails."""

from pathlib import Path

from PIL import Image, ImageOps

SRC_DIR = Path(__file__).parent.parent / "assets" / "images"
DST_DIR = Path(__file__).parent.parent / "assets" / "images_thumbnails"
THUMB_SIZE = (400, 300)  # width, height (4:3)
IMAGE_EXTS = {".jpg", ".jpeg", ".png"}


def make_thumbnail(img: Image.Image) -> Image.Image:
    """Center-crop and resize an image to THUMB_SIZE, filling the frame.

    Args:
        img (Image.Image): source image, any size or aspect ratio.

    Returns:
        Image.Image: RGB image resized to exactly THUMB_SIZE.
    """
    return ImageOps.fit(img.convert("RGB"), THUMB_SIZE, Image.LANCZOS)


def generate_thumbnails() -> None:
    """Generate a same-size thumbnail in DST_DIR for every image in SRC_DIR."""
    DST_DIR.mkdir(parents=True, exist_ok=True)
    for src in sorted(SRC_DIR.iterdir()):
        if src.suffix.lower() not in IMAGE_EXTS:
            continue
        with Image.open(src) as img:
            make_thumbnail(img).save(DST_DIR / f"{src.stem}.jpg", "JPEG", quality=80)
    print(f"Wrote thumbnails to {DST_DIR}")


if __name__ == "__main__":
    generate_thumbnails()

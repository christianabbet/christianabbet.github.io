"""Resize every image in assets/images into fixed-size thumbnails."""

import argparse
from pathlib import Path

from PIL import Image, ImageOps

THUMB_SIZE = (600, 450)  # width, height (4:3)
IMAGE_EXTS = {".jpg", ".jpeg", ".png"}


def make_thumbnail(img: Image.Image) -> Image.Image:
    """Center-crop and resize an image to THUMB_SIZE, filling the frame.

    Args:
        img (Image.Image): source image, any size or aspect ratio.

    Returns:
        Image.Image: RGB image resized to exactly THUMB_SIZE.
    """
    return ImageOps.fit(img.convert("RGB"), THUMB_SIZE, Image.LANCZOS)


def generate_thumbnails(src_dir: Path, dst_dir: Path) -> None:
    """Generate a same-size thumbnail in dst_dir for every image in src_dir."""
    dst_dir.mkdir(parents=True, exist_ok=True)
    for src in sorted(src_dir.iterdir()):
        if src.suffix.lower() not in IMAGE_EXTS:
            continue
        with Image.open(src) as img:
            make_thumbnail(img).save(dst_dir / f"{src.stem}.jpg", "JPEG", quality=80)
    print(f"Wrote thumbnails to {dst_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        type=Path,
        required=True,
        help="Directory of source bird images",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default="assets/images_thumbnails",
        help="Directory to write thumbnails to",
    )
    args = parser.parse_args()

    generate_thumbnails(src_dir=args.input, dst_dir=args.output)

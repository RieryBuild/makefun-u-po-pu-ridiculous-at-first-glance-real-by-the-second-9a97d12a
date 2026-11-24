import os

# One sentence, 143 chars: a bizarre startup that sounds like a joke
# until the money clause lands — idle hearses are the world's quietest
# nap pods, and night-shift nurses will pay for silence nobody dares
# interrupt.
PITCH = (
    "We rent out idle hearses as the world's quietest nap pods, "
    "because night-shift nurses pay $15 for 40 minutes of "
    "silence nobody dares interrupt."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()

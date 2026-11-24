import os

LINE = ("I did not miss that spot. My sensors classified it as a "
        "permanent resident, and I do not evict tenants without a "
        "court order.")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

from pathlib import Path

def clean_text(text):
    lines = text.splitlines()
    lines = [line.strip() for line in lines]
    lines = [line for line in lines if len(line) > 0]
    return "\n".join(lines)

def split_text(text, train_ratio=0.8):
    split_index = int(len(text) * train_ratio)
    return text[:split_index], text[split_index:]

if __name__ == '__main__':
    # Place your extracted raw plain text into these two files first.
    undrip_raw = Path("undrip_raw.txt").read_text(encoding="utf-8")
    economic_raw = Path("economic_raw.txt").read_text(encoding="utf-8")

    undrip_clean = clean_text(undrip_raw)
    economic_clean = clean_text(economic_raw)

    undrip_train, undrip_val = split_text(undrip_clean, train_ratio=0.8)

    Path("undrip_train.txt").write_text(undrip_train, encoding="utf-8")
    Path("undrip_val.txt").write_text(undrip_val, encoding="utf-8")
    Path("economic_test.txt").write_text(economic_clean, encoding="utf-8")
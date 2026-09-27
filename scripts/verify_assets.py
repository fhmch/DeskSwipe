import os
import json
import re

def main():
    print("=== ASSET INTEGRITY VERIFICATION ===")
    missing = []
    
    # 1. Check data/parts_catalog.json
    with open('data/parts_catalog.json', 'r', encoding='utf-8') as f:
        cat = json.load(f)

    for k, v in cat.items():
        if isinstance(v, list):
            for item in v:
                img = item.get('img')
                if img and not os.path.exists(img):
                    missing.append(f"Catalog {k}/{item.get('key')}: {img}")

    # 2. Check index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    assets_in_html = set(re.findall(r'assets/[a-zA-Z0-9_\-/]+\.jpg', html))
    print(f"Total distinct assets referenced in index.html: {len(assets_in_html)}")
    for a in sorted(assets_in_html):
        exists = os.path.exists(a)
        status = "[OK]" if exists else "[MISSING]"
        print(f"  {status} {a} ({os.path.getsize(a) if exists else 0} bytes)")
        if not exists:
            missing.append(f"index.html: {a}")

    if missing:
        print("\nERROR: Found missing assets:")
        for m in missing:
            print("  -", m)
        return 1
    else:
        print("\nSUCCESS: All referenced assets are 100% present on local disk with zero 404s!")
        return 0

if __name__ == '__main__':
    exit(main())

import urllib.request, urllib.parse, json, os, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'DeskStudioApp/1.0 (contact@example.org) AppleWebKit/537.36'
}

def get_wiki_url(file_title):
    try:
        api = 'https://commons.wikimedia.org/w/api.php?' + urllib.parse.urlencode({
            'action': 'query',
            'titles': f'File:{file_title}',
            'prop': 'imageinfo',
            'iiprop': 'url',
            'format': 'json'
        })
        req = urllib.request.Request(api, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=8) as res:
            data = json.loads(res.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            for pid, pinfo in pages.items():
                info = pinfo.get('imageinfo', [{}])[0]
                if 'url' in info:
                    return info['url']
    except Exception as e:
        print(f"Error fetching wiki url for {file_title}: {e}")
    return None

def download_file(url, target_path):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=12) as res:
            data = res.read()
            if len(data) > 3000:
                with open(target_path, 'wb') as f:
                    f.write(data)
                print(f"[OK] Downloaded {target_path} ({len(data)} bytes)")
                return True
            else:
                print(f"[WARN] File too small ({len(data)}b): {url}")
                return False
    except Exception as e:
        print(f"[ERR] Failed {target_path} from {url}: {e}")
        return False

wiki_files = {
    "assets/psu_corsair_modular.jpg": "Modular Power Supply Unit.jpg",
    "assets/psu_bronze.jpg": "Inside a switching power supply.jpg",
    "assets/ram_ddr5_crucial.jpg": "DDR5 UDIMM with PMIC.jpg",
    "assets/ssd_nvme_gen4.jpg": "Samsung PM981 M.2 NVMe SSD.jpg",
    "assets/kb_hhkb_real.jpg": "HHKB Pro2 Type-S.jpg",
    "assets/gpu_dual_fan.jpg": "GeForce RTX 3060 Ti Founders Edition.jpg",
    "assets/gpu_triple_fan.jpg": "GeForce RTX 3080 Ti Founders Edition.jpg"
}

def main():
    print("=== RESOLVING AND DOWNLOADING WIKIMEDIA COMMONS ASSETS ===")
    for target, title in wiki_files.items():
        direct_url = get_wiki_url(title)
        if direct_url:
            download_file(direct_url, target)
        else:
            print(f"[ERR] Could not resolve url for {title}")

if __name__ == '__main__':
    main()

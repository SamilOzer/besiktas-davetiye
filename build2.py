import os

with open('qrcode.min.js', 'r', encoding='utf-8') as f:
    qr_lib = f.read()

with open('jsqr.min.js', 'r', encoding='utf-8') as f:
    jsqr_lib = f.read()

# =============================================
# INDEX.HTML — Davetiye Yönetim + QR Üretici
# =============================================
index = open('index_template.html', 'r', encoding='utf-8').read()
index = index.replace('__QRCODE_LIB__', qr_lib)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index)
print('index.html:', len(index), 'bytes')

# =============================================
# SCANNER.HTML — Kapı Kontrol + QR Okuyucu
# =============================================
scanner = open('scanner_template.html', 'r', encoding='utf-8').read()
scanner = scanner.replace('__JSQR_LIB__', jsqr_lib)

with open('scanner.html', 'w', encoding='utf-8') as f:
    f.write(scanner)
print('scanner.html:', len(scanner), 'bytes')
print('DONE')

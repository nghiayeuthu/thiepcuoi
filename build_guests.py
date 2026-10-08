# Tạo trang riêng cho từng khách: python3 build_guests.py  (sửa danh sách GUESTS bên dưới)
import html, os, re, unicodedata
GUESTS = ["em Việt", "em Hiền", "em Khánh", "anh Thái"]
BASE = "https://nghiayeuthu.github.io/thiepcuoi/"

def slug(name):
    s = re.sub(r"^(anh|chị|chi|em|cô|chú|bác|ông|bà|cậu|mợ|dì|thím)\s+", "", name.strip(), flags=re.I)
    s = unicodedata.normalize("NFD", s.replace("đ", "d").replace("Đ", "D"))
    s = "".join(c for c in s if unicodedata.category(c) != "Mn").lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")

src = open("index.html", encoding="utf-8").read()
for name in GUESTS:
    sl, n = slug(name), html.escape(name)
    page = re.sub(r"([\"'(])img/", r"\1../img/", src)
    page = page.replace('content="' + BASE + '"', 'content="' + BASE + sl + '/"')
    page = re.sub(r'<meta property="og:title" content="[^"]*">',
                  f'<meta property="og:title" content="Thân mời {n} · Thiệp cưới Tuấn Nghĩa &amp; Hoài Thu">', page)
    page = page.replace("<script>", f"<script>window.GUEST={name!r};", 1)
    os.makedirs(sl, exist_ok=True)
    open(f"{sl}/index.html", "w", encoding="utf-8").write(page)
    print(f"{name}: {BASE}{sl}/")

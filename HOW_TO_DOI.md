# Cách đẩy GitHub và lấy DOI (Zenodo)

Gói này nằm trong `ttll-p3/`. Không đẩy cả thư mục `Paper3` (21 GB raster + tọa độ hộ).

Có **hai cách**. Cách A cho DOI gắn với GitHub (nên dùng). Cách B lấy DOI trong ~10 phút nếu chưa muốn mở repo.

---

## Cách A — GitHub công khai + Zenodo (khuyến nghị)

### 1. Tạo repo GitHub

1. Vào https://github.com/new
2. Tên gợi ý: `ttll-p3-metro-lockin`
3. **Public** (Zenodo chỉ mint DOI ổn định cho repo public, trừ Zenodo Sandbox)
4. **Không** thêm README / LICENSE / `.gitignore` (đã có trong thư mục này)
5. Create repository

### 2. Đẩy thư mục này lên

Trong terminal, đứng **trong** `ttll-p3`:

```bash
git init -b main
git add -A
git commit -m "Initial commit: Paper 3 replication package"
git remote add origin https://github.com/<USER>/ttll-p3-metro-lockin.git
git push -u origin main
```

Nếu git đã được khởi tạo sẵn trong thư mục này, chỉ cần thêm `remote` rồi `push`.

### 3. Nối Zenodo

1. Đăng nhập https://zenodo.org bằng tài khoản GitHub
2. GitHub → Settings → Applications → Zenodo: cấp quyền đọc repo
3. Trên Zenodo: **GitHub** (menu tài khoản) → bật công tắc repo `ttll-p3-metro-lockin`
4. Chờ vài giây đến khi Zenodo báo webhook đã gắn

### 4. Tạo Release để mint DOI

Trên GitHub: **Releases → Draft a new release**

- Tag: `v1.0.0`
- Title: `Paper 3 replication package v1.0.0`
- Publish release

Zenodo sẽ tự tạo record và cấp DOI dạng `10.5281/zenodo.xxxxxxx`. Email xác nhận thường tới trong 1–5 phút.

### 5. Gắn DOI vào bài

1. Copy DOI từ trang Zenodo (nút Cite)
2. Thêm vào `CITATION.cff`:

```yaml
identifiers:
  - type: doi
    value: 10.5281/zenodo.xxxxxxx
```

3. Trong bản thảo, Data availability: `The replication package is archived at https://doi.org/10.5281/zenodo.xxxxxxx`
4. Commit và (tuỳ chọn) tạo `v1.0.1` — Zenodo cấp DOI phiên bản mới; **DOI concept** (không có số version) luôn trỏ bản mới nhất. Dùng concept DOI trong bài.

---

## Cách B — Upload zip thẳng lên Zenodo (không cần GitHub)

1. Nén **nội dung** `ttll-p3` (không nén cả `DataPaper3` 21 GB)
2. https://zenodo.org → New upload
3. Upload zip
4. Form:
   - Upload type: **Software** (hoặc Publication → Preprint)
   - Title: lấy từ `CITATION.cff`
   - Authors + ORCID
   - License: **Creative Commons Attribution 4.0**
   - Description: đoạn trong `.zenodo.json`
5. Publish → nhận DOI ngay

Cách này nhanh nhưng không tự version theo git.

---

## Không đưa lên git / Zenodo

| File | Lý do |
|---|---|
| `QData_*.xlsx` gốc, `HoTen`, `Email`, `DT`, `Lat`/`Long` | Định danh hộ |
| `vietnam-*.osm.pbf` | 264 + 304 MB, vượt giới hạn GitHub 100 MB/file |
| Raster GHSL toàn cầu `.tif` / `.ovr` | ~16 GB |
| `osm_cache.zip`, `Paper3_bundle.zip` | Trùng; cache đường lớn |
| `Paper3_GhiChu_TiengViet.docx` | Ghi chú nội bộ |

---

## Kiểm tra trước khi public

```bash
# không được còn cột tọa độ / họ tên
python -c "import pandas as pd; c=pd.read_csv('derived/citizens_analysis_public.csv'); print([x for x in c.columns if x in ['Lat','Long','HoTen','Email','DT']])"
```

Kết quả phải là `[]`.

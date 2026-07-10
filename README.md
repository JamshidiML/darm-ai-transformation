# Darmstaedter + Klevers AI Transformation

این مخزن شامل خروجی‌های کامل پروژه «استراتژی تحول هوش مصنوعی برای Darmstädter و Klevers» است: گزارش راهبردی، ارائه هیئت‌مدیره، نسخه فارسی PDF، تصاویر پیش‌نمایش، منابع تصویری، و مستندات روند تولید.

> نکته محرمانگی: محتوای این مخزن برای استفاده داخلی و مدیریتی طراحی شده است. به دلیل وجود تحلیل راهبردی، فرضیات عملیاتی، و برنامه پیشنهادی تحول AI، بهتر است مخزن در GitHub به صورت **private** نگهداری شود.

## هدف پروژه

هدف این پروژه پیشنهاد چند ایده پراکنده AI نیست. هدف، ساخت یک مسیر اجرایی برای تبدیل دانش فنی منسوجات صنعتی، شواهد کیفیت، داده‌های آزمایشگاه، داده‌های تولید، و تجربه خبرگان به یک مزیت صنعتی قابل اندازه‌گیری است.

توصیه اصلی پروژه:

- شروع با یک پایلوت ۱۲ هفته‌ای فقط خواندنی برای **Coating and Packaging Quality Intelligence**
- اتصال داده‌های سفارش/رول، بازرسی، QC، آزمایشگاه، تولید و شکایات
- ساخت پاسپورت کیفیت سطح رول و تحلیل ریشه‌یابی
- پرهیز از کنترل ماشین در فاز اول
- استفاده از نتایج پایلوت برای پرونده ROI، تامین مالی، و ساخت پلتفرم AI صنعتی

## فایل‌های اصلی

| فایل | توضیح |
|---|---|
| `outputs/AI_TRANSFORMATION_STRATEGY_REPORT.md` | گزارش کامل ۱۳ بخشی استراتژی تحول AI |
| `outputs/Darmstaedter_Klevers_AI_Transformation_Board_Deck.pptx` | ارائه انگلیسی هیئت‌مدیره با speaker notes |
| `outputs/Darmstaedter_Klevers_AI_Transformation_Board_Deck_FA.pptx` | نسخه فارسی قابل ویرایش ارائه |
| `outputs/Darmstaedter_Klevers_AI_Transformation_Board_Deck_FA.pdf` | نسخه فارسی PDF برای ارائه/ارسال |
| `outputs/Darmstaedter_Klevers_AI_Transformation_Board_Deck_montage.png` | پیش‌نمایش تصویری کل ارائه انگلیسی |
| `outputs/Darmstaedter_Klevers_AI_Transformation_Board_Deck_FA_pdf_montage.png` | پیش‌نمایش تصویری کل PDF فارسی |
| `outputs/assets/` | تصاویر و لوگوهای استفاده‌شده در ارائه |
| `docs/ARTIFACT_INDEX_FA.md` | فهرست کامل artifactها و کاربرد هرکدام |
| `docs/PROJECT_PROCESS_FA.md` | روند تولید، تحقیق، ساخت deck، ترجمه فارسی، و کنترل کیفیت |

## ساختار مخزن

```text
.
├── README.md
├── docs/
│   ├── ARTIFACT_INDEX_FA.md
│   └── PROJECT_PROCESS_FA.md
└── outputs/
    ├── AI_TRANSFORMATION_STRATEGY_REPORT.md
    ├── Darmstaedter_Klevers_AI_Transformation_Board_Deck.pptx
    ├── Darmstaedter_Klevers_AI_Transformation_Board_Deck_FA.pptx
    ├── Darmstaedter_Klevers_AI_Transformation_Board_Deck_FA.pdf
    ├── *_montage.png
    ├── *_inspect.ndjson
    ├── Darmstaedter_Klevers_AI_Transformation_Board_Deck*/
    └── assets/
```

## منابع تحقیق

گزارش و ارائه بر اساس منابع عمومی رسمی شرکت‌ها و منابع تامین مالی فعلی ساخته شده‌اند، از جمله:

- Darmstädter: `https://www.darmstaedter.eu/unternehmen/`
- Darmstädter Beschichtungen: `https://www.darmstaedter.eu/beschichtungen/`
- Darmstädter Qualität: `https://www.darmstaedter.eu/qualitaet/`
- Darmstädter Entwicklung: `https://www.darmstaedter.eu/entwicklung/`
- Klevers: `https://klevers.de/unternehmen/`
- Klevers Lieferprogramm: `https://klevers.de/lieferprogramm/`
- Klevers Qualität: `https://klevers.de/qualitaet/`
- Klevers Projekte: `https://klevers.de/projekte/`
- ZIM: `https://www.zim.de/`
- Forschungszulage / BSFZ: `https://www.bescheinigung-forschungszulage.de/`
- NRW.BANK MID: `https://www.nrwbank.de/mid`
- BAFA EEW: `https://www.bafa.de/`
- Eurostars: `https://www.eurekanetwork.org/programmes-and-calls/eurostars/`
- Horizon Europe: `https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-europe_en`
- EIC Accelerator: `https://eic.ec.europa.eu/eic-funding-opportunities/eic-accelerator_en`

## فرضیات داخلی که باید قبل از اجرا راستی‌آزمایی شوند

این موارد در گزارش به عنوان فرضیه/چک‌لیست discovery آمده‌اند و نباید بدون بررسی داخلی به عنوان fact قطعی استفاده شوند:

- وجود یا کیفیت export از ERP/INTEX
- ساختار داده ELSIS یا سیستم بازرسی
- دسترسی به PLC/HMI یا داده‌های خطوط تولید
- امکان اتصال شناسه رول به سفارش، QC، آزمایشگاه، بازرسی و شکایت
- کیفیت برچسب‌گذاری عیوب و استاندارد بودن defect taxonomy
- مقادیر واقعی scrap، rework، complaint cost، OEE، downtime، و زمان release

## نحوه استفاده پیشنهادی

1. ابتدا `outputs/AI_TRANSFORMATION_STRATEGY_REPORT.md` را برای فهم کامل منطق پروژه بخوانید.
2. برای جلسه مدیریت از deck انگلیسی یا PDF فارسی استفاده کنید.
3. برای ارائه فارسی، فایل `outputs/Darmstaedter_Klevers_AI_Transformation_Board_Deck_FA.pdf` آماده‌ترین نسخه است.
4. برای اصلاح متن/اسلاید، فایل `outputs/Darmstaedter_Klevers_AI_Transformation_Board_Deck_FA.pptx` را ویرایش کنید.
5. برای بازسازی یا ادامه پروژه، `docs/PROJECT_PROCESS_FA.md` را مبنا قرار دهید.

## وضعیت فعلی

- گزارش راهبردی کامل شده است.
- deck انگلیسی هیئت‌مدیره ساخته و کنترل کیفیت شده است.
- نسخه فارسی PPTX و PDF ساخته شده است.
- خروجی PDF فارسی ۲۳ صفحه دارد.
- فایل‌های preview و montage برای QA تصویری نگهداری شده‌اند.


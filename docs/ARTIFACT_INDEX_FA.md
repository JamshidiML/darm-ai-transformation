# فهرست فایل‌ها و artifactهای پروژه

این سند توضیح می‌دهد هر فایل داخل مخزن برای چه کاری است و در چه موقعیتی باید استفاده شود.

## خروجی‌های اصلی

### `outputs/AI_TRANSFORMATION_STRATEGY_REPORT.md`

گزارش اصلی و کامل پروژه. شامل:

- تحلیل شرکت Darmstädter و Klevers
- نقشه فرصت AI در کل سازمان
- تحلیل واحد به واحد
- R&D Transformation
- Production Transformation
- Quality Transformation
- Packaging Transformation
- Knowledge Management Platform
- Roadmap سه‌ماهه تا پنج‌ساله
- Funding Opportunities
- Risk Analysis
- Executive Prioritization
- Career Strategy
- طرح ارائه هیئت‌مدیره

کاربرد پیشنهادی: سند مرجع داخلی و leave-behind بعد از جلسه مدیریت.

### `outputs/Darmstaedter_Klevers_AI_Transformation_Board_Deck.pptx`

ارائه انگلیسی هیئت‌مدیره، با طراحی executive و speaker notes برای هر اسلاید.

کاربرد پیشنهادی: ارائه رسمی برای مدیریت، هیئت‌مدیره یا مدیران غیر فارسی‌زبان.

### `outputs/Darmstaedter_Klevers_AI_Transformation_Board_Deck_FA.pptx`

نسخه فارسی قابل ویرایش ارائه. متن‌های روی اسلایدها و speaker notes به فارسی منتقل شده‌اند.

کاربرد پیشنهادی: ویرایش محتوای فارسی قبل از جلسه، تغییر نام‌ها، اضافه کردن اعداد داخلی، یا ساخت نسخه نهایی شرکتی.

### `outputs/Darmstaedter_Klevers_AI_Transformation_Board_Deck_FA.pdf`

نسخه PDF فارسی آماده ارسال/ارائه. این فایل از نسخه فارسی PPTX خروجی گرفته شده و با render صفحه‌ها کنترل شده است.

کاربرد پیشنهادی: ارسال به مدیریت یا استفاده مستقیم در جلسه فارسی.

## فایل‌های کنترل کیفیت و preview

### `outputs/Darmstaedter_Klevers_AI_Transformation_Board_Deck_montage.png`

نمای تصویری تمام اسلایدهای انگلیسی در یک تصویر.

کاربرد پیشنهادی: کنترل سریع طراحی، ترتیب اسلایدها، و شناسایی خطای بصری.

### `outputs/Darmstaedter_Klevers_AI_Transformation_Board_Deck_FA_montage.png`

نمای تصویری تمام اسلایدهای فارسی PPTX.

کاربرد پیشنهادی: کنترل سریع چیدمان فارسی در سطح deck.

### `outputs/Darmstaedter_Klevers_AI_Transformation_Board_Deck_FA_pdf_montage.png`

نمای تصویری تمام صفحات PDF فارسی.

کاربرد پیشنهادی: کنترل نهایی PDF، مخصوصا خوانایی متن فارسی و چیدمان RTL.

### `outputs/Darmstaedter_Klevers_AI_Transformation_Board_Deck/`

رندر PNG اسلایدهای انگلیسی.

کاربرد پیشنهادی: بررسی تک‌اسلایدی، مستندسازی، یا استفاده در گزارش/ایمیل.

### `outputs/Darmstaedter_Klevers_AI_Transformation_Board_Deck_FA/`

رندر PNG اسلایدهای فارسی PPTX.

کاربرد پیشنهادی: کنترل تک‌اسلایدی نسخه فارسی.

### `outputs/Darmstaedter_Klevers_AI_Transformation_Board_Deck_FA_pdf_pages/`

رندر PNG صفحات PDF فارسی.

کاربرد پیشنهادی: کنترل نهایی صفحه به صفحه PDF.

### `*.inspect.ndjson`

خروجی بازرسی ساختاری deckها شامل متن، slide id، object id، و speaker notes.

کاربرد پیشنهادی: دیباگ، بررسی وجود notes، و تحلیل ساختار deck. این فایل برای ارائه لازم نیست اما برای reproducibility نگهداری شده است.

## فایل‌های تصویری

### `outputs/assets/`

شامل تصاویر و لوگوهای استفاده‌شده در deck:

- `darmstaedter_logo.png`
- `darmstaedter_coatings.jpg`
- `darmstaedter_lab.jpg`
- `darmstaedter_factory.jpg`
- `klevers_logo.jpg`
- `klevers_home.jpg`

کاربرد پیشنهادی: بازسازی deck، تغییر طراحی، یا ساخت نسخه‌های بعدی.

## توصیه برای نسخه‌های بعدی

اگر بعدا داده داخلی اضافه شد، بهتر است نسخه‌های جدید با suffix تاریخ یا نسخه ساخته شوند:

- `AI_TRANSFORMATION_STRATEGY_REPORT_v2.md`
- `Darmstaedter_Klevers_AI_Transformation_Board_Deck_v2.pptx`
- `Darmstaedter_Klevers_AI_Transformation_Board_Deck_FA_v2.pdf`

برای داده‌های حساس داخلی، قبل از push به GitHub سطح محرمانگی و visibility مخزن را دوباره بررسی کنید.


# روند تولید پروژه و انتقال به مخزن

این سند روند کاری پروژه را ثبت می‌کند تا ادامه، بازبینی یا ارائه آن ساده باشد.

## 1. ماموریت اولیه

درخواست اولیه این بود که یک استراتژی عمیق و اختصاصی برای تحول AI در Darmstädter و Klevers ساخته شود؛ نه مجموعه‌ای از ایده‌های عمومی. خروجی باید هم از نظر مدیریتی قانع‌کننده باشد و هم برای یک R&D Engineer که می‌خواهد رهبر داخلی تحول AI شود، قابل استفاده باشد.

تمرکز اصلی:

- ارزش کسب‌وکار
- ROI
- امکان‌پذیری فنی
- مزیت رقابتی
- پتانسیل بلندمدت پلتفرم AI صنعتی
- موقعیت‌سازی شغلی AI Champion داخلی

## 2. تحقیق و منبع‌یابی

تحقیق بر پایه منابع عمومی رسمی انجام شد. مهم‌ترین مسیرهای تحقیق:

- صفحات رسمی Darmstädter درباره شرکت، پوشش‌دهی، کیفیت، توسعه و کاربردها
- صفحات رسمی Klevers درباره شرکت، محصولات، بافندگی، پوشش‌ها، لمینیشن، کیفیت و پروژه‌ها
- منابع تامین مالی در آلمان، NRW، اتحادیه اروپا و برنامه‌های نوآوری

در گزارش، داده‌های عمومی از فرضیات داخلی جدا شده‌اند. برای مثال، مواردی مانند INTEX، ELSIS، PLC/HMI، یا کیفیت linkage بین رول و سفارش به عنوان چک‌لیست discovery آمده‌اند، نه fact عمومی.

## 3. طراحی thesis استراتژیک

نتیجه تحلیلی اصلی:

شرکت‌ها فقط تولیدکننده منسوجات نیستند؛ ارزش اصلی در ترکیب‌های مهندسی‌شده بین ماده، فرایند، پوشش، لمینیشن، آزمون، گواهی، کاربرد و دانش خبرگان است. بنابراین بهترین نقطه شروع AI اتوماسیون کامل نیست، بلکه اتصال داده و دانش برای تکرارپذیری، ریشه‌یابی، و یادگیری سازمانی است.

پیشنهاد اصلی:

یک پایلوت ۱۲ هفته‌ای فقط خواندنی با عنوان **Coating and Packaging Quality Intelligence**.

## 4. گزارش راهبردی

گزارش اصلی در این مسیر ساخته شد:

1. Executive Thesis
2. Evidence Base
3. AI Opportunity Map
4. تحلیل واحد به واحد
5. R&D Transformation
6. Production Transformation
7. Quality Transformation
8. Packaging Transformation
9. Knowledge Management Platform
10. Industrial AI Roadmap
11. Funding Opportunities
12. Risk Analysis
13. Executive Prioritization
14. Career Strategy
15. Executive Presentation Storyline

فایل خروجی:

`outputs/AI_TRANSFORMATION_STRATEGY_REPORT.md`

## 5. ساخت ارائه هیئت‌مدیره

ارائه انگلیسی با تمرکز board-ready ساخته شد:

- ۲۳ اسلاید
- متن کم و تصمیم‌محور
- speaker notes روی همه اسلایدها
- تمرکز روی pilot approval، نه نمایش تکنولوژی
- طراحی executive با تصاویر شرکت و ساختار مشاوره‌ای

فایل خروجی:

`outputs/Darmstaedter_Klevers_AI_Transformation_Board_Deck.pptx`

## 6. کنترل کیفیت ارائه انگلیسی

برای deck انگلیسی چند کنترل انجام شد:

- خروجی inspect ساختاری
- render تمام اسلایدها به PNG
- ساخت montage برای مرور کل deck
- تست overflow متن
- اصلاح عنوان‌های بلند و چیدمان قبل از تحویل

فایل‌های مرتبط:

- `outputs/Darmstaedter_Klevers_AI_Transformation_Board_Deck.pptx.inspect.ndjson`
- `outputs/Darmstaedter_Klevers_AI_Transformation_Board_Deck/`
- `outputs/Darmstaedter_Klevers_AI_Transformation_Board_Deck_montage.png`

## 7. ساخت نسخه فارسی

پس از درخواست نسخه فارسی PDF، نسخه فارسی به عنوان artifact جداگانه ساخته شد تا deck انگلیسی دست‌نخورده بماند.

اقدامات:

- ترجمه محتوای اسلایدها به فارسی طبیعی
- نگه‌داشتن اصطلاحات فنی ضروری مثل ERP، QC، AI در جاهایی که خوانایی بهتر بود
- تنظیم متن برای راست‌به‌چپ
- ساخت فایل PPTX فارسی قابل ویرایش
- تبدیل به PDF فارسی با LibreOffice

فایل‌های خروجی:

- `outputs/Darmstaedter_Klevers_AI_Transformation_Board_Deck_FA.pptx`
- `outputs/Darmstaedter_Klevers_AI_Transformation_Board_Deck_FA.pdf`

## 8. کنترل کیفیت نسخه فارسی

برای نسخه فارسی نیز کنترل کیفیت انجام شد:

- تست overflow روی PPTX فارسی
- render اسلایدهای فارسی
- export PDF
- render صفحات PDF فارسی
- ساخت montage PDF فارسی
- بازبینی بصری خوانایی RTL و اصلاح مواردی مثل جای‌گیری `R&D` در متن فارسی

فایل‌های مرتبط:

- `outputs/Darmstaedter_Klevers_AI_Transformation_Board_Deck_FA.pptx.inspect.ndjson`
- `outputs/Darmstaedter_Klevers_AI_Transformation_Board_Deck_FA/`
- `outputs/Darmstaedter_Klevers_AI_Transformation_Board_Deck_FA_pdf_pages/`
- `outputs/Darmstaedter_Klevers_AI_Transformation_Board_Deck_FA_pdf_montage.png`

## 9. انتقال به GitHub

برای انتقال به GitHub، مخزن محلی شامل همه خروجی‌ها و مستندات آماده شده است:

- اضافه شدن `README.md`
- اضافه شدن `docs/ARTIFACT_INDEX_FA.md`
- اضافه شدن `docs/PROJECT_PROCESS_FA.md`
- نگهداری همه فایل‌های `outputs/`
- آماده‌سازی commit اولیه

پیشنهاد visibility برای GitHub:

**Private repository**

دلیل: محتوای پروژه شامل تحلیل راهبردی، نقشه راه AI، فرضیات عملیاتی، و مسیر پیشنهادی برای مدیریت شرکت است.

## 10. گام‌های بعدی پیشنهادی

برای ادامه پروژه پس از ایجاد مخزن:

1. اضافه کردن داده‌های داخلی واقعی scrap/rework/complaint/OEE در یک branch جدا.
2. ساخت نسخه v2 گزارش با اعداد داخلی و ROI دقیق‌تر.
3. ساخت pilot charter رسمی بر اساس deck.
4. افزودن issueهای GitHub برای workstreamها:
   - Data discovery
   - Quality pilot
   - R&D knowledge graph
   - Funding application
   - Management presentation
5. نگه داشتن مخزن private و محدود کردن access به افراد درگیر پروژه.


<div align="center">

<img src="assets/AzizDB_Penguin.png" alt="AzizDB Penguin" width="210">

# 🐧 AzizDB

**قواعد بيانات بدون وجع رأس!**  
*A friendly database manager for Linux.*

**v0.5 · Linux · العربية / English · SQLite · MySQL · SSH**

</div>

---

## 🆕 تحديث النسخ من الجداول — 19 نوفمبر 2026

تمت تجربة ميزة تحديد ونسخ الخلايا والصفوف والأعمدة من **جدول البيانات** و**نتائج SQL**، بما فيها **Copy with Headers** والقائمة بزر الفأرة الأيمن.

> **حالة النشر:** التعديل متاح الآن كتصحيح لملفات Python الخاصة بإصدار **v0.5**. لم تُبنَ أو تُنشر بعد حزمة Snap جديدة تحتويه، ولا تتحدث نسخة v0.5 المثبتة تلقائيًا.

**لتجربة التصحيح على نسخة مصدر v0.5 منفصلة:**

1. نزّل `AzizDB_v0_5.zip` من [إصدار v0.5](https://github.com/mraziz2005-hue/AzizDB/releases/tag/v0.5) وفكّه داخل `~/Downloads`.
2. نزّل [أداة تحديث النسخ](https://raw.githubusercontent.com/mraziz2005-hue/AzizDB/main/tools/azizdb_copy_patch.py) باسم `~/Downloads/azizdb_copy_patch.py`.
3. نفّذ:

```bash
python3 ~/Downloads/azizdb_copy_patch.py
cd ~/Downloads/AzizDB_v0_5
bash run.sh
```

يدعم التصحيح اختيار الخلايا، نطاقات متعددة، الصفوف والأعمدة؛ `Ctrl+C` للنسخ، و`Ctrl+Shift+C` للنسخ مع رؤوس الأعمدة، و`Ctrl+A` لتحديد الكل. يستخدم جدولًا مفصولًا بعلامات تبويب للصق في Excel وغيره. الأداة تنشئ نسخة احتياطية من `main.py` وملف ZIP معدلًا، ولا تمس قاعدة البيانات أو حزمة Snap المثبتة.

الملف الإضافي [table_copy.py](https://github.com/mraziz2005-hue/AzizDB/blob/main/table_copy.py) منشور أيضًا للمراجعة. **مستودع GitHub ما زال لا يحتوي على كامل ملفات التطبيق**؛ المصدر الأساسي متاح في أرشيف الإصدار.

---

## 🌟 وش هو AzizDB؟

**AzizDB** برنامج سطح مكتب لإدارة قواعد البيانات على Linux بواجهة بسيطة ومرحة وشخصية بطريق. صممته عشان أقدر أفتح قاعدة البيانات، أتصفح جداولها، أكتب SQL أو أعدّل الصفوف من الجدول نفسه، بدون كثرة النوافذ والتعقيد.

> **مهم:** AzizDB **مدير قواعد بيانات**؛ ليس بديلًا لمحرك MySQL أو SQL Server. يشغّل ملفات SQLite مباشرة، ويتصل بخادم MySQL الموجود مسبقًا. دعم Microsoft SQL Server وPostgreSQL **غير متوفر في الإصدار v0.5**.

## ✨ أهم المميزات

| الميزة | ماذا تفعل؟ |
|---|---|
| 🐧 واجهة مريحة | ثيم داكن، شخصية بطريق، تصميم منظم، عربية وإنجليزية |
| 🎨 تخصيص الشكل | حجم خط الواجهة ومحرر SQL، ألوان الواجهة، كثافة المسافات |
| 📁 SQLite محلي | إنشاء ملف قاعدة بيانات وفتحه دون تثبيت خادم |
| 🌐 MySQL | الاتصال بخادم MySQL محلي أو بعيد |
| 🔐 SSH Tunnel | الاتصال بـ MySQL عبر نفق SSH، عند توفر بيانات وصلاحيات الاتصال |
| 🗂️ مستكشف الجداول | عرض الجداول والبيانات في شبكة قابلة لتغيير عرض الأعمدة |
| ↔️ تنقل سريع | أول صفحة، السابق، التالي، **آخر صفحة**، إدخال رقم الصفحة |
| 🔢 حجم الصفحة | 50 أو 100 أو 200 أو 500 صف في الصفحة؛ ليس حدًا إجماليًا للسجلات |
| ✏️ تحرير مرئي | إضافة الصفوف وتعديلها وحذفها وإنشاء الجداول بواجهة رسومية |
| 💻 SQL Playground | كتابة الاستعلامات وتنفيذها، والاختصار `Ctrl + Enter` |
| 💾 اتصالات محفوظة | حفظ أسماء وعناوين ومنافذ الاتصالات وإعدادات المظهر؛ **من دون حفظ كلمات المرور** |

**ملاحظة:** معاينة نتائج الاستعلام المباشر في SQL Playground محدودة في الإصدار الحالي، لكن تصفّح الجداول يستخدم صفحات للوصول إلى جميع السجلات.

## 🆕 أحدث إصدار — v0.5.1 (نسخة المصدر)

**تم نشر [AzizDB v0.5.1](https://github.com/mraziz2005-hue/AzizDB/releases/tag/v0.5.1)** مع ميزة تحديد ونسخ الخلايا والصفوف والأعمدة من الجداول ونتائج SQL، ونسخ مع أسماء الأعمدة (Copy with Headers).

- **[تحميل AzizDB_v0.5.1-source.zip](https://github.com/mraziz2005-hue/AzizDB/releases/download/v0.5.1/AzizDB_v0.5.1-source.zip)** — نسخة Python المصدرية الجديدة، وهي الإصدار الأحدث.
- **نسخة Snap المتوفرة حاليًا لا تزال v0.5**، ولم تصدر حزمة Snap v0.5.1 بعد. تعليمات تثبيت Snap أدناه تخص v0.5 فقط.

### تشغيل نسخة v0.5.1 من المصدر

بعد تنزيل الملف وفك الضغط، افتح الطرفية من المجلد الناتج ونفّذ `bash run.sh`. يعتمد التشغيل على متطلبات Python الموضحة في قسم التشغيل من المصدر أدناه. لا تستبدل نسخة Snap المثبتة بهذه النسخة تلقائيًا.

---

## 🚀 التثبيت على Linux

**نفس حزمة AzizDB يمكن استخدامها على توزيعات Linux متعددة تدعم Snap وحزم Classic، بعد تجهيز Snap على التوزيعة.** أوامر تجهيز النظام تختلف؛ أمر تثبيت حزمة البرنامج واحد. هذا لا يعني اختبار كل توزيعة أو ضمان كل إصدار منها.

### التوافق والمتطلبات

| النظام أو المعمارية | الحالة |
|---|---|
| Ubuntu | سبق توثيق تجربة محلية في المشروع؛ لم يُسجّل رقم إصدار النظام في هذا الدليل |
| Fedora المكتبي التقليدي | تأكد تشغيل حزمة v0.5 وظهورها في قائمة التطبيقات بعد إضافة الاختصار يدويًا، بتاريخ 17 نوفمبر 2026؛ رقم إصدار Fedora غير موثق |
| Debian وLinux Mint | خطوات تجهيز Snap موضحة أدناه؛ لا تُعد دليلًا على اختبار AzizDB على كل إصدار |
| Arch وManjaro وopenSUSE وغيرها | راجع دليل Snap الخاص بالتوزيعة؛ تشغيل AzizDB عليها غير مؤكد باختبار مسجل هنا |
| الأنظمة غير القابلة للتغيير مثل Fedora Silverblue / Kinoite | لا تطبق خطوات Fedora التقليدي عليها باعتبارها مضمونة؛ إعداد النظام ودعم Classic قد يختلفان |
| أجهزة Intel / AMD بمعمارية x86_64 | الحزمة الحالية اسمها amd64، وتشمل معالجات Intel وAMD ذات 64 بت |
| ARM / aarch64 وأجهزة 32 بت | حزمة amd64 الحالية ليست مناسبة لها |

نجاح فتح البرنامج لا يعني اختبار جميع وظائف MySQL وSSH والتحرير على كل نظام.

تحتاج إلى جلسة سطح مكتب Linux، واتصال إنترنت لتنزيل الحزمة واعتماديات Snap عند الحاجة، وصلاحية `sudo` للتثبيت. **لا تحتاج إلى تثبيت Python أو pip يدويًا عند اختيار حزمة Snap.**

اعرف توزيعتك ومعمارية جهازك:

```bash
cat /etc/os-release
uname -m
```

إذا أظهر الأمر الثاني `x86_64` فمعمارية الجهاز تطابق الحزمة.

### 1. حمّل ملف البرنامج الصحيح

افتح [إصدار AzizDB v0.5](https://github.com/mraziz2005-hue/AzizDB/releases/tag/v0.5)، ثم افتح **Assets** واختر:

| الملف | استخدامه |
|---|---|
| [azizdb_0.5_amd64.snap](https://github.com/mraziz2005-hue/AzizDB/releases/download/v0.5/azizdb_0.5_amd64.snap) | تثبيت التطبيق باستخدام Snap؛ الخيار المباشر لأجهزة x86_64 |
| [AzizDB_v0_5.zip](https://github.com/mraziz2005-hue/AzizDB/releases/download/v0.5/AzizDB_v0_5.zip) | تشغيل ملفات Python؛ خطواته في القسم التالي |

**لا تستخدم `Code → Download ZIP` أو ملف `Source code (zip)` التلقائي بدل أرشيف البرنامج أعلاه.** وقت تحديث هذا الدليل، ملفات التطبيق موزعة في أصل الإصدار `AzizDB_v0_5.zip`، والمستودع نفسه يحتوي README فقط.

ضع ملف Snap في مجلد التنزيلات. الأمثلة تفترض `~/Downloads`؛ إذا كان مجلدك باسم آخر، افتحه في مدير الملفات واختر **فتح الطرفية هنا** بدل أمر `cd ~/Downloads`.

### 2. جهّز Snap حسب توزيعتك — مرة واحدة

افحص أولًا:

```bash
snap version
```

إذا ظهر إصدار Snap وsnapd، انتقل إلى خطوة تثبيت AzizDB. إذا ظهر `command not found`، اتبع قسم توزيعتك فقط. إذا ظهر `snapd unavailable`، راجع قسم المشاكل الشائعة.

#### Ubuntu

إذا لم يكن Snap مثبتًا:

```bash
sudo apt update
sudo apt install snapd
sudo systemctl enable --now snapd.socket
```

سجّل خروجًا من جلسة سطح المكتب وادخل مجددًا، أو أعد تشغيل الجهاز. ثم أكمل تثبيت AzizDB.

#### Fedora Workstation / KDE التقليدي

**Fedora يستخدم `dnf`؛ لا تستخدم عليه أوامر `apt`.**

ثبّت Snap وفعّل الخدمة:

```bash
sudo dnf install snapd
sudo systemctl enable --now snapd.socket
```

جهّز مسار Classic إذا لم يكن موجودًا:

```bash
if [ ! -e /snap ] && [ ! -L /snap ]; then
    sudo ln -s /var/lib/snapd/snap /snap
fi
```

سجّل خروجًا وادخل مجددًا، أو أعد تشغيل الجهاز. **إغلاق الطرفية وفتحها ليس بديلًا عن تحديث جلسة سطح المكتب.**

ثم تحقق:

```bash
snap version
```

هذه الخطوات مخصصة لفيدورا التقليدي، وليست تعليمات تثبيت مؤكدة لـ Silverblue أو Kinoite.

#### Debian

```bash
sudo apt update
sudo apt install snapd
sudo systemctl enable --now snapd.socket
```

سجّل خروجًا وادخل مجددًا، ثم ثبّت نسخة snapd التي يوصي بها دليل Snap الرسمي لـ Debian:

```bash
sudo snap install snapd
```

ثم أكمل تثبيت AzizDB. إذا ظهرت مشكلة مسار Classic، راجع حلها أدناه.

#### Linux Mint

قد يمنع Linux Mint تثبيت Snap بواسطة الملف `nosnap.pref`. إذا اخترت استخدام Snap، انقل ملف المنع إلى نسخة احتياطية إن كان موجودًا؛ هذا يغيّر تفضيل Mint الذي يمنع تثبيت Snap:

```bash
if [ -f /etc/apt/preferences.d/nosnap.pref ]; then
    sudo mv -n /etc/apt/preferences.d/nosnap.pref /etc/apt/preferences.d/nosnap.pref.azizdb-backup
fi
sudo apt update
sudo apt install snapd
sudo systemctl enable --now snapd.socket
```

إذا بقي `nosnap.pref` موجودًا بسبب وجود نسخة احتياطية بنفس الاسم، لا تحذف الملفات عشوائيًا؛ اختر اسم نسخة احتياطية مختلفًا قبل إعادة المحاولة.

سجّل خروجًا وادخل مجددًا، أو أعد تشغيل الجهاز، ثم أكمل تثبيت AzizDB. ويمكنك اختيار تشغيل ملفات Python إذا لم ترغب في تفعيل Snap.

#### بقية التوزيعات

اتبع دليل Snap الرسمي الخاص بتوزيعتك لتثبيت `snapd` وتفعيل الخدمة ودعم **Classic**، ثم ارجع إلى خطوة تثبيت AzizDB:

- [Arch Linux](https://snapcraft.io/docs/tutorials/install-the-daemon/arch-linux/)
- [Manjaro](https://snapcraft.io/docs/tutorials/install-the-daemon/manjaro/)
- [openSUSE](https://snapcraft.io/docs/tutorials/install-the-daemon/opensuse/)
- [دليل تثبيت Snap واختيار التوزيعة](https://snapcraft.io/docs/installing-snapd/)

لا تستخدم أوامر Ubuntu أو Fedora على توزيعة أخرى دون الرجوع لدليلها.

### 3. ثبّت AzizDB

بعد تجهيز Snap، نفّذ من مجلد التنزيل:

```bash
cd ~/Downloads
ls -lh azizdb_0.5_amd64.snap
sudo snap install --dangerous --classic ./azizdb_0.5_amd64.snap
```

إذا لم يجد `ls` الملف، صحّح المجلد أو اسم الملف قبل متابعة التثبيت.

- `--dangerous`: يسمح بتثبيت ملف Snap محلي دون التحقق من توقيعه عبر المتجر؛ استخدم ملف إصدار المشروع الموثوق.
- `--classic`: يسمح بنمط Classic ذي الوصول الأوسع للنظام.
- هذه تعليمات **تثبيت محلي من GitHub**؛ لا تفترض أن أمر `sudo snap install azizdb` من المتجر متاح.

تحقق من نجاح التثبيت:

```bash
snap list azizdb
```

### 4. شغّل البرنامج

```bash
snap run azizdb
```

أو ابحث عن **AzizDB** في قائمة التطبيقات. **شغّل البرنامج بحسابك العادي، دون `sudo`.**

بعد نجاح تثبيت Snap، يمكنك حذف ملف التنزيل `.snap` دون إزالة التطبيق المثبت؛ لا ينطبق هذا على مجلد نسخة Python.

### 5. إذا اشتغل البرنامج ولم يظهر في قائمة التطبيقات

1. سجّل خروجًا وادخل من جديد، ثم ابحث عن **AzizDB**.
2. إذا لم يظهر، تحقق من وجود اختصار Snap:

```bash
ls -l /var/lib/snapd/desktop/applications/azizdb_azizdb.desktop
```

3. إذا ظهر الملف، أضف رابطًا له في تطبيقات حسابك:

```bash
mkdir -p ~/.local/share/applications
ln -sfnT /var/lib/snapd/desktop/applications/azizdb_azizdb.desktop ~/.local/share/applications/azizdb_azizdb.desktop
```

هذا يربط قائمة حسابك بالاختصار الذي أنشأته الحزمة، دون كتابة مسار إصدار Snap مؤقت. الأمر يستبدل أي اختصار محلي بنفس الاسم؛ إذا سبق تخصيصه يدويًا، احتفظ بنسخة منه أولًا.

4. أغلق قائمة التطبيقات وافتحها وابحث عن **AzizDB**. إذا لم تتحدث، سجّل خروجًا وادخل مجددًا.

**هذه طريقة الاختصار التي نجحت في تجربة Fedora بتاريخ 17 نوفمبر 2026.** ليست خطوة إلزامية إذا ظهر التطبيق تلقائيًا.

إذا كان ملف `.desktop` غير موجود أصلًا، لا تنشئ رابطًا لملف مفقود؛ أرفق ناتج `snap list azizdb` في بلاغ المشكلة.

## 🐍 الطريقة البديلة: التشغيل من ملفات Python

مناسبة لمن يريد تشغيل ملفات المشروع بدل تثبيت Snap. تحتاج Python 3 و`pip` وبيئة `venv`، واتصال إنترنت عند تنزيل المكتبات. قد تحتاج مكتبات Qt إضافية حسب التوزيعة؛ هذه الطريقة ليست ضمانًا للعمل على كل إصدار Linux.

### 1. تثبيت المتطلبات

**Ubuntu / Debian / Linux Mint:**

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip unzip
```

**Fedora التقليدي:**

```bash
sudo dnf install python3 python3-pip unzip
```

**بقية التوزيعات:** ثبّت Python 3 وpip وunzip باستخدام مدير حزم توزيعتك، وتأكد من توفر:

```bash
python3 --version
python3 -m venv --help
```

### 2. تنزيل البرنامج وتشغيله

حمّل [AzizDB_v0_5.zip](https://github.com/mraziz2005-hue/AzizDB/releases/download/v0.5/AzizDB_v0_5.zip) إلى مجلد التنزيلات، ثم:

```bash
cd ~/Downloads
unzip -n AzizDB_v0_5.zip
cd AzizDB_v0_5
bash run.sh
```

إذا كان اسم المجلد المستخرج مختلفًا، افتح المجلد الذي يحتوي `run.sh` و`requirements.txt` ونفّذ `bash run.sh` منه.

بحسب تعليمات الإصدار، يبحث `run.sh` عن بيئة Python صالحة للبرنامج؛ وإن لم يجدها يُنشئ `.venv` ويثبت المكتبات من `requirements.txt` ثم يشغّل التطبيق. عند التشغيل لاحقًا:

```bash
cd ~/Downloads/AzizDB_v0_5
bash run.sh
```

احتفظ بمجلد البرنامج، ولا تشغّل `run.sh` باستخدام `sudo`. هذه الطريقة لا تعني إنشاء اختصار تلقائي في قائمة التطبيقات، وحل رابط Snap أعلاه خاص بنسخة Snap فقط.


## 🧭 الاستخدام من البداية

### 🏠 إنشاء قاعدة SQLite محلية

1. افتح AzizDB واضغط **إنشاء قاعدة بيانات / Create database**.
2. اختر مكان الملف واسمه، مثل `my_database.db`.
3. اضغط **New table / إنشاء جدول** لإضافة جدول بالأعمدة التي تريدها، أو استخدم محرر SQL.
4. افتح الجدول، وأضف الصفوف أو عدّل الخلايا، ثم اضغط **Save edits / حفظ التعديلات**.

لتجربة سريعة، استخدم زر **🐧 جرّب قاعدة جاهزة**. ينشئ نموذج SQLite بجدولَي `users` و`products` على جهازك.

### 🌐 الاتصال بـ MySQL محلي أو عن بُعد

1. اضغط **اتصال جديد** ثم **MySQL**.
2. أدخل اسم المضيف، المنفذ، اسم المستخدم، كلمة المرور، واسم قاعدة البيانات.
3. للاتصال الآمن بخادم بعيد، فعّل **SSH Tunnel** واملأ بيانات SSH عند الحاجة. يجب أن يكون الخادم موثوقًا من قبل في `~/.ssh/known_hosts`.
4. اختر **حفظ إعدادات الاتصال** إن رغبت؛ **لن تُحفظ كلمة مرور MySQL أو SSH**.
5. افتح الجدول الذي تريده؛ يبدأ اتصال MySQL **بالقراءة فقط** في كل جلسة.
6. إذا أردت التعديل، اضغط **Enable editing / تفعيل التعديل** واقرأ التأكيد. تحتاج قاعدة البيانات وحساب المستخدم إلى صلاحيات كتابة مناسبة. تعديل الصفوف عبر الشبكة يحتاج مفتاحًا أساسيًا (`PRIMARY KEY`) في الجدول.

> **للسيرفر الحقيقي:** جرّب التعديل أولًا على قاعدة تجريبية، وخذ نسخة احتياطية قبل التغييرات الكبيرة. لا تفتح منفذ MySQL للعالم فقط لتوصيل البرنامج؛ استخدم SSH Tunnel عند الحاجة.

### 📊 كيف أصل إلى آخر البيانات؟

افتح أي جدول؛ ستجد تحت شبكة البيانات أزرار التنقل **الأولى / السابقة / التالية / الأخيرة ⏭** ورقم الصفحة وحجم الصفحة. استخدام آخر صفحة ينقلك إلى آخر جزء من الجدول بدل أن تتوقف عند 200 صف إجمالًا.

### 💻 كتابة SQL

افتح تبويب **SQL Playground / ملعب SQL** واكتب استعلامك، ثم اضغط تنفيذ أو `Ctrl + Enter`. أوامر الكتابة تتطلب الصلاحيات المناسبة، ويطلب البرنامج تأكيدًا لبعض العمليات التي تغيّر البيانات.

## 💾 وين تُحفظ الإعدادات والبيانات؟

عند التشغيل المعتاد من ملفات Python، يحفظ AzizDB إعداداته هنا:

```text
~/.config/AzizDB/settings.json
```

ويُنشئ قاعدة التجربة الافتراضية هنا:

```text
~/.local/share/AzizDB/Demo.db
```

الإعدادات تحفظ التفضيلات وبيانات تعريف الاتصال، **ولا تحفظ كلمات المرور**. قد يختلف مسار البيانات الفعلي عند التثبيت بحزمة Snap بحسب بيئة التشغيل؛ تأكد منه قبل نقل الإعدادات بين الأجهزة.

**كل جهاز يحتفظ بإعداداته وملفاته المحلية بنفسه**؛ لا توجد مزامنة تلقائية بين اللابتوب وجهاز الدوام.

## 🔄 التحديثات

- **من ملفات المشروع:** حمّل الإصدار الأحدث من [Releases](../../releases) وشغّله في مجلد مستقل، ثم اختبره. احتفظ بنسخة من قاعدة SQLite وملف الإعدادات إن احتجت الرجوع.
- **من Snap محلي:** حمّل حزمة الإصدار الجديد وثبّتها يدويًا بالطريقة الموضحة أعلاه.
- **من Snap Store مستقبلًا:** إذا تمت الموافقة على النشر، يمكن تحديث النسخ المثبتة من القناة المناسبة عبر Snap.

> **GitHub Releases لا يحدّث نسخة Python أو Snap المحلية تلقائيًا** في الإصدار الحالي.

## 🧰 متطلبات التشغيل والمكتبات

- Linux بواجهة سطح مكتب؛ راجع جدول التوافق أعلاه.
- نسخة Snap تتضمن بيئة تشغيل التطبيق؛ لا تحتاج تجهيز Python يدويًا.
- نسخة ملفات Python فقط تحتاج Python 3 مع `venv` و`pip`، والمكتبات من `requirements.txt`: **PySide6، PyMySQL، paramiko**.
- اتصال MySQL يحتاج خادمًا يعمل وبيانات دخول صحيحة؛ SQLite لا يحتاج خادمًا.

## 🗃️ ملفات المشروع

البنية التالية تخص أرشيف البرنامج المرفق في Releases، وليست محتويات المستودع الحالي:

```text
AzizDB/
├── main.py                # الواجهة الرئيسية
├── database.py            # التعامل مع SQLite وMySQL
├── ssh_tunnel.py          # نفق SSH
├── editor_tools.py        # إنشاء الجداول وتحرير الصفوف
├── appearance.py          # إعدادات وألوان الواجهة
├── column_sizing.py       # تنسيق عرض الأعمدة
├── assets/
│   └── AzizDB_Penguin.png # شعار البطريق
├── requirements.txt       # مكتبات Python
├── run.sh                 # تشغيل البرنامج
└── tests/                 # اختبارات برمجية
```

## ❓ مشاكل شائعة

**`No module named venv`**: ثبّت `python3-venv` ثم أعد `bash run.sh`.

**خطأ في تثبيت المكتبات**: تأكد من الإنترنت، ونسخة Python المناسبة للمكتبات، وراجع الرسالة الظاهرة في Terminal.

**اتصال MySQL لا يعمل**: تأكد من عنوان الخادم والمنفذ وصلاحيات المستخدم، وإعدادات SSH إن استخدمتها. لا تشارك كلمات المرور أو المفاتيح الخاصة عند طلب المساعدة.

**زر تحرير MySQL غير متاح**: فعّل التعديل لتلك الجلسة؛ وقد يكون الجدول عرضًا (`VIEW`) أو لا يحتوي مفتاحًا أساسيًا، أو حساب قاعدة البيانات لا يملك صلاحية الكتابة.

**البرنامج لا يظهر في قائمة التطبيقات**: لنسخة Snap، اتبع خطوات فحص وربط الاختصار في قسم التثبيت أعلاه. نسخة Python لا تنشئ بالضرورة اختصارًا تلقائيًا.

**`snap: command not found`**: ثبّت `snapd` باتباع قسم توزيعتك؛ تنزيل ملف AzizDB وحده لا يثبت Snap.

**`apt: command not found` على Fedora**: استخدم `dnf` كما هو موضح أعلاه.

**`cannot communicate with server` أو `snapd unavailable`**: على الأنظمة التقليدية المستخدمة في هذا الدليل، نفّذ:

```bash
sudo systemctl enable --now snapd.socket
systemctl status snapd.socket --no-pager
snap version
```

إذا استمر الخطأ، أرفق نصه بدل تكرار التثبيت.

**خطأ يطلب تثبيت Classic تحت `/snap`**: افحص المسار:

```bash
ls -ld /snap /var/lib/snapd/snap
```

على Fedora التقليدي، إذا كان `/snap` غائبًا وكان المسار الثاني موجودًا، استخدم أمر إنشاء الرابط في قسم Fedora. إذا كان `/snap` موجودًا، لا تحذفه ولا تستبدله عشوائيًا؛ أرفق نتيجة الفحص. على توزيعة أخرى اتبع تعليمات Classic الخاصة بها.

**`No such file or directory` عند التثبيت**: افتح الطرفية في المجلد الذي يحتوي ملف `.snap` وتأكد من اسمه عبر `ls`.

**خطأ معمارية أو `Exec format error`**: افحص `uname -m`؛ ملف amd64 مخصص لـ x86_64 وليس ARM أو 32 بت.

**البرنامج لا يفتح أو يغلق فورًا**: شغّله من الطرفية باستخدام `snap run azizdb` أو `bash run.sh` حسب نسختك، ثم انسخ رسالة الخطأ.

عند فتح [بلاغ مشكلة](https://github.com/mraziz2005-hue/AzizDB/issues)، اذكر اسم التوزيعة وإصدارها، ومعمارية الجهاز، وطريقة التثبيت، ونص الخطأ. لنسخة Snap أرفق أيضًا `snap version` و`snap list azizdb`. احذف بيانات الاتصال الحساسة من المخرجات.

## 🗑️ إزالة نسخة Snap

أغلق AzizDB واحتفظ بنسخة من قواعدك وإعداداتك المهمة قبل الإزالة:

```bash
sudo snap remove azizdb
```

إذا أضفت رابط الاختصار يدويًا بالطريقة أعلاه، أزل الرابط المحلي فقط:

```bash
if [ -L "$HOME/.local/share/applications/azizdb_azizdb.desktop" ]; then
    rm -- "$HOME/.local/share/applications/azizdb_azizdb.desktop"
fi
```

هذه ليست أوامر حذف ملفات قواعد البيانات التي حفظتها بنفسك خارج بيانات الحزمة.

## 📚 مراجع تجهيز Snap

رُوجعت التعليمات بتاريخ **17 نوفمبر 2026**. راجع الدليل الرسمي عند اختلاف إصدار توزيعتك:

- [Ubuntu](https://snapcraft.io/docs/tutorials/install-the-daemon/ubuntu/)
- [Fedora](https://snapcraft.io/docs/tutorials/install-the-daemon/fedora/)
- [Debian](https://snapcraft.io/docs/tutorials/install-the-daemon/debian/)
- [Linux Mint](https://snapcraft.io/docs/tutorials/install-the-daemon/linux-mint/)

هذه مراجع لتجهيز Snap، وليست إثباتًا لاختبار AzizDB على كل نظام.

## 📌 حالة المشروع

هذا إصدار **v0.5 تجريبي** يُطوَّر تدريجيًا. يُدعم حاليًا **SQLite وMySQL**، ولم تُنفّذ بعد موصلات SQL Server أو PostgreSQL. الاختبارات الفعلية تختلف بين الأنظمة والاتصالات؛ لا تعتمد على إصدار تجريبي وحده لإجراء تغييرات حساسة دون نسخة احتياطية.

للملاحظات والأخطاء، استخدم تبويب [Issues](../../issues) في المستودع.

---

## 🌍 English quick start

**AzizDB** is a friendly, penguin-themed desktop database manager for Linux with Arabic and English UI. It supports local SQLite databases, MySQL connections (direct or over SSH), visual row editing and table creation, SQL queries, saved connection profiles without passwords, custom themes/fonts, and paginated table browsing with a last-page button.

**Install the local Snap (x86_64 / amd64):**

Set up snapd and classic support for your distribution first; see the detailed distribution-specific instructions above. Fedora uses `dnf`, Ubuntu/Debian use `apt`, and Linux Mint may block snapd until its preference file is moved. Log out and back in after setup.

Download `azizdb_0.5_amd64.snap` from the v0.5 release, then:

```bash
cd ~/Downloads
sudo snap install --dangerous --classic ./azizdb_0.5_amd64.snap
snap run azizdb
```

If the app runs but is missing from the menu, follow the desktop-file check and link procedure above. Fedora launch and menu integration were confirmed by the maintainer on November 17, 2026; this is not a full feature test on every distribution. ARM and 32-bit devices cannot use this amd64 build.

**Run from source on Ubuntu:**

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip unzip
# Download the AzizDB_v0_5.zip source archive from Releases into ~/Downloads
cd ~/Downloads
unzip -n AzizDB_v0_5.zip
cd AzizDB_v0_5
bash run.sh
```

MySQL sessions start read-only. Writing requires explicitly enabling editing and sufficient database permissions. GitHub releases do **not** automatically update locally installed copies. SQL Server and PostgreSQL are **not supported in v0.5**.

---

<div align="center">

**🐧 AzizDB — Databases don't have to be boring.**

</div>

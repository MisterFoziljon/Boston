## Boston shaharchasidagi uy narxlarini Keras frameworkidan foydalanib, Sun'iy neyron to'ri yordamida bashorat qilish

Datasetdagi har bir ustun Boston hududi yoki shaharchasini tasvirlaydi.
Ma'lumotlar 1970-yilda Boston Standart Metropoliten Statistik Hududidan (SMSA) olingan.

* **CRIM** - shaharlar bo'yicha aholi jon boshiga to'g'ri keladigan jinoyatlar darajasi
* **ZN**: 25 000 kv.ft dan ortiq uchastkalar uchun ajratilgan turar-joy yerlarining ulushi.
* **INDUS**: har bir shahar uchun chakana bo'lmagan biznes akrlarining ulushi
* **CHAS**: Charlz daryosining qo'g'irchoq o'zgaruvchisi (agar trakt daryo bilan chegaradosh bo'lsa = 1; aks holda 0)
* **NOX**: azot oksidi kontsentratsiyasi (10 millionga qism)
* **RM**: bitta turar-joy uchun o'rtacha xonalar soni
* **YOSH**: 1940 yilgacha qurilgan egalari egallagan birliklarning nisbati
* **DIS**: Bostondagi beshta bandlik markazlarigacha bo'lgan masofalar
* **RAD**: radial magistrallarga kirish imkoniyati indeksi
* **SOLIQ**: 10 000 dollar uchun to'liq qiymatli mulk solig'i stavkasi
* **PTRATIO**: shahar bo'yicha o'quvchi-o'qituvchi nisbati
* **B**: (1000(Bk−0,63)2) bu yerda Bk qora tanlilarning nisbati
* **LSTAT**: aholining % pastroq holati
* **MEDV**: Egasi egallagan uylarning o'rtacha qiymati 1000 dollar
(yuqoridagi ma'lumotlar google translate yordamida tarjima qilingan)


### Bajariladigan ishlar ketma-ketligi:

#### 1. Loyihani yuklab olish uchun quyidagi ketma-ketlikni bajaring:
* `windows+R` klavishlarini bosing va paydo bo'lgan oynaga `cmd` buyrug'ini yozing OK tugmachasini bosing.

* Loyihani quyidagi link yordamida yuklab oling. (Loyiha uchun yaratilgan fayl adresni o'zingiz ko'rsatishingiz mumkin)

        C:\> git clone https://github.com/MisterFoziljon/Boston-House-Price-Prediction-with-Keras.git

* Loyiha joylashgan faylga kiring.
         
        C:\> cd Boston-House-Price-Prediction-with-Keras

#### 2. Proyektni ishlatish uchun kerakli modullarni virtual environment yaratib o'rnatib oling.
* O'zingizdagi pip ni so'nggi versiyasiga yangilang.

        C:\Boston-House-Price-Prediction-with-Keras> python -m pip install --upgrade pip
        
* virtual environment yaratish uchun virtualenv modulini o'rnating.
        
        C:\Boston-House-Price-Prediction-with-Keras> python -m pip install --user virtualenv

* Yangi environment yaratish uchun unga nom bering.
        
        C:\Boston-House-Price-Prediction-with-Keras> python -m venv sizning_env
        
* Virtual environmentni ishga tushiring(aktivlashtiring).
        
        C:\Boston-House-Price-Prediction-with-Keras> sizning_env\Scripts\activate.bat
        
* Virtual environment ichiga loyiha ishlashi uchun kerakli bo'lgan modullarni o'rnating (requirements.txt faylining ichida barchasi mavjud).
        
        (sizning_env) C:\Boston-House-Price-Prediction-with-Keras> pip install -r requirements.txt
  
#### 3. Yuqoridagi Proyektni ishlatish uchun sizga `Dataset` va `model` nomli yangi fayllar (folder) kerak bo'ladi. Proyekt joylashgan fayl ichida yuqoridagi 2 ta faylni shunchaki yaratib qo'ying.

#### 4. Proyektni ishlatish uchun jupyter notebook ni ishga tushiring.

        (sizning_env) C:\Boston-House-Price-Prediction-with-Keras> jupyter notebook
        
  * ```Dataset.ipynb``` ni ishga tushiring. Ushbu notebook yordamida keras saytidagi "Boston Housing price regression dataset" ni yuklab olishingiz va uni keyinchalik foydalanish uchun csv fayl ko'rinishida saqlab qo'yishingiz mumkin.
  
  * ```Modelni train, evaluate qilish va saqlash.ipynb``` ni ishga tushiring. Usbu notebookda (a) punktda hosil qilib olingan csv datasetni o'qib olish, uni train va test datalariga ajratish va ularni standard scaler yordamida normallashtirish ko'rsatilgan. Bundan tashqari, natijaviy train data yordamida model train va evaluate qilingan, natijada model (3) punktda siz yaratgan model fayli ichiga h5 formatda saqlanadi.
  
  * ```Modelni yuklash va testdan o'tkazish.ipynb``` ni ishga tushiring. Ushbu notebook yordamida saqlangan modelni load qilish va yangi test qilish datalari yordamida bashorat qilish (predict) ko'rsatib o'tilgan.


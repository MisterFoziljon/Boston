## Boston shaharchasidagi uy narxlarini Keras frameworkidan foydalanib, Sun'iy neyron to'ri yordamida bashorat qilish

Datasetdagi har bir ustun Boston hududi yoki shaharchasini tasvirlaydi.
Ma'lumotlar 1970-yilda Boston Standart Metropoliten Statistik Hududidan (SMSA) olingan.

* **CRIM** - shaharlar bo'yicha aholi jon boshiga to'g'ri keladigan jinoyat darajasi
* **ZN**: 25 000 kv.ft dan ortiq uchastkalar uchun ajratilgan turar-joy yerlarining ulushi.
* **INDUS**: har bir shahar uchun chakana bo'lmagan biznes maydonlarining ulushi
* **CHAS**: Charlz daryosidan uzoq yaqinligi (agar Daryoga yaqin hududda bo'lsa = 1; aks holda 0)
* **NOX**: azot oksidi kontsentratsiyasi
* **RM**: turar-joy uchun o'rtacha xonalar soni
* **YOSH**: 1940-yilgacha qurib foydalanishga topshirilgan obyektlarning nisbati
* **DIS**: Bostondagi 5 ta bandlik markazlarigacha bo'lgan vaznli masofalar
* **RAD**: radial magistrallarga kirish imkoniyati indeksi
* **SOLIQ**: har 10000$ uchun to'liq qiymatli mulk solig'i stavkasi
* **PTRATIO**: shahar bo'yicha o'quvchi-o'qituvchi nisbati
* **B**: qora tanlilarning shahardagi ulushi
* **LSTAT**: aholining % pastroq holati
* **MEDV**: Sotib olingan uylarning o'rtacha qiymati 10 000$
(yuqoridagi ma'lumotlar google translate yordamida tarjima qilingan)


### Bajariladigan ishlar ketma-ketligi:

#### 1. Loyihani yuklab olish uchun quyidagi ketma-ketlikni bajaring:
* `windows+R` klavishlarini bosing va paydo bo'lgan oynaga `cmd` buyrug'ini yozing OK tugmachasini bosing.

![cmd](https://github.com/MisterFoziljon/Keras-yordamida-Boston-shaharchasidagi-uy-joy-narxlarini-bashorat-qilish-modelini-ishlab-chiqish/blob/main/rasmlar/cmd.png)

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

#### 3. Proyektni ishlatish uchun jupyter notebook ni ishga tushiring.

        (sizning_env) C:\Boston-House-Price-Prediction-with-Keras> jupyter notebook
        
  * ```Dataset.ipynb``` ni ishga tushiring. Ushbu notebook yordamida keras saytidagi "Boston Housing price regression dataset" ni yuklab olishingiz va uni keyinchalik foydalanish uchun csv fayl ko'rinishida saqlab qo'yishingiz mumkin. (Ushbu notebook birinchi bo'lib ishga tushiriliadi. ```Ishga tushirish majburiy!!!```)
  
  * ```Modelni train, evaluate qilish va saqlash.ipynb``` ni ishga tushiring. Usbu notebookda hosil qilib olingan csv datasetni o'qib olish, uni train va test datalariga ajratish va ularni standard scaler yordamida normallashtirish ko'rsatilgan. Bundan tashqari, natijaviy train data yordamida model train va evaluate qilingan, natijada model h5 formatda saqlanadi.
  
  * ```Modelni yuklash va testdan o'tkazish.ipynb``` ni ishga tushiring. Ushbu notebook yordamida saqlangan modelni load qilish va yangi test qilish datalari yordamida bashorat qilish (predict) ko'rsatib o'tilgan.

#### 4. Proyektni streamlit yordamida deploy qilish.

        (sizning_env) C:\Boston-House-Price-Prediction-with-Keras> streamlit run streamlit.py

  * Proyekt ```local server```da ishga tushadi va quyidagicha ko'rinishda bo'ladi:

  ![streamlit1](https://github.com/MisterFoziljon/Keras-yordamida-Boston-shaharchasidagi-uy-joy-narxlarini-bashorat-qilish-modelini-ishlab-chiqish/blob/main/rasmlar/streamlit1.png)
  
  * Qiymatlarni kiritib ```Predict qilish``` tugmachasi bosilganda yuqoridagi qiymatlardan foydalanib model uyning narxini bashorat qiladi.
  ![streamlit2](https://github.com/MisterFoziljon/Keras-yordamida-Boston-shaharchasidagi-uy-joy-narxlarini-bashorat-qilish-modelini-ishlab-chiqish/blob/main/rasmlar/streamlit2.jpg)

import streamlit as st
import pandas as pd
import time
from keras.models import load_model
from Standard_Scaler import StandardScaler

model = load_model('model.h5')

title = "Keras yordamida Boston shaharchasidagi uylarning narxini bashorat qilish"
st.markdown("<h1 style='text-align: center;font-size: 30px;'>"+title+"</h1>", unsafe_allow_html=True)

info = {"Asosiy parametrlar":["Optimizer","Loss funksiyasi","Epochs","Train uchun Loss","Evaluate uchun Loss","Parametrlar(weight,bias) soni"],
              "Qiymatlar":["Stocastic Gradient Descent","Mean Squared Error","40","0.0737","0.1038","11 321"]}

st.dataframe(info,width=1000)

CRIM = st.number_input("Shaharlar bo'yicha aholi jon boshiga to'g'ri keladigan jinoyat darajasi")
ZN = st.number_input("25 000 kv.ft dan ortiq uchastkalar uchun rayonlashtirilgan turar-joy yerlarining ulushi.")
INDUS = st.number_input("shaharga to'g'ri keladigan chakana bo'lmagan biznes maydonlarining ulushi")
CHAS = st.selectbox('Charlz daryosidan uzoq yaqinligi', ["Daryoga yaqin hududda","Daryodan uzoqda"])
NOX = st.number_input("Azot oksidi kontsentratsiyasi")
RM = st.number_input("Turar-joy uchun o'rtacha xonalar soni")
AGE = st.number_input("1940-yilgacha qurib foydalanishga topshirilgan obyektlarning nisbati")
DIS = st.number_input("Beshta Boston bandlik markazlarigacha bo'lgan vaznli masofalar")
RAD = st.number_input("Radial magistrallarga kirish imkoniyati indeksi",min_value=0,max_value=24,step=1)
TAX = st.number_input("Har 10000$ uchun to'liq qiymatli mulk solig'i stavkasi")
PTRATIO = st.number_input("Shahar bo'yicha o'quvchi-o'qituvchi nisbati")
B = st.number_input("Qora tanlilarning shahardagi ulushi")
LSTAT = st.number_input("Aholining % past holati")


if st.button("Uy narxini bashorat qilish"):
    if CHAS=="Daryoga yaqin hududda":
        CHAS=1
    else:
        CHAS=0
    X = pd.DataFrame({
            'CRIM': [CRIM],
            'ZN': [ZN],
            'INDUS': [INDUS],
            'CHAS': [CHAS],
            'NOX': [NOX],
            'RM': [RM],
            'AGE': [AGE],
            'DIS': [DIS],
            'RAD': [RAD],
            'TAX': [TAX],
            'PTRATIO': [PTRATIO],
            'B': [B],
            'LSTAT': [LSTAT]
        })
    scale = StandardScaler()
    X_normal = scale.encoder(X)
    Y_predict = model.predict(X_normal)
    Y_decode = scale.decoder(Y_predict).ravel()
    Y_decode = pd.DataFrame(Y_decode,columns=["MEDV"])

    my_bar = st.progress(0, text="Iltimos kuting...")
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text="Uy narxi aniqlanmoqda.Iltimos kuting...")
    result = model.predict(X_normal.to_numpy())
    answer = "Keras yordamida Boston shaharchasidagi uylarning narxini bashorat qilish"
    st.markdown("<h2 style='text-align: center;font-size: 20px;'>"+"Uyning narxi: "+str(result[0][0]*10000)+"$"+"</h2>", unsafe_allow_html=True)
    
    

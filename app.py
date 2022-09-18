from tokenize import Number
import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression

model=pickle.load(open('model_test.pkl','rb'))

st.title('Laptop Price Predictor')
st.image("""https://i.rtings.com/assets/pages/6S2WXjTl/best-laptop-medium.jpg""")
st.header('Enter the Required Specifications of the Laptop:')

# Define the prediction function
def predict(processor_gnrtn, ram_gb, ram_type, ssd, hdd, os_bit,
       graphic_card_gb, warranty, Touchscreen, msoffice,
       old_price, discount, star_rating, ratings, reviews,
       brand_Acer, brand_Alienware, brand_Apple, brand_Asus,
       brand_Avita, brand_Dell, brand_Hp, brand_Iball,
       brand_Infinix, brand_Lenovo, brand_Lg, brand_Mi,
       brand_Microsoft, brand_Msi, brand_Nokia, brand_Realme,
       brand_Redmibook, brand_Samsung, brand_Smartron, brand_Vaio,
       model_14a, model_14s, model_15, model_15_ec1105ax,
       model_15q, model_15s, model_250, model_250_g6,
       model_3000, model_3511, model_430, model_A6_9225,
       model_Alpha, model_Amd, model_Apu, model_Aspire,
       model_Asus, model_Athlon, model_B50_70, model_Book,
       model_Book_slim, model_Bravo, model_Celeron,
       model_Chromebook, model_Commercial, model_Compbook,
       model_Conceptd, model_Cosmos, model_Creator, model_Da,
       model_Dell, model_Delta, model_Dual, model_E,
       model_Eeebook, model_Envy, model_Expertbook, model_Extensa,
       model_F17, model_G15, model_G3, model_G5, model_G7,
       model_Galaxy, model_Gaming, model_Ge76, model_Gf63,
       model_Gf65, model_Gp65, model_Gp76, model_Gram, model_Gs,
       model_Gs66, model_Hp, model_Ideapad, model_Inbook,
       model_Inpiron, model_Inspiron, model_Insprion, model_Intel,
       model_Katana, model_Legion, model_Lenovo, model_Liber,
       model_Macbook, model_Modern, model_Nitro, model_Notebook,
       model_Omen, model_Pavilion, model_Pentium, model_Predator,
       model_Prestige, model_Pro, model_Pulse, model_Pura,
       model_Purebook, model_Rog, model_Ryzen, model_Se,
       model_Spectre, model_Spin, model_Stealth, model_Summit,
       model_Surface, model_Swift, model_Sword, model_T_book,
       model_Thinkbook, model_Thinkpad, model_Thinpad,
       model_Travelmate, model_Tuf, model_Unknown, model_V15,
       model_Vivo, model_Vivobook, model_Vivobook14, model_Vostro,
       model_Wf65, model_X1, model_X360, model_X390, model_Xps,
       model_Yoga, model_Zenbook, model_Zephyrus,
       processor_brand_Amd, processor_brand_Intel,
       processor_brand_M1, processor_brand_Mediatek,
       processor_brand_Qualcomm, processor_name_A6_9225_processor,
       processor_name_Apu_dual, processor_name_Athlon_dual,
       processor_name_Celeron_dual, processor_name_Core,
       processor_name_Core_i3, processor_name_Core_i5,
       processor_name_Core_i7, processor_name_Core_i9,
       processor_name_Core_m3, processor_name_Dual_core,
       processor_name_Ever_screenpad, processor_name_Geforce_gtx,
       processor_name_Geforce_rtx, processor_name_Genuine_windows,
       processor_name_Hexa_core, processor_name_M1,
       processor_name_Mediatek_kompanio, processor_name_Pentium_quad,
       processor_name_Pentium_silver, processor_name_Quad,
       processor_name_Ryzen, processor_name_Ryzen_3,
       processor_name_Ryzen_5, processor_name_Ryzen_7,
       processor_name_Ryzen_9, processor_name_Snapdragon_7c, os_Dos,
       os_Mac, os_Windows, weight_Casual, weight_Gaming,
       weight_Thinnlight):

    #processor_gnrtn
    if processor_gnrtn == '4th':
        processor_gnrtn = 0
    elif processor_gnrtn == '7th':
        processor_gnrtn = 1
    elif processor_gnrtn == '8th':
        processor_gnrtn = 2
    elif processor_gnrtn == 'Unknown':
        processor_gnrtn = 3
    elif processor_gnrtn == '9th':
        processor_gnrtn = 4
    elif processor_gnrtn == '10th':
        processor_gnrtn = 5
    elif processor_gnrtn == '11th':
        processor_gnrtn = 6
    elif processor_gnrtn == '12th':
        processor_gnrtn = 7

    #ram_gb
    if ram_gb == '4':
        ram_gb = 0
    elif ram_gb == '8':
        ram_gb = 8
    elif ram_gb == '16':
        ram_gb = 16
    elif processor_gnrtn == '32':
        ram_gb = 32

    #ram_type
    if ram_type == 'Ddr3':
        ram_type = 0
    elif ram_type == 'Lpddr3':
        ram_type = 1
    elif ram_type == 'Ddr4':
        ram_type = 2
    elif ram_type == 'Lpddr4':
        ram_type = 3
    elif ram_type == 'Lpddr4x':
        ram_type = 4
    elif ram_type == 'Ddr5':
        ram_type = 5

    #ssd
    if ssd == '0':
        ssd = 0
    elif ssd == '32':
        ssd = 32
    elif ssd == '128':
        ssd = 128
    elif ssd == '256':
        ssd = 256
    elif ssd == '512':
        ssd = 512
    elif ssd == '1024':
        ssd = 1024
    elif ssd == '2048':
        ssd = 2048
    elif ssd == '3072':
        ssd = 3072

    #hdd
    if hdd == '0':
        hdd = 0
    elif hdd == '512':
        hdd = 512
    elif hdd == '1024':
        hdd = 1024
    elif hdd == '2048':
        hdd = 2048

    #os_bit
    if os_bit == '32':
        os_bit = 32
    elif os_bit == '64':
        os_bit = 64

    #Touchscreen
    if Touchscreen == 'Yes':
        Touchscreen = 1
    elif Touchscreen == 'No':
        Touchscreen = 0

    #msoffice
    if msoffice == 'Yes':
        msoffice = 1
    elif msoffice == 'No':
        msoffice = 0

    prediction = model.predict(pd.DataFrame([[processor_gnrtn, ram_gb, ram_type, ssd, hdd, os_bit,
       graphic_card_gb, warranty, Touchscreen, msoffice,
       old_price, discount, star_rating, ratings, reviews,
       brand_Acer, brand_Alienware, brand_Apple, brand_Asus,
       brand_Avita, brand_Dell, brand_Hp, brand_Iball,
       brand_Infinix, brand_Lenovo, brand_Lg, brand_Mi,
       brand_Microsoft, brand_Msi, brand_Nokia, brand_Realme,
       brand_Redmibook, brand_Samsung, brand_Smartron, brand_Vaio,
       model_14a, model_14s, model_15, model_15_ec1105ax,
       model_15q, model_15s, model_250, model_250_g6,
       model_3000, model_3511, model_430, model_A6_9225,
       model_Alpha, model_Amd, model_Apu, model_Aspire,
       model_Asus, model_Athlon, model_B50_70, model_Book,
       model_Book_slim, model_Bravo, model_Celeron,
       model_Chromebook, model_Commercial, model_Compbook,
       model_Conceptd, model_Cosmos, model_Creator, model_Da,
       model_Dell, model_Delta, model_Dual, model_E,
       model_Eeebook, model_Envy, model_Expertbook, model_Extensa,
       model_F17, model_G15, model_G3, model_G5, model_G7,
       model_Galaxy, model_Gaming, model_Ge76, model_Gf63,
       model_Gf65, model_Gp65, model_Gp76, model_Gram, model_Gs,
       model_Gs66, model_Hp, model_Ideapad, model_Inbook,
       model_Inpiron, model_Inspiron, model_Insprion, model_Intel,
       model_Katana, model_Legion, model_Lenovo, model_Liber,
       model_Macbook, model_Modern, model_Nitro, model_Notebook,
       model_Omen, model_Pavilion, model_Pentium, model_Predator,
       model_Prestige, model_Pro, model_Pulse, model_Pura,
       model_Purebook, model_Rog, model_Ryzen, model_Se,
       model_Spectre, model_Spin, model_Stealth, model_Summit,
       model_Surface, model_Swift, model_Sword, model_T_book,
       model_Thinkbook, model_Thinkpad, model_Thinpad,
       model_Travelmate, model_Tuf, model_Unknown, model_V15,
       model_Vivo, model_Vivobook, model_Vivobook14, model_Vostro,
       model_Wf65, model_X1, model_X360, model_X390, model_Xps,
       model_Yoga, model_Zenbook, model_Zephyrus,
       processor_brand_Amd, processor_brand_Intel,
       processor_brand_M1, processor_brand_Mediatek,
       processor_brand_Qualcomm, processor_name_A6_9225_processor,
       processor_name_Apu_dual, processor_name_Athlon_dual,
       processor_name_Celeron_dual, processor_name_Core,
       processor_name_Core_i3, processor_name_Core_i5,
       processor_name_Core_i7, processor_name_Core_i9,
       processor_name_Core_m3, processor_name_Dual_core,
       processor_name_Ever_screenpad, processor_name_Geforce_gtx,
       processor_name_Geforce_rtx, processor_name_Genuine_windows,
       processor_name_Hexa_core, processor_name_M1,
       processor_name_Mediatek_kompanio, processor_name_Pentium_quad,
       processor_name_Pentium_silver, processor_name_Quad,
       processor_name_Ryzen, processor_name_Ryzen_3,
       processor_name_Ryzen_5, processor_name_Ryzen_7,
       processor_name_Ryzen_9, processor_name_Snapdragon_7c, os_Dos,
       os_Mac, os_Windows, weight_Casual, weight_Gaming,
       weight_Thinnlight]], columns=['processor_gnrtn', 'ram_gb', 'ram_type', 'ssd', 'hdd', 'os_bit',
       'graphic_card_gb', 'warranty', 'Touchscreen', 'msoffice',
       'old_price', 'discount', 'star_rating', 'ratings', 'reviews',
       'brand_Acer', 'brand_Alienware', 'brand_Apple', 'brand_Asus',
       'brand_Avita', 'brand_Dell', 'brand_Hp', 'brand_Iball',
       'brand_Infinix', 'brand_Lenovo', 'brand_Lg', 'brand_Mi',
       'brand_Microsoft', 'brand_Msi', 'brand_Nokia', 'brand_Realme',
       'brand_Redmibook', 'brand_Samsung', 'brand_Smartron', 'brand_Vaio',
       'model_14a', 'model_14s', 'model_15', 'model_15-ec1105ax',
       'model_15q', 'model_15s', 'model_250', 'model_250-g6',
       'model_3000', 'model_3511', 'model_430', 'model_A6-9225',
       'model_Alpha', 'model_Amd', 'model_Apu', 'model_Aspire',
       'model_Asus', 'model_Athlon', 'model_B50-70', 'model_Book',
       'model_Book(slim)', 'model_Bravo', 'model_Celeron',
       'model_Chromebook', 'model_Commercial', 'model_Compbook',
       'model_Conceptd', 'model_Cosmos', 'model_Creator', 'model_Da',
       'model_Dell', 'model_Delta', 'model_Dual', 'model_E',
       'model_Eeebook', 'model_Envy', 'model_Expertbook', 'model_Extensa',
       'model_F17', 'model_G15', 'model_G3', 'model_G5', 'model_G7',
       'model_Galaxy', 'model_Gaming', 'model_Ge76', 'model_Gf63',
       'model_Gf65', 'model_Gp65', 'model_Gp76', 'model_Gram', 'model_Gs',
       'model_Gs66', 'model_Hp', 'model_Ideapad', 'model_Inbook',
       'model_Inpiron', 'model_Inspiron', 'model_Insprion', 'model_Intel',
       'model_Katana', 'model_Legion', 'model_Lenovo', 'model_Liber',
       'model_Macbook', 'model_Modern', 'model_Nitro', 'model_Notebook',
       'model_Omen', 'model_Pavilion', 'model_Pentium', 'model_Predator',
       'model_Prestige', 'model_Pro', 'model_Pulse', 'model_Pura',
       'model_Purebook', 'model_Rog', 'model_Ryzen', 'model_Se',
       'model_Spectre', 'model_Spin', 'model_Stealth', 'model_Summit',
       'model_Surface', 'model_Swift', 'model_Sword', 'model_T.book',
       'model_Thinkbook', 'model_Thinkpad', 'model_Thinpad',
       'model_Travelmate', 'model_Tuf', 'model_Unknown', 'model_V15',
       'model_Vivo', 'model_Vivobook', 'model_Vivobook14', 'model_Vostro',
       'model_Wf65', 'model_X1', 'model_X360', 'model_X390', 'model_Xps',
       'model_Yoga', 'model_Zenbook', 'model_Zephyrus',
       'processor_brand_Amd', 'processor_brand_Intel',
       'processor_brand_M1', 'processor_brand_Mediatek',
       'processor_brand_Qualcomm', 'processor_name_A6-9225 processor',
       'processor_name_Apu dual', 'processor_name_Athlon dual',
       'processor_name_Celeron dual', 'processor_name_Core',
       'processor_name_Core i3', 'processor_name_Core i5',
       'processor_name_Core i7', 'processor_name_Core i9',
       'processor_name_Core m3', 'processor_name_Dual core',
       'processor_name_Ever screenpad', 'processor_name_Geforce gtx',
       'processor_name_Geforce rtx', 'processor_name_Genuine windows',
       'processor_name_Hexa core', 'processor_name_M1',
       'processor_name_Mediatek kompanio', 'processor_name_Pentium quad',
       'processor_name_Pentium silver', 'processor_name_Quad',
       'processor_name_Ryzen', 'processor_name_Ryzen 3',
       'processor_name_Ryzen 5', 'processor_name_Ryzen 7',
       'processor_name_Ryzen 9', 'processor_name_Snapdragon 7c', 'os_Dos',
       'os_Mac', 'os_Windows', 'weight_Casual', 'weight_Gaming',
       'weight_Thinnlight']))
    return prediction




#Brand
#setting dummy variables to zero
brand_Acer=0
brand_Alienware=0
brand_Apple=0                   
brand_Asus=0
brand_Avita=0
brand_Dell=0
brand_Hp=0
brand_Iball=0           
brand_Infinix=0
brand_Lenovo=0
brand_Lg=0
brand_Mi=0
brand_Microsoft=0
brand_Msi=0
brand_Nokia=0
brand_Realme=0
brand_Redmibook=0
brand_Samsung=0
brand_Smartron=0
brand_Vaio=0         


laptop_brand=st.selectbox('Please select the Laptop Brand',['Acer','Alienware','Apple','Asus','Avita',
                                                                'Dell','Hp','Iball','Infinix','Lenovo',
                                                                'Lg','Mi','Microsoft','Msi','Nokia','Realme',
                                                                'Redmibook','Samsung','Smartron','Vaio'])

if laptop_brand=='Acer':
        brand_Acer =1
elif laptop_brand=='Alienware':
        brand_Alienware =1
elif laptop_brand=='Apple':
        brand_Apple =1
elif laptop_brand=='Asus':
        brand_Asus =1
elif laptop_brand=='Avita':
        brand_Avita =1
elif laptop_brand=='Dell':
        brand_Dell =1                      
elif laptop_brand=='Hp':
        brand_Hp =1
elif laptop_brand=='Iball':
        brand_Iball =1
elif laptop_brand=='Infinix':
        brand_Infinix =1
elif laptop_brand=='Lenovo':
        brand_Lenovo =1
elif laptop_brand=='Lg':
        brand_Lg =1
elif laptop_brand=='Mi':
        brand_Mi =1
elif laptop_brand=='Microsoft':
        brand_Microsoft =1
elif laptop_brand=='Msi':
        brand_Msi =1
elif laptop_brand=='Nokia':
        brand_Nokia =1
elif laptop_brand=='Realme':
        brand_Realme =1
elif laptop_brand=='Redmibook':
        brand_Redmibook =1
elif laptop_brand=='Samsung':
        brand_Samsung =1
elif laptop_brand=='Smartron':
        brand_Smartron =1
elif laptop_brand=='Vaio':
        brand_Vaio =1



#Laptop Model
#setting dummy variables to zero
model_14a=0
model_14s=0 
model_15=0 
model_15_ec1105ax=0
model_15q=0 
model_15s=0 
model_250=0 
model_250_g6=0
model_3000=0 
model_3511=0 
model_430=0 
model_A6_9225=0
model_Alpha=0 
model_Amd=0 
model_Apu=0 
model_Aspire=0
model_Asus=0 
model_Athlon=0 
model_B50_70=0 
model_Book=0
model_Book_slim=0 
model_Bravo=0 
model_Celeron=0
model_Chromebook=0 
model_Commercial=0 
model_Compbook=0
model_Conceptd=0 
model_Cosmos=0 
model_Creator=0 
model_Da=0
model_Dell=0 
model_Delta=0 
model_Dual=0 
model_E=0
model_Eeebook=0 
model_Envy=0 
model_Expertbook=0 
model_Extensa=0
model_F17=0 
model_G15=0 
model_G3=0 
model_G5=0 
model_G7=0
model_Galaxy=0 
model_Gaming=0 
model_Ge76=0 
model_Gf63=0
model_Gf65=0 
model_Gp65=0 
model_Gp76=0 
model_Gram=0 
model_Gs=0
model_Gs66=0 
model_Hp=0 
model_Ideapad=0 
model_Inbook=0
model_Inpiron=0 
model_Inspiron=0 
model_Insprion=0 
model_Intel=0
model_Katana=0 
model_Legion=0 
model_Lenovo=0 
model_Liber=0
model_Macbook=0 
model_Modern=0 
model_Nitro=0 
model_Notebook=0
model_Omen=0 
model_Pavilion=0 
model_Pentium=0 
model_Predator=0
model_Prestige=0 
model_Pro=0 
model_Pulse=0 
model_Pura=0
model_Purebook=0 
model_Rog=0 
model_Ryzen=0 
model_Se=0
model_Spectre=0 
model_Spin=0 
model_Stealth=0 
model_Summit=0
model_Surface=0 
model_Swift=0 
model_Sword=0 
model_T_book=0
model_Thinkbook=0 
model_Thinkpad=0 
model_Thinpad=0
model_Travelmate=0 
model_Tuf=0 
model_Unknown=0 
model_V15=0
model_Vivo=0 
model_Vivobook=0 
model_Vivobook14=0 
model_Vostro=0
model_Wf65=0 
model_X1=0 
model_X360=0 
model_X390=0 
model_Xps=0
model_Yoga=0 
model_Zenbook=0 
model_Zephyrus=0


laptop_model=st.selectbox('Please select the Laptop Model',['14a','14s','15','15-ec1105ax','15q',
														'15s','250','250-g6','3000','3511',
														'430','A6-9225','Alpha','Amd','Apu',
														'Aspire','Asus','Athlon','B50-70','Book',
														'Book-slim','Bravo','Celeron','Chromebook','Commercial',
														'Compbook','Conceptd','Cosmos','Creator','Da',
														'Dell','Delta','Dual','E','Eeebook',
														'Envy','Expertbook','Extensa','F17','G15',
														'G3','G5','G7','Galaxy','Gaming',
														'Ge76','Gf63','Gf65','Gp65','Gp76',
														'Gram','Gs','Gs66','Hp','Ideapad',
														'Inbook','Inpiron','Inspiron','Insprion','Intel',
														'Katana','Legion','Lenovo','Liber','Macbook',
														'Modern','Nitro','Notebook','Omen','Pavilion',
														'Pentium','Predator','Prestige','Pro','Pulse',
														'Pura','Purebook','Rog','Ryzen','Se',
														'Spectre','Spin','Stealth','Summit','Surface',
														'Swift','Sword','T-book','Thinkbook','Thinkpad',
														'Thinpad','Travelmate','Tuf','Unknown','V15',
														'Vivo','Vivobook','Vivobook14','Vostro','Wf65',
														'X1','X360','X390','Xps','Yoga',
														'Zenbook','Zephyrus'])


if laptop_model=='14a':
        model_14a =1
elif laptop_model=='14s':
        model_14s =1
elif laptop_model=='15':
        model_15 =1
elif laptop_model=='15-ec1105ax':
        model_15_ec1105ax =1
elif laptop_model=='15q':
        model_15q =1
elif laptop_model=='15s':
        model_15s =1
elif laptop_model=='250':
        model_250 =1
elif laptop_model=='250-g6':
        model_250_g6 =1
elif laptop_model=='3000':
        model_3000 =1
elif laptop_model=='3511':
        model_3511 =1
elif laptop_model=='430':
        model_430 =1
elif laptop_model=='A6-9225':
        model_A6_9225 =1
elif laptop_model=='Alpha':
        model_Alpha =1
elif laptop_model=='Amd':
        model_Amd =1
elif laptop_model=='Apu':
        model_Apu =1
elif laptop_model=='Aspire':
        model_Aspire =1
elif laptop_model=='Asus':
        model_Asus =1
elif laptop_model=='Athlon':
        model_Athlon =1
elif laptop_model=='B50-70':
        model_B50_70 =1
elif laptop_model=='Book':
        model_Book =1
elif laptop_model=='Book-slim':
        model_Book_slim =1
elif laptop_model=='Bravo':
        model_Bravo =1
elif laptop_model=='Celeron':
        model_Celeron =1
elif laptop_model=='Chromebook':
        model_Chromebook =1
elif laptop_model=='Commercial':
        model_Commercial =1
elif laptop_model=='Compbook':
        model_Compbook =1
elif laptop_model=='Conceptd':
        model_Conceptd =1
elif laptop_model=='Cosmos':
        model_Cosmos =1
elif laptop_model=='Creator':
        model_Creator =1
elif laptop_model=='Da':
        model_Da =1
elif laptop_model=='Dell':
        model_Dell =1
elif laptop_model=='Delta':
        model_Delta =1
elif laptop_model=='Dual':
        model_Dual =1
elif laptop_model=='E':
        model_E =1
elif laptop_model=='Eeebook':
        model_Eeebook =1
elif laptop_model=='Envy':
        model_Envy =1
elif laptop_model=='Expertbook':
        model_Expertbook =1
elif laptop_model=='Extensa':
        model_Extensa =1
elif laptop_model=='F17':
        model_F17 =1
elif laptop_model=='G15':
        model_G15 =1
elif laptop_model=='G3':
        model_G3 =1
elif laptop_model=='G5':
        model_G5 =1
elif laptop_model=='G7':
        model_G7 =1
elif laptop_model=='Galaxy':
        model_Galaxy =1
elif laptop_model=='Gaming':
        model_Gaming =1
elif laptop_model=='Ge76':
        model_Ge76 =1
elif laptop_model=='Gf63':
        model_Gf63 =1
elif laptop_model=='Gf65':
        model_Gf65 =1
elif laptop_model=='Gp65':
        model_Gp65 =1
elif laptop_model=='Gp76':
        model_Gp76 =1
elif laptop_model=='Gram':
        model_Gram =1
elif laptop_model=='Gs':
        model_Gs =1
elif laptop_model=='Gs66':
        model_Gs66 =1
elif laptop_model=='Hp':
        model_Hp =1
elif laptop_model=='Ideapad':
        model_Ideapad =1
elif laptop_model=='Inbook':
        model_Inbook =1
elif laptop_model=='Inpiron':
        model_Inpiron =1
elif laptop_model=='Inspiron':
        model_Inspiron =1
elif laptop_model=='Insprion':
        model_Insprion =1
elif laptop_model=='Intel':
        model_Intel =1
elif laptop_model=='Katana':
        model_Katana =1
elif laptop_model=='Legion':
        model_Legion =1
elif laptop_model=='Lenovo':
        model_Lenovo =1
elif laptop_model=='Liber':
        model_Liber =1
elif laptop_model=='Macbook':
        model_Macbook =1
elif laptop_model=='Modern':
        model_Modern =1
elif laptop_model=='Nitro':
        model_Nitro =1
elif laptop_model=='Notebook':
        model_Notebook =1
elif laptop_model=='Omen':
        model_Omen =1
elif laptop_model=='Pavilion':
        model_Pavilion =1
elif laptop_model=='Pentium':
        model_Pentium =1
elif laptop_model=='Predator':
        model_Predator =1
elif laptop_model=='Prestige':
        model_Prestige =1
elif laptop_model=='Pro':
        model_Pro =1
elif laptop_model=='Pulse':
        model_Pulse =1
elif laptop_model=='Pura':
        model_Pura =1
elif laptop_model=='Purebook':
        model_Purebook =1
elif laptop_model=='Rog':
        model_Rog =1
elif laptop_model=='Ryzen':
        model_Ryzen =1
elif laptop_model=='Se':
        model_Se =1
elif laptop_model=='Spectre':
        model_Spectre =1
elif laptop_model=='Spin':
        model_Spin =1
elif laptop_model=='Stealth':
        model_Stealth =1
elif laptop_model=='Summit':
        model_Summit =1
elif laptop_model=='Surface':
        model_Surface =1
elif laptop_model=='Swift':
        model_Swift =1
elif laptop_model=='Sword':
        model_Sword =1
elif laptop_model=='T-book':
        model_T_book =1
elif laptop_model=='Thinkbook':
        model_Thinkbook =1
elif laptop_model=='Thinkpad':
        model_Thinkpad =1
elif laptop_model=='Thinpad':
        model_Thinpad =1
elif laptop_model=='Travelmate':
        model_Travelmate =1
elif laptop_model=='Tuf':
        model_Tuf =1
elif laptop_model=='Unknown':
        model_Unknown =1
elif laptop_model=='V15':
        model_V15 =1
elif laptop_model=='Vivo':
        model_Vivo =1
elif laptop_model=='Vivobook':
        model_Vivobook =1
elif laptop_model=='Vivobook14':
        model_Vivobook14 =1
elif laptop_model=='Vostro':
        model_Vostro =1
elif laptop_model=='Wf65':
        model_Wf65 =1
elif laptop_model=='X1':
        model_X1 =1
elif laptop_model=='X360':
        model_X360 =1
elif laptop_model=='X390':
        model_X390 =1
elif laptop_model=='Xps':
        model_Xps =1
elif laptop_model=='Yoga':
        model_Yoga =1
elif laptop_model=='Zenbook':
        model_Zenbook =1
elif laptop_model=='Zephyrus':
        model_Zephyrus  =1



#Processor Brand
#setting dummy variables to zero
processor_brand_Amd=0
processor_brand_Intel=0
processor_brand_M1=0
processor_brand_Mediatek=0
processor_brand_Qualcomm=0

processor_brand=st.selectbox('Please select the Processor Brand',['AMD','Intel','M1','Mediatek','Qualcomm'])

if processor_brand=='AMD':
        processor_brand_Amd =1
elif processor_brand=='Intel':
        processor_brand_Intel =1
elif processor_brand=='M1':
        processor_brand_M1 =1
elif processor_brand=='Mediatek':
        processor_brand_Mediatek =1
elif processor_brand=='Qualcomm':
        processor_brand_Qualcomm =1



#Processor Name
#setting dummy variables to zero
processor_name_A6_9225_processor=0
processor_name_Apu_dual=0
processor_name_Athlon_dual=0
processor_name_Celeron_dual=0
processor_name_Core=0
processor_name_Core_i3=0
processor_name_Core_i5=0
processor_name_Core_i7=0
processor_name_Core_i9=0
processor_name_Core_m3=0
processor_name_Dual_core=0
processor_name_Ever_screenpad=0
processor_name_Geforce_gtx=0
processor_name_Geforce_rtx=0
processor_name_Genuine_windows=0
processor_name_Hexa_core=0
processor_name_M1=0
processor_name_Mediatek_kompanio=0
processor_name_Pentium_quad=0
processor_name_Pentium_silver=0
processor_name_Quad=0
processor_name_Ryzen=0
processor_name_Ryzen_3=0
processor_name_Ryzen_5=0
processor_name_Ryzen_7=0
processor_name_Ryzen_9=0
processor_name_Snapdragon_7c=0


processor_name=st.selectbox('Please select the Processor',['A6-9225 processor','Apu dual','Athlon dual','Celeron dual',
                                                                'Core','Core i3','Core i5','Core i7','Core i9','Core m3','Dual core',
                                                                'Ever screenpad','Geforce gtx','Geforce rtx','Genuine windows','Hexa core',
                                                                'M1','Mediatek kompanio','Pentium quad','Pentium silver','Quad','Ryzen',
                                                                'Ryzen 3','Ryzen 5','Ryzen 7','Ryzen 9','Snapdragon 7c'])


if processor_name=='A6-9225 processor':
        processor_name_A6_9225_processor =1
elif processor_name=='Apu dual':
        processor_name_Apu_dual =1
elif processor_name=='Athlon dual':
        processor_name_Athlon_dual =1
elif processor_name=='Celeron dual':
        processor_name_Celeron_dual =1
elif processor_name=='Core':
        processor_name_Core =1
elif processor_name=='Core i3':
        processor_name_Core_i3 =1
elif processor_name=='Core i5':
        processor_name_Core_i5 =1
elif processor_name=='Core i7':
        processor_name_Core_i7 =1
elif processor_name=='Core i9':
        processor_name_Core_i9 =1
elif processor_name=='Core m3':
        processor_name_Core_m3 =1
elif processor_name=='Dual core':
        processor_name_Dual_core =1
elif processor_name=='Ever screenpad':
        processor_name_Ever_screenpad =1
elif processor_name=='Geforce gtx':
        processor_name_Geforce_gtx =1
elif processor_name=='Geforce rtx':
        processor_name_Geforce_rtx =1
elif processor_name=='Genuine windows':
        processor_name_Genuine_windows =1
elif processor_name=='Hexa core':
        processor_name_Hexa_core =1
elif processor_name=='M1':
        processor_name_M1 =1
elif processor_name=='Mediatek kompanio':
        processor_name_Mediatek_kompanio =1
elif processor_name=='Pentium quad':
        processor_name_Pentium_quad =1
elif processor_name=='Pentium silver':
        processor_name_Pentium_silver =1
elif processor_name=='Quad':
        processor_name_Quad =1
elif processor_name=='Ryzen':
        processor_name_Ryzen =1
elif processor_name=='Ryzen 3':
        processor_name_Ryzen_3 =1
elif processor_name=='Ryzen 5':
        processor_name_Ryzen_5 =1
elif processor_name=='Ryzen 7':
        processor_name_Ryzen_7 =1
elif processor_name=='Ryzen 9':
        processor_name_Ryzen_9 =1
elif processor_name=='Snapdragon 7c':
        processor_name_Snapdragon_7c =1




processor_generation = st.selectbox('Processor_generation:', ['4th', '7th', '8th', '9th', '10th','11th','12th','Unknown'])

ram_size = st.select_slider('Ram Size (Gb):',  options=['4', '8', '16', '32'])

ram_Type=st.selectbox('Ram Type :', ['Ddr3', 'Lpddr3', 'Ddr4', 'Lpddr4', 'Lpddr4x','Ddr5'])

ssd_size = st.select_slider('SSD Size (Gb):',  options=['0', '32', '128', '256','512', '1024', '2048', '3072'])

hard_disk_size = st.select_slider('Hard Disk Size (Gb):',  options=['0', '512', '1024', '2048'])

os_bit_size = st.selectbox('OS Bit:', ['32', '64'])

graphic_card_size=st.number_input('Graphic card size (Gb):', min_value=0, max_value=8, value=4,step=2)

warranty_years=st.number_input('Warranty (Years):', min_value=0, max_value=3, value=2,step=1)

touchscreen=st.selectbox('Touch Screen:', ['Yes', 'No'])

ms_office=st.selectbox('MS Office:', ['Yes', 'No'])

old_price=st.number_input('Original_Price (Rs.):',min_value=0)

discount=st.number_input('Discount (%) :',min_value=0,max_value=100)

star_rating=st.number_input('Star Rating  :',min_value=0.00,max_value=5.00,step=0.10)

number_of_ratings=st.number_input('No. of Ratings  :',min_value=0)

number_of_reviews=st.number_input('No. of Reviews  :',min_value=0)


#weight
#setting dummy variables to zero
weight_Casual=0
weight_Gaming=0
weight_Thinnlight=0

weight_type = st.selectbox('Please select the weight type',['Casual','Gaming','Thin & Light'])

if weight_type=='Casual':
        weight_Casual =1
elif weight_type=='Gaming':
        weight_Gaming =1
elif weight_type=='Thin & Light':
        weight_Thinnlight =1
                              

#Os
#setting dummy variables to zero
os_Dos=0
os_Mac=0
os_Windows=0

os = st.selectbox('Please select the Operating System',['Windows','Mac','DOS'])


if os=='Windows':
        os_Windows =1
elif os=='Mac':
        os_Mac =1
elif os=='DOS':
        os_Dos =1



if st.button('Predict Price'):
    price = predict(processor_generation, ram_size, ram_Type, ssd_size, hard_disk_size, os_bit_size,
       graphic_card_size, warranty_years, touchscreen, ms_office,
       old_price, discount, star_rating, number_of_ratings, number_of_reviews,
       brand_Acer, brand_Alienware, brand_Apple, brand_Asus,
       brand_Avita, brand_Dell, brand_Hp, brand_Iball,
       brand_Infinix, brand_Lenovo, brand_Lg, brand_Mi,
       brand_Microsoft, brand_Msi, brand_Nokia, brand_Realme,
       brand_Redmibook, brand_Samsung, brand_Smartron, brand_Vaio,
       model_14a, model_14s, model_15, model_15_ec1105ax,
       model_15q, model_15s, model_250, model_250_g6,
       model_3000, model_3511, model_430, model_A6_9225,
       model_Alpha, model_Amd, model_Apu, model_Aspire,
       model_Asus, model_Athlon, model_B50_70, model_Book,
       model_Book_slim, model_Bravo, model_Celeron,
       model_Chromebook, model_Commercial, model_Compbook,
       model_Conceptd, model_Cosmos, model_Creator, model_Da,
       model_Dell, model_Delta, model_Dual, model_E,
       model_Eeebook, model_Envy, model_Expertbook, model_Extensa,
       model_F17, model_G15, model_G3, model_G5, model_G7,
       model_Galaxy, model_Gaming, model_Ge76, model_Gf63,
       model_Gf65, model_Gp65, model_Gp76, model_Gram, model_Gs,
       model_Gs66, model_Hp, model_Ideapad, model_Inbook,
       model_Inpiron, model_Inspiron, model_Insprion, model_Intel,
       model_Katana, model_Legion, model_Lenovo, model_Liber,
       model_Macbook, model_Modern, model_Nitro, model_Notebook,
       model_Omen, model_Pavilion, model_Pentium, model_Predator,
       model_Prestige, model_Pro, model_Pulse, model_Pura,
       model_Purebook, model_Rog, model_Ryzen, model_Se,
       model_Spectre, model_Spin, model_Stealth, model_Summit,
       model_Surface, model_Swift, model_Sword, model_T_book,
       model_Thinkbook, model_Thinkpad, model_Thinpad,
       model_Travelmate, model_Tuf, model_Unknown, model_V15,
       model_Vivo, model_Vivobook, model_Vivobook14, model_Vostro,
       model_Wf65, model_X1, model_X360, model_X390, model_Xps,
       model_Yoga, model_Zenbook, model_Zephyrus,
       processor_brand_Amd, processor_brand_Intel,
       processor_brand_M1, processor_brand_Mediatek,
       processor_brand_Qualcomm, processor_name_A6_9225_processor,
       processor_name_Apu_dual, processor_name_Athlon_dual,
       processor_name_Celeron_dual, processor_name_Core,
       processor_name_Core_i3, processor_name_Core_i5,
       processor_name_Core_i7, processor_name_Core_i9,
       processor_name_Core_m3, processor_name_Dual_core,
       processor_name_Ever_screenpad, processor_name_Geforce_gtx,
       processor_name_Geforce_rtx, processor_name_Genuine_windows,
       processor_name_Hexa_core, processor_name_M1,
       processor_name_Mediatek_kompanio, processor_name_Pentium_quad,
       processor_name_Pentium_silver, processor_name_Quad,
       processor_name_Ryzen, processor_name_Ryzen_3,
       processor_name_Ryzen_5, processor_name_Ryzen_7,
       processor_name_Ryzen_9, processor_name_Snapdragon_7c, os_Dos,
       os_Mac, os_Windows, weight_Casual, weight_Gaming,
       weight_Thinnlight)
    st.success(f'The predicted price of the Laptop is Rs. {np.exp(price[0]):.2f}  /-')
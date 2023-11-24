import streamlit as st
from PIL import Image
import pickle
import numpy as np

img=Image.open('image.PNG')
st.set_page_config(page_title='predict-n-sell', page_icon=img)
st.subheader('Please select what you want to sell from the drop-down menu ?')
predict_type = st.selectbox('', ['Choose Option','Laptop', 'Car', 'House', 'Bike'])

if predict_type == 'Laptop':
    model = pickle.load(open('pipe1.pkl', 'rb'))
    df = pickle.load(open('df1.pkl', 'rb'))

    st.title('Laptop Price Predictor')

    # Brand
    company = st.selectbox('Brand', df['Company'].unique())

    # Type
    type = st.selectbox('Type', df['TypeName'].unique())

    # Ram
    ram = st.selectbox('Ram (in GB)', [2, 4, 8, 16, 32, 64, ])

    # Weight
    weight = st.number_input('Weight (In KG)')

    if weight < 0.5 or weight > 8:
        st.error("Enter valid Weight")

    # TouchScreen
    touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])

    # IPS
    ips = st.selectbox('Ips (In-Plane Switching)', ['No', 'Yes'])

    # Screen Size
    screen_size = st.number_input('Screen Size (In Inches)')

    if screen_size < 5 or screen_size >30:
        st.error("Enter valid Screen Size")

    # Resolution
    resolution = st.selectbox('Screen Resolution',
                              ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600',
                               '2560x1440', '2304x1440'])

    # cpu
    cpu = st.selectbox('CPU', df['Cpu Brand'].unique())

    # HDD
    hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])

    # SSD
    ssd = st.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024])

    # GPU
    gpu = st.selectbox('GPU', df['Gpu Brand'].unique())

    # Operating System
    os = st.selectbox('Operating System', df['OS'].unique())

    st.title('')

    if st.button("Predict Price"):

        ppi = None

        if touchscreen == 'Yes':
            touchscreen = 1
        else:
            touchscreen = 0

        if ips == 'Yes':
            ips = 1
        else:
            ips = 0

        X_res = int(resolution.split('x')[0])
        Y_res = int(resolution.split('x')[1])
        ppi = ((X_res ** 2) + (Y_res ** 2)) ** 0.5 / screen_size

        query = np.array([company, type, ram, weight, ips, touchscreen, ppi, cpu, ssd, hdd, gpu, os])
        query = query.reshape(1, 12)

        st.title(
            "The predicted price of this configuration is : Rs. " + str(int(np.exp(np.exp(model.predict(query)[0])))))

elif predict_type == 'Car':

    # Import the model
    model = pickle.load(open('pipe2.pkl', 'rb'))
    df = pickle.load(open('df2.pkl', 'rb'))

    st.title('Car Price Predictor')

    # year
    year = st.selectbox('Year',[ 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982,1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994,1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021])

    # km_driven
    km_driven = st.number_input('Kms Drive')
    if km_driven > 1000000:
        st.error("Enter valid Km Drive")

    # Fuel
    fuel = st.selectbox('Fuel Type', df['fuel'].unique())

    # Seller Type
    seller_type = st.selectbox('Seller Type', df['seller_type'].unique())

    # Transmission
    transmission = st.selectbox('Transmission', df['transmission'].unique())

    # Owner
    owner = st.selectbox('Owner', df['owner'].unique())

    # mileage
    mileage = st.number_input('Mileage (In Kmpl)')

    if mileage < 1 or mileage > 70:
        st.error("Enter valid Mileage")

    # engine
    engiene = st.number_input('Engine Capacity (In CC)')

    if engiene < 20 or engiene > 4000:
        st.error("Enter valid Engine Capacity")

    # max power
    max_power = st.number_input('Max Power (In Bhp)')

    if max_power < 30 or max_power > 2500:
        st.error("Enter valid Max Power")

    # Seats
    seats = st.selectbox('No. of Seats', [2,3,4,5,6,7,8,9,10,11,12,113,14,15])

    # Company
    company = st.selectbox('Company Name', df['company'].unique())

    st.title('')

    if st.button("Predict Price"):
        query = np.array(
            [year, km_driven, fuel, seller_type, transmission, owner, mileage, engiene, max_power, seats, company])
        query = query.reshape(1, 11)

        st.title("You can sell your car at Rs." + str(int(np.exp(model.predict(query)[0]))))

elif predict_type == 'House':

    # Import the model
    model = pickle.load(open('pipe4.pkl', 'rb'))
    df = pickle.load(open('df4.pkl', 'rb'))

    st.title('House Price Predictor')

    posted_by = st.selectbox('Posted By', ['Dealer', 'Owner', 'Builder'])

    under_cons = st.selectbox('Under Construction', ['No', 'Yes'])

    rera = st.selectbox('REAR (Real Estate Regulatory Authority) Approval ', ['No', 'Yes'])

    bhk = st.selectbox('No. of BHK', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])

    square_foot = st.number_input('Square Feet')

    if square_foot < 50 or square_foot > 500000:
        st.error("Enter valid Square Foot")

    ready_to_move = st.selectbox('Ready To Move', ['Yes', 'No'])

    resale = st.selectbox('Resale', ['Yes', 'No'])

    longitude = st.number_input('Longitude')

    latitude = st.number_input('Latitude')

    city = st.selectbox('City Name', df['City'].unique())

    st.title('')

    if st.button("Predict Price"):

        if under_cons == 'No':
            under_cons = 0
        else:
            under_cons = 1

        if rera == "No":
            rera = 0
        else:
            rera = 1

        if ready_to_move == 'No':
            ready_to_move = 0
        else:
            ready_to_move = 1

        if resale == 'No':
            resale=0
        else:
            resale=1

        query = np.array(
            [posted_by,  under_cons, rera, bhk, square_foot, ready_to_move, resale, longitude, latitude,
             city])
        query = query.reshape(1, 10)
        st.title("You can sell your house at " + str(int(np.exp(model.predict(query)[0])))+" LAKHS")

elif predict_type == 'Bike':
    # Import the model
    model = pickle.load(open('pipe3.pkl', 'rb'))
    df = pickle.load(open('df3.pkl', 'rb'))

    st.title('Bike Price Predictor')

    year = st.selectbox('Year',
                        [1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985,
                         1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001,
                         2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017,
                         2018, 2019, 2020, 2021])

    seller_type = st.selectbox('Seller Type', ['Individual', 'Dealer'])

    owner = st.selectbox('Owner', ['1st owner', '2nd owner', '3rd owner', '4th owner'])

    km_driven = st.number_input('Kms Drive')

    if km_driven > 100000:
        st.error("Enter valid Km Drive")

    ex_showroom_price = st.number_input('Ex Showroom Price (In Rupees)')

    if ex_showroom_price < 500 or ex_showroom_price > 3000000 :
        st.error("Enter valid Ex Showroom Price")

    company = st.selectbox('Company Name', df['Company'].unique())

    st.title('')

    if st.button("Predict Price"):
        query = np.array([year, seller_type, owner, km_driven, ex_showroom_price, company])
        query = query.reshape(1, 6)

        st.title("You can sell your bike at Rs." + str(int(np.exp(model.predict(query)[0]))))

elif predict_type == 'Choose Option':
    for i in range(15):
        st.text('')
    st.subheader('Provides approximate price of your good, so that you can sell at this approximate price and prevents you got from cheated -- Naman Sethi')
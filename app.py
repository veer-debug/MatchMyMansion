from flask import Flask ,render_template,request,redirect
import pandas as pd
import pickle
import numpy as np



# home=pd.read_csv('home_data.csv')
# home['link'][0]='https://www.openpr.com/wiki/images/642-400x300_4828'
# img_list=home['link'].values

# ========================================================================


with open('Jupiter_works/dataset/df.pkl','rb') as file:
    df = pickle.load(file)

img_list=df.img.values
img_list[0]='https://www.openpr.com/wiki/images/642-400x300_4828'




# built_up_area = float(st.number_input('Built Up Area'))

servant_room = [0.0, 1.0]
store_room = [0.0, 1.0]

furnishing_type = sorted(df['furnishing_type'].unique().tolist())
luxury_category =sorted(df['luxury_category'].unique().tolist())
floor_category = sorted(df['floor_category'].unique().tolist())

# ================================================================================
with open('Jupiter_works/dataset/pipeline1.pkl','rb') as file:
    pipeline = pickle.load(file)




app=Flask(__name__)

status=False


@app.route('/')
def home():
    index_id=df['id'].values
    # index_img=df['img'].values
    index_price=df['price'].values
    index_sector=df['sector'].values
    index_area=df['built_up_area'].values
    index_bedroom=df['bedRoom']
    index_bathroom=df['bathroom'].values
    index_rate=np.round((10000000*df['price'])/df['built_up_area'],0).values
    n=df.shape[0]
    return render_template('index.html',img_list=img_list,n=n,index_area=index_area,index_id=index_id,index_bedroom=index_bedroom,index_price=index_price,index_sector=index_sector,index_rate=index_rate,index_bathroom=index_bathroom)






@app.route('/login')
def login(): 
    return render_template('login.html')
@app.route('/c_login' , methods=['GET','POST'])
def c_login():
    status=True   
    return  prediction()
@app.route('/signup')
def signup():
    return render_template('index.html')










@app.route('/prediction', methods=['POST'])
def redirect_page():
    img_link = request.form.get('button_value')
    return render_template('dastination.html',img_link=img_link,status=status)

@app.route('/regration_prediction',methods=['POST','GET'])
def regration_prediction():
    img_link="https://github.com/veer-debug/music/blob/main/pridict_image.jpg?raw=true"
    low=''
    high=''
    if request.method=='POST':
        property_type = request.form['property_type']
        sector =request.form['sector']
        bedrooms = float(request.form['bedrooms'])
        bathroom = float(request.form['bathroom'])
        balcony =request.form['balcony']
        property_age =request.form['property_age']
        built_up_area = float(request.form['barea'])
        servant_room = float(request.form['servant_room'])
        store_room = float(request.form['store_room'])
        furnishing_type = request.form['furnishing_type']
        luxury_category =request.form['luxury_category']
        floor_category = request.form['floor_category']

        data = [[property_type, sector, bedrooms, bathroom, balcony, property_age, built_up_area, servant_room, store_room, furnishing_type, luxury_category, floor_category]]
        columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

        # Convert to DataFrame
        user_df = pd.DataFrame(data, columns=columns)
        # predict
        base_price = np.round(np.expm1(pipeline.predict(user_df))[0],2)
        low =  np.round((base_price - 0.22),2)
        high = np.round((base_price + 0.22),2)

        # Pridected properties
        pred_df=df[((df['price']>=low) & (df['price']<=high))]
        index_id=pred_df['id'].values
        index_img=pred_df['img'].values
        index_price=pred_df['price'].values
        index_sector=pred_df['sector'].values
        index_area=pred_df['built_up_area'].values
        index_bedroom=pred_df['bedRoom'].values
        index_bathroom=pred_df['bathroom'].values
        index_rate=np.round((10000000*pred_df['price'])/pred_df['built_up_area'],0).values
        n=pred_df.shape[0]    
    return render_template('dastination.html',low=low,high=high,status=status,img_link=img_link,id=id,n=n,index_id=index_id,img_list=index_img,index_price=index_price,index_sector=index_sector,index_area=index_area,index_bedroom=index_bedroom,index_bathroom=index_bathroom,index_rate=index_rate)

@app.route('/prediction_form')
def prediction():
    id=df['id']
    property_type = ['flat','house']
    sector =sorted(df['sector'].unique().tolist())
    bedrooms = sorted(df['bedRoom'].unique().tolist())
    bathroom = sorted(df['bathroom'].unique().tolist())
    balcony =sorted(df['balcony'].unique().tolist())
    property_age =sorted(df['agePossession'].unique().tolist())

    return render_template('prediction_form.html',property_type=property_type,property_age=property_age,sector=sector,bathroom=bathroom,balcony=balcony,servant_room=servant_room,store_room=store_room,furnishing_type=furnishing_type,luxury_category=luxury_category,floor_category=floor_category,bedrooms=bedrooms)


@app.route('/recomendation',methods=['POST','GET'])
def recomendation():
    
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    itr=int(request.form['itr'])
    user_img=df['img'].values[itr]
    user_price=df['price'].values[itr]
    user_sector=df['sector'].values[itr]
    user_area=df['built_up_area'].values[itr]
    user_bedroom=df['bedRoom'].values[itr]
    user_bathroom=df['bathroom'].values[itr]
    user_rate=int((user_price*10000000)/user_area)
    
    return render_template('recomendation.html',user_img=user_img,user_id=itr,user_price=user_price,user_sector=user_sector,user_area=user_area,status=status,user_bathroom=user_bathroom,user_bedroom=user_bedroom,user_rate=user_rate)

@app.route('/contect')
def about():
    return render_template('contect.html')


app.run(debug=True)
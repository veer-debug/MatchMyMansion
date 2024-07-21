from flask import Flask ,render_template,request,redirect
import pandas as pd
import pickle
import numpy as np

# from login import User_othintaction
# from cart import Cart

# user_cart=Cart()
# user=User_othintaction()


# Load datasets


# with open('Jupiter_works/dataset/df.pkl','rb') as file:
#     df = pickle.load(file)
df=pd.read_csv('Jupiter_works/dataset/final_df.csv')

img_list=df.img.values
servant_room = [0.0, 1.0]
store_room = [0.0, 1.0]
furnishing_type = sorted(df['furnishing_type'].unique().tolist())
luxury_category =sorted(df['luxury_category'].unique().tolist())
floor_category = sorted(df['floor_category'].unique().tolist())

# ================================================================================
with open('Jupiter_works\dataset\pipeline1.pkl','rb') as file:
    pipeline = pickle.load(file)

status =True
# login1=True
user_name=None

# Recommendation function=============
with open('Jupiter_works/dataset/cosine_sim1.pkl','rb') as file:
    cosine_sim1 = pickle.load(file)
with open('Jupiter_works/dataset/cosine_sim2.pkl','rb') as file:
    cosine_sim2 = pickle.load(file)
with open('Jupiter_works/dataset/cosine_sim3.pkl','rb') as file:
    cosine_sim3 = pickle.load(file)

with open('Jupiter_works/dataset/Location.pkl','rb') as file:
    location_df = pickle.load(file)

def recommend_properties(property_name, top_n=5):
    
    cosine_sim_matrix = 0.5*cosine_sim1 + 0.8*cosine_sim2 + cosine_sim3
    # cosine_sim_matrix = cosine_sim3
    
    # Get the similarity scores for the property using its name as the index
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))
    
    # Sort properties based on the similarity scores
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the indices and scores of the top_n most similar properties
    top_indices = [i[0] for i in sorted_scores[1:top_n+1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n+1]]
    
    # Retrieve the names of the top properties using the indices
    top_properties = location_df.index[top_indices].tolist()
   
    return top_properties

app=Flask(__name__)

@app.route('/')
def home():
    global status
    global user_name
    index_id=df['id'].values
    # index_img=df['img'].values
    index_price=df['price'].values
    index_sector=df['sector'].values
    index_area=df['built_up_area'].values
    index_bedroom=df['bedRoom']
    index_bathroom=df['bathroom'].values
    index_rate=np.round((10000000*df['price'])/df['built_up_area'],0).values
    n=df.shape[0]
    return render_template('index.html',img_list=img_list,n=52,index_area=index_area,index_id=index_id,index_bedroom=index_bedroom,index_price=index_price,index_sector=index_sector,index_rate=index_rate,index_bathroom=index_bathroom,login=status,user=user_name,status=status)

# @app.route('/login')
# def login(): 
#     return render_template('login.html')
# @app.route('/c_login' , methods=['GET','POST'])
# def c_login():
#     global status
#     global user_name
#     u_name=request.form['u_name']
#     u_password=request.form.get('u_password')
#     check_log=user.login(u_name,u_password)
#     if check_log:
#         status = True
#         user_name=u_name
#         return home()
#     else:
#         return render_template('login.html',message="Invalid user Name or Password")
# @app.route('/sign-up',methods=['GET','POST'])
# def signup():
#     u_name=request.form['u_name']
#     u_email=request.form['u_email']
#     u_password=request.form['u_password']
#     check_user=user.signup(u_name,u_email,u_password)
#     if check_user:
#         return render_template('login.html',message="Signup Successfull !")
#     else:
#         return render_template('login.html',message="User alrady exist Please Login !")


# @app.route('/profile')
# def profile():
#     global user_name
#     user_list=user.profile(user_name)
#     u_name,u_email,u_password,u_date=user_list[1],user_list[2],user_list[3],user_list[4]
#     return render_template('profile.html',u_name=u_name,u_email=u_email,u_password=u_password,u_date=u_date)


@app.route('/logout')
def logout():
    global status
    status=False
   
    return home()

# @app.route('/add-to-cart',methods=['POST'])
# def aad_to_cart():
#     id=int(request.form['id'])
#     print(type(user_name))
#     user_cart.add_to_cart(username=user_name,product_id=id)
#     return cart()


# @app.route('/cart')
# def cart():
#     # index_id=df['id'].values
#     # # index_img=df['img'].values
#     # index_price=df['price'].values
#     # index_sector=df['sector'].values
#     # index_area=df['built_up_area'].values
#     # index_bedroom=df['bedRoom']
#     # index_bathroom=df['bathroom'].values
#     # index_rate=np.round((10000000*df['price'])/df['built_up_area'],0).values
#     # n=df.shape[0]
#     global status
#     index_id=user_cart.user_cart(user_name=user_name)
#     index_img=[]
#     index_price=[]
#     index_sector=[]
#     index_area=[]
#     index_bedroom=[]
#     index_bathroom=[]
#     index_rate=[]
#     for i in index_id:
#         index_img.append(df.img.values[i-1])
#         index_price.append(df.price.values[i-1])
#         index_sector.append(df.sector.values[i-1])
#         index_area.append(df.built_up_area.values[i-1])
#         index_bedroom.append(df.bedRoom.values[i-1])
#         index_bathroom.append(df.bathroom.values[i-1])
#         index_rate.append(np.round((10000000*df['price'].values[i])/df['built_up_area'].values[i],0))
#     n=len(index_id)

#     return render_template('cart.html',img_list=index_img,n=n,index_area=index_area,index_id=index_id,index_bedroom=index_bedroom,index_price=index_price,index_sector=index_sector,index_rate=index_rate,index_bathroom=index_bathroom,user=user_name,status=status)

@app.route('/prediction', methods=['POST'])
def redirect_page():
    global status
    img_link = request.form.get('button_value')
    return render_template('dastination.html',img_link=img_link,status=status,login=status)

@app.route('/regration_prediction',methods=['POST','GET'])
def regration_prediction():
    global status
    global user_name
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
    return render_template('dastination.html',low=low,high=high,status=status,img_link=img_link,id=id,n=n,index_id=index_id,img_list=index_img,index_price=index_price,index_sector=index_sector,index_area=index_area,index_bedroom=index_bedroom,index_bathroom=index_bathroom,index_rate=index_rate,login=status,user=user_name)

@app.route('/prediction_form')
def prediction():
    global status
    global user_name
    id=df['id']
    property_type = ['flat','house']
    sector =sorted(df['sector'].unique().tolist())
    bedrooms = sorted(df['bedRoom'].unique().tolist())
    bathroom = sorted(df['bathroom'].unique().tolist())
    balcony =sorted(df['balcony'].unique().tolist())
    property_age =sorted(df['agePossession'].unique().tolist())

    return render_template('prediction_form.html',property_type=property_type,property_age=property_age,sector=sector,bathroom=bathroom,balcony=balcony,servant_room=servant_room,store_room=store_room,furnishing_type=furnishing_type,luxury_category=luxury_category,floor_category=floor_category,bedrooms=bedrooms,login=status,user=user_name)


@app.route('/recomendation',methods=['POST','GET'])
def recomendation():
    global status
    global user_name
    
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    itr=int(request.form['itr'])
    user_img=df[df['id']==itr].img.values[0]
    user_price=df[df['id']==itr].price.values[0]
    user_sector=df[df['id']==itr].sector.values[0]
    user_area=df[df['id']==itr].built_up_area.values[0]
    user_bedroom=df[df['id']==itr].bedRoom.values[0]
    user_bathroom=df[df['id']==itr].bathroom.values[0]
    user_society=df[df['id']==itr].society.values[0]
    user_location=df[df['id']==itr].near_locatio.values[0]
    user_furnish=df[df['id']==itr].furnishing_type.values[0].title()
    user_propertyt=df[df['id']==itr].property_type.values[0].title()
    location =user_location.strip("{}").replace("'", "")
    user_rate=int((user_price*10000000)/user_area)
    

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # =================================
    socity=df[df['id']==itr].society.values[0]
    results=recommend_properties(socity)

    # result 1 
    r1=df[df['society']==results[0]]
    r1_socity=results[0]
    r1_id=r1['id'].values
    r1_img=r1['img'].values
    r1_price=r1['price'].values
    r1_sector=r1['sector'].values
    r1_area=r1['built_up_area'].values
    r1_bedroom=r1['bedRoom'].values
    r1_bathroom=r1['bathroom'].values
    r1_rate=np.round((10000000*r1['price'])/r1['built_up_area'],0).values
    r1_n=r1.shape[0]
    if r1.shape[0]>4:
       r1_n=4    


    # result 2
    r2=df[df['society']==results[1]]
    r2_socity=results[1]
    r2_id=r2['id'].values
    r2_img=r2['img'].values
    r2_price=r2['price'].values
    r2_sector=r2['sector'].values
    r2_area=r2['built_up_area'].values
    r2_bedroom=r2['bedRoom'].values
    r2_bathroom=r2['bathroom'].values
    r2_rate=np.round((10000000*r2['price'])/r2['built_up_area'],0).values
    r2_n=r2.shape[0]  
    if r2.shape[0]>4:
       r2_n=4

    # result 3
    r3=df[df['society']==results[2]]
    r3_socity=results[2]
    r3_id=r3['id'].values
    r3_img=r3['img'].values
    r3_price=r3['price'].values
    r3_sector=r3['sector'].values
    r3_area=r3['built_up_area'].values
    r3_bedroom=r3['bedRoom'].values
    r3_bathroom=r3['bathroom'].values
    r3_rate=np.round((10000000*r3['price'])/r3['built_up_area'],0).values
    r3_n=r3.shape[0] 
    if r3.shape[0]>4:
       r3_n=4

    # result 4
    r4=df[df['society']==results[3]]
    r4_socity=results[3]
    r4_id=r4['id'].values
    r4_img=r4['img'].values
    r4_price=r4['price'].values
    r4_sector=r4['sector'].values
    r4_area=r4['built_up_area'].values
    r4_bedroom=r4['bedRoom'].values
    r4_bathroom=r4['bathroom'].values
    r4_rate=np.round((10000000*r4['price'])/r4['built_up_area'],0).values
    r4_n=r4.shape[0] 
    if r4.shape[0]>4:
       r4_n=4

    # result 5
    r5=df[df['society']==results[4]]
    r5_socity=results[4]
    r5_id=r5['id'].values
    r5_img=r5['img'].values
    r5_price=r5['price'].values
    r5_sector=r5['sector'].values
    r5_area=r5['built_up_area'].values
    r5_bedroom=r5['bedRoom'].values
    r5_bathroom=r5['bathroom'].values
    r5_rate=np.round((10000000*r5['price'])/r5['built_up_area'],0).values
    r5_n=r5.shape[0]
    if r5.shape[0]>4:
       r5_n=4

    
    return render_template('recomendation.html',user_img=user_img,user_id=itr,user_price=user_price,user_sector=user_sector,user_propertyt=user_propertyt,user_area=user_area,status=status,user_bathroom=user_bathroom,user_bedroom=user_bedroom,user_rate=user_rate,user_furnish=user_furnish,login=status, r1_id=r1_id,r1_img=r1_img,r1_price=r1_price,r1_sector=r1_sector,r1_area=r1_area,r1_bedroom=r1_bedroom,r1_bathroom=r1_bathroom,r1_rate=r1_rate,r1_n=r1_n,r1_socity=r1_socity , r2_id=r2_id,r2_img=r2_img,r2_price=r2_price,r2_sector=r2_sector,r2_area=r2_area,r2_bedroom=r2_bedroom,r2_bathroom=r2_bathroom,r2_rate=r2_rate,r2_n=r2_n ,r2_socity=r2_socity, r3_id=r3_id,r3_img=r3_img,r3_price=r3_price,r3_sector=r3_sector,r3_area=r3_area,r3_bedroom=r3_bedroom,r3_bathroom=r3_bathroom,r3_rate=r3_rate,r3_n=r3_n ,r3_socity=r3_socity, r4_id=r4_id,r4_img=r4_img,r4_price=r4_price,r4_sector=r4_sector,r4_area=r4_area,r4_bedroom=r4_bedroom,r4_bathroom=r4_bathroom,r4_rate=r4_rate,r4_n=r4_n ,r4_socity=r4_socity, r5_id=r5_id,r5_img=r5_img,r5_price=r5_price,r5_sector=r5_sector,r5_area=r5_area,r5_bedroom=r5_bedroom,r5_bathroom=r5_bathroom,r5_rate=r5_rate,r5_n=r5_n,r5_socity=r5_socity,user=user_name,user_location=location,user_society=user_society)

@app.route('/stats', methods=['POST','GET'])
def stats():
    global status
    status=False
    itr=int(request.form['itr'])
    
    
    return render_template('states.html')
   
    



@app.route('/contect')
def about():
    global status
    global user_name
    return render_template('contect.html',login=status,user=user_name)


app.run(debug=True)
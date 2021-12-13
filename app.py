from flask import Flask, request, render_template
from firebase import firebase  
from flask import Response
import pickle


app = Flask(__name__)






model = pickle.load(open('model.sav', 'rb'))
cropl = ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas','mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate','banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple','orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']
p1 = [20, 11,  3,  9, 18, 13, 14,  2, 10, 19,  1, 12,  7, 21, 15,  0, 16, 17,  4,  6,  8,  5]

model2 = pickle.load(open('fert_pred.sav', 'rb'))
fertl = ['Urea', 'DAP', '14-35-14', '28-28', '17-17-17', '20-20','10-26-26']
p2 = [6, 5, 1, 4, 2, 3, 0]
cropmatterenglish = [ "All white rice starts to brown. White rice is just brown rice that's been rid of its outer bran layer and polished. Rice plants grow to a height of 3 to 4 feet over an average of 120 days after planting. During this time, farmers irrigate the rice fields using the method that best fits that field or farm.","Maize, also known as corn, is a cereal grain first domesticated by indigenous peoples in southern Mexico about 10,000 years ago. Maize can take from 60 to 100 days to reach harvest depending upon plant variety and the amount of heat during the growing season.","Eating Chickpeas Regularly Can Lower Your Bad Cholesterol. The chickpea or garbanzo bean is a cool-season annual that requires about 100 days to reach harvest.  ","Kidney beans are an excellent plant-based source of protein. These beans may aid weight loss, promote colon health, and moderate blood sugar levels. Kidney Beans are ready to harvest within about 100 to 140 days.","Pigeon peas are most nutritious and easy to digest in their green stage, just before they become dry and lose their color. Pigeon peas Plants will germinate in 10 to 15 days & pods will appear in 4 months.","Moth beans contain calcium which is the mineral vital for maintaining stronger bones and preventing the risk of osteoporosis. Moth beans take 75 to 90 days to mature, and they are frequently planted at the end of the rainy season.","The major health benefit of the mung beans or green gram is their rich source of cholesterol reducing fibre. Mung beans are a warm-season crop and take between 90-120 days to mature.","It is one of the important pulse crops grown throughout India. Generally it is consumed in the form of ‘Dal’. It is the chief constituent of ‘papad, idli and dosa’. It takes around 70-75 days duration & its production will be around 10-12 days.","Lentils are rich in fibre, folate and potassium making them a great choice for the heart and for managing blood pressure and cholesterol. Lentils require 80 to 110 days to come to harvest.","The word pomegranate means apple with many seeds. Pomegranates are native to the Middle East. They belong to the berry family & are classified as a super fruit. Pomegranate trees can take up to 7 months for their fruit to fully mature. The tree itself will only bear fruit after two to three years of hearty growth.","About 5.6 million hectares of land are used for banana production around the globe. Bananas generally take four to six months for fruit to reach full size after flowering, depending on temperature, variety, moisture and culture practices.","Mangos are also rich in vitamin C, which is important for forming blood vessels and healthy collagen, as well as helping you heal. A mango tree requires 5-8 years before it will bear fruit; a nursery sapling should produce fruit in about four years. The mango fruit takes three to five months to ripen after the tree has flowered.","A grape is still defined as a type of berry in botanical terms. This means that each fruit comes from a single flower on the grapevine. Grape plant begins to grow 10-15 days after planting. ","August 3 is National Watermelon Day, & throughout summer, the backyard mainstay is added to drinks and served as dessert at barbecues across the country. Watermelons require 80-90 days from seed sowing to grow a full-size watermelon. Some smaller-sized watermelons (like Sugar Baby) can reach maturity in closer to 70 days.","Muskmelon has high fiber and water content, which makes it a great natural healer for people suffering from indigestion, constipation, and other digestive system issues. Muskmelon fruits take 35 to 45 days to ripen after the flower has been pollinated.","Apples are 25'%' air. Apples float in water because a whopping 25'%' of their volume is actually air. Apples are less dense than water, making them the perfect fruit for apple bobbing. Standard or full-sized apple trees can grow up to 30 feet tall and can take six years to bear their first fruit.","Oranges are the largest citrus fruit in the world. Orange juice is the most popular fruit juice in America. It can take 3-5 years for an orange tree to produce fruit, depending on how old the tree is when purchasing. Once the tree finally begins producing fruit, they take 7 to 8 months to ripen.","The papaya is botanically a berry. It may look like it grows from a tree, but the papaya is actually the fruit of an herb. It takes 6-12 months to grow papaya from seed to fruit.","On average a coconut tree produces 30 fruits each year, but a tree can produce up to 75 coconuts per year with optimal weather conditions, which is rare. About 61 million tons of coconuts are produced each year. The coconut tree grows from a single seed, which is an entire coconut, taking between 3 and 8 years to bear fruit, and living between 60 and 100 years.","Cotton is one of the most important fiber and cash crops of India and plays a dominant role in the industrial and agricultural economy of the country. It provides the basic raw material (cotton fibre) to the cotton textile industry. Cotton is fully mature and ready for harvesting approximately 160 days after being planted. Once the bolls have burst open, the farmers can prepare the cotton plants for harvesting.","Jute is the second most important vegetable fiber after cotton due to its versatility. Jute is used chiefly to make cloth for wrapping bales of raw cotton, and to make sacks and coarse cloth.  To grow jute, farmers scatter the seeds on cultivated soil. When the plants are about 15–20 cm tall, they are thinned out. About 4 months after planting, harvesting begins.","Coffee is consumed in great quantities, it is the world’s 2nd largest traded commodity, surpassed only by crude oil. Depending on the variety, it will take approximately 3 to 4 years for the newly planted coffee trees to bear fruit."]
fertmatterenglish = ["Urea is a raw material used in the manufacture of many chemicals. It is also essential for making feedstock, glue, fertilizer, commercial products, and in resin production.With the enzyme urease, plus any small amount of soil moisture, urea normally hydrolyzes and converts to ammonium and carbon dioxide. This can occur in 2-4 days and happens more quickly on high pH soils.","DAP fertilizer is an excellent source of P and nitrogen (N) for plant nutrition. It is highly soluble and thus dissolves quickly in soil to release plant-available phosphate and ammonium. DAP is generally applied as a basal dose before sowing. The Earliest seed germination is not earlier than 6 days and roots are initiated.","14-35-14 is a complex fertilizer containing all major nutrients viz. Nitrogen, Phosphorus and Potassium. The only complex having highest total nutrient content among the NPK complex fertilizers. (Total nutrients are 63%).","28-28 is a complex fertilizer containing two major nutrients viz. Nitrogen and Phosphorus. This is the highest Nitrogen containing Complex fertilizer with 28%. 19% of Nitrogen is in Urea form and 9% is in Ammoniacal form. Ammonium Phosphate is coated over Urea prill, due to which the losses from Urea will be minimized. ","17:17:17 is a granulated NPK fertilizer. It contains primary nutrients such as Nitrogen, Phosphorus and Potash in equal proportion. Benefits: It fulfills the Major nutrient requirements for all crops.","20:20 is a chemical blend of 40 parts of Ammonium phosphate and 60 parts of Ammonium sulfate. It contains 20% N and 20% P2O5. The entire N is in ammoniacal form and P is completely water soluble.","10:26:26 contains Phosphorus and Potassium in the ratio of 1:1, the highest among the NPK fertilizers. It contains 7% Nitrogen in the Ammoniacal form, 22% out of 26% phosphate in the water soluble form and the entire 26% potash is available in the water soluble form."]
@app.route('/')
def home():
    return render_template('login.html')



def cropfertpred(cl,fl):
    prediction1 = model.predict([cl])
    output1 = round(prediction1[0], 2)
    crpn = cropl[p1.index(output1)] + ".jpg"
    prediction2 = model2.predict([fl])
    output2 = round(prediction2[0], 2)
    fern = fertl[p2.index(output2)] + ".jpg"
    ol1 = cropl.index(cropl[p1.index(output1)])
    ol2 = fertl.index(fertl[p2.index(output2)])
    return crpn, fern, cropl[p1.index(output1)], fertl[p2.index(output2)], ol1, ol2

@app.route('/table')
def table():
    firebase1 = firebase.FirebaseApplication('https://icps-9cc0a.firebaseio.com/', None)
    count_value = firebase1.get('/count/', '')
    nl=[]
    pl=[]
    kl=[]
    templ=[]
    huml=[]
    moistl=[]
    phl=[]
    lat=[]
    long1=[]
    dt = []
    for i in range(count_value['val'],count_value['val']-5,-1):
        result = firebase1.get('/cropnew/'+str(i), '')
        nl.append(result['n'])
        pl.append(result['p'])
        kl.append(result['k'])
        templ.append(result['temp'])
        huml.append(result['temp'])
        moistl.append(result['hum'])
        phl.append(result['ph'])
        lat.append(result['lat'])
        long1.append(result['long'])
        dt.append(result['dt'])

    print(nl,pl,kl,templ,huml,moistl,phl,lat,long1)
    cl = [nl[4],pl[4],kl[4],templ[4],huml[4],phl[4],71.4]
    fl = [templ[4], huml[4], moistl[4], nl[4],pl[4],kl[4], 9, 3]
    predv = cropfertpred(cl,fl)
    return render_template('rec.html',nl=nl,pl=pl,kl=kl,templ=templ,huml=huml,moistl=moistl,phl=phl, predv = predv, cropeng=cropmatterenglish,ferteng=fertmatterenglish, lat=lat[-1], long1=long1[-1],dt=dt )
@app.route('/predplot')
def predplot():
    td = [53.400000000000006, 94.75, 79.25, 20.0, 4.4, 107.55, 227.5, 115.39999999999999, 86.45, 105.10000000000001, 35.75, 98.35, 118.0, 68.3, 197.3, 40.35, 36.9, 31.349999999999998, 73.0, 102.6, 77.75, 16.400000000000002, 16.6, 101.44999999999999, 80.35, 102.1, 79.15, 90.15, 12.6, 133.45]
    td = sum(td)/30
    rd = sum([0.0,34.3,0.2,22.1,73.8,92.7,94.7,241.5,102.9,134.7,37.7,36.7,7.7,0.0,6.5,68.2,24.5,24.0,70.1,95.8,195.5,352.5,41.7,38.1,25.6,3.2,7.7,17.5,55.0,90.8,42.9,69.8,78.2,167.5,44.2,12.9,0.0,1.3,26.1,15.0,4.1,57.4,183.4,116.4,124.9,175.5,11.7,9.6,10.2,4.3,12.9,35.1,149.7,39.8,122.9,23.1,153.7,124.4,65.6,0.0,1.3,13.6,14.7,38.5,48.4,51.2,133.2,106.6,127.6,304.8,144.8,81.7,0.2,0.0,32.8,9.7,62.7,85.8,43.2,72.0,144.7,88.4,78.6,20.0,0.0,0.5,0.1,6.0,15.1,208.2,83.8,186.9,186.0,176.9,35.3,81.8,6.4,18.7,62.9,4.1,42.1,31.7,81.4,104.9,121.7,126.0,192.1,5.9,0.5,0.0,5.3,8.4,47.4,68.9,33.2,128.5,155.8,69.3,135.6,35.4,4.7,0.8,0.6,13.0,65.4,108.3,187.6,155.0,122.9,83.4,175.1,46.7,0.8,12.1,0.0,34.6,33.0,44.5,128.9,163.6,71.2,107.5,106.9,35.1,2.7,0.0,2.5,32.7,38.8,47.0,139.7,120.0,69.5,113.7,86.6,61.9,1.3,30.6,11.5,26.8,38.9,73.8,95.7,110.3,163.2,169.3,38.6,2.6,0.2,0.7,12.5,5.1,46.7,66.3,68.7,115.1,81.4,104.6,37.8,12.8,1.9,0.0,13.4,73.4,39.7,73.0,43.1,123.6,136.3,106.7,383.8,52.2,7.9,0.0,0.8,0.4,80.5,128.6,131.0,41.5,90.8,14.1,5.4,54.4,3.9,0.0,12.8,8.8,39.9,88.9,52.2,171.6,194.6,221.1,33.3,7.4])/30
    cd = [22.2, 77.1, 73.9, 66.75, 211.35, 63.0, 51.800000000000004, 55.15, 82.0, 84.85000000000001, 59.55, 65.6, 65.6, 21.1, 51.65, 9.6, 26.05, 60.349999999999994, 36.300000000000004, 57.55, 47.1, 56.699999999999996, 38.849999999999994, 50.85, 27.05, 85.8, 104.0, 147.25, 36.5, 40.2]
    cd = sum(cd)/30
    return render_template('rain.html',td=td, cd=cd, rd=rd)


@app.route('/loginto',methods=['POST'])
def loginto():
    features = [x for x in request.form.values()]
    usern = features[0]
    passw =features[1]
    if usern == "9014361324" and passw== "farmer123":
        return render_template('homemine.html')
    else:
        return render_template('login.html', prediction_text="Invalid username and password")





if __name__ == "__main__":
    app.run(debug=False)

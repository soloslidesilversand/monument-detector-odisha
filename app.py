from img_classification import teachable_machine_classification
import streamlit as st
from PIL import Image, ImageOps

st.header('Monuments of Odisha')
st.write("Explore the secret of odisha!")
uploaded_file = st.file_uploader("Select the image of monument", type=["jpg","png","jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Photo', use_column_width=True)
    st.write("")
    st.write("Detecting...")
    label = teachable_machine_classification(image, 'keras_model.h5')
    if label == 0:
        st.write("Ananta vasudev temple")
        st.write("Ananta Vasudev Temple is a Hindu temple located in Bhubaneswar, Odisha, India. The temple is dedicated to Lord Vishnu and is known for its exquisite architecture, especially the intricate carvings on its walls and pillars. The temple is a popular pilgrimage site and a significant cultural landmark of India.")
      
    if label == 1:
        st.write("Barabati fort")
        st.write("Barabati Fort is a historical fort located in Cuttack, a city in the state of Odisha, India. The fort was built in the 14th century by the Ganga dynasty rulers and was later renovated by the Maratha rulers. The fort is known for its architecture, especially the arched gateway and the moat surrounding it. It is now a popular tourist destination and a venue for cultural and sporting events.")
   
    if label == 2:
        st.write("konark sun temple")
        st.write("Sun Temple is a UNESCO World Heritage Site located in Konark, a town in the state of Odisha, India. The temple is dedicated to the Hindu Sun God, Surya. It was built in the 13th century and is known for its exquisite architecture, especially the intricately carved stone wheels that act as sundials. The temple is a popular tourist destination and a significant cultural landmark of India.")
        
    if label == 3:
        st.write("Sri jagganath puri temple")
        st.write("Jagannath Temple is a famous Hindu temple located in the coastal town of Puri in the state of Odisha, India. The temple is dedicated to Lord Jagannath, an incarnation of Lord Vishnu. The temple is known for its annual Rath Yatra festival, where the deities are taken out in a grand procession. The temple is a significant pilgrimage site and attracts a large number of devotees every year.")
        
    if label == 4:
        st.write("Dhauli")
        st.write("Dhauli is a hill located on the banks of the River Daya near Bhubaneswar, the capital city of Odisha, India. It is known for its historical significance as it was the site of the Kalinga War where Emperor Ashoka embraced Buddhism after witnessing the violence and bloodshed of the war. The hill now houses several Buddhist stupas and is a popular pilgrimage site for Buddhists and a tourist destination.")
  
    if label == 5:
        st.write("Khandagiri and udayagiri caves")
        st.write("Also known as Cuttack caves, Khandagiri Caves are artificial caves located in the state of Orissa which date back to 2nd century. This place is quite a sight to see with all the beautifully carved inscriptions and figures. This place holds a great historical significance. A large number of ancient temples with intricate carvings surround this place which have their own significance.")
    
    if label == 6:
        st.write("Rajarani temple")
        st.write("Rajarani Temple is a Hindu temple located in Bhubaneswar, Odisha, India. The temple is known for its architectural style, which is a blend of various schools of architecture. The temple is named after the red sandstone used to build it and is a popular tourist destination, especially among history and architecture enthusiasts.")

    if label == 7:
        st.write("Lingaraj temple")
        st.write("Lingaraj Temple is a Hindu temple located in Bhubaneswar, Odisha, India. The temple is dedicated to Lord Shiva and is known for its architectural beauty, especially the 150-foot high tower. The temple is a significant pilgrimage site and attracts a large number of devotees every year.")
      

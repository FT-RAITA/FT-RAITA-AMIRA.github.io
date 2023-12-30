from PIL import Image
import streamlit as st

st.set_page_config(page_title="My Webpage", page_icon = ":tada:", layout='wide')

st.subheader("Hi my LOBE Amira    :wave:")
st.title("So, 20? huh ? HAPPY BIRTHDAY MY BEAUTIFUL SWEETHEART JE AMAR SHOB COMPLIMENT E JUST CHI CHI KORE!!  <*sad face*>")

image1 = Image.open("images/amirapic.jpg")
image = image1.resize((500,500))
st.image(image, caption= "A LIVING PANDA BUT A VERY BEAUTIFUL ONE")

st.subheader("So what is your birthday present? well it is this website. yes you heard it right. I made this website just for you. I had to learn a lot and watch tutorials.Btw ei website tomar e , ami source code diye diboni")
st.write("I know eita bolle tumi amake believe korbe na, but I love you i really do (tor ja issa tai mone kor idc.) and I want to to smile for ever")
st.write("Beleive me you smile is the most beautiful thing in this world. can make anyone dead (you are dangerous too)")
st.write("[This song describe what i feel for you >](https://youtu.be/RE87rQkXdNw?si=AXGRKj6kjiGBPd9f)")
st.title("ONCE AGAIN HAPPY BIRTHDAY TO YOU AMIRA! YOU ARE MEAN BUT SWEET TOO")
st.write("And I am sorry too if i hurt you in any way or maybe in future")
st.write("after all flirtings, you will be like the song below")
st.write("[This song is your reaction >](https://youtu.be/k5TRnHHQ57U?si=qZ6ZzmAnXN94IPBU)")
st.subheader("From a friend")
fri_img = Image.open("images2/fr.jpg")
st.image(fri_img, caption = "I am more cute than you lol" )
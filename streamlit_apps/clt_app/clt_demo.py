import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


st.title('Illustrating the Central Limit Theorem with Streamlit')
st.subheader('An app by Stijn Servaes')
st.write(('This app simulates a thousand coin flips, using the chance of heads input below,'
'and then samples with replacement from that population and plots the histogram of'
' means of the samples, in order to illustrate the Central Limit Theroem.'))
perc_heads = st.number_input(label = 'Chance of Coins Landing on Heads', min_value = 0.0, max_value = 1.0, value = 0.5)
graph_title = 'Graph Title'
graph_title = st.text_input(label='Graph Title', placeholder = 'Graph Title')
binom_dist = np.random.binomial(1, perc_heads, 100)

list_of_means = []
for i in range(0,1000):
    list_of_means.append(np.random.choice(binom_dist, 100, replace = True).mean())

fig1,ax1 = plt.subplots()
ax1 = plt.hist(list_of_means)
plt.title(graph_title)
st.pyplot(fig1)
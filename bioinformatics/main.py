import streamlit as st
import yfinance as yf
import pandas as pd
from PIL import Image
import altair as alt

#new_image = pd.read_csv('raw_data22.csv')

#new = Image.open(new_image)

image = Image.open('dna.jpg')

st.image(image , use_column_width = True)


st.write("""
# DNA Nucleotide Count Web App
This app counts the nucleotide composition of query DNA!
***
""")

st.header('Enter DNA sequences')

dna_input = ">Dna Query \n CTACTCCATGGGTCTTCGGCTTGACCCGGTCTGTTGGGCCGCGATTGCGTGAGTTTCGGCCCCGCGCTGCGCTGTATAGTC \n GATTCTCATCCGGCCCTCACATCTGGAAACCCCAACTTATTTAGATAACATCATTAGCCGAAGTT \n GCTGGGCATGTCCACCGTGGAGTCCTCCCCGGGC \n GTCCCTCCTTCAAATGACGATAAGCACCGGCAAGCACCATTGATCAAC \n GCAAGGATCGGTGATGTTAACAAAGATTCGGCACATTACT \n CTTGTTGGTGTGGAATCGCTTAACTACGCGGCGAAGCCTTATGGCAAAACCGATGGGGAATGA \n TTCGGGTAGCGCTAAAAGTCCATAGCACGTACATCCCAACCTGGCGTGCGTACAGTTTGACGACC"


dna = st.text_area("Sequence Input" , dna_input , height = 250)
dna = dna.split()
dna = dna[2:]
dna = ''.join(dna)

st.write("""
***
""")


st.subheader("1) Information about your nucleodite composition in a dictionary form")

def dictionary_count(data):
    d = dict([
        ('A' , data.count('A')), 
        ('T' , data.count('T')),
        ('G' , data.count('G')),
        ('C' , data.count('C'))
    ])
    return d

X = dictionary_count(dna)

X



st.subheader("2) Information about your nucleodite composition in a text form")
st.write('There are  ' + str(X['A']) + ' adenine (A) in your DNA')
st.write('There are  ' + str(X['T']) + ' thymine (T) in your DNA')
st.write('There are  ' + str(X['G']) + ' guanine (G) in your DNA')
st.write('There are  ' + str(X['C']) + ' cytosine (C) in your DNA')


st.subheader("3) Information about your nucleodite composition in a tabular form")
df = pd.DataFrame.from_dict(X , orient = 'index')
df = df.rename({0:'count'} , axis='columns')
df.reset_index(inplace = True)
df = df.rename(columns = {'index' : 'nucleodite'})
st.write(df)



st.subheader("4) Information about your nucleodite composition in a graphical form")
p = alt.Chart(df).mark_bar().encode(
    x= 'nucleodite' , 
    y= 'count' , 
)

p = p.properties(
    width = alt.Step(80)
)
st.write(p)
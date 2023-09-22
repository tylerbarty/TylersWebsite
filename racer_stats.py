import streamlit as st
import pandas as pd

st.markdown("# Racer Page 🎈")
st.sidebar.markdown("# This is Racer Page 🎈")
st.write(' # Mariokart *Stats Website*')
st.write('MarioKart *Stats Website*')
df_racer = pd.read_csv('data/racer_stats.csv')
st.write(df_racer)
st.dataframe(df_racer.style
.highlight_max(color='lightgreen', axis=0,subset=['Speed','Acceleration','Weight'])
.highlight_min(color='red', axis=0,subset=['Speed','Acceleration','Weight'] )
)
st.line_chart(df_racer,x='Speed',y=['Acceleration','Weight','Handling','Traction/Grip','Mini-Turbo'])

st.header("Racer Speed doesn't seem to correlate to number of races they win")
x = st.slider('How Many Racers to Show',1,len(df_racer))
st.write("Racers by Speed")
df_fastest_Racers = df_racer[['Character','Speed']].sort_values("Speed",ascending=False).iloc[0:x]
st.dataframe(df_fastest_Racers)
character_dictionary = {'Mario' : 'Crowd favorite', 'Luigi' : 'Just a Green Mario'}


left_column_1, right_column_1 = st.columns(2)
with left_column_1:
    st.write("Racers by Speed")
    df_fastest_Racers = df_racer[['Character','Speed']].sort_values("Speed",ascending=False).iloc[0:x]
    st.dataframe(df_fastest_Racers)
with right_column_1:
    # Bring in Variable Table for percent won
    st.write("Racers by Win Percent")
    df_best = df_racer[['Character','Times First Place','Total Races']]
    df_best['Win Percent'] = df_best['Times First Place'] / df_best['Total Races'] * 100
    df_best = df_best[['Character', 'Win Percent']].sort_values('Win Percent',ascending=False).iloc[0:x]
    st.dataframe(df_best)

st.header("Individual Racer Stats")

left_column_2, right_column_2 = st.columns(2)

chosen = st.selectbox('Pick a Character', df_racer['Character'])
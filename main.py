import datetime
import streamlit as st

st.set_page_config(page_title="Kid's-Clock", page_icon=":smiley:", layout="wide")

gmt_time = datetime.datetime.utcnow() + datetime.timedelta(hours=0)
GMT_time = gmt_time.strftime('%Y-%m-%d %H:%M:%S')

Tehran_time = gmt_time + datetime.timedelta(hours=3.5)
Tehran_Date = Tehran_time.strftime('%A')
Tehran_time = Tehran_time.strftime('%H:%M:%S')

SanJose_time = gmt_time + datetime.timedelta(hours=-7)
SanJose_Date = SanJose_time.strftime('%A')
SanJose_time = SanJose_time.strftime('%H:%M:%S')

Rotterdam_time = gmt_time + datetime.timedelta(hours=2)
Rotterdam_Date = Rotterdam_time.strftime('%A')
Rotterdam_time = Rotterdam_time.strftime('%H:%M:%S')

Belfast_time = gmt_time + datetime.timedelta(hours=1)
Belfast_Date = Belfast_time.strftime('%A')
Belfast_time = Belfast_time.strftime('%H:%M:%S')

Auckland_time = gmt_time + datetime.timedelta(hours=12)
Auckland_Date = Auckland_time.strftime('%A')
Auckland_time = Auckland_time.strftime('%H:%M:%S')

col1, col2, col3, col4, col5 = st.columns(5)


with col1:
    st.image('images/MhmdRezaKetab.jpg')
    st.write("### San Jose")
    st.write("## " + SanJose_Date)
    st.write("# " + SanJose_time)

with col2:
    st.image('images/Sina.jpg')
    st.write("### Belfast")
    st.write("## " + Belfast_Date)
    st.write("# " + Belfast_time)

with col3:
    st.image('images/MhmdRamezani.jpg')
    st.write("### Rotterdam")
    st.write("## " + Rotterdam_Date)
    st.write("# " + Rotterdam_time)

with col4:
    st.image('images/Mehdi.png')
    st.write("### Tehran")
    st.write("## " + Tehran_Date)
    st.write("# " + Tehran_time)

with col5:
    st.image('images/Ali.jpg')
    st.write("### Auckland")
    st.write("## " + Auckland_Date)
    st.write("# " + Auckland_time)



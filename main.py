import datetime
import streamlit as st
import time

st.set_page_config(page_title="Kid's-Clock", page_icon=":smiley:", layout="wide")


st.markdown(
    """
    <style>
    .centered-text {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='centered-text'>Kid's Clock</h1>", unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:

    st.image('images/MhmdRezaKetab.jpg')
    st.write("### San Jose")
    sanJoseDate = st.empty()
    sanJoseClock = st.empty()

with col2:
    st.image('images/Sina.jpg')
    st.write("### Belfast")
    BelfastDate = st.empty()
    BelfastTime = st.empty()

with col3:
    st.image('images/MhmdRamezani.jpg')
    st.write("### Rotterdam")
    RotterdamDate = st.empty()
    RotterdamTime = st.empty()

with col4:
    st.image('images/Mehdi.png')
    st.write("### Tehran")
    TehranDate = st.empty()
    TehranTime = st.empty()

with col5:
    st.image('images/Ali.jpg')
    st.write("### Auckland")
    AucklandDate = st.empty()
    AucklandTime = st.empty()

while True:
    gmt_time = datetime.datetime.utcnow() + datetime.timedelta(hours=0)

    SanJose_time = gmt_time + datetime.timedelta(hours=-7)
    SanJose_Date = SanJose_time.strftime('%A')
    SanJose_Time = SanJose_time.strftime('%H:%M:%S')

    sanJoseDate.write("## " + SanJose_Date)
    sanJoseClock.title(SanJose_Time)

    Belfast_time = gmt_time + datetime.timedelta(hours=1)
    Belfast_Date = Belfast_time.strftime('%A')
    Belfast_time = Belfast_time.strftime('%H:%M:%S')

    BelfastDate.write("## " + Belfast_Date)
    BelfastTime.title(Belfast_time)

    Rotterdam_time = gmt_time + datetime.timedelta(hours=2)
    Rotterdam_Date = Rotterdam_time.strftime('%A')
    Rotterdam_time = Rotterdam_time.strftime('%H:%M:%S')

    RotterdamDate.write("## " + Rotterdam_Date)
    RotterdamTime.title(Rotterdam_time)

    Tehran_time = gmt_time + datetime.timedelta(hours=3.5)
    Tehran_Date = Tehran_time.strftime('%A')
    Tehran_Time = Tehran_time.strftime('%H:%M:%S')

    TehranDate.write("## " + Tehran_Date)
    TehranTime.title(Tehran_Time)

    Auckland_time = gmt_time + datetime.timedelta(hours=12)
    Auckland_Date = Auckland_time.strftime('%A')
    Auckland_time = Auckland_time.strftime('%H:%M:%S')

    AucklandDate.write("## " + Auckland_Date)
    AucklandTime.title(Auckland_time)

    time.sleep(1)

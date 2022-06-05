import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(layout='wide')
placeholder = st.empty()
shoppers = pd.read_csv('data/online_shoppers_intention.csv')


st.sidebar.subheader('📄 데이터셋 설명')
selected = st.sidebar.radio('데이터프레임 출력', ['데이터 보기', '데이터 닫기'], index=1)
if selected == '데이터 보기':
    st.subheader('데이터프레임 데이터 보기')
    st.write(shoppers)
elif selected == '데이터 닫기':
    st.write('')

emt = st.empty()
bt_clicked = st.sidebar.button('각 컬럼 상세 설명')
bt_cnt = 1
if bt_clicked:
    if bt_cnt == 1 :
        st.write(bt_cnt)
        st.subheader('데이터셋 컬럼 설명')
        st.write('''
    * 방문자가 해당 세션에서 방문한 다양한 유형의 페이지 수와 총 시간 표시
        * Administrative : 관리
        * Administrative_Duration : 관리 기간
        * Informational : 정보
        * Informational_Duration : 정보 기간
        * ProductRelated : 제품 관련
        * ProductRelated_Duration : 제품 관련 기간
    * BountceRates : 해당 페이지에서 사이트에 들어간 다음 해당 세션 동안 분석 서버에 대한 다른 요청을 트리거하지 않고 떠나는(바운스) 방문자의 비율
    * ExitRates : 세션에서 마지막이었던 비율
    * PageValues : 사용자가 전자상거래를 완료하기 전에 방문한 웹 페이지의 평균 값
    * Special Day : 거래로 세션이 종료될 가능성이 높은 특별한 날(예:발렌타인 데이)과 가까운 날짜에 0이 아닌 값을 취하며 최대값은 1
    * Month : 월 
    * 웹사이트를 방문하는데 사용되는 다양한 운영체제, 브라우저, 지역 및 트래픽 유형 방문자
        * OperatingSystems : 운영체제
            * 1 : IOS
            * 2 : Android Mobile
            * 3 : Windows
            * 4 : Linux
            * 5 : MS-DOS
            * 6 : Fedora
            * 7 : Ubuntu
            * 8 : Solaris
        * Browser : 브라우저
            * 1 : Firefox
            * 2 : Google Chrome
            * 3 : Microsoft Edge
            * 4 : Apple Safari
            * 5 : Opera
            * 6 : Brave
            * 7 : UCBrowser
            * 8 : DuckDuckgo
            * 9 : Chromium
            * 10 : Epic
            * 11 : Internet  Explorer
            * 12 : Tor Browser
            * 13 : Maxthon
        * Region : 지역
            * 1 : China
            * 2 : Indonesia
            * 3 : India
            * 4 : United States
            * 5 : Brazil
            * 6 : Nigeria
            * 7 : Japan
            * 8 : Russia
            * 9 : Bangladesh
        * TrafficType : 트래픽 유형
    * VisitorType : 고객이 재방문인지 신규 방문자인지 여부
    * Weekend : 방문 날짜가 다음인지 여부를 나타내는 부울 값, 주말
    * Revenue : 수익을 낼 수 있는지 여부를 나타내는 클래스
    ''')
        bt_cnt = 0
        st.write(bt_cnt)
        placeholder.empty()
    if bt_cnt == 0 :
        st.write('')
        

st.sidebar.subheader('📊 데이터 분석')
def rename_visitor_info() : 
    shoppers.loc[shoppers['OperatingSystems'] == 1,'OperatingSystems'] = 'IOS'
    shoppers.loc[shoppers['OperatingSystems'] == 2,'OperatingSystems'] = 'Android Mobile'
    shoppers.loc[shoppers['OperatingSystems'] == 3,'OperatingSystems'] = 'Windows'
    shoppers.loc[shoppers['OperatingSystems'] == 4,'OperatingSystems'] = 'Linux'
    shoppers.loc[shoppers['OperatingSystems'] == 5,'OperatingSystems'] = 'MS-DOS'
    shoppers.loc[shoppers['OperatingSystems'] == 6,'OperatingSystems'] = 'Fedora'
    shoppers.loc[shoppers['OperatingSystems'] == 7,'OperatingSystems'] = 'Ubuntu'
    shoppers.loc[shoppers['OperatingSystems'] == 8,'OperatingSystems'] ='Solaris'

    shoppers.loc[shoppers['Browser'] == 1,'Browser'] = 'Firefox'
    shoppers.loc[shoppers['Browser'] == 2,'Browser'] = 'Google Chrome'
    shoppers.loc[shoppers['Browser'] == 3,'Browser'] = 'Microsoft Edge'
    shoppers.loc[shoppers['Browser'] == 4,'Browser'] = 'Apple Safari'
    shoppers.loc[shoppers['Browser'] == 5,'Browser'] = 'Opera'
    shoppers.loc[shoppers['Browser'] == 6,'Browser'] = 'Brave'
    shoppers.loc[shoppers['Browser'] == 7,'Browser'] = 'UCBrowser'
    shoppers.loc[shoppers['Browser'] == 8,'Browser'] = 'DuckDuckgo'
    shoppers.loc[shoppers['Browser'] == 9,'Browser'] = 'Chromium'
    shoppers.loc[shoppers['Browser'] == 10,'Browser'] = 'Epic'
    shoppers.loc[shoppers['Browser'] == 11,'Browser'] = 'Internet Explorer'
    shoppers.loc[shoppers['Browser'] == 12,'Browser'] = 'Tor Browser'
    shoppers.loc[shoppers['Browser'] == 13,'Browser'] = 'Maxthon'

    shoppers.loc[shoppers['Region'] == 1,'Region'] = 'China'
    shoppers.loc[shoppers['Region'] == 2,'Region'] = 'Indonesia'
    shoppers.loc[shoppers['Region'] == 3,'Region'] = 'India'
    shoppers.loc[shoppers['Region'] == 4,'Region'] = 'United States'
    shoppers.loc[shoppers['Region'] == 5,'Region'] = 'Brazil'
    shoppers.loc[shoppers['Region'] == 6,'Region'] = 'Nigeria'
    shoppers.loc[shoppers['Region'] == 7,'Region'] = 'Japan'
    shoppers.loc[shoppers['Region'] == 8,'Region'] = 'Russia'
    shoppers.loc[shoppers['Region'] == 9,'Region'] = 'Bangladesh'

m_selected = st.sidebar.multiselect('방문자 정보 차트보기', ['OperatingSystems','Browser', 'Region', 'TrafficType'])
rename_visitor_info()
m_selected_index_cnt = 1
if len(m_selected) > 0 :
    fig = plt.figure(figsize=(8,2))
    for x in m_selected :
        plt.subplot(1,len(m_selected), m_selected_index_cnt)
        shoppers[x].value_counts().plot.bar()
        plt.title(x)
        m_selected_index_cnt += 1
    st.pyplot(fig)


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(layout='wide')
shoppers = pd.read_csv('data/online_shoppers_intention.csv')


st.sidebar.subheader('📄 데이터셋 설명')
selected = st.sidebar.radio('데이터프레임 출력', ['데이터 보기', '데이터 닫기'], index=1)
if selected == '데이터 보기':
    st.subheader('데이터프레임 데이터 보기')
    st.write(shoppers)
elif selected == '데이터 닫기':
    pass

bt_col_detail_clicked = st.sidebar.button('각 컬럼 상세 설명')
if bt_col_detail_clicked:
    st.subheader('데이터셋 컬럼 설명')
    st.write('''
* 방문자가 해당 세션에서 방문한 다양한 유형의 페이지 수와 총 시간 표시
    * Administrative : 사용자가 방문한 관리 유형의 페이지 수
    * Administrative_Duration : 관리 범주의 페이지에 머문 시간
    * Informational : 사용자가 방문한 정보 유형의 페이지 수
    * Informational_Duration : 정보 범주의 페이지에 머문 시간
    * ProductRelated : 사용자가 방문한 제품 관련 유형의 페이지 수
    * ProductRelated_Duration : 제품 관련 범주의 페이지에 머문 시간
* BountceRates : 웹 사이트에 들어갔다가 추가 작업을 하지 않고 종료하는 방문자의 비율
* ExitRates : 특정 페이지에서 세션이 마지막이었던 비율
* PageValues : 사용자가 전자상거래를 완료하기 전에 방문한 웹 페이지의 평균 값
* Special Day : 특별한 날 또는 공휴일에 대한 날짜의 근접성 (0~1)
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


st.sidebar.subheader('📊 데이터 분석')
def rename_visitor_info() : 
    visit_env_df = shoppers.iloc[ : , -7:-3 ]
    visit_env_df.loc[visit_env_df['OperatingSystems'] == 1,'OperatingSystems'] = 'IOS'
    visit_env_df.loc[visit_env_df['OperatingSystems'] == 2,'OperatingSystems'] = 'Android Mobile'
    visit_env_df.loc[visit_env_df['OperatingSystems'] == 3,'OperatingSystems'] = 'Windows'
    visit_env_df.loc[visit_env_df['OperatingSystems'] == 4,'OperatingSystems'] = 'Linux'
    visit_env_df.loc[visit_env_df['OperatingSystems'] == 5,'OperatingSystems'] = 'MS-DOS'
    visit_env_df.loc[visit_env_df['OperatingSystems'] == 6,'OperatingSystems'] = 'Fedora'
    visit_env_df.loc[visit_env_df['OperatingSystems'] == 7,'OperatingSystems'] = 'Ubuntu'
    visit_env_df.loc[visit_env_df['OperatingSystems'] == 8,'OperatingSystems'] ='Solaris'

    visit_env_df.loc[visit_env_df['Browser'] == 1,'Browser'] = 'Firefox'
    visit_env_df.loc[visit_env_df['Browser'] == 2,'Browser'] = 'Google Chrome'
    visit_env_df.loc[visit_env_df['Browser'] == 3,'Browser'] = 'Microsoft Edge'
    visit_env_df.loc[visit_env_df['Browser'] == 4,'Browser'] = 'Apple Safari'
    visit_env_df.loc[visit_env_df['Browser'] == 5,'Browser'] = 'Opera'
    visit_env_df.loc[visit_env_df['Browser'] == 6,'Browser'] = 'Brave'
    visit_env_df.loc[visit_env_df['Browser'] == 7,'Browser'] = 'UCBrowser'
    visit_env_df.loc[visit_env_df['Browser'] == 8,'Browser'] = 'DuckDuckgo'
    visit_env_df.loc[visit_env_df['Browser'] == 9,'Browser'] = 'Chromium'
    visit_env_df.loc[visit_env_df['Browser'] == 10,'Browser'] = 'Epic'
    visit_env_df.loc[visit_env_df['Browser'] == 11,'Browser'] = 'Internet Explorer'
    visit_env_df.loc[visit_env_df['Browser'] == 12,'Browser'] = 'Tor Browser'
    visit_env_df.loc[visit_env_df['Browser'] == 13,'Browser'] = 'Maxthon'

    visit_env_df.loc[visit_env_df['Region'] == 1,'Region'] = 'China'
    visit_env_df.loc[visit_env_df['Region'] == 2,'Region'] = 'Indonesia'
    visit_env_df.loc[visit_env_df['Region'] == 3,'Region'] = 'India'
    visit_env_df.loc[visit_env_df['Region'] == 4,'Region'] = 'United States'
    visit_env_df.loc[visit_env_df['Region'] == 5,'Region'] = 'Brazil'
    visit_env_df.loc[visit_env_df['Region'] == 6,'Region'] = 'Nigeria'
    visit_env_df.loc[visit_env_df['Region'] == 7,'Region'] = 'Japan'
    visit_env_df.loc[visit_env_df['Region'] == 8,'Region'] = 'Russia'
    visit_env_df.loc[visit_env_df['Region'] == 9,'Region'] = 'Bangladesh'
    return visit_env_df


if st.sidebar.button('각 컬럼별 수치 차트 보기') :
    for x in shoppers.columns :
        fig = plt.figure()
        sns.countplot(x=shoppers[x])
        st.pyplot(fig)

m_selected = st.sidebar.multiselect('방문자 접속 환경 정보 차트보기', ['OperatingSystems','Browser', 'Region', 'TrafficType'])

m_selected_index_cnt = 1
if len(m_selected) > 0 :
    visit_env_df = rename_visitor_info()
    fig = plt.figure(figsize=(8,2))
    for x in m_selected :
        plt.subplot(1,len(m_selected), m_selected_index_cnt)
        sns.countplot(x = visit_env_df[x], order=visit_env_df[x].value_counts().index)
        plt.xticks(rotation=90)
        #visit_env_df[x].value_counts().plot.bar()
        plt.title(x)
        m_selected_index_cnt += 1
    st.pyplot(fig)


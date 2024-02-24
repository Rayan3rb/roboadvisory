import pandas as pd
import yfinance as yf
import numpy as np
import streamlit as st
from data import grey_line

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Amiri&display=swap');

    .intro {
        font-family: 'Amiri', serif;
        text-align: center;
        color: #333;
    }

    .intro p {
        font-size: 24px; /* Adjust the size as needed */
    }
    </style>
    <div class="intro">
        <p><strong>استثمر بوعيّ</strong></p>
        <p>تم صنع الأداة لمساعدتك في اتخاذ قرارك الاستثماري بشكل أفضل من خلال مقارنة بين مقدمي خدمات المستشارين الآلي في المملكة العربية السعودية تقوم الأداة بمحاكاة أداء المحافظ لكل شركة بناءً على أسعار الصناديق المختارة من قبل كل محفظة</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #335575;'>🌀<a href='https://twitter.com/RayanArab7' target='_blank'>ريان عرب</a></p>", unsafe_allow_html=True)
custom_css = """
    <style>
        .stButton {
            display: flex;
            justify-content: center;
        }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)


if st.button("ابدأ المقارنة"):
    trading_days = 252

    from data import tamra
    from data import malaa
    from data import abyan
    st.markdown("<p style=\"text-align: center; color: #8B0000; font-family: 'Amiri', serif; font-size: 16px;\">تنويه:تاريخ البداية في المقارنة هو بداية عام 2023 وتتحدث البيانات يوميا</p>", unsafe_allow_html=True)
    
    st.markdown(grey_line, unsafe_allow_html=True)    

    st.markdown("<p style=\"text-align: right; color: #5C7791; font-family: 'Amiri', serif; font-size: 20px;\">تحليل أداء محافظ تمرة المالية</p>", unsafe_allow_html=True)
    st.markdown("<p style=\"text-align: right; color: #335575; font-family: 'Amiri', serif; font-size: 18px;\">اذا استثمرت في بداية عام 2023  <b>ريال 10,000</b>💸 في محافظ تمرة المالية</p>", unsafe_allow_html=True)
    st.line_chart(tamra)
    tamra_mp = np.round(tamra.iloc[-1],2)
    tamrahp_return = np.round((tamra.iloc[-1]/tamra.iloc[0]-1)*100,2)
    tamrahp_return2023 = np.round((tamra.loc[tamra[tamra.index.year == 2023].index.max()]/tamra.iloc[0]-1)*100,2)
    tamrahp_return2024 = np.round((tamra.loc[tamra[tamra.index.year == 2024].index.max()]/tamra.loc[tamra[tamra.index.year == 2023].index.max()]-1)*100,2)
    tamrageometric_mean = np.round((((np.prod(1 + tamra.pct_change()))**(trading_days/len(tamra.pct_change()))) - 1)*100,4)
    tamrastandard_deviation = np.round(tamra.pct_change().std()* np.sqrt(trading_days)*100,4)
    tamrabeta = tamra.pct_change().corr()['S&P500']
    tamrametrics = pd.concat([tamra_mp,tamrahp_return,tamrageometric_mean,tamrastandard_deviation,tamrabeta, tamrahp_return2023,tamrahp_return2024],axis=1)
    tamrametrics.columns = ["القيمة السوقية","عائد الاستثمار%", 'المتوسط الهندسي%', 'الانحراف المعياري%','بيتا',"2023 عائد الاستثمار%","2024 عائد الاستثمار%",]
    st.write(tamrametrics)

    st.markdown(grey_line, unsafe_allow_html=True)
    
    st.markdown("<p style=\"text-align: right; color: #5C7791; font-family: 'Amiri', serif; font-size: 20px;\">تحليل أداء محافظ  ملاءة التقنية</p>", unsafe_allow_html=True)
    st.markdown("<p style=\"text-align: right; color: #335575; font-family: 'Amiri', serif; font-size: 18px;\">اذا استثمرت في بداية عام 2023  <b>ريال 10,000</b>💸 في محافظ ملاءة التقنية</p>", unsafe_allow_html=True)
    st.line_chart(malaa)
    malaa_mp = np.round(malaa.iloc[-1],2)
    malaahp_return = np.round((malaa.iloc[-1]/malaa.iloc[0]-1)*100,2)
    malaahp_return2023 = np.round((malaa.loc[malaa[malaa.index.year == 2023].index.max()]/malaa.iloc[0]-1)*100,2)
    malaahp_return2024 = np.round((malaa.loc[malaa[malaa.index.year == 2024].index.max()]/malaa.loc[malaa[malaa.index.year == 2023].index.max()]-1)*100,2)    
    malaageometric_mean = np.round((((np.prod(1 + malaa.pct_change()))**(trading_days/len(malaa.pct_change()))) - 1)*100,4)
    malaastandard_deviation = np.round(malaa.pct_change().std()* np.sqrt(trading_days)*100,4)
    malaabeta = malaa.pct_change().corr()['S&P500']
    malaametrics = pd.concat([malaa_mp,malaahp_return,malaageometric_mean,malaastandard_deviation,malaabeta,malaahp_return2023,malaahp_return2024],axis=1)
    malaametrics.columns = ["القيمة السوقية","عائد الاستثمار%", 'المتوسط الهندسي%', 'الانحراف المعياري%','بيتا',"2023 عائد الاستثمار%","2024 عائد الاستثمار%",]
    st.write(malaametrics)

    st.markdown(grey_line, unsafe_allow_html=True)

    st.markdown("<p style=\"text-align: right; color: #5C7791; font-family: 'Amiri', serif; font-size: 20px;\">تحليل أداء محافظ ابيان المالية</p>", unsafe_allow_html=True)
    st.markdown("<p style=\"text-align: right; color: #335575; font-family: 'Amiri', serif; font-size: 18px;\">اذا استثمرت في بداية عام 2023  <b>ريال 10,000</b>💸 في محافظ ابيان المالية</p>", unsafe_allow_html=True)
    st.line_chart(abyan)
    abyan_mp = np.round(abyan.iloc[-1],2)
    abyanhp_return = np.round((abyan.iloc[-1]/abyan.iloc[0]-1)*100,2)
    abyanhp_return2023 = np.round((abyan.loc[malaa[abyan.index.year == 2023].index.max()]/abyan.iloc[0]-1)*100,2)
    abyanhp_return2024 = np.round((abyan.loc[abyan[abyan.index.year == 2024].index.max()]/abyan.loc[abyan[abyan.index.year == 2023].index.max()]-1)*100,2)    
    abyangeometric_mean = np.round((((np.prod(1 + abyan.pct_change()))**(trading_days/len(abyan.pct_change()))) - 1)*100,4)
    abyanstandard_deviation = np.round(abyan.pct_change().std()* np.sqrt(trading_days)*100,4)
    abyanbeta = abyan.pct_change().corr()['S&P500']
    abyanmetrics = pd.concat([abyan_mp,abyanhp_return,abyangeometric_mean,abyanstandard_deviation,abyanbeta,abyanhp_return2023,abyanhp_return2024],axis=1)
    abyanmetrics.columns = ["القيمة السوقية","عائد الاستثمار%", 'المتوسط الهندسي%', 'الانحراف المعياري%','بيتا',"2023 عائد الاستثمار%","2024 عائد الاستثمار%",]
    st.write(abyanmetrics)

    st.markdown(grey_line, unsafe_allow_html=True)
 
    st.markdown("<p style=\"text-align: right; font-family: 'Amiri', serif; font-size: 20px;\">مقارنة المحافظ ذات الاعلى مخاطر في كل شركة</p>", unsafe_allow_html=True)
    st.markdown("<p style=\"text-align: right; font-family: 'Amiri', serif; font-size: 18px;\">لأن منصات الاستثمار الآلي مناسبة للذين يخططون للاستثمار على المدى الطويل(10+ سنوات)، سأقوم بمقارنة بين المحافظ عالية المخاطر لان كلما زادت الفترة الزمنية للاستثمار، زادت قدرتك على تحمل المخاطر </p>", unsafe_allow_html=True)

    highriskporfolio = pd.concat([tamrametrics.iloc[0],malaametrics.iloc[0], abyanmetrics.iloc[0]],axis=1).T
    highriskporfolio['المحفظة'] = ["تمرة المالية", "ملاءة التقنية", "ابيان المالية"]
    highriskporfolio = highriskporfolio.T
    # st.write(highriskporfolio)

    portfolio_highes = highriskporfolio.loc['عائد الاستثمار%'].idxmax()
    highestreturn = highriskporfolio[portfolio_highes].head(2)[1]
    portfolio_company = highriskporfolio[portfolio_highes].tail(1)[0]

    portfolio_beta = highriskporfolio.loc['بيتا'].idxmax()
    highestbeta = highriskporfolio[portfolio_beta].tail(5)[1]
    portfolio_companybeta = highriskporfolio[portfolio_beta].tail(1)[0]

    portfolio_std = highriskporfolio.loc['الانحراف المعياري%'].idxmin()
    loweststd = highriskporfolio[portfolio_std].tail(6)[1]
    portfolio_companystd = highriskporfolio[portfolio_std].tail(1)[0]
    st.markdown(f"""
        <ul style="text-align: right; color: #4A4A4A; font-family: 'Amiri', serif; font-size: 18px;">
            المحفظة ذات أعلى عائد هي المحفظة <b>{portfolio_highes}</b> بعائد %<b>{highestreturn}</b> المقدمة من <b>{portfolio_company}</b><br>
            المحفظة ذات أعلى معامل بيتا هي المحفظة <b>{portfolio_beta}</b> يساوي <b>{highestbeta}</b> المقدمة من <b>{portfolio_companybeta}</b> وذلك يعني انها تتبع عائد المؤشر بشكل أفضل من منافسيها<br>
            المحفظة ذات أقل انحراف معياري هي المحفظة <b>{portfolio_std}</b> يساوي %<b>{loweststd}</b> المقدمة من <b>{portfolio_companystd}</b><br>
        </ul>
    """, unsafe_allow_html=True)
    st.markdown("<br><p style=\"text-align: center; font-family: 'Amiri'; font-size: 30px;\"><a href='https://www.buymeacoffee.com/rayan3rab7' target='_blank'>اذا استفدت من الخدمة يمديك تدفع مقابلها</a></p>", unsafe_allow_html=True)
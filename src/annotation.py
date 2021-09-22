import streamlit as st
import pandas as pd
import glob
import os
from utils.util import setup_logger, list_class

logger = setup_logger(__name__)

option = st.selectbox(
    'choose a prediction file',
    list(glob.glob('../predictions/*.jsonl'))
)

filename_an = f'{os.path.splitext(option)[0]}_an.jsonl'.replace('predictions','annotated')
if os.path.exists(filename_an):
    logger.info(f'annotated file exists in {filename_an}')
    _df = pd.read_json(filename_an,orient='records',lines=True)
else:
    logger.info(f'annotated file not exists in {filename_an}')
    _df = pd.read_json(option,orient='records',lines=True)

if 'class' not in _df.columns:
    _df['class']=list(range(len(_df)))

def save_df():
    _df['class'] = [st.session_state[f'{i}_c'] for i in range(len(_df))]
    _df.to_json(filename_an,orient='records',lines=True,force_ascii=False)
    logger.info(f'saved annotated file in {filename_an}')

iter_se  = _df['tokens'].iteritems()
while True:
    try:
        index, value = next(iter_se)
        s1,s2,_ = value.split('[SEP]')
        s1 = s1.lstrip('[CLS]')
        st.header(s1)
        st.header(s2)
        key = f'{index}_c'
        init_value = _df.loc[index]['class'] if _df.loc[index]['class'] != [] else []
        st.multiselect('含意関係の分類',list_class,init_value,key=key,on_change=save_df)
    except StopIteration:
        break
import plotly
import plotly.graph_objects as go
import math
import pandas as pd
import numpy as np
from dash_player import DashPlayer
from dash import Dash, dcc, html, Input, Output,ctx, State
from flask import Flask, Response, request
import dash_bootstrap_components as dbc

from src.infopage import layout as info_content
from src.sheetpage import SheetPage

# 1. raw 데이터프레임 갖고오기
df = pd.read_csv('./data/die-casting_dataset.csv')

# 2. id, className 이름들 변수화
# -> container 이름들
info_container = 'infoContainer'
sheet_container = 'sheetContainer'
# -> title 이름들
info_title = 'infoTitle'
sheet_plus_btn_title = 'sheetPlusBtnTitle'
# -> content 이름들
info_contents = 'infoContents'
# -> header 이름들

# -> body 이름들
info_body = 'infoBody'

# -> button 이름들
sheet_plus_btn = 'sheetPlusBtn'



# 3. 서버 생성
server = Flask(__name__)
app = Dash(__name__, server=server)

# 4. 레이아웃 셍성
app.layout = html.Div(
    className = 'Container',
    children = [
        html.Div(
            id = info_container,
            children = [
                html.H2(
                    id = info_title,
                    children = ['데이터 x-value']
                ),
                html.Div(
                    id = info_contents,
                    children = []
                )
            ]
        ),
        html.Div(
            id = sheet_plus_btn,
            children = [
                html.H2(
                    id = sheet_plus_btn_title,
                    children = ['Sheet 추가'],
                    n_clicks=0
                )
            ]
        ),
        html.Div(
            id = sheet_container,
            children = [
                html.H1(
                    id = 'ssss',
                    children = ['아 시발 집 가고싶다.']
                )
            ]
        )
    ]
)
# 5. 레이아웃에 callback 함수 생성
# 0. 인스턴스 생성시 필요한 변수들
global sheet_num, sheet_input_list_1,sheet_input_list_2,sheet_input_list_3, sheet_output_list
sheet_num = 1
sheet_input_list_1 = []
sheet_input_list_2 = []
sheet_input_list_3 = []
sheet_output_list = []



# a. 변수들 정보들 
@app.callback(
    Output(info_contents, 'children'),
    Input(info_container, 'n_clicks')
)
def info_window(n):
    if n %2 == 1:
        return info_content

# b. sheet 를 추가하는 버튼
@app.callback(
    Output(sheet_container,'children'),
    Input(sheet_plus_btn, 'n_clicks'),
    State(sheet_container, 'children')
)
def sheet_plus(n,container):
    global sheet_num, sheet_input_list, sheet_output_list
    sheet_instance = SheetPage()
    globals()["{0}_sheet".format(sheet_num)] = sheet_instance.create_layout(create_sheet_index(sheet_num))
    sheet_num += 1
    container.append(sheet_instance.create_layout(create_sheet_index(sheet_num)))
    return container

def create_sheet_index(sheet_num):
    drop_id_1 = '{0}_sheet_ddn1'.format(sheet_num)
    drop_id_2 = '{0}_sheet_ddn2'.format(sheet_num)
    drop_id_3 = '{0}_sheet_ddn1'.format(sheet_num)
    graph_id = '{0}_sheet_graph'.format(sheet_num)
    drop_data_2 = df.columns
    drop_data_3 = df.columns
    return drop_id_1, drop_id_2, drop_id_3, graph_id, drop_data_2, drop_data_3
    

# 6. 최종 생성한 서버 run
if __name__ == '__main__':
    app.run_server(debug=True)
from dash import dcc, html
from dash import Dash, dcc, html, Input, Output

# 클래스 형태로 페이지 기능을 구현한다.
graph_settings = [
    {'label' : 'Scatter', 'value' : 'scatter'},
    {'label' : 'Box', 'value' : 'box'}
]


class SheetPage:
    def __init__(self):
        # containr 의 div className
        # -> 여러개의 Sheet가 생길때, container의 스타일을 한번에 수정하기 용이함

        # dropdown의 id
        self.dropdown_id_1 = None
        self.dropdown_id_2 = None
        self.dropdown_id_3 = None

        # 그래프 id
        self.graph_id = None
        
        # dropdown 데이터
        self.dd_data_id2 = None
        self.dd_data_id3 = None

    
    def create_layout(self, tuple):
        self.dropdown_id_1 = tuple[0]
        self.dropdown_id_2 = tuple[1]
        self.dropdown_id_3 = tuple[2]
        self.graph_id = tuple[3]
        self.dd_data_id2 = tuple[4]
        self.dd_data_id3 = tuple[5]

        return html.Div(
                className = 'instanceSheetContainer',
                children = [
                    dcc.Dropdown(
                        id = self.dropdown_id_1,
                        options = graph_settings
                    ),
                    dcc.Graph(id = self.graph_id),
                    html.Div(
                        className = 'xyValueChoiceContainer',
                        children = [
                            dcc.Dropdown(
                                id = self.dropdown_id_2,
                                options = self.dd_data_id2
                            ),
                            dcc.Dropdown(
                                id = self.dropdown_id_3,
                                options = self.dd_data_id3
                            )
                        ]
                    )
                ]
            )





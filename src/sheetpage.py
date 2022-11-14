from dash import dcc, html

# graph_option = [
#             {'label' : 'Scatter', 'value' : 'scatter'},
#             {'label' : 'Box', 'value' : 'box'}
#         ]


# 클래스 형태로 페이지 기능을 구현한다.
class SheetPage:
    def __init__(self):
        # containr 의 div className
        # -> 여러개의 Sheet가 생길때, container의 스타일을 한번에 수정하기 용이함
        self.graph_option = [
            {'label' : 'Scatter', 'value' : 'scatter'},
            {'label' : 'Box', 'value' : 'box'}
        ]

    def create_layout(self, index, dropdown_option):
        # index : 동적으로 인스턴스 생성시 인스턴스끼리 구분하기 위한 번호
        # dropdown_option : dropdown에 들어갈 값
        return html.Div(
                className = 'instanceSheetContainer',
                children = [
                    dcc.Dropdown(
                        id = {
                            'type' : 'graph-change',
                            'index' : index
                        },
                        options = self.graph_option, 
                        style = {
                            'width' : '800px'
                        },
                        value = dropdown_option[0]
                    ),
                    dcc.Graph(
                        id = {
                            'type' : 'graph',
                            'index' : index
                        },
                        figure = {}
                    ),
                    html.Div(
                        className = 'xyValueChoiceContainer',
                        children = [
                            dcc.Dropdown(
                                id = {
                                    'type' : 'dynamic-x1',
                                    'index' : index
                                    },
                                options = [{'label' : item, 'value' : item} for item in dropdown_option],
                                style = {
                                    'width' : '430px'
                                },
                                value = dropdown_option[0]
                            ),
                            dcc.Dropdown(
                                id = {
                                    'type':'dynamic-x2',
                                    'index': index
                                },
                                options = [{'label' : item, 'value' : item} for item in dropdown_option],
                                style = {
                                    'width' : '430px'
                                },
                                value = dropdown_option[0]
                            )
                        ]
                    )
                ]
            )





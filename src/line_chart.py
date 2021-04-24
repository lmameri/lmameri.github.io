import plotly.express as px
import preprocess


import plotly.graph_objects as go

import plotly.express as px
import preprocess
import plotly.graph_objects as go

colors=['rgb(243, 231, 155)', 'rgb(250, 196, 132)', 'rgb(248, 160, 126)', 'rgb(235, 127, 134)', 'rgb(206, 102, 147)', 'rgb(160, 89, 160)', 'rgb(92, 83, 165)',
        'rgb(243, 231, 155)', 'rgb(250, 196, 132)', 'rgb(248, 160, 126)', 'rgb(235, 127, 134)', 'rgb(206, 102, 147)', 'rgb(160, 89, 160)', 'rgb(92, 83, 165)',
        'rgb(243, 231, 155)', 'rgb(250, 196, 132)', 'rgb(248, 160, 126)', 'rgb(235, 127, 134)', 'rgb(206, 102, 147)', 'rgb(160, 89, 160)', 'rgb(92, 83, 165)',
        'rgb(243, 231, 155)', 'rgb(250, 196, 132)', 'rgb(248, 160, 126)', 'rgb(235, 127, 134)', 'rgb(206, 102, 147)', 'rgb(160, 89, 160)', 'rgb(92, 83, 165)',
        'rgb(243, 231, 155)', 'rgb(250, 196, 132)', 'rgb(248, 160, 126)', 'rgb(235, 127, 134)', 'rgb(206, 102, 147)', 'rgb(160, 89, 160)', 'rgb(92, 83, 165)',
       ]

colorsh=[['crimson','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey',],['lightgrey','crimson','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey',],['lightgrey','lightgrey','crimson','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey',],['lightgrey','lightgrey','lightgrey','crimson','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey',],['lightgrey','lightgrey','lightgrey','lightgrey','crimson','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey',],['lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','crimson','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey',],['lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','crimson','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey',],['lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','crimson','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey',],['lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','crimson','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey',],['lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','crimson','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey',],['lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','crimson','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey',],['lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','crimson','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey',],['lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','crimson','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey',],['lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','crimson','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey',],['lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','crimson','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey',],['lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','crimson','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey',],['lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','crimson','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey',],['lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','crimson','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey',],['lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','crimson','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey',],['lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','crimson','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey',],['lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','crimson','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey',],['lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','crimson','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey',],['lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','crimson','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey',],['lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','crimson','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey',],['lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','crimson','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey',],['lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','crimson','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey',],['lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','crimson','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey',],['lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','crimson','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey',],['lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','crimson','lightgrey','lightgrey','lightgrey','lightgrey',],['lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','crimson','lightgrey','lightgrey','lightgrey',],['lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','crimson','lightgrey','lightgrey',],['lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','crimson','lightgrey',],['lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','lightgrey','crimson',],]
opacityh=[[1,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,],[0.4,1,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,],[0.4,0.4,1,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,],[0.4,0.4,0.4,1,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,],[0.4,0.4,0.4,0.4,1,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,],[0.4,0.4,0.4,0.4,0.4,1,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,],[0.4,0.4,0.4,0.4,0.4,0.4,1,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,],[0.4,0.4,0.4,0.4,0.4,0.4,0.4,1,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,],[0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,1,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,],[0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,1,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,],[0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,1,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,],[0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,1,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,],[0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,1,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,],[0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,1,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,],[0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,1,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,],[0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,1,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,],[0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,1,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,],[0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,1,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,],[0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,1,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,],[0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,1,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,],[0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,1,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,],[0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,1,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,],[0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,1,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,],[0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,1,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,],[0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,1,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,],[0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,1,0.4,0.4,0.4,0.4,0.4,0.4,0.4,],[0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,1,0.4,0.4,0.4,0.4,0.4,0.4,],[0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,1,0.4,0.4,0.4,0.4,0.4,],[0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,1,0.4,0.4,0.4,0.4,],[0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,1,0.4,0.4,0.4,],[0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,1,0.4,0.4,],[0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,1,0.4,],[0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,1,],]

def get_linechart(df,media_list):
    fig = go.Figure()

    for i in range(0,len(media_list)):
        fig=fig.add_trace(go.Scatter(
            x=df.loc[df['compte'] == media_list[i]]['date'],
            y=df.loc[df['compte'] == media_list[i]]['MaxFollowers'],
            name=media_list[i])) 
    fig.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            direction="down",
            x=2,
            y=1.2,
            showactive=True,
            buttons=list([
                    dict(
                        args=[{"line.color":  colors, "opacity":1}],
                        label="Vue générale",
                        method="update"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[0],"opacity":opacityh[0]}],
                        label=media_list[0],
                        method="restyle"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[1],"opacity":opacityh[1]}],
                        label=media_list[1],
                        method="restyle"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[2],"opacity":opacityh[2]}],
                        label=media_list[2],
                        method="restyle"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[3],"opacity":opacityh[3]}],
                        label=media_list[3],
                        method="restyle"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[4],"opacity":opacityh[4]}],
                        label=media_list[4],
                        method="restyle"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[5],"opacity":opacityh[5]}],
                        label=media_list[5],
                        method="restyle"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[6],"opacity":opacityh[6]}],
                        label=media_list[6],
                        method="restyle"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[7],"opacity":opacityh[7]}],
                        label=media_list[7],
                        method="restyle"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[8],"opacity":opacityh[8]}],
                        label=media_list[8],
                        method="restyle"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[9],"opacity":opacityh[9]}],
                        label=media_list[9],
                        method="restyle"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[10],"opacity":opacityh[10]}],
                        label=media_list[10],
                        method="restyle"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[11],"opacity":opacityh[11]}],
                        label=media_list[11],
                        method="restyle"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[12],"opacity":opacityh[12]}],
                        label=media_list[12],
                        method="restyle"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[13],"opacity":opacityh[13]}],
                        label=media_list[13],
                        method="restyle"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[14],"opacity":opacityh[14]}],
                        label=media_list[14],
                        method="restyle"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[15],"opacity":opacityh[15]}],
                        label=media_list[15],
                        method="restyle"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[16],"opacity":opacityh[16]}],
                        label=media_list[16],
                        method="restyle"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[17],"opacity":opacityh[17]}],
                        label=media_list[17],
                        method="restyle"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[18],"opacity":opacityh[18]}],
                        label=media_list[18],
                        method="restyle"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[19],"opacity":opacityh[19]}],
                        label=media_list[19],
                        method="restyle"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[20],"opacity":opacityh[20]}],
                        label=media_list[20],
                        method="restyle"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[21],"opacity":opacityh[21]}],
                        label=media_list[21],
                        method="restyle"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[22],"opacity":opacityh[22]}],
                        label=media_list[22],
                        method="restyle"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[23],"opacity":opacityh[23]}],
                        label=media_list[23],
                        method="restyle"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[24],"opacity":opacityh[24]}],
                        label=media_list[24],
                        method="restyle"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[25],"opacity":opacityh[25]}],
                        label=media_list[25],
                        method="restyle"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[26],"opacity":opacityh[26]}],
                        label=media_list[26],
                        method="restyle"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[27],"opacity":opacityh[27]}],
                        label=media_list[27],
                        method="restyle"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[28],"opacity":opacityh[28]}],
                        label=media_list[28],
                        method="restyle"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[29],"opacity":opacityh[29]}],
                        label=media_list[29],
                        method="restyle"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[30],"opacity":opacityh[30]}],
                        label=media_list[30],
                        method="restyle"
                    ),
                    dict(
                        args=[{"line.color":  colorsh[31],"opacity":opacityh[31]}],
                        label=media_list[31],
                        method="restyle"
                    ),

                
            ])
        )
    ])
    fig.update_layout(title='Nombre maximum de followers par mois par média',xaxis_title="Années",yaxis_title="Nombre maximum de followers")

    return fig


def get_linechartexample():
    # Add data
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
            'August', 'September', 'October', 'November', 'December']
    high_2000 = [32.5, 37.6, 49.9, 53.0, 69.1, 75.4, 76.5, 76.6, 70.7, 60.6, 45.1, 29.3]
    low_2000 = [13.8, 22.3, 32.5, 37.2, 49.9, 56.1, 57.7, 58.3, 51.2, 42.8, 31.6, 15.9]
    high_2007 = [36.5, 26.6, 43.6, 52.3, 71.5, 81.4, 80.5, 82.2, 76.0, 67.3, 46.1, 35.0]
    low_2007 = [23.6, 14.0, 27.0, 36.8, 47.6, 57.7, 58.9, 61.2, 53.3, 48.5, 31.0, 23.6]
    high_2014 = [28.8, 28.5, 37.0, 56.8, 69.7, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9]
    low_2014 = [12.7, 14.3, 18.6, 35.5, 49.9, 58.0, 60.0, 58.6, 51.7, 45.2, 32.2, 29.1]

    fig = go.Figure()
    # Create and style traces
    fig.add_trace(go.Scatter(x=month, y=high_2014, name='High 2014',
                            line=dict(color='firebrick', width=4)))
    fig.add_trace(go.Scatter(x=month, y=low_2014, name = 'Low 2014',
                            line=dict(color='royalblue', width=4)))
    fig.add_trace(go.Scatter(x=month, y=high_2007, name='High 2007',
                            line=dict(color='firebrick', width=4,
                                dash='dash') # dash options include 'dash', 'dot', and 'dashdot'
    ))
    fig.add_trace(go.Scatter(x=month, y=low_2007, name='Low 2007',
                            line = dict(color='royalblue', width=4, dash='dash')))
    fig.add_trace(go.Scatter(x=month, y=high_2000, name='High 2000',
                            line = dict(color='firebrick', width=4, dash='dot')))
    fig.add_trace(go.Scatter(x=month, y=low_2000, name='Low 2000',
                            line=dict(color='royalblue', width=4, dash='dot')))

    # Edit the layout
    fig.update_layout(title='Average High and Low Temperatures in New York',
                    xaxis_title='Month',
                    yaxis_title='Temperature (degrees F)')
    return fig

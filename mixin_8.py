
import panel as pn
import uuid
import plaidcloud.utilities.debug.wingdbstub
import param



class State(param.Parameterized):
    # some example params
    trigger = param.Event()
    foo = param.String()
    # other params go here

class GlobalStateMixin:
    @property
    def app(self):
        return pn.state.cache['app']

class Color(pn.viewable.Viewer):
    flavor = param.String(allow_refs=True)
    shape = param.String(allow_refs=True)
    
    color = param.Selector(default="red", objects=["red", "blue"])
    
    def __panel__(self):
        return pn.Column("## Color", self.param.color, self._get_info, styles={"border": "4px solid red"})
    
    @pn.depends("flavor", "shape", "color")
    def _get_info(self):
        return f"""
        Flavor:{self.flavor}\n
        Shape:{self.shape}\n
        Color:{self.color}
        """

class Shape(pn.viewable.Viewer):
    flavor = param.String(allow_refs=True)
    color = param.String(allow_refs=True)
    
    shape = param.Selector(default="square", objects=["square", "circle", "triangle"])

    def __panel__(self):
        return pn.Column("## Shape", self.param.shape, self._get_info, styles={"border": "4px solid green"})
    
    @pn.depends("flavor", "shape", "color")
    def _get_info(self):
        return f"""
        Flavor:{self.flavor}\n
        Shape:{self.shape}\n
        Color:{self.color}
        """

class ApplicationOld(pn.viewable.Viewer):
    app_id = str(uuid.uuid4())[:4]
    
    shape = param.String(allow_refs=True)
    color = param.String(allow_refs=True)
    
    flavor = param.Selector(default="beans", objects=['rice', 'beans', 'guac'])

    def __panel__(self):
        return pn.Column(
            '# Application {}'.format(self.app_id),
            self.param.flavor,
            pn.Row(self._get_info), 
            pn.Row(
                Shape(flavor=self.param.flavor),
                Color(flavor=self.param.flavor),
            ),
            styles={"border": "6px solid black"}
        )
    
    @pn.depends("flavor", "shape", "color")
    def _get_info(self):
        return f"""
        Flavor:{self.flavor}\n
        Shape:{self.shape}\n
        Color:{self.color}
        """
    
class Application(param.Parameterized):
    state = State()

    def __init__(self, **params):
        super().__init__(**params)
    
        
        app_id = str(uuid.uuid4())[:4]
        title = f'TestApp {app_id}'
        
        self.shape = param.String(allow_refs=True)
        self.color = param.String(allow_refs=True)
        
        self.flavor = param.Selector(default="beans", objects=['rice', 'beans', 'guac'])

        self.template = pn.template.MaterialTemplate(
            title=title, 
            sidebar=[
                self.flavor,
                #self._get_info()
            ],
            main=[
                pn.Row(
                    Shape(flavor=self.param.flavor),
                    Color(flavor=self.param.flavor),
                )
            ]
        )

    #def __panel__(self):
        #return pn.Column(
            #'# Application {}'.format(self.app_id),
            #self.param.flavor,
            #pn.Row(self._get_info), 
            #pn.Row(
                #Shape(flavor=self.param.flavor),
                #Color(flavor=self.param.flavor),
            #),
            #styles={"border": "6px solid black"}
        #)
    
    #@pn.depends("flavor", "shape", "color")
    #def _get_info(self):
        #return f"""
        #Flavor:{self.flavor}\n
        #Shape:{self.shape}\n
        #Color:{self.color}
        #"""

if __name__ == "__main__":
    Application().template.show()

if pn.state.served:
    Application().servable()

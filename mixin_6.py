import uuid
import plaidcloud.utilities.debug.wingdbstub

import panel as pn
import param


class State(param.Parameterized):
    trigger = param.Event(allow_refs=True, nested_refs=True)
    foo   = pn.widgets.TextInput(
        name='FOO',
        #value='FOO3', <-This will show up in Thing 2 initially, but won't update.
    )
    bar = param.String(
        allow_refs=True,
        nested_refs=True, 
    )
    
    #Just to show that we can get something from State into Thing1 and Thing2
    thirty_seven = param.Integer(default=37) #Can read into Thing1 and Thing2

class GlobalStateMixin:
    @property
    def app(self):
        #print('app - GlobalStateMixin')
        return pn.state.cache['app']
    
class Thing1(GlobalStateMixin, pn.viewable.Viewer):
    def __init__(self, **params):
        super().__init__(**params)
    
    widget_local = pn.widgets.TextInput(
        name='LOCAL',
        placeholder='....'
    )
    
    @param.depends(
        'app.state.thirty_seven',
        watch=True
    )
    def __panel__(self):
        return pn.Column(
            '## Thing 1',
            self.app.state.foo,
            pn.widgets.TextInput(
                value = self.app.state.bar,
                name='BAR',
                placeholder='...'
            ),
            self.widget_local, 
            self._get_info(),
            styles={'border': '4px solid blue'}
        )
    @param.depends(
        #'app.state.foo',
        ##'app.state.bar',
        'app.state.thirty_seven',
        watch=True
    )
    def print_something(self):
        print(f'name has changed to {self.app.state.foo}')
        
    @param.depends(
        'app.state.thirty_seven',
        watch=True
    )
    def _get_info(self):
        return f"""
        Local:{self.widget_local.value} \n
        Foo:{self.app.state.foo.value} \n
        Bar:{self.app.state.bar}  \n
        thirty_seven:{self.app.state.thirty_seven}
        """

class Thing2(GlobalStateMixin, pn.viewable.Viewer):
    def __init__(self, **params):
        super().__init__(**params)
        print('init Thing')
        
    @param.depends(
        'app.state.foo',
        'app.state.thirty_seven',
        'app.state.bar',
        watch=True
    )
    def __panel__(self):
        return pn.Column(
            '## Thing 2',
            self._get_info(),
            styles={'border': '4px solid green'}
        )
    
    @param.depends(
        'app.state.foo',
        'app.state.thirty_seven',
        'app.state.bar',
        watch=True
    )
    def _get_info(self):
        return f"""
        Foo:{self.app.state.foo.value} \n
        Bar:{self.app.state.bar}  \n
        thirty_seven:{self.app.state.thirty_seven}
        """

class App(param.Parameterized):
    state = State()

    def __init__(self, **params):
        super().__init__(**params)
        # do some stuff here to set things up
        # now put ourselves in the cache
        pn.state.cache['app'] = self
        self.title = 'Two Components'
        self.thing1 = Thing1()
        self.thing2 = Thing2()
        self.thing1.print_something()
        
        self.template = pn.template.MaterialTemplate(
            title=self.title, 
            sidebar=[
                self.thing1
            ]
        )
        self.template.main.append(
            pn.Column(
                self.thing2,
            ),
        )

if __name__ == "__main__":
    App().template.show()


if pn.state.served:
    App().template.servable()

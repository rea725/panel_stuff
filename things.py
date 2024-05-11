import uuid
import panel as pn
import param

class State(param.Parameterized):
    # this is global state. it only has param objects, not widgets
    color = param.String(allow_refs=True, nested_refs=True, default="ORANGE-default")
    foo = param.String(allow_refs=True, nested_refs=True, default="FOOO-default")
    bar = param.String(allow_refs=True, nested_refs=True, default="BAR-default")
    thirty_seven = param.Integer(default=37)
    
class GlobalStateMixin:
    @property
    def app(self):
        return pn.state.cache['app']

class Thing1(GlobalStateMixin, pn.viewable.Viewer):
    # this is a class that has widgets locally, this is what people will see
    foo = pn.widgets.TextInput(name='Foo')
    bar = pn.widgets.TextInput(name='Bar')
    thirty_seven = pn.widgets.IntInput(name='thirty-seven')
    color = pn.widgets.StaticText(name='color')
    #shape = pn.widgets.Select(name='Shape', options=['square', 'circle'], value='square')
    shape = pn.widgets.TextInput(name='Shape')

    def __init__(self, **params):
        super().__init__(**params)
        #self.foo.value = DEFAULTS['foo']
        #self.color.value = self.app.state.color
        #self.bar.value = self.app.state.bar
        #self.thirty_seven.value = self.app.state.thirty_seven

    # the function below will listen for updates on any of the widgets
    # note that callbacks do not return any values. functions that have watch=True should
    # typically not return values
    @pn.depends('color.value', 'foo.value', 'bar.value', 'thirty_seven.value', watch=True)
    def widget_state_changed(self):
        self.app.state.color = self.color.value
        self.app.state.foo = self.foo.value
        self.app.state.bar = self.bar.value
        self.app.state.thirty_seven = self.thirty_seven.value

    # we don't want to put any listeners on panel, as this function gets invoked
    # automatically in another context
    def __panel__(self):
        return pn.Column(
            '## Thing 1',
            self.color,
            self.foo,
            self.bar,
            self.thirty_seven,
            styles={'border': '4px solid blue'}
        )
    
    @param.depends('app.state.color', 'app.state.foo', 'app.state.bar', 'app.state.thirty_seven', watch=True)
    def update_labels(self):
        # we have to set the value property of the components
        self.color.value = self.app.state.color
        self.foo.value = self.app.state.foo
        self.bar.value = self.app.state.bar
        self.thirty_seven.value = self.app.state.thirty_seven
        
class Thing2(GlobalStateMixin, pn.viewable.Viewer):
    # these are just labels
    foo = pn.widgets.StaticText(name='Foo', value='')
    bar = pn.widgets.StaticText(name='Bar', value='')
    thirty_seven = pn.widgets.StaticText(value='', name='thirty seven')
    color = pn.widgets.TextInput(name='Color', value='ColorValue')
    
    def __init__(self, **params):
        super().__init__(**params)
        self.color.value = self.app.state.color
        self.foo.value = self.app.state.foo
        self.bar.value = self.app.state.bar
        self.thirty_seven.value = self.app.state.thirty_seven
 
    def __panel__(self):
        return pn.Column(
            '## Thing 2',
            self.foo,
            self.bar,
            self.color,
            self.thirty_seven,
            styles={'border': '4px solid green'}
        )
    
    @pn.depends('color.value', watch=True)
    def widget_state_changed(self):
        self.app.state.color = self.color.value
        
    #@param.depends('app.state.foo', 'app.state.bar', 'app.state.thirty_seven', watch=True)
    @param.depends('app.state.color', 'app.state.foo', 'app.state.bar', 'app.state.thirty_seven', watch=True)
    def update_labels(self):
        # we have to set the value property of the components
        self.color.value = self.app.state.color
        self.foo.value = self.app.state.foo
        self.bar.value = self.app.state.bar
        self.thirty_seven.value = self.app.state.thirty_seven
        
class Thing3(GlobalStateMixin, pn.viewable.Viewer):
    # these are just labels
    foo = pn.widgets.StaticText(name='Foo', value='')
    bar = pn.widgets.StaticText(name='Bar', value='')
    thirty_seven = pn.widgets.StaticText(value='', name='thirty seven')
    color = pn.widgets.TextInput(name='Color', value='ColorValue')
    
    def __init__(self, **params):
        super().__init__(**params)
        self.color.value = self.app.state.color
        self.foo.value = self.app.state.foo
        self.bar.value = self.app.state.bar
        self.thirty_seven.value = self.app.state.thirty_seven
 
    def __panel__(self):
        return pn.Column(
            '## Thing 3',
            self.color,
            self.foo,
            self.bar,
            self.thirty_seven,
            styles={'border': '4px solid red'}
        )
    
    @pn.depends('color.value', watch=True)
    def widget_state_changed(self):
        self.app.state.color = self.color.value
        
    #@param.depends('app.state.foo', 'app.state.bar', 'app.state.thirty_seven', watch=True)
    @param.depends('app.state.color', 'app.state.foo', 'app.state.bar', 'app.state.thirty_seven', watch=True)
    def update_labels(self):
        # we have to set the value property of the components
        self.color.value = self.app.state.color
        self.foo.value = self.app.state.foo
        self.bar.value = self.app.state.bar
        self.thirty_seven.value = self.app.state.thirty_seven
        
class Thing4(GlobalStateMixin, pn.viewable.Viewer):
    # these are just labels
    foo = pn.widgets.StaticText(name='Foo', value='')
    bar = pn.widgets.StaticText(name='Bar', value='')
    thirty_seven = pn.widgets.StaticText(value='', name='thirty seven')
    color = pn.widgets.TextInput(name='Color', value='ColorValue')
    
    def __init__(self, **params):
        super().__init__(**params)
        self.color.value = self.app.state.color
        self.foo.value = self.app.state.foo
        self.bar.value = self.app.state.bar
        self.thirty_seven.value = self.app.state.thirty_seven
 
    def __panel__(self):
        return pn.Column(
            '## Thing 4',
            self.bar,
            self.color,
            self.foo, 
            self.thirty_seven,
            styles={'border': '4px solid yellow'}
        )
    
    @pn.depends('color.value', watch=True)
    def widget_state_changed(self):
        self.app.state.color = self.color.value
        
    #@param.depends('app.state.foo', 'app.state.bar', 'app.state.thirty_seven', watch=True)
    @param.depends('app.state.color', 'app.state.foo', 'app.state.bar', 'app.state.thirty_seven', watch=True)
    def update_labels(self):
        # we have to set the value property of the components
        self.color.value = self.app.state.color
        self.foo.value = self.app.state.foo
        self.bar.value = self.app.state.bar
        self.thirty_seven.value = self.app.state.thirty_seven
        
class Thing5(GlobalStateMixin, pn.viewable.Viewer):
    # these are just labels
    foo = pn.widgets.StaticText(name='Foo'
    #                            , value=''
    )
    bar = pn.widgets.StaticText(name='Bar', value='')
    thirty_seven = pn.widgets.StaticText(name='thirty-seven', value='')
    color = pn.widgets.StaticText(name='Color', value='')
    
    def __init__(self, **params):
        super().__init__(**params)
        self.color.value = self.app.state.color
        self.foo.value = self.app.state.foo
        self.bar.value = self.app.state.bar
        self.thirty_seven.value = self.app.state.thirty_seven
 
    def __panel__(self):
        return pn.Column(
            '## Thing 5',
            self.color,
            self.foo,
            self.bar,
            self.thirty_seven,
            styles={'border': '4px solid orange'}
        )
    
    @pn.depends('color.value', watch=True)
    def widget_state_changed(self):
        self.app.state.color = self.color.value
        
    #@param.depends('app.state.foo', 'app.state.bar', 'app.state.thirty_seven', watch=True)
    @param.depends('app.state.color', 'app.state.foo', 'app.state.bar', 'app.state.thirty_seven', watch=True)
    def update_labels(self):
        # we have to set the value property of the components
        self.color.value = self.app.state.color
        self.foo.value = self.app.state.foo
        self.bar.value = self.app.state.bar
        self.thirty_seven.value = self.app.state.thirty_seven


class Thing6(GlobalStateMixin, pn.viewable.Viewer):
    # these are just labels
    foo = pn.widgets.TextInput(name='Foo')
    bar = pn.widgets.TextInput(name='Bar')
    thirty_seven = pn.widgets.IntInput(name='thirty-seven', value=37)
    color = pn.widgets.TextInput(name='Color', value='ColorValue')
    
    def __init__(self, **params):
        super().__init__(**params)
        self.color.value = self.app.state.color
        self.foo.value = self.app.state.foo
        self.bar.value = self.app.state.bar
        self.thirty_seven.value = self.app.state.thirty_seven
        
 
    def __panel__(self):
        return pn.Column(
            '## Thing 6',
            self.color,
            self.foo,
            self.bar,
            self.thirty_seven,
            styles={'border': '4px solid purple'}
        )
    
    @pn.depends('color.value', 'foo.value', 'bar.value', 'thirty_seven.value', watch=True)
    def widget_state_changed(self):
        self.app.state.color = self.color.value
        self.app.state.foo = self.foo.value
        self.app.state.bar = self.bar.value
        self.app.state.thirty_seven = self.thirty_seven.value
        
    #@param.depends('app.state.foo', 'app.state.bar', 'app.state.thirty_seven', watch=True)
    @param.depends('app.state.color', 'app.state.foo', 'app.state.bar', 'app.state.thirty_seven', watch=True)
    def update_labels(self):
        # we have to set the value property of the components
        self.color.value = self.app.state.color
        self.foo.value = self.app.state.foo
        self.bar.value = self.app.state.bar
        self.thirty_seven.value = self.app.state.thirty_seven

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
        #self.thing2a = Thing2()
        #self.thing2b = Thing2()
        self.thing3 = Thing3()
        self.thing4 = Thing4()
        self.thing5 = Thing5()
        self.thing6 = Thing6()
        
        self.template = pn.template.MaterialTemplate(
            title=self.title, 
            sidebar=[
                self.thing1
            ]
        )
        self.template.main.append(
            pn.Column(
                self.thing2, 
                #self.thing2a,
                #self.thing2b,
                self.thing3,
                self.thing4,
                self.thing5,
                self.thing6,
            ),
        )
        #set defaults now
        #self.state.color = 'BROWN'
        #self.state.foo = 'FOO'
        #self.state.bar = 'BAR'
        #self.state.thirty_seven = 37

if __name__ == "__main__":
    App().template.show()


if pn.state.served:
    App().template.servable()


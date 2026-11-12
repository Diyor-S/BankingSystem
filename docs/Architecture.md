Banking System Architecture:

Domain:
- Bank
- Account
- Card
- Client


User Interfaces:
- Web
- Cli


Domain Entities should know nothing about how they are going to be presented.
They only must know how to perform entity-specific operations.

The very first thing we need to consider:  
How to manage multiple platforms for the same content?

Beeware Toga is worth checking and studying because it uses key components:
- `interface`: Public API, methods, operations that are exposed
- `_impl`: Platform-specific implementation detail that satisfies that `interface`.


app = App(
    storage=InMemoryStorage/DatabaseStorage/FileStorage
    runtime_adapter=Cli/Web/Gui/Mobile
)


app.create(Client, kwargs=kwargs)
app.create(Card, kwargs=kwargs)
app.create(Account, kwargs=kwargs)

Cli:
app = Cli()

Commands:
Entities: dict[str, type] = {
    "client": Client,
    "card": Card,
    "account": Account
}

- CREATE => app.create(<Entity>, <EntityKwargs, e.g: Name, Age, create_at>) ? 
- UPDATE => app.update(<Entity_ID>, <EntityKwargs, e.g: EntityID>)


Subclassing-based App:

class App:
    Minimal number of methods
    
class Cli(App):
    pass
    
class Web(App):
    inherit App
    
    add "endpoints" support.

class Gui(App):
    inherit App
    
    add "gui related components" like 'window', button etc.
    
    
class Mobile(App):
    add "mobile-related components" also some kind of API.
    
What matters here, we are in the backend. Backend is concerned about COMMANDS (Cli), API (Web, Mobile).

Fronted should be written separately.

Backend might implement visual (Cli), 
but the entirely separate programming language (Javascript, HTML, CSS) might implement that while the Backend only
exposes the api within the server.

Subclassing method, is that even possible to get all from App, while also adding entirely customized behavior, 
within the Cli?
Whatever Cli methods introduces we would be providing some additional "Services".

The same applies for Web App.
The Web App would inherit the basic logic, while also introducing its own methods.

But there is an issue, yes we could write the things for the cli ourselves, but for the web app it is easier
to get some fastapi or another just server itself, however we are lacking some useful tools as well.

Integrating the API endpoints, writing the openapi schema, implementing the server, all would need to be properly
handled. Is this even possible with the subclassing approach?

No, inheritance is going to cause issues. And there's another approach like Adapter pattern.

So that means that while our App provides core operations between our domain, the Adapter's like Cli,
Web would be providing their own way in terms of operations how to use that ready App.

However, if the App has to manage all of that, it is gonna be a bit overloaded class, and also I think
there are still issues with the approach of having dict of Entities all available ones, tho it might seem to be
good because we are reducing the code, but that also means that if there are specific methods to the Entity being applied
in that case, even services can not solve that? Or maybe having Service is gonna overturn the table?

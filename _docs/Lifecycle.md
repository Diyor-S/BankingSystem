What should be the flow of Banking app look like?

Okay, so first of all, the entry point to the program:

App.run() -> startup() -> init_entities() = ?

Wait, so how should we run the program? 
App.run() should mean different things on configuration level.

Because run() should account with the config as running web, cli, and gui is gonna
be different. 

For web: we require the `Server` that should start running. If I do not want to make 
everything myself, then we might need to go for fastapi?

If we run with the fastapi for the web, then how we are supposed to accomplish that?

Running the program with fastapi indicates that we are running things asynchronously
and we would need uvicorn as well.

Well, we have got the core Bank entities within the Domain. As long as they do not
depend on anything external, the access method can be changed.

For the web, we might initialize the database, we might need a server, we might need 
much more things. 

So what are we going to do? 

For the web we might also require the pydantic? 

Okay that already means that we need to define as many things as possible,
but that should be separated, like what do we call them? 

Adapters? Plugins? I suppose if we call that:
plugins/web
plugins/cli
plugins/gui

Then we would need to define how to properly initialize them within each file itself.

Most of the code on how to store and do the things should be happening within those plugins in that case.

How are we going to connect those things?

I guess all three things, should bring with themselves the exact way to run, 
but also we need to have some public API, for the plugins.

Because we need to define the base minimum like plugin should define method
run which our application internally would call. 

All three plugins should have access to everything.
config ?, most likely is gonna be crucial part
domain YES
core YES


Now we have the config here. We have got the run config, so what?

How can we run different applications, for cli on the console, and for web,
we would need to setup the server.



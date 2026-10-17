Homework:

Banking System:

Person
Client
Account



require_password - decorator, before calling the functions that return the balance, passport, we could wrap
them with that decorator so it first accepts some passwords and always compares them with the first password that is global and that has been set by the user.


What is even the **flow** of the **App**?

There is App that has references:
1. `Bank` (Banking System Backend) 
2. `UI` (User Interface `UIHandler`)

What should the App be doing?

It should be invoking the `startup` and `exit` methods for both **Bank** and **UI** if present.

`App` should also have `run` method to keep the program alive, and shutdown condition differs and depends on the `UI implementation`.


The only reason to introduce `App` class was because of support of different UI implementations.
I do not know for sure whether that was the good idea yet.

What should be the role of the `UIHandler`?

UIHandler is obviously responsible for how the things are visualized for the end user.

The idea came into mind to allow different UI implementations like:
1. CLI-based
2. GUI-based
3. Web-based

But the question is, all of them have different ways of displaying the data.

So the `data` which refers to the Backend is gonna stay the same.
While the way to display it would differ across different User Interface implmentations.

So how do I achieve this?
I need some standard to judge the UI.
To understand that yes, all of them have the same BASE interface,
tho they define their own platform specific methods to display the things.

I can see the problem with the current approach.
Okay I have UIHandler class, that accepts some UI implementation.
And then so what? It means UIHandler has to somehow allow all the  methods
of that implemenation to work. 

That means UIHandler would have to support all the methods for all different implementations.
That is the wrong approach.

What is the right one?
Let's hold on a little.

The App should be able to receive the UIHandler. In case
of the Web-based UI, in this case, App should dynamically look for the right package (server)
like uvicorn, or at least no, we should have default server implementation.

So for the Web App would need to inspect that. And in order to make it inspect,
we come to the concept of `config`. We need to store the dictionary of the UI Implementations
that our `App` would be able to work with.

So by having that, our App would compare the given interface for example as name of the interface
and retrieve the right class handler to get the UI implementation.

Meaning App would store that as its instance level attribute the UI class, 

So I might have base class implementations for all three of the different UIs.
And then if anyones would want to extend that further they would need to inherit.


Okay let's stop for a little bit. 

What is the core of the Banking System?

What is its core things without which the Banking System would not be able to exist?

In the very low-level, there is contracts on how to pass the data. 

These should be the rules on how the data travels.
Maybe the JSON, Encoding, Decoding,
Validators - validatings the values,
Exceptions to raise when the values are not of the appropriate type. 

Defining the contracts the rules, the types.
Defining the handlers on the low-level generic interfaces that do not depend on domain-specific entities.




So, I thought of how to introduce Cli, and Web to work with the App.

I have within the App class lifecycle operations: startup, exit, run.

And I thought I should have the same things for Cli UI Adapter as well.
Because Cli might add cli-specific operations, attributes, I moved the ownership of the 
App to the Cli.

That way Cli can define its own lifecycle, and invoke whatever App brings.

The same goes for the Web. The web-specific things are added and web also uses the 
App instances however it wants.

But here's the problem: I had for both Cli and Web their own lifecycle methods:
- startup
- run
- exit

However this brings issues as well: what happens when I want to add new features to the
Cli adapter? That means I write the classes etc things, but to actually integrate that
new functionality, I would have to modify startup, or run, or exit...
This is a problem, because modifying those critical methods might actually introduce
bugs and even crash the program entirely.

So, how am I supposed to approach this issue?
I heard about the concept of `registering`, we need to have some `mechanism`
to register the new functionality so that new functionality would be able to 
participate in the lifecycle without actually writing them manually within the `run`
or other main lifecycle operations.

There is the concept of `extension point`, so in this direction that would be a mechanism
whihc is an extension point where the new functionality can register itself, to automate
its participation within the lifecycle.



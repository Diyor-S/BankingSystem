During implementation of `Client Service` **create** operation may not just create
a Client instance, it should perform some more operations at once - atomicity needed.

For example: create of client might mean triggering first client instance creation,
then the client needs some default account to be assigned as well as some default 
card state (even if client does not have cards yet, Card instance should be created).

These things should ALL happen as one atomic operation or not happen at all, and should 
be rolled back if anything goes wrong.

That means that our `Services` actually require some kind of transaction management class
often referred as `Unit of Work`. I heard about that in case of the sqlalchemy, but 
it is also present within the django, in how it manages the transactions.

So our services would also need to support these kind of things. While my first idea
was to introduce the `locks`, that should work for the case of standard library usage.

But what if I want to integrate with some database and I want to use some third-party
unit of work mechanism, e.g: **sqlalchemy**? In that case that would require me to modify
the source code, which already shows that there are going to be issues.

That is why in order to support different `Unit of Work` mechanisms, I would have to 
come up with some basic interface , public api for classes that provide that mechanism.

And e.g: for InMemoryStorage, I might provide some default Locking mechanism, 
whereas in case of DatabaseStorage, we might need to subclass our standard interface, 
and provide the wrapper to reuse whatever Database provides the way to implement its unit of work.

Overall, this issue should be investigated properly.

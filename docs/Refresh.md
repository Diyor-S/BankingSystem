What exactly do I want? 

Domain Problem: Building Banking Application (scope: broad).

Technical Part:
- I want the Application to be scalable. (broad)
    - `Scalable` what that means to me?
    - Let's say that I build the core, I need to introduce some new `core entity`
    - I do not want to rewrite parts of the old-code just to introduce this new entity.
    - So it should be scalable,
    - in a way that even the core components do not depend on each other.

Adding a new class, thereafter making at an attribute of some existing code is not considered
to be a `rewrite`, so it is fine. 

However, if the new feature: a class, a function, or some other utility requires us to 
change the existing code, even minor modification to the code in terms of replacing the old code
to the new code, `THIS` is considered a `violation`. It must be avoided.

How are we supposed avoid this? What are the concepts that we should always think of
even when designing the core domain classes, so that later on when trying to introduce, a
new domain entity, we integrate it seamlessly.

Some of them are: `Composition`, and `Aggregation`.
We always need to consider these two designs when implementing the classes, especially,
the core domain classes. We should be considering the inheritances, the extension parts
for the domain classes. Meaning, they might some subclasses that might provide some additional
attributes, and operations that can be performed only on the subclass. 

Not all domain classes require that, but we truly might have different subclasses of them. 
For example: Client, inherits from the Person? Why is that relevant to banking system? 
Because banking system nowadays requires the passport details, so this is primary
source of identifying the Person in the society in the first place.

There are also different Price classes that might be present, there might be Discount
class as well. There might be some other things like, some bonuses, cash backs, that 
might require subclassing behavior. 

For this kind of classes, it is super necessary to actually design the classes properly,
for them to be scalable, so that we would not remove from the existing code the old parent
classes of the domain entity, and replace it with its subclass. Doing that means the violation,
because it was poorly designed if that requires the replacement of the existing parent class
with its subclass. 

One particular direction to solve this might be to allow extension, and using aggregation.
Aggregation allows our classes to instantiate their instances with different values. 
So values here might be parent class of the domain entity , and there might also be 
a subclass of the same domain entity. 

With composition, we would have to modify the class literally remove the existing instnatiated class,
with another subclass of it. This is violation. But even if we use the composition, we
might introduce the setters as well, to set another value to that attribute. In that case, 
even tho we have the composition, at any time we can override that attribute.

With aggregation, the class receives the value during the instantiation of the instance.
Tho even with aggregation, we could allow the setters, to even then override them. 

So what is the difference between the Composition and Aggregation in that case, if for both of them
we could provide the setters. The difference is that Composition means, that attribute
is part of that class, meaning it can not exist independently of that class. 
It is the core part of it, while aggregation means, that attribute can be standalone object
itself, while also can be passed to the function as an attribute.


- I want to have one `Core Domain` banking system logic (scope: more specific, still broad).
- I want to have multiple ways to `reuse`: provide interfaces to the same core. (scope: specific, still broad). 


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
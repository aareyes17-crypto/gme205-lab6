# LABORATORY 6: From UML Class Diagram to Python Code
---
## Description
This laboratory applies Object-Oriented Analysis and Design (OOAD) by translating a UML class diagram into a working Python system. It focuses on identifying core objects, assigning attributes and behaviors to the correct classes, and implementing meaningful relationships between them.

---
## REFLECTION
---
### Part B.2 Questions
---
1. Why does SpatialObject own geometry?
- SpatialObject owns geometry because all the spatial entities share a location or shape and need location data to function. Methods like distance and intersection rely on this so having geometry in the base class ensures that every object can use it. This also avoids repeating the same attribute in each subclass while making the data automatically available to all of them.
---
2. Why should distance_to() not be rewritten in every subclass?
- The distance_to() should not be rewritten in every subclass because all of the spatial objects use the same logic to compute distance. Keeping it in the base class ensures that every object calculates distance the same way. This also avoids duplicating the same code in each subclass and reduce errors.
---
3. How does this support abstraction and reuse?
- This supports abstraction by keeping common spatial logic in one base class instead of spreading it across multiple classes. The subclasses can focus on their own properties and behaviors without dealing with the shared functions. It also supports reuse by allowing subclasses to inherit and directly use the methods defined in the base class.

---
### Author
- Audrey Marie Justine A. Reyes
- MS Geomatics Engineering (GeoInf)
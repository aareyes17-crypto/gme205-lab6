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
### Part B.4 Questions
---
1. Did I include the important attributes?
- Yes, I included all the important attributes from the UML diagram. The Parcel class includes parcel_id, area, and zone. The Building class includes building_id, height, and usage. The Road class includes road_id, length, and road_type.Lastly, the Household class includes household_id, num_people, income, and tenure_type. Each object stores all the data it needs based on the design.
---
2. Did I place them in the correct class?
- Yes, I placed each attribute in the class where it belongs based on its meaning. Attributes related to land, such as area and zone, are in the Parcel class. Attributes related to structures, such as height and usage, are in the Building class. Attributes related to roads, such as length and road_type, are placed in the Road class. Lastly, Household-related data such as income and num_people are placed in the Household class. This separation reflects the real-world roles of each object and keeps their responsibilities clearly defined.
---
3. Did I avoid putting unrelated data into this object?
- Yes, I avoided putting unrelated data to any class, and each class only contains attributes relevant to its purpose. The Parcel class did not include income or height, because those belonged to Household and Building. It also did not include length or road_type, beause it belonged to the Road class. For the Household class, it did not contain spatial attributes like area, geometry, or road-related attributes, since it is not a spatial object. By ensuring that only relevant attributes are included per class, this keeps each class focused and avoids mixing unrelated types of data within a single object.
---

---
### Author
- Audrey Marie Justine A. Reyes
- MS Geomatics Engineering (GeoInf)
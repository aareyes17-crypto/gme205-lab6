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
### Part B.6 Questions
---
1. Does each spatial class inherit from SpatialObject?
- Yes, the spatial classes Parcel, Building, and Road inherit from SpatialObject, allowing them to share a common structure and access the same spatial properties and behaviors. By using inheritance, the design ensures that all spatial objects remain consistent and follow the same design defined in the base class. The Household class is not included in this inheritance because it is not a spatial object and does not require geometry or shared spatial behavior.
---
2. Does each one call super().__init__(geometry)?
- Yes, the spatial classes Parcel, Building, and Road call super().__init__(geometry) in their constructors, allowing the geometry attribute to be properly set up from the parent class. This ensures that all spatial objects store their geometry in a consistent way and can use it for shared spatial operations. By using this approach, the subclasses reuse the same initialization logic instead of redefining it, which keeps the code clean and organized. The Household class does not call this method because it does not inherit from SpatialObject and does not contain spatial data.
---
3. Are shared methods inherited instead of rewritten?
- Yes, the shared methods distance_to() and intersects() are inherited from SpatialObject instead of being rewritten in each subclass. This allowed spatial classes such as Parcel, Building, and Road to use the same logic for spatial operations. This also prevented duplication of code and ensured that all spatial objects behave consistently when performing distance and intersection calculations. By inheriting these methods, the subclasses reused the same implementation defined in the base class, which kept the code clean, organized, and easier to maintain and update. The Household class is not included in this because it did not inherit from SpatialObject and did not require spatial methods.
---
### Part D.2 README Documentation
---
### *Part B Summary*
---
- In Part B of this Laboratory Exercise, the Lecture 6 case study was implemented in Python by following the object-oriented design described in the lab instructions. The design concepts were interpreted and converted into classes, attributes, methods, and relationships. The parent class in the system is SpatialObject, which was created to store shared spatial data and behavior. It serves as the base class so that common functionality is implemented once and reused by other spatial classes. The classes that inherited from it are Parcel, Building, and Road, allowing them to access shared spatial methods without duplicating code and ensuring consistent behavior across the system. The shared methods implemented in the base class are distance_to() and intersects(). These were used by the spatial objects: Parcel, Building, and Road to perform distance calculations and intersection checks. Since these methods are in the parent class, each subclass can reuse the same logic without redefining it. This helps maintain consistency and keeps the implementation easier to manage. Several relationships were implemented to reflect how objects interact in the system. Building is associated with Parcel, Household is linked to Building, and Road is adjacent to one or more Parcel objects. These relationships were implemented using object references, allowing the objects to directly interact with each other and form a connected system instead of being isolated classes.
---
### *Part C Summary*
---
- In Part C, my own UML diagram from Prelaboratory 6 was implemented in Python by converting the defined classes, attributes, methods, and relationships into code. The classes in my model are SpatialObject, Parcel, and OutputManager. SpatialObject serves as the base class for shared spatial behavior, Parcel represents the main entity in the system, and OutputManager handles the display and reporting of results. The attributes that became object state were parcel_id, owner, and geometry in the Parcel class, geometry in the SpatialObject class, and results in the OutputManager class. These attributes were taken directly from the UML diagram, and were placed inside the constructors to represent the state of each object. The methods that became behaviors were compute_area(), get_bounds(), detect_overlap(), and load_from_geojson() in the Parcel class, as well as display_results(), export_geojson(), and generate_report() in the OutputManager class. The shared spatial methods such as intersects() and area() were implemented in the SpatialObject class and inherited by Parcel. This allowed consistent spatial operations across the model. The hardest relationship to implement was the interaction between multiple Parcel objects during overlap detection, since each parcel needed to be compared with others while avoiding comparing itself. This required going through a list of parcel objects and making sure a parcel does not compare itself when checking for overlaps. This was handled by checking object references and using a threshold-based condition. 
---
### UML Evidence
---
My UML diagram is stored at: [uml/own_uml.jpg](uml/own_uml.jpg)
---
### **FINAL REFLECTION**
1. What was easier to translate into code: attributes, methods, or inheritance?
- The easiest to translate into code were the attributes, since they directly became variables inside the constructors of each class. In the Parcel class, the attributes: parcel_id, owner, and geometry from the UML were directly assigned as self.parcel_id, self.owner, and self.geometry in the constructor. The SpatialObject class stores the geometry attribute, while the OutputManager class includes a results list to handle output data. These attributes simply represent the state of each object, so they did not require complex logic to implement. Compared to methods and inheritance, attributes were easier to translate because they were clearly defined in the UML and only needed to be assigned to each object without additional conditions or behavior.
---
2. Which relationship in your UML was hardest to implement?
- As I have already mentioned in my Part C Summary, the hardest relationship to implement was the interaction between multiple Parcel objects during overlap detection. This is because each parcel needed to be compared with other parcels while avoiding comparing itself. This required going through a list of parcel objects and adding an extra condition in the logic. This made the implementation more complex because it required careful handling of object references to ensure correct comparisons, along with a threshold-based condition.
---
3. Did your code exactly match your UML, or did you revise some parts during implementation?
- The code mostly matched the UML diagram, but some small adjustments were made during implementation to ensure that the system works correctly. One change was in the overlap detection method, it needed to be refined so that it functions properly when comparing multiple Parcel objects. This change included adding conditions to prevent a parcel from comparing itself and ensuring that comparisons between objects are handled correctly. While these changes required modifying parts of the logic, they did not change the overall design of the UML. These changes actually helped improve the accuracy and reliability of the system, making the implementation more stable and consistent with the intended behavior.
---
4. What did you learn about the importance of OOAD from this exercise?
- From this laboratory exercise, I learned that OOAD is important because it provided a clear structure before coding, which made it easier for me to organize classes and assign responsibilities correctly. By defining the classes, attributes, methods, and relationships in advance, it became clearer to me how each part of the system should behave and interact. Having a well-defined design helped guide my implementation and reduced confusion while writing the code. In my experience during this laboratory exercise, OOAD helped me maintain consistency throughout the implementation process because the design served as a reference when I was implementing features. It also made the system easier for me to understand, since each class had a specific role and responsibility. This was especially useful when I was working with multiple related classes, as it prevented me from mixing responsibilities and helped keep the structure organized. Overall, OOAD helped me make the implementation process more systematic, organized, and easier to manage from design to implementation.
---
### Author
- Audrey Marie Justine A. Reyes
- MS Geomatics Engineering (GeoInf)
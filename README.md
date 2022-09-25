# First
1.	Goal
Our goal in this assignment is to become familiar with OpenBIM concepts. Working on this started with defining the use case – Structural aspects of a building. Having required standards we will build an optimal model for those requirements. Then we will analyze it we would like to create an effective structural system. Next, we have done several exercises that mainly consist of collaborating with IFC file format using blender and associated Open BIM standards. For an easier understanding of what we are thinking about in our use case, we created a BPMN diagram.

2.	Use case
Our chosen use case is the Structural aspects of a building. We would like to focus on its technical aspects such as geometry and properties so structural engineers and contractors are the people to whom this use case is addressed for. It requires disciplinary validation structural analysis and material properties analysis. It is a forecast type of analysis where communication between processes is needed. This structure will avoid lost data in file exchange when we use FEM software. Speaking about structural elements in a building we are thinking about bearing elements that we would like to highlight in our script in the IFC file. We use already created similar systems as a disciplinary analysis for our solution. Before we can start our use case some others have to be done such as architecture (they will be in IFC model). After we finish we can provide gained solutions to other waiting use cases such as Cost Estimation, Fire Safety, and Material LCA. Inputs (material of interest, code, and regulations) and outputs (stakeholder feedback)  are easy to see in this scheme. Information in IFC model: Heating & Cooling, Architectural, Structural, Plumbing, Usage, Electrical, Merged, and Mechanical are both input and output because we receive them from other stakeholders and use them in the material of interest retrieve.

3.	Process
Business Process Model and Notation is a popular way of showing how the described process is carrying on. Data flow and communication between involved members are some of the information that is in this document.
We extracted three main areas:
•	Process – where we put the most important parts of the route from starting point 	where we define the purpose/use of our work to getting the final structural model 	where we check our solution on the way. The most important one is about satisfying 	the condition. 
•	Reference information – in this part there is an important element of the whole 	process which is “code and regulations”. This block informs us about rules that we 	need to follow and this is judging coefficient in checking condition satisfying. Building 	specification is also included in part of the diagram together with feedback from 	other stakeholders. 
•	Information exchange – we are assuming providing information with other 		stakeholders about the final structural model and the prototype of this model too. 	From them, we receive feedback that gives us the ability to make improvements in 	IFC model which is our input data to the “material of interest”.  

4.	Information Exchange
For our process, we need detailed information about construction materials e.g. load bearing and stabilizing layer. The Level Of Development should be 400 but a lower rating could also be useful. Precise values are 400 for Level Of Information, 300 for Level Of Reliability, and 325 for Level Of Geometry.

5.	Workflow

Usually, the first step would be to get source data from reference files/assumptions. From that data, we will take necessary parts that we want to submit in our calculation process for instance: bearing length. Then we will be able to express loads that are carried through the structure. If we get results that will suit our expectations workflow circle have done its job. Otherwise, some changes should be made.   
6.	IFC
The IFC elements and entities that will be required for this particular use case:
-	IfcBeam (source element: All beams; Type Name: Found directly as a property of the entity)
-	IfcSlab (source element: All slabs; Type Name: Found in Pset ConcreteElementGeneral)
-	IfcWall (source element: Exterior, Interior; Type Name: Found in Pset   	ConcreteElementGeneral)
-	IfcWallStandardCase (suorce element: Exterior, Interior; Type Name: Found in Pset ConcreteElementGeneral)
-	IfcMaterial (source element: Found directly as a source; Type Name: IfcMaterial)
-	IfcLocation (source element: All areas; Type Name: Found in area properties)

7.	Delivery
Using a text editor that is compatible with python adding an ifcopenshell package with blenderbim add-on is required. And with that, getting important use case data (from provided ifc file) is easy to do. Functions give us the possibility of further investigation on more detailed information.    

8.	Summary
BPMN diagram was used for graphical use case description where we have shown information exchange between stakeholders and how this fact is developed in our process. This way of data management was useful for targeting the scope of our script. Despite checking the most important requirement (satisfying the condition) this process is also checked for optimal aspects. Any changes that could occur will be taken into account.  

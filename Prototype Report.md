# Prototype \- SSH Group Ordering 

Saad Mustafa (2673835), Hasaan Afroze (2602085), Aarij Omar Khan (2525401), Fizan Shamjith (2603883)

## Report  **What was accomplished?**

Our group selected the Joint Group Ordering problem and used our colleague Fizan’s EDR to base our prototype off of. When starting the prototype, we aimed to implement all of the features listed in the EDR of the Group ordering page in our prototype. We managed to accomplish a fully functional full stack application that emulated the processes involved in joining a group order as listed in our chosen EDR. Our prototype utilized a database that was integrated to the back-end API and a user friendly frontend interface, ensuring a seamless experience for users.

Although we could not create our prototype to the full complexity of the joint group ordering as described in the EDR, we were successful in emulating it on a smaller and more manageable scale. We had to omit certain functions of the project described in the EDR from our prototype such as the notifications system and live tracking feature. We did this as the aforementioned features were not essential to the joint group ordering function and increased the complexities of the programs significantly. 

Despite having to simplify certain functions, our prototype was a good indication to other software developers that the SSH joint group ordering function was a viable and achievable design. Our prototype demonstrated that the SSH Joint Group ordering feature can be implemented on the larger scale with all of its functionality remaining as well as retaining the functions we choose to omit for the sake of necessity.

### **How it was accomplished?** 

We aimed to break down and delegate tasks to each of the engineers in our group by utilizing the AGILE software engineering methodology. We broke our project down into sprints in which we focused on separate aspects of the prototype such as: Back-end Development which Saad and Hasaan Handled, Front-end development which Fizan handled, and the creation of API endpoints using FAST API framework, creating  pytests, implementing CI pipelines, implementing poetry for dependency management and containerizing the prototype  was done by Aarij.  Once the bigger aspects of the full stack were broken down and delegated to each member we assigned each task like so:

Planning and task management of each task was done by creating issues on GitHub which were assigned to each member according to their responsibilities ie:

- Front-end Development: Designing UI for order creation and marketplace  
- Back-end Development: Connect back-end to database to fetch data  
- Testing and Debugging: Ensuring functionality and fixing bugs. 

We accomplished our task by first creating a functional command line program that simulated the joint group ordering. First a joint order with hard coded students and products in it is created, and then the user has the freedom to enter their name and join the order and select from a plethora of different options: View cart, browse the marketplace and add or remove items, top up the wallet, view the order summary, and checkout. With the basic idea of how our program should work, we started to build and populate our database that stored products along with their price, name and categories. We used generative AI to create records and populate our database by feeding it a couple examples of how different products should look (ie: “give me 100 products in the format:{Product ( id, name, price, category)}” ). While the back-end was being worked on, the front-end engineer was working on developing a simple front-end implementation using React-Native with logic from the back-end. Once that had been created correctly and we were happy with it, we connected both the front and back ends using the FastAPi framework.

We tried to frequently commit to GitHub to ensure that each member had the latest version of the code and could implement it for their part of the prototype as needed. This ensured that the version of the code that each member worked on was the latest one. Each member had a separate branch to which they committed their work to, and once it was reviewed by all members and was seen fit to be adapted to the overall project, we pushed it onto the main branch.

We faced our first challenge when trying to connect our database to the back-end. The products from the database were not being fetched in the correct format and thus the back-end would not print it correctly, this in turn added a range of different issues with the code. We overcame this issue by watching a few videos on YouTube to correctly connect a database to python code.

Furthermore, during the first few days of creating the prototype we found a challenge with working at times in which each member was available to contribute as we initially worked online. We managed to overcome this issue by meeting daily or every two days and arranging sprints. This improved our feedback loop and gave clarity of the direction that the prototype needed to go in. During these meetings we clearly identified functions that our prototype absolutely needed like, the marketplace, cart, checkout page, just to name a few. 

In our meetings, we found ways in which adapting some features may be illogical and not be as viable for the prototyping phase. We found during multiple stages of creating the prototype that some functions listed in the EDR were not viable to create for us as when we tried to implement them we would spend a lot of time on features that were not essential. One of these functions being the notifications system, as creating and implementing  a system that sends real time updates and alerts to a user would add a layer of complexity to the prototype that would have been very difficult to overcome. Similarly, with the real time updates of deliveries which would have also been a challenge to implement. We decided to leave such features out and only focus on the pivotal features of the group ordering such as starting a group order, browsing the marketplace, managing the cart, and checking out with split delivery costs.

###  **Log of implementations:** 

* Back-end  
  * Created Products class & associated methods  
    * Created constructor  
  * Created Students class & associated methods  
    * Created constructor  
    * Created methods : canAffordProduct, addToCart, removeFromCart, viewCart, getCartTotal, checkout  
  * Created Group Order class & associated methods  
    * Created constructor  
    * Created methods: addParticipant, calcIndividualCost, displayOrderSummary  
  * Created Marketplace class & associated methods  
    * Hardcoded products to be used for the command line version  
    * Created methods: fetchProducts  
  * Created Main  
    * Display the menu  
    * Take the user choice and execute that command  
    * Create a group order with dummy values  
    * Randomize products that the dummy values add to give variance of each test run  
  * Generated csv file  
    * Generated csv file for products and imported it into the database  
  * Created Aiven database  
    * Used Aiven to host the database online  
  * Created Method to fetch products from database  
    * Connects to the database  
    * Query to fetch the products from the database  
  * Created Method to save group orders to the database  
    * Connects to the database  
    * Query to insert the group orders and participant data into the database  
* Front-end  
  * Created a React Native project   
  * Made a basic home screen  
    * Added group order section in the home screen  
    * Edited the explore section to talk about other SSH features  
  * Created a basic profile page  
  * Created a new page for the group order  
    * Added a button to simulate joining a group  
    * Added a button to simulate creating a group  
    * Added a start group order button that leads the user to the marketplace page  
  * Created a new page for marketplace   
    * Tested the page with sample data to see if it pulled products from the FastAPI backend and displayed it to the user   
    * Implemented functions that allow users to add products to cart and see their cart  
  * Created a checkout page  
    * The user’s cart is displayed   
    * Flatmates and their carts are randomly generated to add to the group order  
    * Delivery and service fee is displayed and shared among group members  
    * Added user’s wallet and functionality to let users to manage their wallet balance and use it to checkout successfully 

**Screenshots of the Command Line implementation: (read from left to write)**

### 

### 

### 

### 

### 

### 

### 

### 

### Peer Reflections: 

Mohammad Saad Mustafa  \- Peer reflections on colleagues 

**Reflection on Mohammad Fizan Shamjith**

Fizan was in charge of creating and implementing the front-end of our joint group order prototype, he used the react-native framework to create it. Working with him has been a positive experience. 

During the development of the front-end it was motivating to see how Fizan was able to learn the fundamentals of react-native watching videos and reading documentation, a framework that he had amateur experience in, and apply it to the project. Furthermore, since we used Fizan’s EDR to implement the prototype, he explained it very well to ensure that our colleagues that chose the other SSH task for their EDR’s understood the Joint group ordering problem statement well and how his EDR and our prototype planned on fixing it.

However, an area in which Fizan lacked was that when facing an error, he would give up sometimes and wait a bit to fix it. This would leverage other colleagues' ability to work on the prototype as the tasks would sometimes depend on his code. I think this happened due to him burning out while working and could have been fixed by taking regular breaks or switching tasks when he would get too burnt out.

**Reflection on Hasaan Afroze**

Hasaan worked on the back-end with me and helped to implement some key tasks that proved to be very useful in the utility of the back-end. He was in charge of creating and populating the database as well as integrating it to the backend.  Since Hasaan and I worked alongside in implementing the back-end we had many meetings in which we tried to coordinate our codes and resolve issues. 

Hasaan was tasked with connecting the database he made with my backend code to fetch products from it. During my time working with him, I noticed that he was always diligent with implementing new changes to his code as I would make various changes to my base code, which his code relied on. This showed his amazing level of communication skills as he would effectively understand and alter his code based on my feedback and changes.

However, an area that I would like to see Hasaan improve in was his allocation of time to perform lower priority tasks such as making a company logo. Although the logo was not a pivotal part of our project, he proposed to make it as soon as possible. In the future, I recommend that Hasaan should effectively prioritize higher priority tasks first and keep tasks that have little impact to the project delivery for last.

**Reflection on Aarij Omar Khan**

Aarij played a crucial role in the development and management of our prototype as a whole. He was in charge of connecting the front and back ends using the FastAPI framework.

Aarij’s strengths lay in the technical part of the project as he took on the job of assigning each colleague their respective roles as well as monitoring them. This played a huge part in the effective management of our prototype. Furthermore, Aarij took the initiative and created the pytests to test our code, connect the back-end and front-end together, and deploy continuous integration tools to our project to ensure it is usable on all systems. Aarij’s ability to adapt to a tricky situation and take charge really helped the whole team when we were stuck and impacted the prototype.

However, during the initial stages of the project, Aarij did not provide a lot of hands-on experience due to him focusing more on managing each colleague which put more stress on the rest of the members as we had to do a bit more work. However, after speaking to Aarij about this he took charge and provided more support on the technical side. Moving forward, I am positive that Aarij will provide support with different aspects of the project from the moment it has started while also balancing his role as the monitor.

Hasaan Afroze – Peer reflections on colleagues  					

**Reflection on Mohammad Saad Mustafa**			

Saad played a crucial role in developing the main backend for the group ordering page. He implemented the core features such as joining a group order, managing the shopping cart and viewing the order summary. His contributions were essential in bringing the prototype together.

One of Saad’s strengths is his dedication to making improvements and refining his code. He is always looking for ways to refine things which can lead to better solutions. However, this can also be a weakness. His frequent changes to the base code, after I had implemented my parts, caused some disruptions. I had to adjust my changes multiple times to match the new updates to his code, which resulted in additional back-and-forth between us and slowed down progression.

In the future, I would suggest that Saad focus on finalizing the code before making further adjustments. This would reduce unnecessary code reworks, streamline development, and allow for smoother collaboration.			

Overall, Saad’s commitment to improving the project was valuable and helped enhance the code. With a bit more focus on finalizing core components before making updates, future collaborations would be more efficient and smoother. His attention to detail and efforts to improve the work were important to the project’s progress.

					  
**Reflection on Mohammad Fizan Shamjith**				

Fizan was responsible for developing the front-end of the group ordering system, and he did a good job creating a user-friendly interface. In addition to the front-end design, Fizan also helped connect the front-end to the back-end, ensuring they worked together smoothly. This was important for making the system function properly.					

One of Fizan's strengths is his ability to quickly learn and apply new tools, like React Native, during the project. While he wasn’t fully proficient with React Native at the start, his willingness to learn and figure things out allowed him to make steady progress. He took the initiative to learn and apply new tools as needed, which helped drive the front-end development forward and made a valuable contribution to the team's progress.				

However, one area for improvement is that Fizan sometimes focused more on the design and functionality of the front-end without fully considering how it would integrate with the back- end. This occasionally led to delays when the front-end needed adjustments to work with the back-end logic. In the future, it would be helpful if Fizan worked more closely with the back-end team during the development phase to ensure smoother integration from the start.				

**Reflection on Aarij Omar Khan**				

Aarij was responsible for integrating the back-end with the front-end using the FastAPI framework, creating tests, and handling Docker tasks. His technical contributions were crucial, especially when we encountered issues with the integration of the front-end and back-end, where he played an important role in resolving those problems.					

One of Aarij’s strengths is his ability to delegate tasks effectively and manage the overall project organization. He was good at assigning tasks, keeping track of the team, and managing Git workflows, which helped the team stay organized and focused on their respective tasks.		

However, while Aarij was effective in delegating tasks, he wasn’t as involved in the technical work during the early stages of the project. The need for his involvement became clear when we encountered challenges connecting the front-end and back-end. Aarij then stepped in and took responsibility for establishing the connection, using the FastAPI framework to set up the necessary endpoints.				

In future projects, it would be helpful for Aarij to be more involved throughout the development process, rather than waiting until issues arise. This would contribute to a more efficient workflow and help identify problems earlier. Aarij’s ability to organize the team and his support during the integration were important to the project's success. 

Mohammad Fizan Shamjith– Peer reflections on colleagues  

**Reflection on Aarij Omar Khan**

Aarij has been a straightforward and reliable teammate. Early on, he took the initiative and stepped up as a leader, which helped the team focus and set clear priorities. By assigning us roles after discussions with the group, he gave us a clear direction and ensured that everyone had a defined contribution. Aarij worked closely with me to integrate the backend with my front end, tackling many challenges despite both of us having limited prior experience with such integrations. He also shared useful resources, which helped us make the code compatible and functional.

Aarij also took charge of setting up our GitHub repository, assigning tasks, and ensuring we regularly committed and pushed updates. This helped solve a recurring issue where we all worked with outdated code from each other, which wasted a lot of time as that code could not be used later.

While the rest of us focused on coding and building the project, Aarij dedicated time to understanding Docker and continuous integration. At first, it seemed like he wasn’t as hands-on as the rest of us, which made the workload feel a bit uneven. However, his focus on these aspects and his technology recommendations, like using FastAPI, did eventually streamline our workflow and improve our efficiency.

In the future, I’d want Aarij to communicate more clearly about his behind-the-scenes work. Sharing updates on progress with tools like Docker or continuous integration would help the team see the value of his contributions in real time which would improve team coordination. Overall, Aarij was a vital member of the team and played a key role in ensuring the project’s success.

**Reflection on Mohammad Saad Mustafa**

From the very beginning, Saad has been an invaluable team member as he worked effectively to develop our minimum viable product (MVP) throughout the project. His work on the command-line version of our prototype gave the team a clear starting point and made it easier to understand what needed to be implemented in my frontend. He consistently added new features to the command-line version and kept the team updated on his progress, which helped incorporate those features into our own code.

One of Saad’s greatest strengths was his ability to simplify the core functions and present them clearly. This made it much easier for the rest of us to refer to his work when writing our own Code.

However, a challenge we faced was that Saad occasionally missed some of the scheduled meetings. This made us unsure of the status of his work and how it aligned with the rest of the team. In the future, it would be really helpful if Saad could prioritize attending meetings and sticking to agreed schedules. This would help improve communication, trust, and ensure the entire team is on the same page. Overall, Saad’s contributions have been really helpful because he provided us with the core logic needed in our project.

**Reflection on Hasaan Afroze**

Hasaan has stood out to me during our project due to his consistency in being a very reliable and efficient team member. He was responsible for creating the Aiven database, which stores product information, and he handled SQL queries in PostgreSQL to manage group orders and fetch products. His backend work was important in ensuring that our project’s data management was functional.

Hasaan’s greatest strengths is his punctuality and efficiency. He consistently completed his tasks on time, which made the workflow smoother for the rest of the team. Knowing that he would handle his responsibilities without any issues helped keep the project on track.

However, one area where Hasaan could improve is communication. Most of the time, I wasn’t aware of what he was working on, as he primarily coordinated with Saad as they both worked on the backend. This lack of communication made it harder to fully understand his contributions and integrate his work with other parts of the project. In the future, I would encourage Hasaan to collaborate more actively with all team members and share brief updates regularly, on his progress.

Aarij Omar Khan – Peer reflections on colleagues  					

**Reflection on Hasaan Afroze**  
Hasaan worked alongside Saad as the database engineer of this project. His main responsibility was to integrate database functionality with our backend. 

As database engineer, Hasaan was able to not only create a database that could interact with our FAST API backend, but also he used problem-solving skills to find a way to host the database on a server. This shows that Hasaan has foresight and is able to ascertain how microservices like the one we are making fit into the larger system, as the SQL injections he made for the console version of the microservice were able to be used by me when creating the API endpoints. Moreover, he has shown great collaborative skills as he would correspond with Saad regularly to ensure that his designs would integrate with the core logic of the program.

To enhance his ability in a software engineering team I would strongly advice Hasaan to work on his documentation and effectiveness in using version control. Hasaan was not that confident with git commands which resulted in him using GitHub extensively for commits, pull requests. Although he followed proper versioncontrol etiquettes, his usage of Github solely and not the terminal meant that development on his branches was slow. Had he been working completely on his own on the backend this approach would prove to be quite troublesome. Perhaps he should work on some more individual projects to get better aligned with using git commands effectively. All in all, it was a pleasure working with Hasaan. 

**Reflection on Mohammad Fizan Shamjoth**  
Fizan was the front-end engineer for this project. He utilized the React Native Framework. Also, Fizan’s engineering design review was used to aid in the development of our prototype.

Fizan demonstrated great communication skills by clearly and succinctly explaining his EDR design which allowed us to plan and streamline the prototype development process effectively. Additionally, he showed admirable perseverance as despite not having much experience with front-end development, he undertook the challenge of designing and then creating a UI that struck the middle grounds of being basic enough to work for our prototype and already having enough complexities for the eventual integration of the group ordering microservice in our systems. 

However, despite making an effective front-end, Fizan did at times spend time implementing certain features in the front end which were not as integral to the prototype. For instance, initially, he created a login page and other app elements. This time could have spent that time working on some other component in the design process. For instance, he could have supported Hasaan in database management or even helped me in creating the testing API endpoints. Hence, in the future, I would advise Fizan to look specifically at the requirements of the issue at hand and not get carried away with developing his work beyond its means. Overall, I look forward to working with Fizan in the future. His willingness to learn technologies is one that any team would be glad to have.

**Reflection on Mohammad Saad Mustafa**  
Saad worked alongside Hasaan on the backend logic of our program. Essentially he made the minimal viable product of our microservice.

Saad demonstrated great creativity as he expertly designed the logic of our microservice which was able to be used by me to create the API endpoints for the FAST API backend. He has shown attention to detail as he would constantly be refining his logic and code and making sure there were no errors to its implementation. Furthermore, he was able to articulate  the main features of the microservice and simulate those that were not as significant. This was very important as it helped streamline the development of the prototype and ensure that he did not spend time implementing logic that is not directly related to the microservice. 

Important to note that initially, I had assigned the tasks of creating the backend to Saad. However his unfamiliartity with API endpoints propelled him to not being that confident in creating them, hence me taking over. Therefore, in the future I would advice Saad to work more out of his comfort zone as in the future he may be tasked with working with a technology he has not learnt and by taking on such challenges regularly it can help him become a better engineer. Overall it was a pleasure working with Saad and I hope he can take the feedback i give and apply it in the future


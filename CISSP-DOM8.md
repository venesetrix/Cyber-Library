# CISSP Domain 8 - Software Development Security

Software Development Life Cycle (SDLC)
    • Phases
        ○ Requirements gathering (functional - what, performance - how well)
        ○ Design (how)
        ○ Development/acquisition - Programmed internally or acquired
        ○ Testing - Verifying the functional and performance requirements
        ○ Operations/maintenance - Implementing, change management, updates
        ○ Retirement/Replacement
    • Development Methodologies
        ○ Waterfall - Structured, sequential, need gatekeeping events (reviews, approvals)
        ○ Incremental - Each iteration is a finished workable product, also called iterative methodology (multiple instances of Waterfall)
        ○ Spiral - Each iteration or spiral is carefully planned. Each new spiral has specific objectives it must meet.
        ○ Prototyping - Customer receives prototypes for testing and approval. A usable version is called an operational prototype. 
            § Rapid prototypes are pieces of code that fills a functional requirement
            § Evolutionary prototypes are built and presented with the intention of incremental improvement through customer feedback
        ○ Rapid Application Development (RAD)
            § The requirements are discovered and built-in as the application is developed and tested
            § 60% solution right now is better than a 100% solution in three years
        ○ Agile
            § Promotes agility in software development that is not restricted by the overuse of structured processes
            § Focus on delivering small increments of functional code
            § Key characteristic of Agile is a user story/a use case from the user's point of view which states the functions, the result and the performance
            § Key agile methodologies:
                □ Scrum - Uses a 2w dev interval called a sprint and a daily scrum meeting
                □ Extreme Programing (XP) - Without the sprints and with more code review (pair programming), where two developers are constantly inputting and checking each other's work. They write test cases before the code is even written
                □ Kanban - Visual tracking of tasks
        ○ DevOps / DevSecOps
            § Integrated dev teams consists of developers and operations personnel
            § Developers and operators can work together to produce code that better meets customer requirements
            § DevSecOps integrates security personnel into the DevOps team
    • Maturity Models
        ○ Formalized model for determining how well organized, defined and managed an organizations development effort is
        ○ Capability Maturity Model Integration (CMMI)
            § Originally developed by Carnegie Mellon University and now managed by ISACA. Provides Measurements and guidance and best practices
            § Six maturity levels
                1) Incomplete - No formal processes
                2) Initial - Development effort is unpredictable and reactive. Often over budget and behind schedule
                3) Managed - Beginnings of a management infrastructure. Basic planning techniques and metrics
                4) Defined - Formal organization standards in place that provide structure.
                5) Quantitatively Managed - Formal processes and extrapolations of data to gain efficiencies and a roadmap for more effective management
                6) Optimizing - Focus on continuous process improvement and long-term software development program strategy
        ○ Software Assurance Maturity Model (SAMM)
            § From OWASP and specially focused on secure software development
            § Broken into five critical business functions. Every function is broken down into three security practices which contain security-related activities.
            § The total of 15 sec practices can be assessed for effectiveness and maturity
    • Operation and Maintenance (O&M)
        ○ Version control is of critical importance
    • Change Management
        ○ Must be a formalized process with structure
        ○ Changes must always be carefully considered, tested and documented
        ○ Change control - Process of controlling and documentation of specific changes in an application. Also referred as software version control.
    • Integrated product team (IPT)
        ○ Is a management technique where people from a variety of functional areas to be involved in the software development process. IPT often use Agile methods
        ○ Consists of team members with expertise in a wide variety of areas.

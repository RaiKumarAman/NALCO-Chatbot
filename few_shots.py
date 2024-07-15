few_shots=[
    {
        'Question' : "How many What is my salary?, ID=1",
        'SQLQuery' : "SELECT Salary FROM employee WHERE ID=1; ",
        'SQLResult': "Result of the SQL query",
        'Answer' : "Your salary is Rs. 80000.00"
    },
    {
        'Question' : "What is my designation and department?, ID=4",
        'SQLQuery' : "SELECT Designation, Department FROM employee WHERE ID=4;",
        'SQLResult': "Result of the SQL query",
        'Answer' : 'Your designation is HR Specialist and department is Human Resources'

    },
    {
        'Question' : "When did I join the company?, ID=10",
        'SQLQuery' : "SELECT JoiningDate FROM employee WHERE ID=10;",
        'SQLResult': "Result of the SQL query",
        'Answer' : "Your DOJ is 2009-08-05"
    },
    {
        'Question' : "What is my highest qualification?, ID=8",
        'SQLQuery' : "SELECT HighestQualification FROM employee WHERE ID=8;",
        'SQLResult': "Result of the SQL query",
        'Answer' : "Your highest qualification is M.Tech"
    },
    {
        'Question' : "What is my phone number?, ID=3",
        'SQLQuery' : "SELECT PhoneNumber FROM employee WHERE ID=3;",
        'SQLResult': "Result of the SQL query",
        'Answer' : "Your contact is 555-123-4567"

    },
    {
        'Question' : "What is my address?, ID=7",
        'SQLQuery' : "SELECT Address FROM employee  WHERE ID=7;",
        'SQLResult': "Result of the SQL query",
        'Answer' : "876 Maple St, Mountainview"
    },
    {
        'Question' : "When am I expected to retire?, ID=2",
        'SQLQuery' : "SELECT Retirement FROM employee WHERE ID=2;",
        'SQLResult': "Result of the SQL query",
        'Answer' : "Your retirement is on 2055-11-25"
    },
    {
        'Question' : "What is my current role and salary?, ID=4",
        'SQLQuery' : "SELECT Designation, Salary FROM employee WHERE ID=4;",
        'SQLResult': "Result of the SQL query",
        'Answer' : "Your designation is HR Specialist and salary is 75000.00"

    },
    {
        'Question': "How can I be reached by phone?, ID=4",
        'SQLQuery': "SELECT PhoneNumber FROM employee WHERE ID=4;",
        'SQLResult': "Result of the SQL query",
        'Answer': "Your contact is 222-333-4444"
    },
    {
        'Question': "When did I start working here?, ID=6",
        'SQLQuery': "SELECT JoiningDate FROM employee WHERE ID=6;",
        'SQLResult': "Result of the SQL query",
        'Answer': 'Your DOJ is 2015-09-15'

    },
    {
        'Question': "Deptartment, ID=7",
        'SQLQuery': "SELECT Department FROM employee WHERE ID=7;",
        'SQLResult': "Result of the SQL query",
        'Answer': 'Your department is Finance'
    },
    {
        'Question': "Designation, ID=9",
        'SQLQuery': "SELECT Designation FROM employee WHERE ID=9;",
        'SQLResult': "Result of the SQL query",
        'Answer': 'Your designation is Quality Assurance Specialist'

    },
    {
        'Question': "Salary, ID=1",
        'SQLQuery': "SELECT Salary FROM employee WHERE ID=1;",
        'SQLResult': "Result of the SQL query",
        'Answer': 'Your salary is Rs. 80000.00'
    },
    {
        'Question': "Wages, ID=1",
        'SQLQuery': "SELECT Salary FROM employee WHERE ID=1;",
        'SQLResult': "Result of the SQL query",
        'Answer': 'Your salary is Rs 80000.00'
    },
    {
        'Question': "Who are my Collegues, ID=3",
        'SQLQuery': "SELECT Name FROM employee;",
        'SQLResult': "Result of the SQL query",
        'Answer': 'John Doe, Jane Smith, Michael Johnson, Emily Brown, David Lee, Sarah Wilson, Kevin Martinez, Linda Thomas, Mark Anderson, Anna Garcia'
    },
    {
        'Question': "Contact, ID=4",
        'SQLQuery': "SELECT PhoneNumber FROM employee WHERE ID=4;",
        'SQLResult': "Result of the SQL query",
        'Answer': 'Your contact is 222-333-4444'
    },
    {
        'Question': "Recovery Loan, ID=9",
        'SQLQuery': "SELECT Car_Loan+ Home_Loan FROM employee WHERE ID=9;",
        'SQLResult': "Result of the SQL query",
        'Answer': 'Your recovery loan is Rs. 1000.00'
    },
    {   
        'Question': "Loan, ID=9",
        'SQLQuery': "SELECT Car_Loan+ Home_Loan FROM employee WHERE ID=9;",
        'SQLResult': "Result of the SQL query",
        'Answer': 'Your total loan is Rs. 1000.00'

    },
    {
        'Question': "About, ID=10 ",
        'SQLQuery': "SELECT AboutCompany FROM employee WHERE ID=10;",
        'SQLResult': "Result of the SQL query",
        'Answer': 'NALCO, officially known as National Aluminium Company Limited, was established in 1981 and is headquartered in Bhubaneswar, Odisha, India. Specializing in the mining, refining, and production of aluminum, NALCO operates mines, alumina refineries, and aluminum smelters across India. The company plays a pivotal role in the entire value chain of aluminum production, from extracting bauxite to refining alumina and smelting aluminum.'
        
    },
    {
        'Question': "company name, ID=10 ",
        'SQLQuery': "SELECT Company FROM employee WHERE ID=1;",
        'SQLResult': "Result of the SQL query",
        'Answer': 'National Aluminium Company Limited (NALCO)'
        
    },
    {
        'Question': "Headquarter, ID=10",
        'SQLQuery': "SELECT Headquarters FROM employee WHERE ID=1;",
        'SQLResult': "Result of the SQL query",
        'Answer': 'Headquaters is situated at Bhubaneswar'
    },
    {
        'Question': "Hi, ID=10",
        'SQLQuery': "SELECT Name FROM employee WHERE ID=1;",
        'SQLResult': "Result of the SQL query",
        'Answer': 'Hello, John Doe, how may i help you?'

    },
    {
        'Question': "Hello, ID=1",
        'SQLQuery': "SELECT Name FROM employee WHERE ID=1;",
        'SQLResult': "Result of the SQL query",
        'Answer': 'Hello, John Doe, how may i help you?'
    }
]
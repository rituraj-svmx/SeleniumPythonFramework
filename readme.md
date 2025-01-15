# create Browser invocation fixture(scope='class') in conftest . Hold the driver obj 
in request.cls.driver
# Create a BaseClass and use this fixture
# inherit the BaseClass where ever required 
## Pass command line options to select browser at runtime >conftest
# pageObject design pattern : 
> craete page for each screen 
> store locator in a tuple form 
> create a constructor of this class and create object for this class in test class
> smart way of creating object > get a jucntion point b/w the page and do inside the fuction
# Implement data driven mechanism by removing hard coded data from tests 
>create a fixture (params=[()])...and fetch the data based on the index
# for better readability use Disctionary and take the data from the seperate class 
> instead of tuple use (params=[{}])
> Craete a TestData package and create a class and store the data for a specific 
> page in a variable and call that vairable in params=<class.variablename>
# Attach logs > crate a getLogger() funtions in BaseClass : Provide the right path
# Generate html Report > pip install pytest-html > cmd line >pytest --html=report.html
# Attach screenshot in a report upon failures 
> add a function in conftest
> global driver (so that in capture screenshot function)
# Integrating framework to Jenkins 
> download jenkins.war file 
> cmd > run : java -jar jenkins.war -httpPort=8080
> localhost:8080 or IP4:<Port>
> Create new item > freestyle project > copy workspace from IDE > select use custom ws 
> Pass Browser name , env at run time. To achieve this : select This project is 
> parameterized > add choice parameter > in command replace value with "$<varname>"
# Create Jenkins junit result with pytest commands
> python -m pytest --html=<path> -v --junitxml="result.xml"
> Go to post build actions and select generate junit result
# Read write data from excel in pytest framework
>pip install openpyxl
> workbook = openpyxl.loadworkbook("<path>")
> sheet = workbook.active
> cell = sheet.cell(row=1,column=2)
> cell.value
# create a static method by @staticmethod annotation
# To upload a file
> type should be file in order to work with sendkeys and pass the path
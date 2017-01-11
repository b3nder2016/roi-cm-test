# roi-cm-test 
## Trial Task

Make fork of this project.

Upload all code to GitHub, keep original code in master branch, make your changes in develop branch.


1. Write a python script which will change version of each project based on properties file. Properties file should be in YAML format. I.e :

    project name : 'new version'

    I.e -
   
        TestWebApp  : '5.1.0',
        testapp3 : '5.1.0',
        testapp1 : '2.0.0'
      
2. Add *testapp03* as a dependency to the *TestWebApp*, make sure it's jar will be placed to the **WEB-INF/lib** directory

3. Using maven war overlay edit *TestWebApp* **pom.xml** to put properties.xml from testapp3's resources to the **WEB-INF/classes** of TestWebApp war.

4. Using maven add build hostname to the **WEB-INF/hostinfo.txt** file

5. Write an ansible role which will deploy *TestWebApp.war* to the tomcat server (use local connection).

6. Run ansible from previous task inside docker.

7. Build and run docker image with *TestWebApp.war*

As a result give a link to your GitHub repo.


# Take control of your car repairs

#### Video Demo:  https://youtu.be/0F94ViExQ0s

#### Description: This is a Flask app coded in python that allows users to keep track of the repairs of their cars.
####              It allows to see by license plate what fixes have been made, when it was made and how much it costed.
####              Finally it allows to download a report in a excel sheet.

####              I choose Flask as a web framework as it allows to dinamically update databases and with python is flexible to choose and import libraries
####              that allowed me to interact with the user and provide a visualized web app that is easy to interact with.

####              app.py is the basis of the code, here the Flask framework is stablished, also the database and the
####              code to create and update the excel document. It includes libraries to manipulate the excel "xlsxwritter"
####              and the "send_from_directory" from Flask in order to download the created excel file. Also OS is included in order to get the path instance of the project and be able
####              to get the correct excel file that the program created thanks to the xlsx writter library.

####              The main core of the code is to save input in a database (license, plates, repairs and cost) and show the user that information with the help of
####              Flask and some Jinja tags. The user will be available to visualize all the repairs in the same index web and will only show the information of the license plate
####              that is prompted.

####              The download code was more complicated as it includes the use of external libraries, the main one xlsx writter that allows the sheet to be created and written
####              To write the file is similar of what is made with Flask and how it show row by row and column by column. The excel file is created and saved in the main path
####              of the project so its easy to retrive. To download it is used a Flask function send from directory, it search for a specific document or file in a specific path,
####              this was a challange as I almost can´t find the real path that the function needed to find the main file. Finally I found the OS function in order to get
####              the real path. Once thats done, the code runs perfectly as it found and matches for the excel file that was created with the help of the xlsx library. It automatically
####              downloads it to your downloads file.

####              index.html and download.html are the web pages that show the information. It´s builded with html tags with support of bootstrap.
####              index.html have the tags in order to show all the updates that have been made to a particular car, it shows that information in the same webpage index.
####              download.html is a basic form that inputs the license plates and if the information is stores, downloads a excel file to your pc.

####              layout.html have the source of bootstrap library and also some flash messages when some input is missing.
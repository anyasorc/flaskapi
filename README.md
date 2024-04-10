# API Development with Flask
A python application powered by flask framework to run as an API.
The purpose for this application is to show how to run convert your python applicaiton to an API that can be called via Postman or any application.

How to run and call the api
1. Download or clone the code
2. Open the code via VS code
3. Run the app.py file and you get the endpoint to call which is http://127.0.0.1:5000/
4. To call the /api/echo, you will have to go to postman change the verb from Get to Post, and paste this http://127.0.0.1:5000/api/echo 
5. Based on step 4, you will have to select body and then raw. This the json below inside the body:
    {
        "amt":200
    }
6. click on the send button.
7. To call the /api/hello endpoint, you will have to go to postman and leave the verb as GET and then paste the endpoint http://127.0.0.1:5000/api/hello and hit the send button.
# ChefAi
An AI Based Recipe Generator based on Llama 2 by Together AI

### Steps to run the application:
1. Clone the repo using: ```git clone https://github.com/ichbineshan/ChefAi.git```
2. Add the ```TOGETHER_API_KEY``` into the ```.env``` file located in the cloned project directory.
3. Create a Virtual Environment using: ```python3 -m venv venv```
4. Activate the Virtual Environment using: 
```source venv/bin/activate``` (for unix) | 
```./venv/Scripts/activate``` (for windows)
5. Install all the dependencies using: ```pip install -r requirements.txt```
6. Start the application using: 
```set FLASK_APP=app.py``` , followed by 
```flask --app app run```            

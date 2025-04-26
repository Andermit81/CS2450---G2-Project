# CS2450---G2-Project

## Project Presentation
[View our group presentation](./docs/CS2450%20Prez.pdf)

## Demo Video
[Watch a short demo](./docs/demo.mp4)

## About the Project
G2's Task Manager is a Python application that helps users organize and track their tasks efficiently. Users can add, edit, delete, and sort tasks in a tabular format with fields for title, description, due date, priority, and tags. Tasks can be marked as done, and a built-in visualizer (using matplotlib) displays the completion rate as a pie chart. The interface allows easy toggling between a table view and a calendar view. In calendar view, users can select a date to see tasks due on that day, with dates highlighted yellow for pending tasks and green for completed ones. Tasks marked as done are highlighted green in both views for clear visibility. 

### Key Features  
-Add new tasks with descriptions and due dates  
-Edit existing tasks to update details  
-Mark tasks as complete/incomplete  
-Delete tasks you no longer need  
-Give tasks custom tags  
-Sort and filter tasks by tags  
-Visualize task completeness  

## How to Run the Project

## **Step 1: Create a Folder**
Run the following commands in your terminal:

```   
cd Desktop
```

``` 
mkdir MyProject
```

``` 
cd MyProject  
``` 

## **Step 2: Clone the Repository**
Run the following command in your terminal:

```  
git clone https://github.com/Andermit81/CS2450---G2-Project.git
```  

## **Step 3: Create a Virtual Environment**
Run the following commands in your terminal:

``` 
python -m venv venv
```

``` 
source venv/bin/activate  # On Windows use: venv\Scripts\activate  
```   

## **Step 4: Install Dependencies**
Run the following commands in your terminal:

``` 
cd CS2450---G2-Project
```

``` 
pip install -r requirements.txt  
```  

## **Step 5: Run the Project**
Run the following command in your terminal:

```
python -m src.gui.gui 
```

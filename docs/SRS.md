# Software Requirements Specification
## For <Task Manger>

Version 0.1  
Prepared by <Carson Grant>  
<Group 2>  
<02-05-25>  

## Revision History
| Name           | Date      | Reason For Changes     | Version   |
| ----           | -------   | -------------------    | --------- |
| Mitchell A.    |  2/19/25  | Milestone 2            |  0.2      |
| Mitchell A.    |  3/29/25  | Milestone 4            |  0.4      |
| Carson G,      |  4/14/25  | Milestone 5            |  0.5      |

Table of Contents
=================
* [Revision History](#revision-history)
* 1 [Initial Requirement Analysis](#1-initial-requirement-analysis)
  * 1.1 [User Stories](#11-user-stories)
* 2 [Product Overview](#2-product-overview)
* 3 [Requirements](#3-requirements)
  * 3.1 [Functional Requirements](#31-functional-requirements)
  * 3.2 [Non-Functional Requirements](#32-non-functional-requirements)

## 1. Initial Requirement Analysis
Tool used to determine the requirements necessary for the task manager application.

### 1.1 User Stories
As a student, I want to be able to see a list of all of my assignments sorted by priority so that I don't miss any deadlines.
As a user, I want to be able to check off when a task is done so I can stay organized.
As a user, I want to be able to see a list of completed tasks so that I know what I have done so far.

As a user, I want to be able to create repeating tasks so I can set and forget tasks I have each week
As a forgetful person, I want to be able to set reminders.
As a user, I want to collaborate with my friends for tasks, so we can hold each other accountable.

As a google calendar user, I want my tasks to integrate with my google calendar, so I can connect my schedule and tasks together.
As a user, I want to be able to add or drop tasks easily and quickly.
As a user, I want to be able to change the priority on a task.

As a user, I want to be able to color-code my tasks so I can see what’s related at a glance.
As a user, I want to be able to group my tasks together so I can see what kind of overall progress I make. 
As a user, I want to set deadlines on my tasks so I can have a better sense of when to do my tasks.

As a user, I want to categorize my tasks so that I can more easily manage them.
As a user, I want my tasks to be grouped by day so that I can set tasks for a day further in advance.
As a user, I want my old tasks stored together so I can go back and look at my accomplishments.

As a user, I want to be able to add tags to my tasks so that I can categorize them for better organization.
As a user, I want to be able to remove tags from my tasks so that I can update or clean up my task organization.
As a user, I want to mark tasks as "Done" so that I can track completed tasks and focus on pending ones.
As a user, I want tasks marked as "Done" to be visually distinct (e.g., highlighted) so that I can easily identify completed tasks.

## 2. Product Overview
The Task Manager is a software application designed to help users efficiently organize, track, and manage their tasks. The system provides essential features for task creation, prioritization, scheduling, and completion tracking. Users can set deadlines, assign tasks to collaborators, and receive notifications for upcoming tasks. Additionally, the system offers integration with external tools like Google Calendar to enhance productivity and synchronization.

The system also supports advanced task management features, such as tagging tasks for better categorization and marking tasks as "Done" to track progress. Tasks marked as "Done" are visually highlighted, allowing users to easily distinguish completed tasks from pending ones.

This Task Manager is intended for individuals, students, and teams looking to improve their workflow and productivity. With user-friendly interfaces, intuitive categorization, and collaboration features, the system aims to provide a seamless experience for managing daily tasks effectively.

## 3. Requirements
This section specifies the software product's requirements. Specify all of the software requirements to a level of detail sufficient to enable designers to design a software system to satisfy those requirements and to enable testers to test that the software system satisfies those requirements.

The specific requirements should:

Be uniquely identifiable.

State the subject of the requirement (e.g., system, software, etc.) and what shall be done.

Optionally state the conditions and constraints, if any.

Describe every input (stimulus) into the software system, every output (response) from the software system, and all functions performed by the software system in response to an input or in support of an output.

Be verifiable (e.g., the requirement realization can be proven to the customer's satisfaction).

Conform to agreed-upon syntax, keywords, and terms.

### 3.1 Functional Requirements
 Task Creation – The system shall allow users to create a new task by specifying a title, description, due date, priority level, and category.
 
 Task Modification and Deletion – The system shall allow users to edit or delete existing tasks, ensuring only authorized users can make       
  modifications.
  
 Task Filtering and Sorting – The system shall allow users to filter and sort tasks based on priority, due date, category, and completion status.
 
 Notifications and Reminders – The system shall send users reminders for upcoming tasks based on their configured notification preferences.
 
 Task Assignment and Collaboration – The system shall allow users to assign tasks to other registered users and manage task ownership with specific permissions.

 Task Editing – The system shall allow users to:
   View current task details before making changes.

   Modify individual fields (title, description, due date, priority, category) without affecting other attributes.

   Cancel edits and retain the original task details.

   Save changes and update the task list in real time.

 Task Tagging - The system shall allow users to:
   Add one or more tags to a task during task creation or editing.

   Allow users to remove tags from a task during task editing.

   Display tags associated with each task in the tabular format.

   Filter tasks based on tags.

 Marking Tasks as Done - The system shall: 
   Allow users to mark a task as "Done" by clicking a button.

   Visually distinguish tasks marked as "Done" (by changing the row color in the tabular format)

   Update the task list in real time when a task is marked or unmarked as "Done"
  

### 3.2 Non-Functional Requirements 
 Usability – The system shall have an intuitive and user-friendly interface that allows users to easily add, modify, and manage their tasks with    
  minimal learning effort.

 Performance – The system shall respond to user actions within 1 second under normal load and handle at least 1000 concurrent users without 
  significant performance degradation.

 Security – The system shall encrypt all sensitive user data, including passwords, using industry-standard encryption methods and enforce secure 
  authentication mechanisms.

 Scalability – The system shall be designed to support future growth, allowing for an increase in the number of users and tasks without requiring 
  major architectural changes.

 Availability – The system shall maintain an uptime of at least 99.9%, ensuring users have consistent access to their tasks and data with minimal 
  downtime.

### 4. Additional Features

Added a Sorting feature that allows users to sort their task list by priority, title, or due date.
Added a Calendar view that gives the user a visual representation of when their tasks are due.
Added a Task Visualizer that shows in a pie chart the ratio of completed and uncompleted tasks.
Added undo redo functionality that will allow users to undo mistakes such as deleting a task.


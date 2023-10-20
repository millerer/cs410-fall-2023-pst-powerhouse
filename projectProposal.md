# CS 410 Project Proposal: Fall 2023

## Introduction
This document contains the proposed project and group for team **PST Powerhouse**. 
    
Included is a list of members, what the project is, why the project was chosen, and the planned approach and time breakdown.

<br>

## Group Information

### **Name:**
- PST Powerhouse

### **Members**: 
| Name                  | NetID                 | Capitan  |
|-----------------------|-----------------------|----------|
| Eric Miller           | ericlm3@illinois.edu  | Yes      |
| Arjun Balakrishnan    | arjun12@illinois.edu  |          |
| Mark Lee              | ml171@illinois.edu    |          |
| Yong Yang             | yongy3@illinois.edu   |          |
| Jayashree Ganesan     | ganesan8@illinois.edu |          |

<br>

## Project Proposal and Outline

### **Project Topic:** 
- Free Topic

### **1. What is the task?** 
The proposed task is to develop a video game recommendation tool which provides a list of titles based on a user’s query and the reviewer sentiment for each game (positive sentiment giving a higher weight).

#### **2. Why is this important or interesting?**
Video games are a popular media form that, while widespread, doesn’t enjoy the systematized recommendation tools that music or movies do. This holds true for both projects in this class and in general (beyond recommendations based on purchase history).

While review sites are plentiful, tools providing a personalized list of recommended games remain rare.  This is despite video games being the fastest growing media industry compared to television, movies, and music (*Schedy et al.*). 

Given the size of the industry and the large quantity of yearly releases (especially in the indie space), there is an opportunity for a consumer-focused tool such as the one proposed to meet the needs of this overlooked market.

### ***3. What is your planned approach?***
-	Find a robust dataset. A collection of reviews that can be checked for query terms and author sentiment is required. 
-	Determine what data we can scrape from the dataset that would meet the project’s needs. 
-	Decide what libraries and technologies to use. 
-	Decide what algorithms would be most appropriate for our search needs.
-	Develop the recommendation tool. 
-	Test the output and refine as needed. 

### **4. What tools, systems, or datasets are involved?**
Given the robust collection of reviews on the data source (Metacritic), we have decided to use [Kaggle datasets for Metacritic media reviews]("https://www.kaggle.com/datasets?search=metacritic").

### **5. What is the expected outcome?**
Upon entering a query related to the domain of video games, users will receive a ranked listing of ‘k’ video game titles ranked on relevance to their query and then positive reviewer sentiment.

### **6. How are you going to evaluate your work?**
-	Manually confirm output to check for actual relevance and discover where improvements can be made.
-	Get relevance feedback from other potential users.
 -	Use automated testing with metapy.

### **7. What programming language do you plan to use?**
- Python

### **8. Please justify that the workload of your topic is at least 20*N hours, N being the total number of students in your team.**

| Task                                                                  | Estimated Hours   |
|-----------------------------------------------------------------------|-------------------|
| Research datasets and determine scope of relevant data                | 16                |
| Research python libraries to use for our project                      | 8                 |
| Research algorithms that would best meet our needs                    | 8                 |
| Develop backend for the recommendation tool                           | 56                |
| Develop user interface for the recommendation tool                    | 16                |
| Test and refine tool                                                  | 24                |
| Prepare Presentation materials                                        | 16                |
**TOTAL: 144 Hours**

<br>

## Citations
Schedy et al. “Game Changer: Accelerating the Media Industry’s Most Dynamic Sector”, Boston Consulting Group, June 09, 2023, https://www.bcg.com/publications/2023/drivers-of-global-gaming-industry-growth
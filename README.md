# MANA
A crypto trading bot that analyzes Twitter tweets and news websites for trading sentiments.

# MANA Flow Diagram

To help understand how MANA will work, I have also included the flow diagrams. I am not great with these so don't mind the errors!

I have seperated the flow of each components and there is a good reason for it! I want the components to be independent of each other. If one module stops working, it should not stop the other from operating. This is why it is important to use database supported by an API, instead of using traditional local filesystem for storing and retrieving data.

**Note:** Since this project is more likely to change with time as per the requirements, these diagram will be outdated as well! But you'll get the general idea of how things are working behind the scene.

## Scraper Flow Diagram
![MANA Scraper Flow Diagram (1)](https://user-images.githubusercontent.com/91176669/136932603-9585b6b7-43fe-43f5-abfc-a27a7fbae417.png)

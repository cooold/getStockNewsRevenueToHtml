# getStockNewsRevenueToHtml
Since I didn't find a website that can make the news and revenue of the stocks I screened on the same page at the same time, I decided to make it myself to save the time of querying information.

1. I use [goodinfo](https://goodinfo.tw) to enter the filtering conditions to get the stocks I want to pay attention to.
- Use pandas' DataFrame to grab the data in the table and clean the data.
- Save those dates in txt.
- Part of the data stores the original HTML(like mutual fund buying).
2. Organize data (according to my needs).
- I use compare to create new stocks that appear on the day and save them to txt.
3. Using a web crawler to fetch revenue-related([twse](https://mops.twse.com.tw)) data (for the past three months).
- Actually storing the data in a database is more correct, but I think I can perform web crawls every day does not depend on the database.
4. Using a web crawler to fetch Google News made into a JSON
5. Use JSON to make HTML
- Reorder the dictionary to put the highest revenue growth on top
![GITHUB](https://i.imgur.com/uQ4cTnS.png "StockNewsRevenueToHtml")

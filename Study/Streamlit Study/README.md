# Sales Dashboard

This is an interactive sales dashboard built with **Streamlit** and **Plotly** that visualizes sales data by region, time, product category, and salesperson. The dashboard fetches data from an API endpoint and allows dynamic filtering and exploration of sales performance across Brazil.

---

## Features

- Filter sales data by region (Brazil or specific regions)
- Select sales year or view data for all years
- Filter by specific salespeople
- Visualize revenue and number of sales:
  - By state/region (map and bar charts)
  - Monthly time series trends
  - Product categories
  - Top salespeople by revenue and volume
- Interactive charts with hover details
- Metrics summary showing total revenue and total sales count

---

## Technologies Used

- [Streamlit](https://streamlit.io/) for web app UI
- [Pandas](https://pandas.pydata.org/) for data manipulation
- [Plotly Express](https://plotly.com/python/plotly-express/) for interactive charts
- [Requests](https://requests.readthedocs.io/) for fetching data from API

---

## Live Demo

Access the live Streamlit app here:  
[Sales Dashboard App](https://dasboard-vendas-study.streamlit.app/)

---

## Data Source, Usage, and Notes

- **Data Source:** The app fetches product sales data from a public API endpoint:  
  `https://labdados.com/produtos`

- **Usage:**  
  Use the sidebar to filter data by region, year, and salespeople.  
  Navigate through tabs to view revenue, sales quantity, and salespeople performance.  
  Interact with maps and charts to explore sales patterns geographically and over time.

- **Notes:**  
  The dashboard is designed for sales data in Brazil and its regions.  
  Date parsing assumes the purchase date format is `DD/MM/YYYY`.  
  Revenue and sales counts are aggregated accordingly.

---

## How to Run

1. Clone the repository  
2. Install dependencies:
   ```bash
   pip install streamlit pandas plotly requests
3.  Run the Streamlit app:
    ```bash
    streamlit run Dashboard.py
   

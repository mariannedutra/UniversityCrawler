# University Crawler

## Overview
The University Crawler is a web scraping project designed to extract monographs from the repository of the Brazilian University Ulbra campus Palmas-TO, but you can change it to your own interests. This project aims to streamline the process of accessing and gathering monograph data for research purposes.

## Prerequisites
Before running the spider, ensure you have the following installed on your system:
- Python 3.x
- Scrapy

You can install Scrapy using pip: **pip install Scrapy**


## How to Use
1. **Installation**: Clone the repository to your local machine.
2. **Setup Environment**: Ensure you have Python installed. Install the required dependencies.
3. **Run the Crawler**: Execute the crawler script, providing necessary parameters such as the URL of the Ulbra Palmas-TO repository and any specific criteria for data extraction.
    3. 1.  **Navigate to Spider Directory**: Enter the spider directory: **cd crawler_project**
    3. 2. **Run the Spider**: Execute the spider using the following command: **scrapy crawl go-spider -o output.json**
4. **Export Data**: Once the crawler completes its task, the extracted data will be available in the specified output format.
5. **Analysis and Utilization**: Analyze the extracted data for research purposes, academic studies, or any other relevant applications.
5. **Monitor Progress**: Scrapy will display logs and progress information in the terminal as the spider runs. You can monitor the scraping process and any errors or warnings that occur.
6. **View Output**: Once the spider completes its task, you can find the extracted files in '/downloads' and the saved informations in the `output.json` file.



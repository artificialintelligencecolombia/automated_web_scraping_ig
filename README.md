# Automated Instagram Web Scraper

## Description
*An advanced web scraping tool designed to collect business data from Instagram, specifically targeting Spanish-speaking e-commerce and online businesses. The scraper intelligently handles anti-bot measures and provides structured data output for market research purposes.*

> [!IMPORTANT]
> This software is provided for educational and research purposes only. The author and contributors assume no responsibility for any misuse or damage resulting from the use of this program.

### Target criteria
- Follower range: 100 to 100,000
- Region: Latin America and Spain
- Focus: E-commerce and online businesses
- Language: Spanish-speaking markets

## Notice
BY USING THIS SOFTWARE, YOU ACKNOWLEDGE AND AGREE:
1. You are solely responsible for how you use this tool
2. You will comply with Instagram's Terms of Service and robots.txt
3. You will obtain necessary permissions before collecting any data
4. You will respect rate limits and implement appropriate delays
5. You will not use this tool for any malicious purposes
6. You understand that web scraping may be against some websites' terms of service
7. You accept all risks associated with the use of this software

> [!NOTE]
> The authors and contributors cannot be held liable for any damages or legal issues arising from the use or misuse of this tool.

### Features
- Smart Search Logic: SEO-optimized queries for business discovery
- Anti-Detection Measures: Human-like browsing patterns
- Comprehensive Data Collection: Business profiles, metrics, and contact info
- Automated CAPTCHA Handling: Built-in security measure management
- Structured Data Export: Excel format with categorized information

## Tech Stack
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/numpy?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/Excel-blue?style=for-the-badge&logo=googlesheets&color=blue)
![Static Badge](https://img.shields.io/badge/selenium-orange?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/chrome--browser-yellow?style=for-the-badge)


## Installation
1. Clone repository
```
git clone https://github.com/username/repository.git
cd repository
```
2. Set up virtual environment (optional but recommended)
```
python -m venv venv
source venv/bin/activate  
```
3. Install dependencies
```
pip install selenium pandas openpyxl webdriver_manager
```
4. Configure webdriver
```
def setup_webdriver():
    chrome_options = Options()
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    # Additional configuration as needed
    return webdriver.Chrome(options=chrome_options)
```

## Running the scraper
```
python scraper.py --output business_data.xlsx
```

## Usage
Card: front side
![russian](https://github.com/user-attachments/assets/be9c5814-959c-4f9d-bbbc-8bb23b274ebc)
Card:  back side
![english](https://github.com/user-attachments/assets/503bf012-66b8-4c16-8f2f-a401bab65499)
Words Dataset
![words_dataset](https://github.com/user-attachments/assets/85001ecd-61e2-4bad-8fc3-8fbac7ccb8b6)

## Output Format
The scraper generates an Excel file with the following data points:
1. Business Category
2. Follower Count
3. Following Count
4. Full Business Name
5. URL/Website
6. Verification Status
7. Country
8. Additional Business Info

## Anti-Detection Features
- Random delays between actions (2-25 seconds)
- Human-like scrolling behavior
- Cookie management
- Character-by-character typing simulation

> [!IMPORTANT]
> Limitations:
>
> - Rate limiting considerations
> - Region-specific targeting 
> - Requires API integration for Instagram scraper
> - May need periodic updates for anti-bot measures

## License
Distributed under the MIT License. `LICENSE.txt` for more information.

## Contributor(s)
[@artificialintelligencecolombia](https://www.linkedin.com/in/danielmaldonadoco/)

## Contact
![Static Badge](https://img.shields.io/badge/Linkedin-blue?style=flat&logo=linkedin&link=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fdanielmaldonadoco%2F)
![Static Badge](https://img.shields.io/badge/Upwork-black?style=flat&logo=upwork&link=https%3A%2F%2Fwww.upwork.com%2Ffreelancers%2F~0120be438cd3814aaa%3Fmp_source%3Dshare)
![Static Badge](https://img.shields.io/badge/%40aicolombiatech-darkgrey?logo=x&cacheSeconds=https%3A%2F%2Fx.com%2Faicolombiatech)
![Static Badge](https://img.shields.io/badge/%40artificialintelligencecolombia-%23e4405f?logo=instagram&logoColor=white&cacheSeconds=https%3A%2F%2Fwww.instagram.com%2Fartificialintelligencecolombia%2F)
![Static Badge](https://img.shields.io/badge/%40artificialintelligencecolombia-%23ff0000?logo=youtube&logoColor=white&cacheSeconds=https%3A%2F%2Fwww.youtube.com%2F%40ArtificialIntelligenceColombia)
![Static Badge](https://img.shields.io/badge/Twitch-%239146ff?style=flat&logo=Twitch&logoColor=white&link=https%3A%2F%2Fwww.twitch.tv%2Fartificialintelligencecol)

## Acknowledgments
- Selenium Documentation
- Python Requests Library
- Apify API Documentation
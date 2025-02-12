# Google Place Scraping
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

<p> A Python-based app to scrape places near a given address using <b>SerpAPI</b> and <b>geopy</b>, storing details such as name, address, phone and rating in a Excel file. </p>




## 📥 Installation
1. Clone the repository and navigate into the directory
   ```bash
   git clone https://github.com/HugoCDM/Google_Place_Scraping.git
   cd Google_Place_Scraping
   ```
2. Create and activate a virtual environment(optional)
   ```bash
   python -m venv venv 
   .\venv\Scripts\activate 
   ```
3. Install the dependencies -requirements
   ```bash
   pip install -r requirements.txt 
   ```
If you have trouble with .\venv\Scripts\activate, run Windows PowerShell on your search bar as an administrator and write:
```bash
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser # Then type Y and press Enter. Go to step 2
```
## 🖱 Usage and Functionalities
### 1. Address input
- Once you enter the desired address, the geolocator retrieves its coordinates to find nearby places.  
### 2. Search input
- Same way as before, but now with your desired search, e.g., restaurants, hospitals.

### 3. Requests
- A request is sent to a SerpAPI server with the specified parameters.

### 4. While loop
- With each loop, the variable start increases by 20. It means that 20 places are shown in each request(only if the results exceed 20).

### 5. Pandas
- After finishing the program, an Excel file called <b>places.xlsx</b> is generated.

## 🌅 Image section
### Example 1: Wall Street, New York
![addressandsearch](https://github.com/user-attachments/assets/3f3dc10f-10d0-4786-9ed4-4c17dba4817f)

![example](https://github.com/user-attachments/assets/d97b4308-3936-4937-8c92-6d958dd987da)

![example1](https://github.com/user-attachments/assets/c1ea6a87-9b20-45de-ad6c-45ba813bbf7a)

### Example 2: Rio de Janeiro

![addressandsearch2](https://github.com/user-attachments/assets/55059f3b-b219-4046-a07c-5b3f455cbcee)

![example2](https://github.com/user-attachments/assets/dfd91c76-c643-466c-82e2-62530de035ff)
![example2 1](https://github.com/user-attachments/assets/6cf35306-1d45-4c91-828c-c8c853beb2a1)



### *Made by [Hugo Mello](https://github.com/HugoCDM)*








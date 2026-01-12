from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import yt_dlp
import time

# --- 1. SETUP ---
search_query = input("What video should I download? ")

print("🤖 Launching Browser...")
driver = webdriver.Firefox()

try:
    # --- 2. SELENIUM: FIND THE VIDEO ---
    print("🤖 Searching YouTube...")
    driver.get("https://www.youtube.com")

    # Handle "Accept Cookies" popup (Common in Europe/etc) - Try/Except lets us ignore it if not there
    try:
        cookie_button = driver.find_element(By.XPATH, '//button[@aria-label="Accept the use of cookies and other data for the purposes described"]')
        cookie_button.click()
    except:
        pass

    # Find Search Bar
    # YouTube's search bar name is usually "search_query"
    search_box = driver.find_element(By.NAME, "search_query")
    search_box.send_keys(search_query)
    time.sleep(1)
    search_box.send_keys(Keys.RETURN)

    # Wait for results to load
    time.sleep(4) 

    # Find the first video title link
    # We look for the ID "video-title" which YouTube uses for results
    video_link = driver.find_element(By.ID, "video-title")
    
    # Extract the URL (href)
    video_url = video_link.get_attribute("href")
    video_title = video_link.get_attribute("title")
    
    print(f"✅ FOUND: {video_title}")
    print(f"🔗 URL: {video_url}")

    # Close browser (We don't need it anymore, we have the link!)
    driver.quit()

    # --- 3. YT-DLP: DOWNLOAD THE VIDEO ---
    if video_url:
        print("⬇️  Starting Download... (This might take a minute)")
        
        # Configure downloader options
        ydl_opts = {
            'format': 'best', # Get best quality
            'outtmpl': '%(title)s.%(ext)s', # Name the file matching the video title
            'quiet': True, # Don't print too much junk text
        }

        # Run the download
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
            
        print(f"🎉 SUCCESS! '{video_title}' has been downloaded to your folder.")

except Exception as e:
    print(f"❌ Something went wrong: {e}")
    driver.quit()
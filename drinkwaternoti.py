import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="**Please Drink WATER Now!!",
            message="The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men.",
            app_icon=r"C:\Users\user\Downloads\water.ico",
            timeout=12
        )
        time.sleep(3600)




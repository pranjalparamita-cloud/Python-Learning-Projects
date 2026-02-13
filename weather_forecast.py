weather_data={
    "bhubaneswar": {"temp": 72, "condition": "Sunny", "humidity": 45},
    "cuttak": {"temp": 55, "condition": "raining", "humidity": 80},
    "bihar": {"temp": 82, "condition": "Cloudy", "humidity": 60},
    "mumbai": {"temp": 95, "condition": "raining", "thunderstorm": 90},
}

def run_weather_system():
    print("--- Welcome to the Weather System ---")
    
    while True:
        print("\nOptions: 1. View Forecast  2. Check Alerts  3. Exit")
        choice=input("Enter what u want to: ")

        if choice=='1':
            city=input("Enter city name: ").title()
            if city in weather_data:
                data=weather_data[city]
                print(f"\nForecast for {city}:")
                print(f"- Temperature: {data['temp']}°F")
                print(f"- Condition: {data['condition']}")
                print(f"- Humidity: {data['humidity']}%")
            else:
                print("City not found in our database.")

        elif choice=='2':
            print("\n--- Severe Weather Alerts ---")
            alert_count=0
            for city,info in weather_data.items():
                if info['temp'] > 90 or info['condition']=="Stormy":
                    print(f"Severe weather in {city} ({info['condition']}, {info['temp']}°F)")
                    alert_count+=1
            
            if alert_count==0:
                print("All clear No severe weather detected.")

        elif choice=='3':
            print("Shutting down... Stay safe")
            break
        
        else:
            print("Invalid choice. Please try again.")
run_weather_system()
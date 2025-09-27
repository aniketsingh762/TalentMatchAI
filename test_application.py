import os
import django
import requests
import time

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TalentMatch_AI.settings')
django.setup()

def test_application():
    print("Testing TalentMatch AI Application")
    print("=" * 40)
    
    # Test 1: Check if the server is running
    try:
        response = requests.get('http://127.0.0.1:8000/')
        if response.status_code == 200:
            print("✓ Server is running and accessible")
        else:
            print("✗ Server returned status code:", response.status_code)
    except requests.exceptions.ConnectionError:
        print("✗ Server is not accessible. Make sure it's running.")
        return
    except Exception as e:
        print("✗ Error connecting to server:", str(e))
        return
    
    # Test 2: Check API endpoints
    try:
        response = requests.get('http://127.0.0.1:8000/api/jobs/')
        if response.status_code == 200:
            data = response.json()
            print("✓ Job descriptions API is working")
            print(f"  Found {len(data.get('data', []))} job descriptions")
        else:
            print("✗ Job descriptions API returned status code:", response.status_code)
    except Exception as e:
        print("✗ Error testing job descriptions API:", str(e))
    
    print("\nApplication tests completed!")

if __name__ == "__main__":
    test_application()
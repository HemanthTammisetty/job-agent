import requests

print("=" * 50)
print("🚀 Job Agent Started")
print("=" * 50)

url = "https://remotive.com/api/remote-jobs"

response = requests.get(url)

if response.status_code == 200:
    jobs = response.json()["jobs"]

    print(f"Total Jobs Found: {len(jobs)}")

    print("\nTop 5 Jobs:\n")

    for job in jobs[:5]:
        print("----------------------------")
        print("Company :", job["company_name"])
        print("Role    :", job["title"])
        print("Location:", job["candidate_required_location"])
        print("URL     :", job["url"])

else:
    print("Failed to fetch jobs.")

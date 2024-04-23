import requests
import csv

HOST = "betterbody-co-test.myshopify.com"
auth_token = "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"

auth_url = f"https://{HOST}/admin/api/2024-01/orders.json?status=any"
headers = {
    'X-Shopify-Access-Token': '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'
   
}

response = requests.get(auth_url, headers=headers,)
data = response.json()

print (data)

csv_file_path = 'data.csv'

with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=data['orders'].keys())
    writer.writeheader()
    for row in data:
        writer.writerow(row)

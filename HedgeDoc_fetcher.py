import requests

def fetch_hedgedoc_content():
    # Make a request to the HedgeDoc API to get the content of your document
    hedgedoc_url = "https://your-hedgedoc-instance.com/documents/your-document-id"
    response = requests.get(hedgedoc_url)
    content = response.json()["content"]

    # Write the content to a Markdown file
    with open("README.md", "w") as f:
        f.write(content)

if __name__ == "__main__":
    fetch_hedgedoc_content()

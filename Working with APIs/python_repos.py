import requests

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'} #GitHub is currently on the third version of its API, 
# so we define headers for the API call that ask explicitly to use this version of the API.

r = requests.get(url, headers=headers) # r has a status_code attribute to tell us if call was successful.  200 is successful
print(f"Status code: {r.status_code}")

# Store the API response in a variable.
response_dict = r.json() #.json converts information to Python dictionary
print(f"Total repositories: {response_dict['total_count']}")

# Simple calls like this should return a complete set of results, so it’s safe to ignore the
# value associated with 'incomplete_results'. But when you’re making more complex
# API calls, your program should check this value. 

# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
	print("\nSelected information about first repository:")
	print(f"Name: {repo_dict['name']}")
	print(f"Owner: {repo_dict['owner']['login']}")
	print(f"Stars: {repo_dict['stargazers_count']}")
	print(f"Repository: {repo_dict['html_url']}")
	print(f"Created: {repo_dict['created_at']}")
	print(f"Updated: {repo_dict['updated_at']}")
	print(f"Description: {repo_dict['description']}")
	#print(f"Description: {repo_dict['description'].encode('utf-8')}")

# Check API limit https://api.github.com/rate_limit We get 10 per minute without any API keys

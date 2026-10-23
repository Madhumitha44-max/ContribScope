import  requests

def get_repository(owner , repo):
    
    url = f"https://api.github.com/repos/{owner}/{repo}"

    try:

        response = requests.get(url,timeout=10)

    except requests.exceptions.Timeout: 
            
            print("GitHub API request timeout!!")
            return None
    
    except requests.exceptions.ConnectionError:
            
            print("Could not connect to GitHub!!")
            return None
    
    except requests.exceptions.RequestException as error:
            
            print("Error: Request Failed!!" , error)
            return None
    
    if response.status_code == 200:
            
            try:

                return response.json()
            
            except ValueError:
                
                print("Error : GitHub returned invalid JSON data!!")
                return None
            
    elif response.status_code == 403:
            
            print("Repository is not found or inaccessible!!")
            return None
    
    elif response.status_code == 404:
            
            print("Forbidden access or API limit has been exceeded!!")
            return None 
    elif response.status_code == 429:
           
           print("Too many requests.....Try again!!")
           return None

    elif response.status_code in {500 , 501 , 502 , 503 , 504}:
           
           print("Server-side or gateway errors")
           return None

    else:  
            
            print("Failed to fetch repository data")
            print("status_code :",response.status_code)
            return None

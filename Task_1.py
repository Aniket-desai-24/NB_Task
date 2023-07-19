import os
import requests
from google_images_search import GoogleImagesSearch

def download_images(search_term, num_images, save_directory):
    # Create the directory if it doesn't exist
    os.makedirs(save_directory, exist_ok=True)

    # Configure the Image Search client
    image_search = GoogleImagesSearch('AIzaSyDSq9IQErlw5AMHAW0aiXPE5AFG1e720C0', 'd422c3587786e4b21')

    # Set the search parameters
    search_params = {
        'q': search_term,
        'num': num_images,
        'safe': 'high',
        'fileType': 'jpg',
        'imgType': 'photo'
    }

    # Perform the search
    image_search.search(search_params=search_params)

    # Download and save the images
    for i, image_result in enumerate(image_search.results()):
        response = requests.get(image_result.url)

        # Save the image to the directory
        with open(os.path.join(save_directory, f'{search_term}_{i}.jpg'), 'wb') as f:
            f.write(response.content)

    print(f'{num_images} images downloaded successfully.')


# Main program
if __name__ == '__main__':
    user_search_term = input('Enter your search term: ')
    user_num_images = 50
    user_save_directory = r'C:\Users\user\Desktop\NewBieron Technologies\PHOTOS'

    download_images(user_search_term, user_num_images, user_save_directory)

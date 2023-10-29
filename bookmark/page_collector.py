from pywebcopy import save_webpage

def download_page(url: str, project_folder: str) -> bool:
    
    save_webpage(url=url, project_folder=project_folder, project_name="download", open_in_browser=False)
    
    return True
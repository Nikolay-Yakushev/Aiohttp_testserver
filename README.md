# aiohttp-server
Aiohttp based server to download and upload files. Getting size of downloaded file is also possible.


1) pip install -r requirements.txt
2) python3 entry.py --host=0.0.0.0 --port=8080
    
    Or use Dockerfile

- download image locally:
    
    
        sudo docker run -it -p 8000:8080 driver220v/aiohttp-server
- move to project directory and run server
        
        
        cd conserv/
        python3 entry.py --host=0.0.0.0 --port=8080
        
        
        ======== Running on http://0.0.0.0:8080 ========
        (Press CTRL+C to quit)
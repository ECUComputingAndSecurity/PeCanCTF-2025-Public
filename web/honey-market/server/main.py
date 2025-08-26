from app import app
from settings import *
from seed import *
import routes 

if __name__ == "__main__": 

    seed_data() 

    app.run(port=PORT, host=HOST, debug=DEVELOPMENT)
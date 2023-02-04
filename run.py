from apps.config import db
from apps import create_app

app = create_app(db)

if __name__ == "__main__": 
    app.run(host='0.0.0.0', port=5005, debug=True)
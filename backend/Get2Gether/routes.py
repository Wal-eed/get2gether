from Get2Gether import app
from Get2Gether.utils.colourisation import printColoured
from Get2Gether.api_routes import (
    schedule_router
)

# Registering route handler blueprints
app.register_blueprint(schedule_router)

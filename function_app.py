import azure.functions as func
import json, logging
from datetime import datetime, timezone 

app = func.FunctionApp()

@app.event_hub_message_trigger(arg_name="eventhubtrigger", event_hub_name="%EventHubInstance%",
                               connection="EventHubNamespace") 
def eventhub_trigger(eventhubtrigger: func.EventHubEvent):
    # logging.info('Python EventHub trigger processed an event: %s',
    #             azeventhub.get_body().decode('utf-8'))
    datetime_now = datetime.now(timezone.utc).strftime("%Y-%m%d %H:%M:%S")    
    logging.info(f"eventhub_trigger starts processing: {datetime_now}")

    try: 
        events_str = eventhubtrigger.get_body().decode('utf-8')
        events = json.loads(events_str) 

    except Exception as e:
        logging.info(f"Error: {e}")


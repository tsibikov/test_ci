import json
import io


with io.open("test.json", 'r') as f:
        settings = json.load(f)
        alerts_list = settings["alerts"]
        for alert in alerts_list:
                alert_name = alert.get["alert_name"]
                regis_id = alert.get["regis_id"]
                ignore = alert.get["ignore"]
                if alert_name == None or regis_id == None or ignore == None:
                        raise Exception("Can not pasrse json")
                                
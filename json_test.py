import json
import io


with io.open("test.json", 'r') as f:
        try:
                settings = json.load(f)
        except Exception as e:
                print(e)
        alerts_list = settings["alerts"]
        for alert_settings in alerts_list:
                alert_name = alert_settings.get("alert_name")
                regis_alert_id = alert_settings.get("regis_id")
                ignore = alert_settings.get("ignore")
                if alert_name == None or regis_alert_id == None or ignore == None:
                        raise Exception("Can not parse json")
                                
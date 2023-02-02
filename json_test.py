import json
import io


if __name__ == "__main__":
        with io.open("test.json", 'r') as f:
                settings = json.load(f)
                alerts_list = settings.get("alerts")
                if alerts_list == None:
                        raise Exception(f"Can not parse json. No alerts list")
                for alert_settings in alerts_list:
                        alert_name = alert_settings.get("alert_name")
                        if alert_name == None:
                                raise Exception(f"No alert name")
                        regis_alert_id = alert_settings.get("regis_id")
                        if regis_alert_id == None:
                                raise Exception(f"No regis_alert_id")
                        ignore = alert_settings.get("ignore")
                        if ignore == None:
                                raise Exception(f"No ignore status")
                                        
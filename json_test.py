import json
import io


if __name__ == "__main__":
        with io.open("test.json", 'r') as f:
                settings = json.load(f)
                alerts_list = settings["alerts"]
                i = 1
                for alert_settings in alerts_list:
                        i += 1
                        alert_name = alert_settings.get("alert_name")
                        if alert_name == None:
                                raise Exception(f"No alert name in string {i}")
                        regis_alert_id = alert_settings.get("regis_id")
                        if regis_alert_id == None:
                                raise Exception(f"No alert name in string {i}")
                        ignore = alert_settings.get("ignore")
                        if ignore == None:
                                raise Exception(f"No alert name in string {i}")
                                        
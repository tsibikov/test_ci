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
                                error = f"No alert name in string {i}"
                                raise Exception(error)
                        regis_alert_id = alert_settings.get("regis_id")
                        if regis_alert_id == None:
                                error = f"No alert name in string {i}"
                                raise Exception(error)
                        ignore = alert_settings.get("ignore")
                        if ignore == None:
                                error = f"No ignore status in string {i}"
                                raise Exception(error)
                                        
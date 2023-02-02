import json
import io


if __name__ == "__main__":
        with io.open("test.json", 'r') as f:
                settings = json.load(f)
                alerts_list = settings["alerts"]
                i = 1
                for alert_settings in alerts_list:
                        i += 1
                        try:
                                alert_name = alert_settings["alert_name"]
                        except:
                                print(f"No alert name in string {i}")
                                raise Exception()
                        try:
                                regis_alert_id = alert_settings["regis_id"]
                        except:
                                print(f"No regis id in string {i}")
                                raise Exception()
                        try:
                                ignore = alert_settings["ignore"]
                        except:
                                print(f"No ignore status in string {i}")
                                raise Exception()

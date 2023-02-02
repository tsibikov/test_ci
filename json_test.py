import json
import io


with io.open("test.json", 'r') as f:
        settings = json.load(f)
        for setting in settings:
                alert_name = setting.get["alert_name"]
                regis_id = setting.get["regis_id"]
                ignore = setting.get["ignore"]
                if alert_name == None or regis_id == None or ignore == None:
                        raise Exception("Can not pasrse json")
                                
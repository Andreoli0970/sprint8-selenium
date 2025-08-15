import json
import re

def retrieve_phone_code(driver):
    """
    Lê os logs de desempenho do Chrome e extrai o código de confirmação enviado por SMS.
    """
    logs = driver.get_log("performance")
    for log in logs:
        message = json.loads(log["message"])["message"]
        if (
            "Network.responseReceived" in message["method"]
            and "sms-code" in str(message)
        ):
            sms_match = re.search(r"\b\d{4}\b", str(message))
            if sms_match:
                return sms_match.group(0)
    return None
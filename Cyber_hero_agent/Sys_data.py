import win32evtlog
import time

server = 'localhost'
logtype = 'Security'

def get_security_logs():
    handler = win32evtlog.OpenEventLog(server, logtype)
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

    events = win32evtlog.ReadEventLog(handler, flags, 0)
    return events

while True:
    events = get_security_logs()

    with open("logs.txt", "a") as logf, open("alert.txt", "a") as alertf:
        for event in events[:10]:  # read 10 newest events
            event_id = event.EventID

            if event_id == 4625:  # failed login
                msg = f"Failed login attempt by user {event.StringInserts[5]} on {event.TimeGenerated}\n"
                alertf.write(msg)
                logf.write(msg)

            if event_id == 4624:  # successful login
                msg = f"Successful login by user {event.StringInserts[5]} on {event.TimeGenerated}\n"
                logf.write(msg)

    time.sleep(5)
